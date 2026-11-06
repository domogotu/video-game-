"""World turn coordinator for the Reedwater ecology prototype."""
import json
from .reedwater import Simulation
from .lifecycle import LifecycleManager

class ReedwaterWorld:
    def __init__(self, sim):
        self.sim = sim
        self.life = LifecycleManager(sim)
        self.turn = 0

    def run(self, turns=1, season="wet"):
        if type(turns) is not int or not 1 <= turns <= 1000:
            raise ValueError("invalid turn count")
        if season not in ("wet", "dry"):
            raise ValueError("invalid season")
        for _ in range(turns):
            self.sim.step()
            self.sim.ecology_tick(season=season)
            self.life.advance()
            # Each source is evaluated once; destinations do not become new sources
            # until the next turn.
            origins = [(cell, species) for cell in sorted(self.sim.cells)
                       for species in ("current_dart", "bark_lantern", "gloam_moth")
                       if self.sim.count(cell, species) > 0]
            moved_into = set()
            for cell, species in origins:
                if (cell, species) in moved_into:
                    continue
                before = {n: self.sim.count(n, species)
                          for n in self.sim.cells[cell].neighbors}
                moved = self.life.seek_habitat(cell, species)
                if moved:
                    for n, previous in before.items():
                        if self.sim.count(n, species) > previous:
                            moved_into.add((n, species))
            self.turn += 1
            self.sim._record("world_turn", "", "", 1, season)

    def save(self):
        return json.dumps({
            "version": 1, "turn": self.turn,
            "simulation": json.loads(self.sim.snapshot()),
            "ages": [[cell, species, age] for (cell, species), age
                     in sorted(self.life.juvenile_age.items())],
        }, sort_keys=True)

    @classmethod
    def load(cls, raw):
        data = json.loads(raw)
        if data.get("version") != 1 or type(data.get("turn")) is not int or data["turn"] < 0:
            raise ValueError("invalid world save")
        world = cls(Simulation.from_snapshot(json.dumps(data["simulation"])))
        world.turn = data["turn"]
        for cell, species, age in data["ages"]:
            if cell not in world.sim.cells or type(age) is not int or age < 0:
                raise ValueError("invalid age record")
            if world.sim.count(cell, species, "juvenile") <= 0:
                raise ValueError("orphaned age record")
            key = (cell, species)
            if key in world.life.juvenile_age:
                raise ValueError("duplicate age record")
            world.life.juvenile_age[key] = age
        return world
