# Ultimate Ability Vertical Slice — Fire, Wind, Water, and World Response

**Status:** Detailed implementation specification; not implemented or tested.  
**Parent specifications:** Ability Weaving and Multi-Tree Progression; Ultimate Abilities and Persistent Environmental Impact; System Alignment and Development Roadmap.

## Goal

Define one bounded, end-to-end gameplay slice that proves Lethal Absorption's core promise: a player learns and combines abilities, masters the result, unlocks a stronger ultimate, and visibly changes the environment under consistent world rules.

This is a reference implementation target, not a claim that a playable game exists.

## Player-facing experience

The player begins with a basic Fire ability. Through relevant use, research, and training, the player discovers a distinct Fire Refinement technique. Adding Wind changes how the flame travels and spreads. Adding Water may produce a steam/thermal-pressure reaction if the player has discovered and stabilized that recipe. The advanced version can change the battlefield more dramatically, while a mastered ultimate can destroy eligible structures and leave a persistent environmental scar.

The player should understand:
- What ingredients the technique uses.
- What each added ingredient changes.
- Why a recipe is locked, unstable, or incompatible.
- What the attack is expected to affect.
- Its costs, risks, counterplay, and persistence.
- Which parts of the environment are destructible and which are protected.

## Dependencies and unlock chain

1. **Fire Base:** available only when the character has a compatible source, ability unlock, and sufficient control.
2. **Fire Refinement:** learned as a distinct ability through a qualifying use/research/training gate; it is not a free duplicate of Fire.
3. **Wind Conduit:** requires Wind source control and a compatible delivery method or anatomy.
4. **Steam / Thermal-Pressure Weave:** requires Fire, Fire Refinement, Wind, Water source control, and the specific discovered recipe. The order and output must be defined in the recipe record.
5. **Stabilizing Trait:** a specified trait, mutation, or mastery threshold prevents the high-pressure branch from becoming unstable. Its exact acquisition gate must be documented by the implementation team.
6. **Mastery Milestones:** relevant successful use improves control, efficiency, reliability, or branch access; repetition without meaningful success is insufficient.
7. **Ultimate Variant:** requires a defined evolutionary stage, mastery milestone, resource capacity, and a qualifying trial or discovery. It does not unlock from numeric level alone.

The exact character level, resource amounts, and progression thresholds remain tuning decisions and must be recorded in data rather than scattered as hard-coded assumptions.

## Registered stages and outputs

### Stage 1 — Fire
- **Purpose:** simple direct attack.
- **Environmental response:** applies heat and localized scorch to eligible surfaces; may ignite explicitly flammable materials if heat, duration, and world conditions meet the material threshold.
- **Limits:** cannot automatically ignite everything or damage protected objects.

### Stage 2 — Refined Fire
- **Purpose:** improved delivery and control.
- **Environmental response:** stronger localized heat, more reliable ignition of eligible materials, and a more distinct impact profile.
- **Trade-off:** increased resource use, charge, recovery, or another documented cost.

### Stage 3 — Fire + Wind
- **Purpose:** change trajectory, reach, spread, and pressure.
- **Environmental response:** moves light debris, disturbs foliage, changes flame direction, and may increase spread where fuel and wind rules allow it.
- **Limits:** the ability does not create unlimited wind or fuel. Strong environmental spread remains bounded by the simulation and the recipe.

### Stage 4 — Fire + Refinement + Wind + Water
- **Purpose:** a discovered steam/thermal-pressure branch.
- **Environmental response:** creates a defined pressure burst, localized steam hazard, and eligible material damage. It may crack weak masonry or break a specifically configured destructible surface if the attack meets that material's threshold.
- **Compatibility:** requires a registered recipe and adequate water source/power. If unavailable, the ability explains whether it lacks an ingredient, source, trait, or mastery.
- **Failure behavior:** an unregistered or incompatible combination must not trigger an improvised, unbounded effect. It is rejected with feedback or follows an explicitly authored unstable branch.

The same four components do not have to produce the same output in every context. Any contextual variant must be registered and previewable.

## Ultimate variant

The ultimate is an evolution of the registered weave, not an unrestricted fifth ability or an automatic multiplier.

**Proposed behavior:** a charged, telegraphed thermal-pressure discharge with a wider bounded footprint, a stronger impact, and a persistent crater/scorch/debris state on eligible surfaces. The ultimate may collapse configured weak structures if the structural simulation confirms the damage threshold. It does not automatically destroy every building, permanently reshape the entire map, or ignore protected areas.

Required constraints:
- Explicit evolutionary and mastery gates.
- Higher resource burden and defined cooldown/recovery.
- Clear startup and counter windows.
- Bounded footprint, duration, and number of chain reactions.
- Self/ally/neutral impact rules.
- Server-side validation of recipe, resources, stage, and world effects.
- A defined interruption and cancellation path.
- No resource farming loop where destruction returns more resources than the action costs.

Ultimate scale must be data-driven by the ability's family, form, recipe, and world context. Other abilities may have different maximum expressions, including protection, healing, control, movement, or creation rather than mass destruction.

