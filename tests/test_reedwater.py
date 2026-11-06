"""Run: python -m unittest discover -s tests -v (from repository root)."""
import unittest
from simulation.reedwater import example, SPECIES

class ReedwaterTests(unittest.TestCase):
    def test_roster(self):
        self.assertEqual(len(SPECIES), 12)

    def test_feed_is_bounded(self):
        sim = example()
        self.assertEqual(sim.feed("river", "current_dart", "plankton", 100), 20)
        self.assertEqual(sim.cells["river"].resources["plankton"], 0)
        self.assertEqual(sim.feed("river", "current_dart", "plankton", 1), 0)

    def test_predation_conserves_kills(self):
        sim = example()
        sim.cohorts[("oxbow", "current_dart", "adult")] = type(next(iter(sim.cohorts.values())))("current_dart", "oxbow", 1)
        self.assertEqual(sim.predation("oxbow", "mire_needle", "current_dart", 3), 1)
        self.assertEqual(sim.predation("oxbow", "mire_needle", "current_dart", 1), 0)
        self.assertEqual(sim.count("oxbow", "current_dart"), 0)

    def test_migration_and_disconnect(self):
        sim = example()
        self.assertEqual(sim.migrate("river", "oxbow", "current_dart", 4), 4)
        self.assertEqual(sim.count("river", "current_dart"), 6)
        sim.cells["oxbow"].water_connected = False
        self.assertEqual(sim.migrate("river", "oxbow", "current_dart", 4), 0)

    def test_unknown_reproduction_blocked(self):
        sim = example()
        with self.assertRaises(ValueError):
            sim.recruit("wood", "null_slime", 2, evidence=True)
        with self.assertRaises(ValueError):
            sim.recruit("wood", "reedstalker", 2, evidence=True)

    def test_oxygen_and_humidity_gates(self):
        sim = example()
        sim.cells["river"].oxygen = 10
        self.assertEqual(sim.recruit("river", "current_dart", 4, evidence=True), 0)
        sim.cells["wood"].humidity = 30
        self.assertEqual(sim.recruit("wood", "bark_lantern", 4, evidence=True), 0)

    def test_recruitment_capacity(self):
        sim = example()
        self.assertEqual(sim.recruit("river", "current_dart", 100, evidence=True), 20)
        self.assertEqual(sim.population("river"), 30)

    def test_deterministic_snapshot(self):
        a, b = example(), example()
        a.feed("river", "current_dart", "plankton", 3)
        b.feed("river", "current_dart", "plankton", 3)
        self.assertEqual(a.snapshot(), b.snapshot())

    def test_negative_resource_rejected(self):
        sim = example()
        sim.cells["wood"].resources["fruit"] = -1
        with self.assertRaises(ValueError):
            sim.validate()

if __name__ == "__main__":
    unittest.main()
