"""Deterministic, standard-library-only Reedwater ecology foundation.

Prototype, not a game engine. All quantities are abstract nonnegative units.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
import json
import random

SPECIES = {
    "null_slime": "unknown", "glassfilm_microbe": "clonal",
    "reed_skipper": "eggs", "silt_burrower": "eggs",
    "glass_eyed_pouncer": "litter", "mire_needle": "eggs",
    "moss_horn_browser": "unknown", "root_crown_forager": "unknown",
    "current_dart": "eggs", "reedstalker": "unknown",
    "bark_lantern": "eggs", "gloam_moth": "eggs",
}

@dataclass
class Cell:
    id: str
    resources: dict[str, int]
    capacity: int
    water_connected: bool = False
    oxygen: int = 100
    humidity: int = 50
    neighbors: list[str] = field(default_factory=list)

@dataclass
class Cohort:
    species: str
    cell: str
    count: int
    stage: str = "adult"

@dataclass
class Event:
    seq: int
    kind: str
    species: str
    cell: str
    amount: int
    detail: str = ""

class Simulation:
    def __init__(self, cells: list[Cell], cohorts: list[Cohort], seed: int = 1):
        self.cells = {c.id: c for c in cells}
        self.cohorts = {(c.cell, c.species, c.stage): c for c in cohorts}
        self.seed = seed
        self.rng = random.Random(seed)
        self.events: list[Event] = []
        self.validate()

    def validate(self):
        for c in self.cells.values():
            if c.capacity < 0 or not 0 <= c.oxygen <= 100 or not 0 <= c.humidity <= 100:
                raise ValueError("invalid habitat bounds")
            if any(v < 0 for v in c.resources.values()):
                raise ValueError("negative resource")
            if any(n not in self.cells for n in c.neighbors):
                raise ValueError("unknown neighbor")
        for (cell, species, stage), c in self.cohorts.items():
            if cell not in self.cells or species not in SPECIES or c.count < 0:
                raise ValueError("invalid cohort")

    def count(self, cell: str, species: str, stage: str = "adult") -> int:
        return self.cohorts.get((cell, species, stage), Cohort(species, cell, 0, stage)).count

    def _record(self, kind, species, cell, amount, detail=""):
        self.events.append(Event(len(self.events) + 1, kind, species, cell, amount, detail))

    def feed(self, cell: str, species: str, resource: str, units: int) -> int:
        if units <= 0 or self.count(cell, species) <= 0:
            raise ValueError("invalid feed request")
        habitat = self.cells[cell]
        available = habitat.resources.get(resource, 0)
        taken = min(units, available)
        habitat.resources[resource] = available - taken
        self._record("feed", species, cell, taken, resource)
        self.validate()
        return taken

    def predation(self, cell: str, predator: str, prey: str, amount: int = 1) -> int:
        if predator == prey or amount <= 0 or self.count(cell, predator) <= 0:
            raise ValueError("invalid predation")
        prey_cohort = self.cohorts.get((cell, prey, "adult"))
        if prey_cohort is None:
            return 0
        killed = min(amount, prey_cohort.count)
        prey_cohort.count -= killed
        self.cells[cell].resources["detritus"] = self.cells[cell].resources.get("detritus", 0) + killed
        self._record("predation", predator, cell, killed, prey)
        self.validate()
        return killed

    def migrate(self, origin: str, destination: str, species: str, amount: int) -> int:
        if amount <= 0 or destination not in self.cells[origin].neighbors:
            raise ValueError("invalid migration route")
        source = self.cohorts.get((origin, species, "adult"))
        if source is None:
            return 0
        target = self.cohorts.setdefault((destination, species, "adult"), Cohort(species, destination, 0))
        moved = min(amount, source.count, max(0, self.cells[destination].capacity - self.population(destination)))
        if species == "current_dart" and not (self.cells[origin].water_connected and self.cells[destination].water_connected):
            moved = 0
        source.count -= moved
        target.count += moved
        self._record("migrate", species, origin, moved, destination)
        self.validate()
        return moved

    def population(self, cell: str) -> int:
        return sum(c.count for c in self.cohorts.values() if c.cell == cell)

    def recruit(self, cell: str, species: str, amount: int, *, evidence: bool = False) -> int:
        if amount <= 0 or not evidence or SPECIES[species] == "unknown":
            raise ValueError("recruitment requires known reproduction and evidence")
        habitat = self.cells[cell]
        if species in ("current_dart", "mire_needle") and (not habitat.water_connected or habitat.oxygen < 40):
            return 0
        if species == "bark_lantern" and habitat.humidity < 60:
            return 0
        if species == "gloam_moth" and habitat.resources.get("hostleaf", 0) <= 0:
            return 0
        added = min(amount, max(0, habitat.capacity - self.population(cell)))
        cohort = self.cohorts.setdefault((cell, species, "juvenile"), Cohort(species, cell, 0, "juvenile"))
        cohort.count += added
        self._record("recruit", species, cell, added)
        self.validate()
        return added

    def snapshot(self) -> str:
        payload = {"seed": self.seed, "cells": [asdict(self.cells[k]) for k in sorted(self.cells)],
                   "cohorts": [asdict(self.cohorts[k]) for k in sorted(self.cohorts)],
                   "events": [asdict(e) for e in self.events]}
        return json.dumps(payload, sort_keys=True, separators=(",", ":"))

def example() -> Simulation:
    return Simulation(
        [Cell("river", {"plankton": 20, "detritus": 0}, 30, True, 85, 60, ["oxbow"]),
         Cell("oxbow", {"plankton": 8, "hostleaf": 3}, 15, True, 65, 75, ["river", "wood"]),
         Cell("wood", {"fruit": 12, "fungal_film": 7}, 20, False, 100, 80, ["oxbow"])],
        [Cohort("current_dart", "river", 10), Cohort("mire_needle", "oxbow", 2),
         Cohort("bark_lantern", "wood", 5), Cohort("null_slime", "wood", 1)])
