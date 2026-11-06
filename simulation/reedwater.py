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
        self.tick = 0
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
        if type(units) is not int or units <= 0 or self.count(cell, species) <= 0:
            raise ValueError("invalid feed request")
        habitat = self.cells[cell]
        available = habitat.resources.get(resource, 0)
        taken = min(units, available)
        habitat.resources[resource] = available - taken
        self._record("feed", species, cell, taken, resource)
        self.validate()
        return taken

    def predation(self, cell: str, predator: str, prey: str, amount: int = 1) -> int:
        if predator == prey or type(amount) is not int or amount <= 0 or self.count(cell, predator) <= 0:
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
        if type(amount) is not int or amount <= 0 or destination not in self.cells[origin].neighbors:
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
        if type(amount) is not int or amount <= 0 or not evidence or SPECIES[species] == "unknown":
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

    def step(self, ticks: int = 1) -> None:
        """Advance bounded environmental ticks; no automatic breeding or AI."""
        if type(ticks) is not int or not 1 <= ticks <= 1000:
            raise ValueError("ticks must be an integer in 1..1000")
        for _ in range(ticks):
            self.tick += 1
            for cell_id in sorted(self.cells):
                cell = self.cells[cell_id]
                for resource, limit in (("plankton", 20), ("fruit", 12),
                                        ("fungal_film", 7), ("hostleaf", 3)):
                    if resource in cell.resources:
                        cell.resources[resource] = min(limit, cell.resources[resource] + 1)
                self._record("environment_tick", "", cell_id, 1)
            self.validate()

    def ecology_tick(self, *, season: str = "wet") -> None:
        """One explicit ecological turn with finite feeding, aging and mortality.

        Prototype rules are deliberately conservative: no automatic births and
        no assumptions about species with undocumented diets/reproduction.
        """
        if season not in ("wet", "dry"):
            raise ValueError("season must be wet or dry")
        self.tick += 1
        diets = {"current_dart": "plankton", "bark_lantern": "fungal_film"}
        for cell_id in sorted(self.cells):
            habitat = self.cells[cell_id]
            if season == "dry":
                habitat.humidity = max(0, habitat.humidity - 5)
                if habitat.water_connected:
                    habitat.oxygen = max(0, habitat.oxygen - 5)
            else:
                habitat.humidity = min(100, habitat.humidity + 2)
                if habitat.water_connected:
                    habitat.oxygen = min(100, habitat.oxygen + 2)
            for key in sorted(self.cohorts):
                cohort = self.cohorts[key]
                if cohort.cell != cell_id or cohort.count == 0:
                    continue
                food = diets.get(cohort.species)
                if food is None:
                    continue  # No unsupported species diet invented.
                stock = habitat.resources.get(food, 0)
                eaten = min(stock, cohort.count)
                habitat.resources[food] = stock - eaten
                if eaten:
                    self._record("ecology_feed", cohort.species, cell_id, eaten, food)
                shortage = cohort.count - eaten
                if cohort.species == "current_dart" and habitat.oxygen < 40:
                    shortage = cohort.count
                if cohort.species == "bark_lantern" and habitat.humidity < 30:
                    shortage = cohort.count
                deaths = min(cohort.count, shortage)
                cohort.count -= deaths
                if deaths:
                    habitat.resources["detritus"] = habitat.resources.get("detritus", 0) + deaths
                    self._record("ecology_death", cohort.species, cell_id, deaths, "starvation_or_habitat")
            self._record("ecology_tick", "", cell_id, 1, season)
        self.validate()

    @classmethod
    def from_snapshot(cls, snapshot: str) -> "Simulation":
        """Restore exact model state from versioned JSON."""
        data = json.loads(snapshot)
        if data.get("version") != 1:
            raise ValueError("unsupported snapshot version")
        sim = cls([Cell(**c) for c in data["cells"]],
                  [Cohort(**c) for c in data["cohorts"]], seed=data["seed"])
        sim.tick = data["tick"]
        if not isinstance(sim.tick, int) or sim.tick < 0:
            raise ValueError("invalid tick")
        sim.events = [Event(**e) for e in data["events"]]
        if any(e.seq != i for i, e in enumerate(sim.events, start=1)):
            raise ValueError("invalid event sequence")
        sim.validate()
        return sim

    def snapshot(self) -> str:
        payload = {"version": 1, "tick": self.tick, "seed": self.seed, "cells": [asdict(self.cells[k]) for k in sorted(self.cells)],
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
