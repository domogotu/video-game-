# Lethal Absorption — Master Design Index and Preservation Rules

**Repository:** https://github.com/domogotu/video-game-  
**Primary branch:** `main`  
**Tagline:** Consume. Evolve. Survive.  
**Document status:** Project navigation and preservation policy  
**Project truth:** Design documentation is not evidence that a playable game exists or that a feature has been implemented, tested, or verified.

## 1. Why this file exists

Lethal Absorption is a large, connected game concept. This file is the navigation map and preservation policy so ideas do not get lost across conversations or buried in separate documents.

**Rule: no accepted idea is discarded just because it is not part of the first playable slice.** It must be recorded in the appropriate specification or an explicit backlog/deferred list. If a decision changes, record the replacement and why; do not silently overwrite the history of a meaningful decision.

GitHub is the persistent design record. Each committed change is part of repository history. This is not a substitute for an independent backup of the repository, so periodic repository exports or a second remote backup remain recommended.

## 2. Where to start

1. Read the [README and project overview](../README.md) for the high-level game concept and current status.
2. Read the [Game Design Bible](GAME_DESIGN_BIBLE.md) for the core vision, progression, game pillars, and overall systems.
3. Use this master index to find the detailed specification for each subsystem.
4. Use the [Master Requirements Ledger](MASTER_REQUIREMENTS_LEDGER.md) to track cross-system requirements, dependencies, status, and acceptance criteria.
5. Read the [System Alignment and Development Roadmap](SYSTEM_ALIGNMENT_AND_DEVELOPMENT_ROADMAP.md) before planning implementation.
6. Read the [Design Workflow, Step Gates, and Loop Prevention](DESIGN_WORKFLOW_STEP_GATES_AND_LOOP_PREVENTION.md) before continuing project work.
7. Use the [first cellular vertical slice](VERTICAL_SLICE_01_CELLULAR_OPENING_TO_FIRST_EVOLUTION.md) as the initial scope boundary; the first slice is not the entire game.

## 3. Current design-document index

### Core vision, progression, and workflow

- [Game Design Bible](GAME_DESIGN_BIBLE.md) — central game vision, pillars, character progression, Evolution Atlas, world and core systems.
- [System Alignment and Development Roadmap](SYSTEM_ALIGNMENT_AND_DEVELOPMENT_ROADMAP.md) — how systems fit together and the proposed delivery sequence.
- [Design Workflow, Step Gates, and Loop Prevention](DESIGN_WORKFLOW_STEP_GATES_AND_LOOP_PREVENTION.md) — one finite step at a time, acceptance criteria, honest statuses, review and closure.
- [Progressive Stage Transitions: Cell to Cosmic](PROGRESSIVE_STAGE_TRANSITIONS_CELL_TO_COSMIC.md) — progression from early cellular play through later evolutionary and cosmic stages.
- [Core Gameplay Loop and Player Feedback](CORE_GAMEPLAY_LOOP_AND_PLAYER_FEEDBACK.md) — action loops, feedback, readability, and player learning.
- [First Vertical Slice: Cellular Opening to First Evolution](VERTICAL_SLICE_01_CELLULAR_OPENING_TO_FIRST_EVOLUTION.md) — deliberately small opening sequence and first stage transition.

### Evolution, abilities, mutations, and combat

- [Power and Ability Catalogue](POWER_ABILITY_CATALOGUE.md) — broad ability families and possible powers.
- [Expanded Ability Coverage Matrix](EXPANDED_ABILITY_COVERAGE_MATRIX.md) — coverage across gameplay situations and ability families.
- [Ability Weaving and Multi-Tree Progression](ABILITY_WEAVING_AND_MULTI_TREE_PROGRESSION.md) — compatible ability combinations, progression, and weaving rules.
- [Character-Specific Powerset Requirements](CHARACTER_SPECIFIC_POWERSET_REQUIREMENTS.md) — character-specific route requirements and coherent power identities.
- [Ultimate Abilities and Environmental Destruction](ULTIMATE_ABILITIES_AND_ENVIRONMENTAL_DESTRUCTION.md) — environmental impact, world state, limits, costs, and safeguards.
- [Ultimate Ability Vertical Slice Specification](ULTIMATE_ABILITY_VERTICAL_SLICE_SPEC.md) — bounded representative test design for ultimate-ability behavior.
- [Species and Body-Plan Catalogue](SPECIES_AND_BODY_PLAN_CATALOGUE.md) — species/body-plan concepts that can inform anatomy and evolution.

### Creature ecosystem, collection, luck, and mutations

- [Living Creature Ecosystem and Collection-Inspired Discovery](LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md) — creature discovery, habitats, behaviors, journal, optional bonding/companions, variants, and ecological interactions.
- [Creature Diet, Predation, and Cross-Species Mutations](CREATURE_DIET_PREDATION_AND_CROSS_SPECIES_MUTATIONS.md) — NPC diets, wild hunting, food webs, growth, and cross-species mutation opportunities.
- [Alpha and Special Creatures](ALPHA_AND_SPECIAL_CREATURES.md) — Alpha individuals, rare variants, apex/ancient/anomalous/named creatures, encounter rules, and ecological effects.
- [Luck and Random Discovery System](LUCK_AND_RANDOM_DISCOVERY_SYSTEM.md) — chance, rare early unlocks, bad-luck protection, useful duplicates, and fair progression.

### Special evolutionary routes and original character direction

