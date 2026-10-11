# Vertical Slice 01 — System Interactions and Edge Cases

**Project:** Lethal Absorption  
**Status:** Implementation-ready design specification; not implemented, play-tested, or runtime-verified.  
**Scope:** Frozen first slice only: cellular onboarding, first trait choice, first evolution, and the compact animal-scale arrival habitat.

## 1. Authority and scope

This document translates the frozen first-slice baseline into state transitions, event rules, failure recovery, persistence requirements, and acceptance tests. The existing [Vertical Slice 01](VERTICAL_SLICE_01_CELLULAR_OPENING_TO_FIRST_EVOLUTION.md) remains authoritative for the player-facing sequence and scope boundary. The creature diet and luck specifications remain authoritative for whole-game principles; this document defines only the smallest proof needed in this slice.

Included: one compact cellular play space, bounded nutrients/resources, a readable hazard/threat, one starter trait choice, a visible evolution gate, one transition, and a compact animal habitat with one predator/prey relationship and one bounded diet/adaptation demonstration.

Excluded: multiplayer, a complete food web, breeding, Alpha encounters, full research crafting, broad procedural mutation generation, planetary systems, large-scale destruction, and the complete species catalogue. These remain deferred, not removed.

## 2. State model

Keep prototype state explicit and serializable. The names below are conceptual fields, not a required programming language or architecture.

### 2.1 Character state

- **Stage:** CELLULAR or ANIMAL_INTRO.
- **Growth:** current value and displayed threshold for the active stage.
- **Starter trait:** unset, CURRENT_SENSITIVE_MEMBRANE, or IMPACT_RESISTANT_MEMBRANE.
- **Tutorial flags:** movement demonstrated, absorption demonstrated, dodge/safe evasion demonstrated, attack/disengage demonstrated, resource view introduced, discovery record introduced, trait selected.
- **History:** meaningful nutrient/resource types absorbed, notable hazard/survival events, selected trait, transition cause, and relevant observations.
- **Discoveries:** separate records for clue/rumor, observed, verified, acquired, stabilized, and mastered where applicable. The slice need not expose every category in a menu, but must not conflate them.
- **Animal condition:** bounded health/energy/growth or condition values appropriate to the prototype.
- **Adaptation clues:** observed diet-related clue identifiers; these are not owned abilities.
- **Checkpoint:** last safe recovery point and last committed progression milestone.

Do not use one generic “unlocked” flag for every progression state. A clue is not a mutation, an acquired trait is not mastery, and growth is not character level.

### 2.2 Creature state

Each nearby creature needs only data required for this bounded demonstration: species and role (PREY or PREDATOR); current behavior state (IDLE, FORAGING, ALERT, FLEEING, STALKING, PURSUING, FEEDING, RETREATING); hunger/feeding need, health/condition, valid food preferences, perception and target eligibility, recent diet event and whether its consequence was applied, and membership in the local encounter budget.

A creature must never receive an invalid target, food item, or mutation merely because a state transition or save/load occurred at an inconvenient time.

## 3. Event and transition contracts

### 3.1 Cellular onboarding

| Event | Preconditions | State change | Feedback | Recovery / guard |
|---|---|---|---|---|
| Enter cellular space | New or resumed slice | Load checkpoint and stage | One short objective and movement cue if not demonstrated | Never reset committed trait/history on re-entry |
| Move successfully | Input produces valid movement | Set movement flag | Subtle response; stop repeating prompt after success | Blocked input does not count; ensure a navigable route |
| Absorb nutrient | Valid absorbable target, in range, not consumed | Consume once; apply bounded growth/resource value; append history | Target response and clear growth delta | Invalid attempts grant nothing; duplicate events are idempotent |
| Encounter threat | Threat active and perceivable | Set encounter context; threat telegraph begins | Readable tell and visible escape option | No unavoidable damage during first teaching beat |
| Dodge or evade | Threat has a valid tell and player has control | Resolve movement/dodge; record survival demonstration when danger avoided | Clear success/near-miss feedback | Safe movement away can count; no required damage |
| Attack practice target | Attack valid and target eligible/in range | Apply bounded hit and response; set attack flag on valid attempt | Distinguish hit, miss, invalid target | Safe disengagement is an alternative; no forced kill |
| Open resource view | Relevant milestone reached | Mark view introduced | Show current resource and one contextual explanation | Reopening does not duplicate rewards or reset progress |
| Open discovery record | Meaningful observation exists | Mark record introduced | Label clue/observation separately from owned trait | Empty state must not imply a missed secret |
| Select starter trait | Choice presented and not committed | Store one option; apply defined effect once; record history | Preview advantage/trade-off and confirmation | Prevent double selection; provide confirm/cancel before commit |
| Meet evolution gate | Growth threshold and required teaching flags complete | Set readiness once | Show exact remaining requirements or readiness | No hidden timer, random roll, kill quota, or repeated grind |
| Begin transition | Ready state confirmed | Commit checkpoint/history, then play cinematic | Explain why evolution occurs | Save before stage swap; recover if commit fails |
| Finish/skip cinematic | Transition committed | Set ANIMAL_INTRO; preserve trait/history | Concise recap if skipped | Skip and full playback produce identical gameplay state |

