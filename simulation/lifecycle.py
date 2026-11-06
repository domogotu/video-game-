"""Optional lifecycle layer for the Reedwater prototype.

Explicit, evidence-gated population development. No automatic unknown-species
reproduction, invented hybrid fertility, or silent population creation.
"""
from dataclasses import dataclass
from .reedwater import Simulation, Cohort, SPECIES

# Abstract simulation-turn ages, NOT canonical biological lifespans.
MATURITY = {
    "current_dart": 3, "bark_lantern": 4, "reed_skipper": 4,
    "silt_burrower": 5, "mire_needle": 5, "gloam_moth": 6,
    "glassfilm_microbe": 2,
}
# Resource links are provisional mechanics, not validated diet science.
NURSERY = {
    "current_dart": ("plankton", "water"),
    "bark_lantern": ("fungal_film", "humidity"),
    "gloam_moth": ("hostleaf", "host"),
}
@dataclass
class LifecyclePolicy:
    species: str
    maturity_ticks: int
    offspring_per_event: int = 1

    def __post_init__(self):
        if self.species not in SPECIES or self.maturity_ticks < 1 or self.offspring_per_event < 1:
            raise ValueError("invalid lifecycle policy")

class LifecycleManager:
    def __init__(self, sim: Simulation):
        self.sim = sim
        self.juvenile_age: dict[tuple[str, str], int] = {}

    def advance(self, ticks: int = 1) -> None:
        """Age juveniles and mature supported cohorts without spontaneous births."""
        if not isinstance(ticks, int) or not 1 <= ticks <= 1000:
            raise ValueError("ticks must be in 1..1000")
        for _ in range(ticks):
            for key in sorted(list(self.sim.cohorts)):
                cell, species, stage = key
                if stage != "juvenile" or species not in MATURITY:
                    continue
                juvenile = self.sim.cohorts[key]
                if juvenile.count == 0:
                    self.juvenile_age.pop((cell, species), None)
                    continue
                age_key = (cell, species)
                age = self.juvenile_age.get(age_key, 0) + 1
                if age >= MATURITY[species]:
                    adults = self.sim.cohorts.setdefault(
                        (cell, species, "adult"), Cohort(species, cell, 0))
                    adults.count += juvenile.count
                    self.sim._record("mature", species, cell, juvenile.count)
                    juvenile.count = 0
                    self.juvenile_age.pop(age_key, None)
                else:
                    self.juvenile_age[age_key] = age
            self.sim.validate()

    def breed(self, cell: str, species: str, *, verified: bool = False) -> int:
        """Opt-in same-species recruitment; no hybrid breeding."""
        if species not in MATURITY or not verified or self.sim.count(cell, species) < 2:
            return 0
        habitat = self.sim.cells[cell]
        if species == "gloam_moth" and habitat.resources.get("hostleaf", 0) < 1:
            return 0
        if species == "current_dart" and (not habitat.water_connected or habitat.oxygen < 40):
            return 0
        if species == "bark_lantern" and habitat.humidity < 60:
            return 0
        return self.sim.recruit(cell, species, 1, evidence=True)

    def seek_habitat(self, origin: str, species: str, amount: int = 1) -> int:
        """Move to a better adjacent cell only when explicitly requested."""
        if amount < 1:
            raise ValueError("amount must be positive")
        if species not in NURSERY or self.sim.count(origin, species) == 0:
            return 0
        food, condition = NURSERY[species]
        source = self.sim.cells[origin]
        candidates = []
        for dest in sorted(source.neighbors):
            target = self.sim.cells[dest]
            if species == "current_dart" and not (source.water_connected and target.water_connected):
                continue
            if condition == "humidity" and target.humidity < 60:
                continue
            if condition == "water" and target.oxygen < 40:
                continue
            if condition == "host" and target.resources.get("hostleaf", 0) == 0:
                continue
            if self.sim.population(dest) >= target.capacity:
                continue
            if target.resources.get(food, 0) > source.resources.get(food, 0):
                candidates.append((target.resources.get(food, 0), dest))
        if not candidates:
            return 0
        _, destination = max(candidates, key=lambda x: (x[0], x[1]))
        return self.sim.migrate(origin, destination, species, amount)
