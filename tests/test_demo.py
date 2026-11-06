import unittest
from simulation.demo import run_demo

class DemoTests(unittest.TestCase):
    def test_smoke_demo(self):
        result = run_demo()
        self.assertTrue(result["save_load_equal"])
        self.assertEqual(result["simulation_tick"], 3)
        self.assertGreater(result["events"], 0)
        self.assertGreaterEqual(result["final_population"]["river"], 0)


    def test_world_turn_roundtrip(self):
        from simulation.world import ReedwaterWorld
        from simulation.reedwater import example
        world = ReedwaterWorld(example())
        world.run(2, season="dry")
        self.assertEqual(ReedwaterWorld.load(world.save()).save(), world.save())

    def test_world_turn_determinism(self):
        from simulation.world import ReedwaterWorld
        from simulation.reedwater import example
        first, second = ReedwaterWorld(example()), ReedwaterWorld(example())
        first.run(3)
        second.run(3)
        self.assertEqual(first.save(), second.save())

    def test_world_rejects_bad_season(self):
        from simulation.world import ReedwaterWorld
        from simulation.reedwater import example
        world = ReedwaterWorld(example())
        before = world.save()
        with self.assertRaises(ValueError):
            world.run(season="winter")
        self.assertEqual(world.save(), before)

    def test_world_persists_juvenile_age(self):
        from simulation.world import ReedwaterWorld
        from simulation.reedwater import example, Cohort
        world = ReedwaterWorld(example())
        world.sim.cohorts[("river", "current_dart", "juvenile")] = Cohort("current_dart", "river", 2, "juvenile")
        world.life.advance()
        loaded = ReedwaterWorld.load(world.save())
        self.assertEqual(loaded.life.juvenile_age[("river", "current_dart")], 1)

    def test_world_blocks_multi_hop_migration(self):
        from simulation.world import ReedwaterWorld
        from simulation.reedwater import Cell, Cohort, Simulation
        cells = [
            Cell("a", {"plankton": 1}, 20, True, neighbors=["b"]),
            Cell("b", {"plankton": 5}, 20, True, neighbors=["a", "c"]),
            Cell("c", {"plankton": 15}, 20, True, neighbors=["b"]),
        ]
        world = ReedwaterWorld(Simulation(cells, [Cohort("current_dart", "a", 3)]))
        world.run(1)
        self.assertEqual(world.sim.count("c", "current_dart"), 0)

    def test_world_rejects_duplicate_age_records(self):
        import json
        from simulation.world import ReedwaterWorld
        from simulation.reedwater import example, Cohort
        world = ReedwaterWorld(example())
        world.sim.cohorts[("river", "current_dart", "juvenile")] = Cohort("current_dart", "river", 2, "juvenile")
        data = json.loads(world.save())
        data["ages"] = [["river", "current_dart", 1], ["river", "current_dart", 1]]
        with self.assertRaises(ValueError):
            ReedwaterWorld.load(json.dumps(data))

if __name__ == "__main__":
    unittest.main()
