# Lethal Absorption — Skill Tree and Evolution Atlas

> **Status:** Approved design direction / design-only. This document specifies intended behavior; it does not claim that the UI, progression logic, saving, or balance has been implemented or tested.

## 1. Core rule

The skill tree is the **Evolution Atlas**: one persistent, zoomable progression system for anatomy, traits, abilities, mastery, transformations, fusions, and later planetary-to-cosmic evolution. It is not a set of fixed classes. Players shape a personal build through choices, actions, diet, absorbed genetic information, training, research, environmental survival, and discoveries.

The Atlas should have the depth and interconnected planning of a large ARPG passive tree, while keeping individual skills understandable and making the results visible in action-RPG combat. References are design touchstones only; all final names, artwork, interface, abilities, and lore must be original.

## 2. Three connected progression layers

1. **Evolution Atlas (build-wide):** persistent nodes that change what the character is, which systems they can access, and which branches or combinations become possible.
2. **Ability development (move-specific):** each ability has its own proposed level range of 1–20, branch choices, and unlockable mechanics or variants.
3. **Use-based mastery (execution):** improves through meaningful use, timing, and application. Mastery is separate from character level and does not automatically unlock every branch.

A character can be high-level while still learning a newly acquired ability. Unlocking a node should explain whether it grants a permanent trait, enables an option, modifies an ability, or merely reveals a research path.

## 3. Atlas zoom levels

- **Micro / cellular:** nutrient processing, membrane traits, sensing, movement, absorption, survival.
- **Organism / anatomy:** organs, limbs, armor, claws, tendrils, wings, tails, senses, regeneration, body plan, diet adaptations.
- **Combat / technique:** attacks, dodges, counters, launchers, ranged delivery, mobility, defense, summons, combos, ability modifiers.
- **Evolution / transformation:** new forms, temporary transformations, permanent body transitions, ultimates, signature techniques, anatomy loadouts.
- **Planetary:** environmental adaptation, habitat dominance, faction/ecosystem consequences, planet-completion capabilities.
- **Cosmic / advanced:** biological spaceflight and Living Ship Form, then later cosmic, dimensional, time, reality, creation, and godlike branches where the story and prerequisites support them.

Zoom changes how nodes are grouped and viewed, not whether earlier choices still matter. Later branches may connect back to early traits and abilities.

## 4. Major node families

| Node family | What it changes |
|---|---|
| Anatomy and organs | Body parts, silhouette, reach, hitboxes, movement, available attack routes |
| Traits and mutations | Resistances, senses, metabolism, regeneration, environmental adaptation, trade-offs |
| Active abilities | New player-triggered moves, powers, tools, summons, counters, mobility |
| Ability modifiers | Delivery, area, duration, targeting, behavior, resource cost, combo links |
| Passive adaptations | Persistent benefits and conditional effects |
| Technique / mastery gates | New combo routes, timing windows, cancels, follow-ups, alternate uses |
| Fusion / synergy | Compatible combinations between abilities, anatomy, elements, and traits |
| Transformations / ultimates | Form changes, altered move sets, signature finishers, high-cost abilities |
| Knowledge / research | Reveals hypotheses, requirements, and eligible routes without granting unearned powers |
| World / cosmic milestones | Stage-gated access to planetary, spaceflight, and late-game systems |

## 5. Node requirements and readable outcomes

Nodes can require one or more grounded prerequisites:
- Character level or evolutionary stage.
- A prior node, a compatible body part, or an ability.
- Genetic information or a specimen the player actually encountered and studied.
- Training, mastery, a qualifying combat/hunting feat, or a discovered interaction.
- Survival in a relevant environment or access to a credible location.
- Materials, research, or a story/world milestone when appropriate.

Requirements must be shown before a player commits. Each node preview states: **what it unlocks, what it changes, cost, prerequisites, benefits, trade-offs, compatibility, and how to test or use it**. The Codex must distinguish confirmed facts from hypotheses. A research clue may reveal a possible route but does not silently award a rare ability.

Do not make every branch require grind. Important paths should have alternate qualifying routes when thematically plausible; rare signature branches can require deliberate feats or discoveries.

## 6. Branching, cross-links, and hybrid builds

The Atlas should encourage exploration across branches rather than force a single class lane. Examples:
- Armor + tendrils → defensive grapples, anchoring, and counterattacks.
- Wings + ranged energy → aerial attack and repositioning routes.
- Regeneration + stamina training → endurance-focused combat with distinct resource limits.
- Senses + stealth anatomy → tracking and ambush routes.
- Gravity + mobility → movement control and combo extensions.
- Compatible fire + wind traits → a wider or more persistent flame effect, if rules, costs, and counters support it.

