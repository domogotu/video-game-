# Lethal Absorption — Master Requirements Ledger

**Status:** Initial documentation inventory; design requirements only  
**Source of truth:** The topic-specific specifications linked below, with the Game Design Bible as the central vision document and the Master Design Index as the navigation/preservation policy.  
**Important:** Statuses here describe documentation maturity, not implementation. No requirement is considered implemented or tested based on documentation alone.

## 1. Status meanings

- **Specified:** described in a current design document; still needs implementation and validation.
- **Proposed/open:** concept exists, but important design decisions remain.
- **Deferred:** preserved for a later milestone, not removed.
- **Not verified:** no playable-build evidence has been established.

## 2. Master requirements

| ID | Requirement | Source of detail | Acceptance criteria | Current status |
|---|---|---|---|---|
| VISION-001 | Preserve the full evolutionary action-RPG vision from cell to cosmic forms. | [Game Design Bible](GAME_DESIGN_BIBLE.md); [Stage Transitions](PROGRESSIVE_STAGE_TRANSITIONS_CELL_TO_COSMIC.md) | All stages and their distinct gameplay remain represented in the roadmap. | Specified; not implemented |
| ONBOARD-001 | Keep the opening simple and teach controls gradually. | [First Vertical Slice](VERTICAL_SLICE_01_CELLULAR_OPENING_TO_FIRST_EVOLUTION.md); [Core Gameplay Loop](CORE_GAMEPLAY_LOOP_AND_PLAYER_FEEDBACK.md) | New players can move, absorb/gather, evade, and attack before deep systems are introduced. | Specified; not tested |
| STAGE-001 | Each evolutionary stage must introduce meaningfully different gameplay. | [Stage Transitions](PROGRESSIVE_STAGE_TRANSITIONS_CELL_TO_COSMIC.md) | Every stage has a clear fantasy, mechanics, transition trigger, and carry-forward history. | Specified; not implemented |
| PROG-001 | Keep character level, ability level, acquisition, stabilization, mastery, and evolution distinct. | [Game Design Bible](GAME_DESIGN_BIBLE.md); [Ability Weaving](ABILITY_WEAVING_AND_MULTI_TREE_PROGRESSION.md) | UI and systems do not conflate these progression dimensions. | Specified; not tested |
| ATLAS-001 | Provide a history-sensitive, expandable evolution/progression atlas. | [Game Design Bible](GAME_DESIGN_BIBLE.md); [System Alignment](SYSTEM_ALIGNMENT_AND_DEVELOPMENT_ROADMAP.md) | Availability reflects discovered routes, compatibility, and character history; exact scale is balanced in stages. | Proposed; large-scale scope deferred |
| ABILITY-001 | Support broad ability families with compatible modifications and combinations. | [Power Catalogue](POWER_ABILITY_CATALOGUE.md); [Expanded Coverage](EXPANDED_ABILITY_COVERAGE_MATRIX.md) | Each implemented ability defines eligibility, cost, behavior, counterplay, and feedback. | Specified; not implemented |
| WEAVE-001 | Ability weaving combines compatible components into a registered interaction rather than uncontrolled simultaneous effects. | [Ability Weaving](ABILITY_WEAVING_AND_MULTI_TREE_PROGRESSION.md) | Recipes obey compatibility, resource/cooldown rules, and chain-reaction limits. | Specified; not tested |
| BODY-001 | Body plan and anatomy affect movement, interaction, combat, and compatible traits. | [Species and Body Plans](SPECIES_AND_BODY_PLAN_CATALOGUE.md); [Character Powersets](CHARACTER_SPECIFIC_POWERSET_REQUIREMENTS.md) | A body configuration changes actual capabilities and constraints, not just appearance. | Specified; not implemented |
| ECO-001 | Populate the world with creatures that have distinct species, habitats, and behavior. | [Living Creature Ecosystem](LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md) | Each implemented species has a role, valid habitat, behavior states, and discoverable cues. | Specified; not implemented |
| ECO-002 | NPC creatures hunt, forage, scavenge, evade, compete, and respond to food availability. | [Creature Diet and Predation](CREATURE_DIET_PREDATION_AND_CROSS_SPECIES_MUTATIONS.md) | At least one predator-prey loop runs coherently with bounded simulation and observable outcomes. | Specified; not tested |
| ECO-003 | NPC diet can affect growth, condition, trait refinement, and mutation opportunities. | [Creature Diet and Predation](CREATURE_DIET_PREDATION_AND_CROSS_SPECIES_MUTATIONS.md) | Diet outcomes follow eligibility rules; repeated feeding cannot create infinite growth or rolls. | Specified; not tested |
| ECO-004 | Compatible cross-species diets can rarely produce novel hybrid abilities or mutations. | [Creature Diet and Predation](CREATURE_DIET_PREDATION_AND_CROSS_SPECIES_MUTATIONS.md) | An eligible example can produce a documented hybrid result; incompatible combinations cannot bypass rules. | Specified; not tested |
| ECO-005 | Alpha and special creatures have meaningful identity and ecological influence. | [Alpha and Special Creatures](ALPHA_AND_SPECIAL_CREATURES.md) | An Alpha differs through behavior, history, trait, or regional influence—not only inflated stats. | Specified; later milestone |
| ECO-006 | Creature discovery includes observation, research, variants, and optional bonding/companions where appropriate. | [Living Creature Ecosystem](LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md) | Journal distinguishes seen, observed, studied, bonded, absorbed, and mastered states. | Specified; scope deferred |
| LUCK-001 | Random luck can grant early rare encounters or eligible discoveries. | [Luck and Random Discovery](LUCK_AND_RANDOM_DISCOVERY_SYSTEM.md) | Eligible rare outcomes are possible and clearly recorded; luck cannot violate compatibility. | Specified; not balanced |
| LUCK-002 | Essential progression remains possible without lucky drops. | [Luck and Random Discovery](LUCK_AND_RANDOM_DISCOVERY_SYSTEM.md); [Alpha and Special Creatures](ALPHA_AND_SPECIAL_CREATURES.md) | Every required progression gate has a deterministic or repeatable alternative route. | Specified; not tested |
| DISC-001 | Distinguish rumors, observations, verified knowledge, acquisition, stabilization, and mastery. | [Living Creature Ecosystem](LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md); [Game Design Bible](GAME_DESIGN_BIBLE.md) | Journal and progression state never misrepresent a clue as an owned/mastered ability. | Specified; not implemented |
| ULT-001 | The representative ultimate-ability slice validates a bounded Fire/Wind/Water combination and persistent world response. | [Ultimate Ability Vertical Slice](ULTIMATE_ABILITY_VERTICAL_SLICE_SPEC.md); [Ultimate Abilities and Destruction](ULTIMATE_ABILITIES_AND_ENVIRONMENTAL_DESTRUCTION.md) | Eligible materials react correctly; incompatible recipes are bounded; protected boundaries, costs, persistence, collision/navigation, and effect budgets remain valid. | Specified; implementation and runtime tests deferred |
| WORLD-001 | World changes and ecosystem consequences persist coherently and remain bounded. | [Ultimate Abilities and Destruction](ULTIMATE_ABILITIES_AND_ENVIRONMENTAL_DESTRUCTION.md); [Game Design Bible](GAME_DESIGN_BIBLE.md) | State survives save/load; protected areas and critical mission states remain valid. | Specified; not tested |
| PERF-001 | Simulate nearby creatures in detail and distant ecology at a lower cost. | [Creature Diet and Predation](CREATURE_DIET_PREDATION_AND_CROSS_SPECIES_MUTATIONS.md); [Living Creature Ecosystem](LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md) | Simulation respects defined CPU/entity budgets without incoherent population jumps. | Proposed; budget not measured |
| SAFETY-001 | Powerful abilities and mutations have costs, counters, and chain-reaction limits. | [Ultimate Abilities](ULTIMATE_ABILITIES_AND_ENVIRONMENTAL_DESTRUCTION.md); [Ability Weaving](ABILITY_WEAVING_AND_MULTI_TREE_PROGRESSION.md) | No infinite resource, damage, destruction, or mutation loop can be exploited. | Specified; not tested |
| NARR-001 | Sapient species retain agency, culture, and distinct treatment from ordinary prey/resources. | [Living Creature Ecosystem](LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md); [Creature Diet and Predation](CREATURE_DIET_PREDATION_AND_CROSS_SPECIES_MUTATIONS.md) | Core progression does not require treating sapient beings as interchangeable loot. | Specified; not tested |
| IP-001 | All shipped creative expression is original despite broad genre inspirations. | [Character Inspiration and Roster](CHARACTER_INSPIRATION_AND_ORIGINAL_ROSTER.md); special-route documents | Final names, designs, assets, story, and signature presentation pass originality review. | Required; review outstanding |
| ROUTE-001 | Preserve distinct hidden and specialized evolution routes. | [Slime Route](SLIME_ACTION_GATED_EVOLUTION.md); [Skeleton Route](HIDDEN_SKELETON_ASCENDANT.md); [Shadow/Limit Breaker/Goblin Routes](SHADOW_SOVEREIGN_LIMIT_BREAKER_GOBLIN_ROUTES.md); [Staff Ascendant](WUKONG_INSPIRED_MYTHIC_STAFF_ASCENDANT.md) | Each route retains its prerequisites, unique identity, action gates, risks, and reward structure. | Specified; not implemented |
| SLICE-001 | Build and verify one small opening slice before expanding the first milestone. | [First Vertical Slice](VERTICAL_SLICE_01_CELLULAR_OPENING_TO_FIRST_EVOLUTION.md); [Workflow Gates](DESIGN_WORKFLOW_STEP_GATES_AND_LOOP_PREVENTION.md) | Scope and acceptance criteria are frozen; implementation tasks and runtime evidence remain separate. | Design baseline frozen; audit review recorded; implementation deferred |
| DOC-001 | Every accepted idea remains recorded and traceable. | [Master Design Index and Preservation Rules](MASTER_DESIGN_INDEX_AND_PRESERVATION_RULES.md) | All current documents are indexed; new ideas have a source, status, dependencies, and acceptance criteria. | Index created; inventory ongoing |
| TEST-001 | Never claim implementation, tests, or verification without evidence. | [Master Design Index and Preservation Rules](MASTER_DESIGN_INDEX_AND_PRESERVATION_RULES.md); [Workflow Gates](DESIGN_WORKFLOW_STEP_GATES_AND_LOOP_PREVENTION.md) | Each implemented milestone has named test evidence and a recorded pass/fail status. | Required workflow rule |

