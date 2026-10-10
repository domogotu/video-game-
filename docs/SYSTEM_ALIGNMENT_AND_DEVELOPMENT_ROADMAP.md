# System Alignment and Development Roadmap

**Project:** Lethal Absorption  
**Tagline:** Consume. Evolve. Survive.  
**Status:** Design alignment and implementation planning only. This document does not claim that a playable build, runtime systems, or tests exist.

## Purpose

This document is the consistency checkpoint for new features and existing specifications. Every proposal should reinforce the same player experience: consume and investigate the world, earn compatible traits and powers, experiment through meaningful use, weave techniques together, evolve the body, master the result, and survive the consequences.

Use this roadmap to resolve contradictions before expanding the content catalogue. It supplements, rather than silently replaces, the Game Design Bible and system-specific specifications.

## Product pillars

1. **Evolution is earned:** growth follows actions, discoveries, compatibility, resources, mastery, and world milestones—not arbitrary menu purchases alone.
2. **Builds are expressive:** no fixed classes; anatomy, body plan, powers, traits, skills, forms, and play style create a distinct character.
3. **Systems connect without collapsing together:** each tree has a clear purpose and communicates prerequisites and effects to the others.
4. **Experimentation creates knowledge:** players can discover techniques through deliberate use, environmental interactions, analysis, training, and trials.
5. **Complexity has readable controls:** powerful combinations must be previewable, configurable, learnable, and usable without requiring frame-perfect execution for basic functions.
6. **Power has counterplay:** every strong effect has relevant costs, constraints, vulnerabilities, interruption windows, or tactical answers.
7. **The world responds consistently:** anatomy, terrain, resources, NPC knowledge, ecology, and multiplayer state must obey shared rules.
8. **Permanent consequences remain meaningful:** death, absorption, PvP, and legacy systems must not bypass the established permanent-death rule.
9. **Character-specific routes remain specific:** the six requested character routes require individual source-scoped inventories; generic archetypes do not count as complete.
10. **Implementation status is evidence-based:** a design proposal is not an implementation; a code change is not proof of a working runtime; tests must have recorded results.

## Unified progression architecture

The trees have separate responsibilities and explicit links:

- **Skill Tree — execution:** timing, movement, defense, technique, weapon use, crafting, and combat control.
- **Ability Tree — actions:** active techniques, attacks, utility, mobility, summons, barriers, and variants.
- **Power Tree — source and control:** elemental, energy, supernatural, magical, psychic, cosmic, or other power sources.
- **Mutation Tree — body:** organs, anatomy, body plans, resistances, adaptations, and biological trade-offs.
- **Trait Tree / Trait Ledger — properties and compatibility:** passive effects, acquired properties, stabilization, expression, and suppression.
- **Mastery Tree — refinement:** reliability, efficiency, control, timing windows, and earned variants.
- **Synthesis / Weaving Tree — invention:** registered recipes that combine compatible ingredients into new outputs.
- **Form / Evolution Tree — capacity and transformation:** lineage branches, evolutionary stages, form-bound abilities, and new system capacity.

These trees must not become eight disconnected progression currencies. A recipe can require an ability from one tree, a source from another, a stabilizing trait, an anatomy requirement, and a mastery threshold. The UI must explain every missing requirement. Unlocking one component never grants all dependent components automatically.

## Four-component ability weaving

The player's controller idea is preserved: one input set can represent a technique with up to four compatible components. Example: hold LT and press X.

The four components define a **registered, staged weave**, not four unrestricted attacks firing simultaneously.

Illustrative staged example:
1. Fire produces a basic flame attack.
2. Fire plus a separately learned refinement changes control, density, or delivery.
3. Adding Wind changes spread, travel, range, or pressure.
4. Adding Water may produce a steam or thermal-pressure reaction if the recipe, order, anatomy, and power sources are compatible.

A fourth ingredient does not automatically increase damage. It can improve control, movement, defense, efficiency, status interactions, or unlock a branch. An incompatible combination must have a legible outcome: blocked with an explanation, unstable with a cost/risk, or redirected into a defined alternative. No component may be duplicated to gain free power; repeated elemental inputs require a distinct learned refinement or amplification component.

Input defaults remain configurable. LT+X may activate the base output, while a supported hold/charge or alternate gesture selects a higher stage or registered branch. Keyboard/mouse remapping, accessible alternatives, clear previews, costs, and cancel paths are required.

## Learn-through-use loop

1. **Exposure:** observe, receive, or attempt an ability interaction.
2. **Hypothesis:** record a possible relationship or recipe clue.
3. **Discovery:** complete a qualifying sequence, challenge, or environmental experiment.
4. **Stabilization:** meet any material, biomass, trait, training, or compatibility requirement.
5. **Mastery:** improve reliability, control, efficiency, or access to defined branches through successful use.
6. **Synthesis or evolution:** unlock a new registered recipe, variant, trait, or form capacity at a meaningful milestone.

Repetition alone should not automatically grant every ability. Practice must be relevant, and discoveries must respect source, compatibility, resource, and progression rules. The Shared Discovery Network shares verified knowledge; it does not transfer personal ownership, mastery, rare components, or unlocks automatically.

## Character-specific routes

