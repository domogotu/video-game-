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

    def test_tick_and_roundtrip(self):
        sim = example()
        sim.feed("river", "current_dart", "plankton", 5)
        sim.step(3)
        self.assertEqual(sim.tick, 3)
        self.assertEqual(sim.cells["river"].resources["plankton"], 18)
        restored = type(sim).from_snapshot(sim.snapshot())
        self.assertEqual(restored.snapshot(), sim.snapshot())

    def test_tick_rejects_invalid_bounds(self):
        sim = example()
        for ticks in (0, -1, 1001, 1.5):
            with self.assertRaises(ValueError):
                sim.step(ticks)

    def test_snapshot_version_rejected(self):
        sim = example()
        with self.assertRaises(ValueError):
            type(sim).from_snapshot('{"version":2}')

    def test_ecology_food_shortage_is_finite(self):
        sim = example()
        sim.cells["river"].resources["plankton"] = 3
        sim.ecology_tick()
        self.assertEqual(sim.count("river", "current_dart"), 3)
        self.assertEqual(sim.cells["river"].resources["plankton"], 0)
        self.assertEqual(sim.cells["river"].resources["detritus"], 7)

    def test_ecology_dry_habitat_and_snapshot(self):
        sim = example()
        sim.ecology_tick(season="dry")
        self.assertEqual(sim.cells["wood"].humidity, 75)
        self.assertEqual(sim.cells["river"].oxygen, 80)
        self.assertEqual(type(sim).from_snapshot(sim.snapshot()).snapshot(), sim.snapshot())

    def test_ecology_invalid_season_no_mutation(self):
        sim = example()
        before = sim.snapshot()
        with self.assertRaises(ValueError):
            sim.ecology_tick(season="winter")
        self.assertEqual(sim.snapshot(), before)

    def test_negative_resource_rejected(self):
        sim = example()
        sim.cells["wood"].resources["fruit"] = -1
        with self.assertRaises(ValueError):
            sim.validate()

if __name__ == "__main__":
    unittest.main()
