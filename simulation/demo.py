"""Command-line smoke scenario for the standalone Reedwater prototype.

Run: python -m simulation.demo
No external dependencies, network, accounts, or game-engine installation.
"""
import json
from .reedwater import example, Simulation
from .lifecycle import LifecycleManager

def run_demo():
    sim = example()
    life = LifecycleManager(sim)
    initial = {cell: sim.population(cell) for cell in sorted(sim.cells)}
    sim.feed("river", "current_dart", "plankton", 3)
    sim.step(2)
    life.breed("river", "current_dart", verified=True)
    life.advance(3)
    sim.ecology_tick(season="dry")
    restored = Simulation.from_snapshot(sim.snapshot())
    if restored.snapshot() != sim.snapshot():
        raise AssertionError("save/load mismatch")
    return {
        "simulation_tick": sim.tick,
        "initial_population": initial,
        "final_population": {cell: sim.population(cell) for cell in sorted(sim.cells)},
        "events": len(sim.events),
        "save_load_equal": True,
        "note": "Abstract simulation demonstration, not playable gameplay",
    }

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2, sort_keys=True))