The frozen gate is a visible growth threshold plus demonstration of movement, absorption, dodge/safe evasion, and attack/disengagement once, along with the starter trait choice. Exact numeric growth values remain prototype tuning. Killing a creature is not required.

### 3.2 Animal-scale arrival

1. Load the bounded habitat only after the cellular transition state is committed.
2. Spawn in a safe arrival clearing, outside predator attack range and away from blocked geometry.
3. Restore the chosen trait and display its effect through an observable cue or interaction.
4. Introduce the immediate objective and one manageable threat in context.
5. Keep the predator/prey demonstration outside the essential control-teaching path; it must not prevent completion of the first animal objective.
6. Persist the animal-stage checkpoint after arrival and meaningful progression milestones.

Camera presentation may be first-person-forward with anatomy feedback as specified in the baseline; optional third-person presentation, if built, must not alter collision, detection, combat, or progression rules.

## 4. Absorption and growth rules

- Validate target identity, availability, range, stage compatibility, and one-time consumption before granting anything.
- Apply each resource/growth event once. Repeated input, duplicate overlap callbacks, reloads, or repeated event delivery must not duplicate rewards.
- Growth feedback must state what changed; no silent growth or unexplained threshold changes.
- Clamp growth, energy, health, and condition to bounded values. One resource cannot overflow the meter or skip a required choice without explicit handling.
- If the player reaches the threshold before completing teaching beats, preserve growth and show remaining required actions. Do not secretly discard growth or require excessive grinding.
- If teaching beats complete before the threshold, show the remaining growth requirement and provide a nearby safe, repeatable resource route.
- Record meaningful absorption categories/events, not an unbounded log of every frame or repeated contact.

## 5. Starter trait rules

The baseline choices are:

- **Current-Sensitive Membrane:** a visible, bounded improvement to reading or moving with currents.
- **Impact-Resistant Membrane:** a visible, bounded reduction to one defined environmental collision or minor-impact effect.

Before confirmation, explain the practical effect and trade-off in plain language. Both choices must remain viable; neither may be strictly superior in every situation. Apply a trait once and store its stable identifier. The cinematic and animal-stage recap must read that identifier, not infer the choice from appearance or random state.

If the player closes the menu before confirming, retain the pending choice without granting either trait. If save/load occurs after confirmation, restore exactly the committed choice. Duplicate selection must not stack the effect.

## 6. Bounded predator/prey and diet demonstration

### 6.1 Minimal behavior loop

The slice proves one local predator and one prey species; it does not simulate a full food web.

- Prey selects a valid escape route when it detects the predator and may flee toward cover or away from danger.
- Predator may detect, stalk/approach, pursue, and attack only when target, distance, and local encounter rules permit.
- Prey can break line of sight, escape beyond the bounded encounter area, or use a simple defense. A hunt is not guaranteed to end in a kill.
- The player receives readable cues for detection, pursuit, escape, and disengagement.
- Only nearby actors run detailed updates. Distant creatures are not spawned or simulated at high cost for this slice.
- If an encounter becomes stuck, crosses the boundary, or cannot find a path, use a bounded timeout to retreat/reset to a valid state. Never teleport an attacker onto the player or award an invisible kill.

### 6.2 Diet event pipeline

For the animal-stage demonstration, one valid feeding event can produce ordinary condition/growth change and a possible adaptation clue. The minimum acceptance case does not require a rare mutation.

1. Verify that a predator completed feeding on a valid prey target, or that the player consumed a permitted resource.
2. Commit the diet event with a unique event identifier.
3. Apply a bounded nutrition/condition/growth result once.
4. Evaluate whether the diet is relevant to an adaptation clue using species/form, food properties, and previous exposure.
5. If eligible, reveal a clue/observation—not an automatic ability grant.
6. Record the event and clue state so save/load or repeated processing cannot award it again.

