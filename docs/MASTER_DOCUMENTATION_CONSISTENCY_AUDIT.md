# Master Documentation Consistency Audit

**Project:** Lethal Absorption  
**Audit scope:** Current Markdown design documents under `docs/` on `main`  
**Audit type:** Documentation inventory, cross-system consistency review, and one correction pass  
**Status:** Completed at design-document level; runtime behavior not tested

## 1. Purpose and limits

This audit checks that the known design documents are present, indexed, and aligned on the most important shared rules. It is not a line-by-line proof that every sentence has been converted into a requirement, and it is not evidence of a playable implementation. The Game Design Bible is large and remains the central vision reference; topic-specific documents provide detailed rules for their systems.

## 2. Inventory checked

The following 24 Markdown documents were fetched from the current `main` branch during this review:

1. `ABILITY_WEAVING_AND_MULTI_TREE_PROGRESSION.md`
2. `ALPHA_AND_SPECIAL_CREATURES.md`
3. `CHARACTER_INSPIRATION_AND_ORIGINAL_ROSTER.md`
4. `CHARACTER_SPECIFIC_POWERSET_REQUIREMENTS.md`
5. `CORE_GAMEPLAY_LOOP_AND_PLAYER_FEEDBACK.md`
6. `CREATURE_DIET_PREDATION_AND_CROSS_SPECIES_MUTATIONS.md`
7. `DESIGN_WORKFLOW_STEP_GATES_AND_LOOP_PREVENTION.md`
8. `EXPANDED_ABILITY_COVERAGE_MATRIX.md`
9. `GAME_DESIGN_BIBLE.md`
10. `HIDDEN_SKELETON_ASCENDANT.md`
11. `LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md`
12. `LUCK_AND_RANDOM_DISCOVERY_SYSTEM.md`
13. `MASTER_DESIGN_INDEX_AND_PRESERVATION_RULES.md`
14. `MASTER_REQUIREMENTS_LEDGER.md`
15. `POWER_ABILITY_CATALOGUE.md`
16. `PROGRESSIVE_STAGE_TRANSITIONS_CELL_TO_COSMIC.md`
17. `SHADOW_SOVEREIGN_LIMIT_BREAKER_GOBLIN_ROUTES.md`
18. `SLIME_ACTION_GATED_EVOLUTION.md`
19. `SPECIES_AND_BODY_PLAN_CATALOGUE.md`
20. `SYSTEM_ALIGNMENT_AND_DEVELOPMENT_ROADMAP.md`
21. `ULTIMATE_ABILITIES_AND_ENVIRONMENTAL_DESTRUCTION.md`
22. `ULTIMATE_ABILITY_VERTICAL_SLICE_SPEC.md`
23. `VERTICAL_SLICE_01_CELLULAR_OPENING_TO_FIRST_EVOLUTION.md`
24. `WUKONG_INSPIRED_MYTHIC_STAFF_ASCENDANT.md`

The master index contains links to the design topics. The master requirements ledger tracks the main cross-system requirements. This audit itself is a new evidence record and must be added to the index.

## 3. Cross-system consistency checks

### 3.1 Evolution stages and opening simplicity

**Rule retained:** The full vision progresses from cellular survival through animal-scale and apex-creature survival, main-form action adventure, and later living-ship/cosmic exploration. The first minutes teach movement, absorption/gathering, evasion, and a basic attack before exposing complex menus.

**Audit result:** Compatible. The opening remains a deliberately small slice; later-stage systems are preserved as later milestones rather than deleted.

### 3.2 Creature ecology, diet, predation, and mutation

**Rule retained:** NPC creatures hunt suitable prey, forage or scavenge as appropriate, and respond to food availability. Diet can affect growth, condition, trait refinement, and eligible mutation opportunities. Cross-species diets can rarely produce coherent hybrid outcomes. Alpha and special creatures need distinct behavior/history/ecological influence, not only inflated statistics.

**Correction made:** Added a tightly bounded predator-prey relationship and one observable diet-driven growth/condition change plus an adaptation clue to the first-slice acceptance checklist. This demonstrates the core ecosystem idea without requiring a complete food-web simulator, guaranteed rare mutation, or Alpha boss in the opening.

### 3.3 Luck and progression fairness