Maintain six dedicated route inventories for:
- Sung Jinwoo — *Solo Leveling*.
- Goku — *Dragon Ball*.
- The goblin protagonist of *Re:Monster*; verify the intended name and adaptation scope.
- Sun Wukong — distinguish mythic sources from individual adaptations and games.
- Rimuru Tempest — *That Time I Got Reincarnated as a Slime*.
- Ainz Ooal Gown — *Overlord*.

For every route, track individual in-scope powers, active skills, passives, traits, transformations, summons, equipment-linked effects, upgrades, unlock conditions, dependencies, costs, counters, and status. Generic labels such as “energy blast,” “summons,” or “shadow powers” do not satisfy route completeness. Record source/version and deferred entries. Before commercial use of protected characters or expressive elements, confirm rights/licensing or formally approve a distinct original adaptation.

## Shared rules every feature must obey

- **Anatomy:** an ability requiring wings, lungs, hands, a core, or another organ must check whether the current form has it or a valid substitute.
- **Resources:** costs, upkeep, cooldowns, recovery, and overload must be consistent across abilities and forms.
- **World effects:** terrain, NPCs, ecology, evidence, and structures react according to defined and persistent rules.
- **Multiplayer authority:** the server validates recipe ownership, compatibility, stage, timing, resources, cooldowns, and effects.
- **Balance:** strong combinations have counters and limits; no unlimited recipe explosion, free stacking, or unintended infinite-resource loops.
- **Death and PvP:** no combination, legacy, copy, or progression route may silently resurrect a permanently dead character or bypass established challenge/consent rules.
- **Discovery:** clues may be shared; personal unlocks, mastery, compatibility, and acquisition remain individual unless a rule explicitly says otherwise.
- **Accessibility:** remapping, readable feedback, and non-frame-perfect alternatives are part of the design, not post-launch extras.
- **Clarity:** players can inspect what an ability does, what it costs, why it is locked, what a combination changes, and how opponents can counter it.

## Delivery order and gates

### Gate 1 — Consolidate rules
Resolve terminology, progression-tree responsibilities, recipe terminology, resource conventions, input vocabulary, character-route scope, and implementation-status labels. Flag contradictions rather than quietly inventing answers.

### Gate 2 — Specify one vertical slice
Fully specify one four-stage elemental weave, one incompatible recipe, one stabilizing trait, one use-based discovery, one mastery improvement, and at least one form/anatomy restriction. Include UI states, failure paths, resource costs, counters, accessibility behavior, and multiplayer validation.

### Gate 3 — Prototype and test
When a codebase and playable runtime are available, implement the slice behind a defined interface and add unit/integration tests. Record build commands, environment, test results, known gaps, and reproducible evidence. Do not mark a gate complete based on documentation alone.

### Gate 4 — Validate progression and balance
Check resource loops, exploit paths, stage transitions, counterplay, discovery fairness, PvP behavior, death persistence, and server/client agreement. Expand only after the slice passes agreed acceptance criteria.

### Gate 5 — Expand in tracked batches
Add recipe families, mutation interactions, forms, and the six character-specific catalogues in bounded groups. Each batch needs prerequisites, source traceability where applicable, test cases, deferred-item tracking, and a clear implementation status.

### Gate 6 — Final verification
Run the full planned verification only after the agreed implementation groups are complete. Separate design review, static checks, automated tests, runtime/playtest evidence, and release readiness. Never describe a design-only repository as a finished game.

## Required status vocabulary

- **Proposed:** idea recorded, unresolved.
- **Specified:** rules and acceptance criteria documented.
- **Prototyped:** an experimental implementation exists.
- **Implemented:** code is integrated in the target project.
- **Tested:** named tests were run and results recorded.
- **Verified:** acceptance criteria passed with reproducible evidence.
- **Deferred:** intentionally postponed with reason and planned milestone.
- **Blocked:** cannot proceed until a named dependency or decision is resolved.

Status changes must cite concrete repository files, commits, test outputs, or runtime evidence.

## Open decisions to keep visible

Do not silently treat these as settled until the design owner confirms them:
- Whether the named franchise characters appear directly under a licensed arrangement or become separately approved original adaptations.
- Exact source/version boundaries for each character-specific route.
- Final controller/keyboard input mapping and stage-selection gestures.
- Recipe discovery visibility and how much the Evolution Atlas reveals.
- Exact costs, cooldowns, mastery thresholds, level curves, and PvP tuning.
- Which inventory/progression elements carry into NG+.
- The actual engine, runtime architecture, and implementation/test environment.

## Definition of a consistent new feature

Before adding any feature, answer:
1. Which core pillar does it support?
2. Which existing systems does it touch?
3. What unlocks it, and what does it require?
4. What does it cost and what counters it?
5. How does it interact with anatomy, forms, world state, multiplayer, and permanent death?
6. How does the player understand and control it?
7. What acceptance tests prove it works?
8. Is it proposed, specified, prototyped, implemented, tested, verified, deferred, or blocked?

If these questions cannot be answered, record the idea as proposed and resolve the missing design before presenting it as complete.

**Project status:** This roadmap is a design alignment document. It does not claim that the listed features are implemented, playable, or tested.
