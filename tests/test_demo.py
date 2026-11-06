import unittest
from simulation.demo import run_demo

class DemoTests(unittest.TestCase):
    def test_smoke_demo(self):
        result = run_demo()
        self.assertTrue(result["save_load_equal"])
        self.assertEqual(result["simulation_tick"], 3)
        self.assertGreater(result["events"], 0)
        self.assertGreaterEqual(result["final_population"]["river"], 0)

if __name__ == "__main__":
    unittest.main()
