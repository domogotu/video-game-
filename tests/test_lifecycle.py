"""Integration tests for the optional lifecycle manager."""
import unittest
from simulation.reedwater import Cell, Cohort, Simulation, example
from simulation.lifecycle import LifecycleManager

class LifecycleTests(unittest.TestCase):
    def test_maturation_conserves_population(self):
        sim = example()
        sim.cohorts[("river", "current_dart", "juvenile")] = Cohort("current_dart", "river", 4, "juvenile")
        manager = LifecycleManager(sim)
        before = sim.population("river")
        manager.advance(3)
        self.assertEqual(sim.count("river", "current_dart", "juvenile"), 0)
        self.assertEqual(sim.count("river", "current_dart"), 14)
        self.assertEqual(sim.population("river"), before)

    def test_unknown_reproduction_is_blocked(self):
        sim = example()
        manager = LifecycleManager(sim)
        self.assertEqual(manager.breed("wood", "null_slime", verified=True), 0)
        self.assertEqual(manager.breed("river", "current_dart", verified=False), 0)

    def test_breeding_with_evidence(self):
        sim = example()
        manager = LifecycleManager(sim)
        self.assertEqual(manager.breed("river", "current_dart", verified=True), 1)
        self.assertEqual(sim.count("river", "current_dart", "juvenile"), 1)

    def test_habitat_seeking_respects_water(self):
        sim = example()
        sim.cells["oxbow"].resources["plankton"] = 30
        manager = LifecycleManager(sim)
        self.assertEqual(manager.seek_habitat("river", "current_dart", 2), 2)
        sim.cells["oxbow"].water_connected = False
        self.assertEqual(manager.seek_habitat("river", "current_dart", 2), 0)

    def test_maturation_unknown_species_not_invented(self):
        sim = example()
        sim.cohorts[("wood", "null_slime", "juvenile")] = Cohort("null_slime", "wood", 2, "juvenile")
        LifecycleManager(sim).advance(100)
        self.assertEqual(sim.count("wood", "null_slime", "juvenile"), 2)

    def test_habitat_seeking_no_free_population(self):
        sim = example()
        manager = LifecycleManager(sim)
        before = sum(c.count for c in sim.cohorts.values())
        manager.seek_habitat("river", "current_dart", 4)
        after = sum(c.count for c in sim.cohorts.values())
        self.assertEqual(before, after)

if __name__ == "__main__":
    unittest.main()