The player must be able to observe at least one diet-driven condition/growth change and one possible adaptation clue without needing a lucky roll. A rare mutation is optional and cannot be the only way to complete the slice. If random discovery is used, luck cannot bypass compatibility or grant an ineligible trait.

### 6.3 Diet edge cases

- **No food available:** creature searches briefly, changes route, rests, or retreats; it does not loop at full update rate forever.
- **Prey escapes:** predator ends pursuit after its bounded disengagement condition; prey receives no false death/feeding event.
- **Target dies but cannot be reached:** no feeding effect until a valid feeding interaction completes.
- **Duplicate feeding event:** idempotency prevents repeated growth/clue grants.
- **Incompatible food:** ordinary rejection or limited nutrition; no mutation from an invalid combination.
- **Repeated same food:** common meals mainly support condition/growth; no infinite growth or unlimited mutation rolls.
- **Rare outcome fails:** player still receives useful ordinary feedback or a clue when appropriate; essential progress remains available by a deterministic/repeatable route.
- **Creature or player leaves area:** finish or cancel interaction in a defined state and preserve only committed results.
- **Sapient target:** do not treat as ordinary prey/resource by default; this slice uses non-sapient creatures only.

## 7. Luck, randomness, and progression fairness

- Mandatory tutorial flags, trait choices, and evolution requirements are deterministic.
- The animal-stage adaptation clue has a deterministic observable route; an optional rare mutation may be rolled only after compatibility eligibility passes.
- Random rolls are event-based, not triggered every frame, overlap tick, or repeated interaction.
- A failed optional roll cannot erase growth, change the starter trait, or block the next objective.
- Use a stable event identifier or equivalent deduplication key so loading/retrying cannot reroll the same event indefinitely.
- If a random result is saved, restore it; do not silently reroll on load.
- Exact odds and bad-luck thresholds remain configurable and untuned until prototype evidence exists. Do not invent final probabilities in this specification.

## 8. Failure, recovery, and softlock prevention

| Failure condition | Required behavior |
|---|---|
| Player takes damage during teaching | Recover at safe checkpoint or restore bounded health; preserve committed flags/history |
| Player is defeated before first evolution | Return to safe cellular checkpoint; no permanent death during basic-control teaching |
| Player cannot find nutrient | Keep a clear nearby fallback resource route; do not rely on random spawn |
| Player misses/refuses attack practice | Permit safe disengagement route; do not softlock |
| Player ignores/closes a menu | Keep progress; reopen contextually when required; no duplicate reward |
| Player selects neither trait | Remain in choice state; do not trigger evolution |
| Player reaches threshold early | Preserve growth and show missing teaching requirements |
| Teaching completes early | Show remaining growth requirement and safe nearby source |
| Transition save fails | Do not swap stages; retain recoverable pre-transition state and show retry message |
| Cinematic is skipped/interrupted | Load the same committed animal-stage state and show recap |
| Animal spawn is invalid | Try predefined safe fallback; if all fail, return to last valid stage checkpoint |
| Predator/prey pathing fails | Timeout, retreat/reset, record diagnostic; never softlock objective |
| Save lacks optional creature data | Recreate bounded default ecosystem state without overwriting player progression |
| Save has unknown optional trait/clue ID | Preserve other data, safely ignore/migrate unknown optional record, emit diagnostic |
| Repeated input/event occurs | Deduplicate state changes and rewards |
| Player exits during pending action | Commit completed actions only; cancel incomplete interactions cleanly |

Permanent death remains a whole-game principle, but must not be sprung on a new player before foundational controls and recovery are learned. This first-slice tutorial uses recoverable failure.

## 9. Save/load and transition integrity

Persist at the appropriate checkpoint: current stage/checkpoint; growth and committed resource state; tutorial flags; selected trait and application state; relevant absorption/observation history; transition-ready/committed state; animal arrival completion; committed diet event IDs, bounded condition/growth changes, and discovered clue IDs.

Save transaction rules:

1. Validate state before writing.
2. Commit player history and transition marker before changing the active stage.
3. Never grant the same resource, diet effect, or clue twice after reload.
4. Treat incomplete transition writes as recoverable; never load into a half-cell/half-animal state.
5. Version the save payload or provide migration/defaulting for fields added during development.
6. Do not discard valid player progress because optional ecosystem state is absent or malformed.

## 10. Feedback and interface requirements

