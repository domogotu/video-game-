# Reedwater prototype — runnable developer guide

**Scope:** First engineering slice of Lethal Absorption's Veyra/Reedwater ecology. Python 3.12, standard library only. This is a deterministic **abstract cohort simulator**, not a 3D game, complete AI, validated ecology, or multiplayer server.

## Commands

From repository root:

```bash
python -m unittest discover -s tests -v
python -m simulation.demo
```

The test workflow at `.github/workflows/reedwater-tests.yml` also runs on relevant pushes. A committed workflow is not evidence of a passing run; inspect the GitHub Actions job before declaring verification.

## Delivered implementation

- `simulation/reedwater.py`: 12-species registry, habitat cells, cohort counts, feeding, predation, migration, recruitment gates, environmental ticks, seasonal ecology updates, event log, versioned snapshot and restore.
- `simulation/lifecycle.py`: explicitly invoked maturation, evidence-gated same-species recruitment, and adjacent-habitat seeking. Maturity thresholds are placeholder simulation turns, **not** canonical lifespans. No spontaneous reproduction.
- `simulation/demo.py`: reproducible smoke scenario combining feeding, environmental ticks, one authorized recruitment, maturation, seasonal resource pressure, and JSON round-trip.
- `tests/test_reedwater.py`, `tests/test_lifecycle.py`, `tests/test_demo.py`: 22 authored tests. Results require execution.

## Design boundaries and caveats

1. Ecological rates and resource caps are placeholder mechanics; no balancing is claimed.
2. The lifecycle manager's juvenile age counters are **not yet serialized**; save/restore of the core simulation does not preserve partial maturation progress. Do not deploy as persistent lifecycle state.
3. Recruitment is explicitly authorized by `verified=True` for a same-species rule, not proof of scientifically verified breeding or hybrid compatibility.
4. Unknown reproductive modes (including Null Slime and Reedstalker) cannot reproduce through the manager.
5. Current Dart movement requires connected water; migration is not autonomous except when the caller explicitly invokes habitat seeking.
6. Only Current Dart and Bark Lantern have automatic feeding/death rules in `ecology_tick`; remaining species require authored ecology.
7. No creature ages into senescence, and no species-specific natural-death rates are implemented.
8. Events are records of operations, not an independently replayable command stream. The saved snapshot is the source of restored state.
9. No concurrent event arbitration, networking, character physics, game UI or playable scene is present.

## Next build gates

1. Execute the 22 tests; repair failures; verify CI.
2. Persist lifecycle ages and seed/RNG state, add state schema migration and corruption checks.
3. Add bounded starvation reserves, developmental stages, aging/senescence and environment-driven migration with per-species policy.
4. Integrate the other ten species only after verifying their dossier-specific diets and reproduction.
5. Implement server-authoritative resource transactions and replay before multiplayer testing.