Cross-links require actual compatibility and prerequisites. The interface should explain why a combination works or is unavailable; it must not imply that every imaginable pair has a finished move. Build diversity should emerge from combinations, not from arbitrary class restrictions.

## 7. Active skill loadout and combat usability

Unlocking a move does not require equipping every move at once. Players use a configurable combat loadout with quick-access powers, defensive actions, mobility, signature techniques, and transformations. The power menu should support:
- Search and filter by effect, element/source, body part, range, role, resource, and compatibility.
- Preview of move behavior and combo links.
- Loadout presets for supported forms or activities.
- Clear indicators for locked, learned, equipped, mastered, and temporarily unavailable abilities.
- Controller remapping and accessible alternatives for complex input sequences.

Keep the Atlas for planning and progression; keep moment-to-moment combat readable. Avoid requiring deep menu navigation during fast combat.

## 8. Costs, trade-offs, and build integrity

Nodes can consume defined progression points, research, materials, or other explicit resources. Exact point generation, costs, and refund limits remain open for prototyping. Do not silently charge multiple currencies or hide recurring costs.

Powerful choices should create meaningful options, not universal upgrades. A mutation might improve armor while reducing agility; a large body plan may improve reach while changing stealth and traversal; a strong ability may cost more energy or expose a recovery window. Every significant drawback must be visible in advance and should have counterplay.

## 9. Respec, experimentation, and saved builds

- Early tutorial choices should be recoverable so players can learn the system without permanent punishment.
- Ordinary nodes should support a clearly disclosed respec policy. Exact currency, limits, and whether refunds require a safe location are open balance decisions.
- Story-defining permanent evolution should be clearly distinguished from reversible build choices and must never be disguised as an ordinary node.
- Let players save named build/loadout plans, compare two builds, preview their differences, and see which prerequisites remain unmet.
- Previewing or planning a build must not spend resources or alter the live character.
- Respec must not erase legitimate discoveries, Codex evidence, story flags, or earned mastery unless a future rule explicitly says so and explains it.

## 10. Character stage and access rules

The tree grows as the character evolves, but does not expose every cosmic power at the beginning. The player can see distant branches as silhouettes, hints, or locked routes without revealing every story secret. Requirements may depend on credible discoveries and evolutionary stage, not merely a high level.

The normal character level cap remains **1050**. Ability levels remain separate from character level. Completing the main story unlocks NG+ without requiring level 1050. Planetary completion and biological survival capabilities remain prerequisites for space progression; the character evolves into a **Living Ship Form** rather than using a conventional ship or vehicle.

## 11. Fairness, multiplayer, and permanent consequences

- PvP must not permanently delete a player character, remove owned assets, or steal their progression, regardless of rank or consent.
- Build previews and combat telegraphs must make major effects and reasonable counters legible.
- Avoid a single mandatory best build; balance through opportunity costs, situational strengths, resources, recovery, and counterplay.
- Shared discoveries may reveal knowledge, but personal prerequisites, compatibility, acquisition, and mastery still apply.
- Permanent death remains limited to eligible NPC-controlled threats under the project's separate fair-encounter rules; the skill tree must not bypass those protections.

## 12. Interface requirements

The Atlas should support a large canvas with pan, zoom, search, category filters, node details, prerequisite paths, and a build-planner mode. Distinguish visually between:
- Unknown / undiscovered
- Hypothesized
- Revealed but locked
- Available to unlock
- Unlocked / active
- Mastered
- Incompatible with current anatomy or form

Provide a compact summary of active build identity: key anatomy, main combat approach, strongest synergies, costs, weaknesses, and next suggested options. Suggestions are optional guidance, not automatic build decisions.

## 13. Suggested acceptance gates for a future implementation

1. Every node has a unique ID, description, prerequisites, costs, effects, compatibility rules, and state.
2. Prerequisites and cross-links are validated; circular dependency errors are rejected or explicitly supported by a defined rule.
3. Unlocking/refunding a node updates the character and displayed preview consistently.
4. Save/load preserves node state, ability levels, mastery, loadouts, research confidence, and evolution history.
5. Incompatible anatomy and form states are explained rather than silently failing.
6. Respec and build preview cannot duplicate resources or mutate the live build unexpectedly.
7. Controller and accessibility flows support browsing, comparing, and confirming nodes.
8. Multiplayer validation is authoritative for unlocks and prevents forged node states or cross-player data leakage.
9. Automated tests cover node graphs, prerequisites, costs, refunds, save migration, and combinations; playtests evaluate clarity, build diversity, and combat usability.

**Implementation status:** This is a design specification only. The Atlas UI, node data, unlock logic, respec system, save persistence, multiplayer validation, and acceptance tests have not been implemented or verified by this document.