- One primary objective at a time during onboarding.
- Show evolution-gate progress and identify remaining requirements.
- Distinguish clue/observation from acquired or usable trait.
- Show resource and condition changes with a concise cause.
- Show the chosen starter trait's effect in the cellular stage and after transition.
- Telegraph predator intent before a dangerous action; communicate when pursuit ends.
- Make menus reopenable without resetting progress.
- After cinematic skip, recap the new form, retained trait, and first animal objective.
- Quiet prompts after the corresponding action is demonstrated; avoid persistent tutorial spam.
- Provide a safe fallback route for required resources and objectives.

## 11. Performance and bounded simulation

For this slice only: one active threat at a time on the immediate onboarding path; one local predator/prey demonstration plus a small handful of neutral/resource creatures as needed; no high-cost off-screen AI; bounded pathfinding retries, pursuit duration, feeding retries, and repeated event processing; effects and sensor cues within a prototype budget.

Exact actor counts, update rates, distances, and timings are engineering/profiling decisions, not finalized promises. If the budget is exceeded, preserve essential interactions first and simplify distant/nonessential behavior. Do not remove the predator/prey/diet acceptance case; reduce presentation or unrelated entities instead.

## 12. Acceptance tests for later implementation

These are required cases to implement and run later. They are **not** claims that tests have already run.

### Cellular flow
- [ ] New entry teaches movement first and records successful movement.
- [ ] A valid nutrient grants growth exactly once.
- [ ] Invalid or repeated absorption grants no duplicate reward.
- [ ] Threat cues appear before a dodge/evasion opportunity.
- [ ] Safe evasion can satisfy the survival beat without killing a creature.
- [ ] Attack feedback distinguishes hit/miss; safe disengagement does not softlock.
- [ ] Resource and discovery menus appear contextually and can be reopened.
- [ ] Both starter traits have distinct observable effects and neither is granted before confirmation.
- [ ] Early threshold completion preserves growth and displays missing requirements.
- [ ] Completed teaching beats with insufficient growth show a safe repeatable route.
- [ ] Evolution readiness requires specified flags and visible threshold; no hidden random gate exists.

### Transition and persistence
- [ ] Transition state is committed before stage change.
- [ ] Full cinematic and skipped cinematic lead to equivalent gameplay state.
- [ ] Trait and relevant history survive transition and save/load.
- [ ] Interrupted/failed transition recovers to a valid checkpoint.
- [ ] Invalid animal spawn resolves to a safe fallback.
- [ ] Duplicate input, callbacks, or load cycles cannot duplicate rewards or traits.

### Ecosystem and diet
- [ ] Prey detects and escapes a valid predator threat using readable behavior.
- [ ] Predator pursues only eligible prey and can disengage without a stuck loop.
- [ ] No feeding reward is granted before a valid feeding event completes.
- [ ] A completed diet event applies bounded condition/growth change once.
- [ ] At least one adaptation clue is discoverable through a repeatable route.
- [ ] Clue state is not mislabeled as an owned/mastered ability.
- [ ] Incompatible diet cannot generate an ineligible mutation.
- [ ] Optional randomness is event-based and cannot gate mandatory progression.
- [ ] Save/load preserves committed diet effects and prevents reroll duplication.
- [ ] Predator/prey behavior respects the bounded actor and update budget.

### Recovery and scope
- [ ] Tutorial failure is recoverable and preserves committed learning/history.
- [ ] No required objective is blocked by a random spawn, rare mutation, kill requirement, or pathing failure.
- [ ] Missing optional creature data does not destroy player progression.
- [ ] Sapient beings are outside the slice prey/resource loop.
- [ ] Excluded systems remain deferred rather than silently added to the slice.

## 13. Implementation handoff checklist

Before calling the slice implemented, engineering must identify the runtime/engine and project entry point; state owner and save/load implementation; event deduplication mechanism; tutorial progression owner; creature state machine and bounded AI update strategy; test framework and named automated/manual playtest cases; profiling method for target hardware; and placeholder-asset/final-art replacement plan.

Do not begin unrelated full-game feature implementation until this slice passes its acceptance criteria or a documented blocker is approved. Do not claim the game is playable, implemented, tested, or verified from this document alone.

## 14. Open implementation decisions

Intentionally left for runtime implementation/prototype: engine/runtime and exact module names; final controls and accessibility options; numeric growth thresholds, damage, hunger, detection distance, timing, and actor budgets; exact resource quantities and mutation odds; save format/migration implementation; whether optional third-person camera fits the slice; final art/audio/animation.

Resolve numeric values through prototype observation and profiling. Preserve the behavior contracts when tuning values.