**Rule retained:** Luck may produce early rare discoveries, unusual variants, or eligible mutation outcomes. It cannot bypass compatibility or create a mandatory rare-drop wall. Research alternatives, useful duplicates, and bad-luck protection are required design principles. Numeric probabilities remain unfinalized until testing.

**Audit result:** Compatible with creature rarity and special encounters. Exact rates and protection thresholds remain open tuning values, not missing design commitments.

### 3.4 Ability combinations and environmental effects

**Rule retained:** Ability combinations require eligibility and a defined recipe; a four-component set is a registered interaction, not four uncontrolled attacks at once. Costs, cooldowns, counters, chain-reaction limits, protected boundaries, persistence, collision/navigation, and save/load are explicit concerns.

**Correction made:** Added a dedicated master-ledger requirement for the ultimate-ability representative slice, including its Fire/Wind/Water combination and world-response acceptance criteria.

### 3.5 Knowledge versus ownership/mastery

**Rule retained:** Rumor, observation, research, recipe discovery, ability acquisition, stabilization, and mastery remain distinct states. Sharing knowledge does not automatically transfer another character's powers or mastery.

**Audit result:** Compatible across the luck, ecosystem, ability, and progression documents.

### 3.6 Character routes and originality

**Rule retained:** Specialized routes remain separately documented and should not be collapsed into generic classes. Inspiration from existing games or mythology describes broad desired qualities only; final names, character designs, story, and signature expression must be original.

**Audit result:** The route documents remain indexed. Final originality review is still required before release.

### 3.7 Death, persistence, multiplayer, and performance

**Rule retained:** Permanent character death applies to the full game vision, but the opening tutorial must not demand a permanent loss before the player understands its basic mechanics. Save/load, world persistence, multiplayer authority, and bounded simulation require their own implementation tests. Multiplayer remains part of the wider vision but must not block the first single-player slice.

**Audit result:** These are compatible when scope is respected: tutorial recovery is a slice-level teaching rule; permanent death is a full-game rule. Multiplayer/network requirements are later-stage validation, not evidence that they are already built.

## 4. Corrections committed during this audit

1. **First vertical slice:** Replaced the outdated open-decision list with the accepted provisional baseline for starter traits, evolution trigger, animal-stage layout, camera, and simulation budget.
2. **First vertical slice:** Added a minimal predator-prey interaction, diet-driven condition/growth change, and possible adaptation clue to its acceptance checklist.
3. **First vertical slice:** Clarified that the slice design baseline is frozen for implementation handoff, while numeric tuning and runtime verification remain outstanding.
4. **Master requirements ledger:** Added the ultimate-ability vertical slice as an explicit traceable requirement and updated the opening-slice status.
5. **Design workflow:** Updated the current work ledger to reflect the frozen opening-slice design baseline and recorded this audit as the consistency review/correction pass.

## 5. Remaining gaps and honest status

- The index and ledger are an initial traceability system; they do not yet atomize every paragraph and edge case from all documents into individual requirement IDs.
- The current design is not a playable implementation. No runtime, gameplay, performance, save/load, or automated acceptance tests were executed by this audit.
- Exact balance values remain open: rarity probabilities, bad-luck thresholds, mutation rates, precise creature counts, and simulation budgets.
- The first slice's detailed edge-case/system specifications and UI/feedback rules still need to be turned into implementation-ready acceptance criteria.
- The ultimate-ability slice is a separate representative system specification and is not part of the initial cellular opening unless explicitly brought into scope later.
- A second independent backup of the repository has not been created by this audit.

## 6. Scope and preservation decision

No feature or route was removed as part of this audit. Features beyond the first slice remain **deferred, not deleted**. The current slice scope is frozen at the design level to prevent circular redesign; it can be reopened only for a concrete inconsistency, an acceptance criterion that cannot be met, or new evidence from implementation/playtesting.

## 7. Next step

**Next design step:** Specify the frozen first slice's system interactions and edge cases, then define the minimum UI/feedback needed to teach and communicate them. Keep this step bounded to the cellular opening and the compact animal habitat. Do not expand the full creature catalogue, Alpha catalogue, cosmic endgame, or multiplayer architecture during this step.

**Current status:** Documentation inventory and one consistency/correction pass completed. Design scope frozen for the first slice. Implementation and runtime verification deferred.