## 3. Deferred, not deleted

These are intentionally beyond the initial cellular slice, not rejected:
- Full open-world and planet-scale streaming.
- Full creature roster, Alpha catalogue, rare variants, and detailed food-web simulation.
- Deep companion, bonding, breeding, migration, and ecosystem population systems.
- Full ability catalogue, all synthesis recipes, environmental destruction at large scales, and cosmic powers.
- Later evolutionary stages, biological spaceflight, planetary/cosmic content, and specialized secret routes.
- Multiplayer, PvP, shared discovery, and other network-dependent systems.
- Final numeric balancing for levels, drop chances, pity thresholds, mutation rates, and simulation budgets.
- Final production art, audio, animation, narrative, and accessibility implementation.

## 4. Inventory notes and limits

This ledger covers the major cross-system requirements represented by the current indexed design documents. It is an initial traceability ledger, not proof that every sentence from every file has been atomized into a requirement. The next consistency pass should compare this ledger against the complete current contents of each specification, then add missing requirement IDs without deleting existing entries.

When a requirement changes, keep its ID when its intent remains the same, update the source and acceptance criteria, and record the decision. Create a new ID for a genuinely new requirement. Do not mark a requirement Verified until the implementation and evidence exist.

**Current implementation state:** Design repository/documentation. Playable implementation, automated tests, and end-to-end verification have not been established by this ledger.