## Environmental material model for the slice

Implement only a small, representative material set at first:
- **Scorchable surface:** receives visible heat/scorch state but remains structurally intact.
- **Flammable object:** may ignite after defined exposure and environmental checks.
- **Light debris / foliage:** can be displaced by a qualifying wind or pressure impulse.
- **Weak destructible wall:** has an explicit damage threshold and a defined broken/collapsed state.
- **Persistent ground surface:** can retain a crater, crack, or scorch decal/state with a known save/reset policy.
- **Protected boundary:** provides a clear example of an object the attack cannot destroy.

Each material entry needs a stable identifier, relevant physical properties, damage threshold, allowed reactions, collision/navigation consequences, visual state, persistence class, and test coverage. The first slice should avoid simulating every possible physical property in the entire world.

## Environmental state and persistence

Each impact resolves in a controlled sequence:
1. Validate the ability recipe, player state, target, resources, and cooldown.
2. Calculate the ability's bounded footprint and force/heat exposure.
3. Evaluate target materials and environmental conditions.
4. Apply eligible visual, physical, damage, and hazard state changes.
5. Update collision and navigation if the material changes.
6. Replicate authoritative results to relevant clients.
7. Save persistent changes according to the area's persistence policy.
8. Emit structured telemetry for test/debug evidence without exposing private player information.

Visual effects must not claim destruction if the authoritative collision/world state remains intact. If the engine cannot support physical deformation, use a clearly defined break-state and debris substitute rather than inconsistent collision.

## UI and control feedback

Before a charged or ultimate activation, communicate:
- Current weave stage and ingredients.
- Expected area/footprint.
- Resource cost and cooldown/recovery.
- Known material interactions and uncertain outcomes.
- Effects on allies, neutral NPCs, objectives, and protected spaces.
- Cancel/interrupt option and counterplay window.

After activation, explain significant outcomes such as “weak wall collapsed,” “fuel sustained the fire,” or “recipe unstable: stabilizing trait missing.” Do not promise deterministic outcomes when weather, material state, or dynamic world conditions legitimately change the result.

Input mappings must remain configurable. Hold/charge behavior needs an accessible alternative that does not require frame-perfect timing. The stage-selection rules must not make ordinary activation unpredictable.

## Failure and edge cases

The implementation plan must explicitly cover:
- Missing Fire, Wind, or Water source.
- Missing refinement ability or stabilizing trait.
- Current form cannot deliver the technique.
- Insufficient resources, cooldown active, or ability interrupted.
- Target outside range, behind valid cover, or in a protected area.
- Target is resistant, wet, frozen, already burning, or structurally supported.
- Multiple players trigger overlapping effects.
- Chain reaction reaches the maximum allowed budget.
- Player disconnects during a charged attack.
- World save/load occurs after structural change.
- Collision/navigation update fails or is delayed.
- Client visual prediction differs from server resolution.
- Destruction attempts to block a required mission route or spawn region.

Each case needs a defined result, player feedback where relevant, and test coverage.

## Acceptance tests

Do not mark this slice complete until evidence demonstrates all applicable criteria:

1. Base Fire causes localized effects on eligible materials.
2. Fire Refinement is a separate earned ability with a visible unlock reason.
3. Fire + Wind changes a documented delivery or environmental property.
4. The four-component recipe unlocks only when prerequisites are met.
5. An incompatible recipe is rejected or follows a defined bounded failure branch.
6. The stabilizing trait changes the specified stability behavior.
7. Meaningful use advances discovery/mastery only under documented qualifying conditions.
8. The ultimate has a distinct footprint and impact beyond the base ability.
9. A configured weak wall breaks at the correct threshold; a protected boundary remains intact.
10. Persistent terrain/structure state, collision, navigation, visuals, and save/load remain consistent.
11. Costs, cooldowns, interruption, and counterplay work as specified.
12. Server authority prevents clients from inventing recipes, costs, destruction, or resource returns.
13. Simultaneous attacks and chain reactions respect effect budgets and do not create infinite loops.
14. Accessibility alternatives and input remapping preserve stage selection and cancellation.
15. Performance measurements are recorded under a documented test scenario.
16. Test commands, environment, results, known failures, and runtime evidence are attached to the project record.

## Implementation tracking fields

Track each acceptance criterion with:
- ID and requirement.
- Design status.
- Code/file location.
- Test name and test result.
- Runtime evidence or reproducible steps.
- Known gaps and owner.
- Status: proposed, specified, prototyped, implemented, tested, verified, deferred, or blocked.

A passing documentation review is not a passing runtime test. A passing unit test alone does not establish that visuals, collision, navigation, persistence, and multiplayer replication all work together.

## Explicit non-goals for the first slice

- Universal destruction of every asset.
- Unbounded chain reactions.
- Full planetary destruction simulation.
- Every elemental recipe.
- All ultimate abilities or character-specific routes.
- Final resource balance or complete progression curves.
- Claims of a finished or verified game.

**Completion definition:** the slice is complete only after the specified mechanics are implemented in the actual game runtime and the acceptance tests are run with recorded results.