- [Character Inspiration and Original Roster](CHARACTER_INSPIRATION_AND_ORIGINAL_ROSTER.md) — original roster and broad genre inspiration, with an originality boundary.
- [Hidden Skeleton Ascendant](HIDDEN_SKELETON_ASCENDANT.md) — secret skeleton evolution route.
- [Shadow Sovereign, Limit Breaker, and Goblin Routes](SHADOW_SOVEREIGN_LIMIT_BREAKER_GOBLIN_ROUTES.md) — multiple distinct earned evolution routes.
- [Slime Action-Gated Evolution](SLIME_ACTION_GATED_EVOLUTION.md) — hidden slime route with specific in-world action gates.
- [Wukong-Inspired Mythic Staff Ascendant](WUKONG_INSPIRED_MYTHIC_STAFF_ASCENDANT.md) — original staff-fighter route informed by broad mythic action-adventure qualities.

## 4. Connected requirements that must not be lost

- [Master Documentation Consistency Audit](MASTER_DOCUMENTATION_CONSISTENCY_AUDIT.md) — current inventory and consistency/correction pass.

The following are cross-system commitments. New specifications must remain consistent with them or explicitly propose a reviewed change.

- The experience starts simple and teaches movement, absorption/gathering, evasion, and a basic attack before exposing deep menus.
- The larger game changes gameplay across evolutionary stages rather than merely reskinning one combat loop.
- There are no fixed classes; anatomy, compatible traits, mutations, knowledge, and choices shape builds.
- Character level, ability level, mastery, acquisition, stabilization, and evolution are separate progression concepts.
- Luck can enable rare early discoveries but cannot create a mandatory progression wall.
- NPC creatures have their own diets and behaviors. Wild predators hunt appropriate prey; prey evade, hide, group, or defend.
- Diet can affect growth, conditioning, refinements, mutation opportunities, and rare cross-species abilities, but no meal guarantees a power.
- Alpha and special creatures differ through behavior, ecology, history, or unique adaptations—not just inflated health.
- Creatures can be observed, researched, avoided, helped, bonded with where appropriate, battled, or absorbed when allowed. Not every creature supports every interaction.
- Ecosystem consequences must be coherent and observable without simulating every organism at full detail across the entire world.
- Sapient species have agency and culture; they are not interchangeable loot containers.
- Rare discoveries must have clues or alternate routes where needed; essential progress cannot rely on a specific random spawn.
- Major abilities and environmental effects need compatibility rules, costs, counterplay, performance limits, and persistence/save rules.
- Use original characters, species, names, designs, lore, and expression; inspiration is not permission to copy another franchise.
- Multiplayer and endgame scale must not block delivery of the first single-player vertical slice.
- Never describe a planned system as implemented, tested, verified, or production-ready without evidence.

## 5. How to preserve new ideas

For every new idea, use this process:

1. **Capture it first.** Record the requirement in the relevant specification or create a clearly named new document. Do not rely on chat history alone.
2. **Keep the original intent.** Translate examples into requirements, behaviors, constraints, and acceptance criteria without losing the user's core idea.
3. **Link the system relationships.** Explain how the idea interacts with progression, ecosystem, combat, UI, persistence, performance, and accessibility where relevant.
4. **Record unresolved choices.** Label undecided details as open decisions; do not invent final numeric values or silently choose a permanent answer.
5. **Separate scope from omission.** If an idea is too large for the current slice, mark it deferred/backlog—not removed.
6. **Check consistency.** Search for conflicts with existing specs and note which file is authoritative for that topic.
7. **Commit and verify.** Commit changes to GitHub, then fetch the resulting file to verify its actual contents.
8. **Report truthfully.** State what was documented, what was changed, and what remains unimplemented or untested.

## 6. Version history and recovery

- Use Git commits as the record of accepted design changes.
- Prefer additive updates or carefully scoped edits; do not replace broad documents with shortened summaries.
- Before substantial edits, fetch the current version and its current blob SHA.
- After an edit, fetch the saved version and verify key sections.
- When a design decision is superseded, retain the reason and prior decision in a change note where material.
- Do not delete an idea because it is difficult, expensive, or outside the current milestone. Move it to a deferred list with dependencies and rationale.
- A second independent repository backup is recommended. This index does not claim that a separate backup has been created.
- If any file is missing, search repository history and branches before reconstructing it from memory.

## 7. Status vocabulary

Use these statuses consistently:

- **Captured:** idea recorded, not yet specified in sufficient detail.
- **Proposed:** one possible approach, awaiting a decision.
- **Specified:** behavior and constraints documented.
- **Ready for review:** enough detail exists for a bounded review.
- **Scope frozen:** scope and acceptance criteria are fixed for the current step.
- **Implemented:** actual code/assets exist in the project.
- **Tested:** named tests or playtests were run, with results recorded.
- **Verified:** acceptance criteria passed with evidence.
- **Deferred:** deliberately moved to a later milestone, still preserved.
- **Blocked:** a named dependency prevents progress.

Documentation alone does not move a feature to Implemented, Tested, or Verified.

## 8. Immediate next preservation step

Before adding more large feature concepts, conduct a **documentation inventory and consistency pass**:
- Compare the current repository files with this index.
- Check for duplicate or conflicting rules across the Game Design Bible and subsystem documents.
- Identify important ideas that exist only in conversation and capture them without expanding their scope.
- Create one consolidated requirements ledger with IDs, source document, dependencies, status, and acceptance criteria.
- Mark what belongs to the first vertical slice versus later stages.
- Do not begin implementation or claim the game is playable as part of this documentation pass.

**Completion criteria for preservation:** every currently tracked design document is indexed; important cross-system rules are recorded; deferred ideas remain visible; repository content has been fetched and verified; implementation status is stated honestly.
