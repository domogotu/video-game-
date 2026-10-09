# Lethal Absorption — Action-Gated Slime Evolution Route

> **Status:** Approved design direction / detailed proposal. This is design documentation only; no playable implementation or tests are claimed.

## User intent

A player must be able to start as a weak, simple slime-like organism and become an exceptionally powerful slime through specific in-world actions, discoveries, survival feats, absorption choices, and evolution milestones. The player must not simply select the final form from a menu. The route should feel earned, visible in the Evolution Atlas, and replayable through different choices.

The user specifically referenced the progression and powers of the slime protagonist from *That Time I Got Reincarnated as a Slime*. Treat that as the desired reference for progression density and ability fantasy. **Exact franchise character identity, named signature skills, dialogue, story events, visual design, and other distinctive expression must not be copied into the unlicensed game.** If exact franchise content is desired, licensing is a separate requirement. Without a license, implement the same broad mechanics using original names, presentation, lore, and balanced rules.

## Route principles

1. Start weak. Early survival depends on consuming basic nutrients, hiding, escaping, and choosing safe encounters.
2. Unlock abilities through specific actions, not level alone.
3. Separate **discovery**, **eligibility**, **acquisition**, **evolution**, **mastery**, and **equipping/activating**.
4. Show prerequisites and progress in the Evolution Atlas, including hidden conditions only after discovery.
5. Make abilities available to the slime route once their conditions are met; do not silently grant mastery or skip costs.
6. Allow the player to develop a different route by what they absorb and how they behave.
7. Major milestones should trigger an explicit evolution scene, updated body/visual effects, a Codex entry, and new optional branches.
8. Maintain counters, costs, and multiplayer validation. High power does not mean unlimited use, universal knowledge, or immunity to all counterplay.

## Proposed action-gated progression

These are candidate gates for tuning, not a finalized numerical balance specification.

| Milestone | Required actions / proof | Unlocks |
|---|---|---|
| 0. Nutrient Blob | Gather enough safe nutrients to maintain biomass; survive first environmental hazard | Basic nutrient absorption, slow crawling/flowing, split-second concealment, basic threat sense |
| 1. Adaptive Slime | Absorb several distinct safe organic materials; survive a predator encounter by escaping or hiding | Elastic body, surface adhesion, basic shape change, controlled compression, improved environmental sensing |
| 2. Selective Devourer | Successfully absorb and analyze a compatible creature or specimen; identify what was gained and what was rejected | Selective absorption, material storage, trait analysis, limited mimicry of analyzed forms/materials |
| 3. Thinking Organism | Complete a research/discovery chain, solve a non-combat environmental challenge, and survive a serious encounter | Advanced cognition, parallel task processing at a limited rate, memory/Codex improvements, better threat assessment |
| 4. Adaptive Predator | Acquire compatible mobility and defense traits from different sources; demonstrate their use in combat and traversal | Combat-form shaping, limb/weapon shaping, improved regeneration, selected resistances, fast form switching |
| 5. Elemental Core | Encounter and study a world-specific elemental source; absorb a compatible sample and pass a stability test | One initial elemental affinity, energy conversion, elemental resistance, related branches based on world rules |
| 6. Arcane / Energy Specialist | Learn the world's energy system through observation, research, practice, and a meaningful trial | Energy sensing, controlled energy storage, ranged projection or barrier branch, resource-efficient use with mastery |
| 7. Multi-Core Evolution | Acquire and stabilize several compatible traits/cores; resolve instability through research or a rare event | Multiple ability slots, ability synthesis, advanced barrier, expanded storage, stronger analysis, selective resistance |
| 8. Sovereign Slime | Complete a high-stakes personal feat, defeat or resolve a qualifying apex encounter, and satisfy world-specific evolution conditions | Major body evolution, sovereign aura/pressure, advanced regeneration, mass control, multi-target abilities, faction/world consequences |
| 9. Ultimate Intelligence | Complete several distinct mastery and research trials; prove the character can control rather than merely possess its power | High-speed analysis, advanced parallel processing, automated defensive responses with explicit limits, ability optimization, advanced synthesis |
| 10. Mythic / Cosmic Slime | Complete the game's relevant planetary/cosmic progression and survive a transformation trial | Cosmic adaptation, space survival, biological propulsion, high-tier energy manipulation and godlike absorption branch only when the game's three-planet rule is satisfied |

Do not require every player to use the same prey or kill the same character. Where a specific action is essential to the fantasy, provide several valid ways to prove the underlying achievement: combat, exploration, research, diplomacy, survival, or a rare environmental event.

## Original ability suite for the slime route

The following mechanics should be designed as distinct abilities with visible unlock states. Names are working names and should be revised for originality.

### Absorption and analysis
- **Selective Assimilation:** consume eligible material or a qualifying specimen and choose which compatible traits to attempt to acquire.
- **Inner Archive:** preserve analyzed material/trait records and show provenance; storage limits and permanent-death rules still apply.
- **Predator's Appraisal:** analyze visible/encountered targets and identify likely traits, weaknesses, and unknowns based on evidence.
- **Form Echo:** temporarily reproduce an analyzed shape or locomotion pattern; does not automatically copy mastery, identity, or all abilities.
- **Trait Weaving:** combine compatible traits after research and a stability/cost check.

### Slime anatomy and survival
- **Elastic Morphology:** stretch, flatten, squeeze through openings, and reshape mass within physical limits.
- **Adhesive Flow:** cling to suitable surfaces and move along walls or ceilings.
- **Distributed Body:** divide into controllable fragments for scouting or simultaneous tasks; fragments have range, attention, and vulnerability limits.
- **Reconstitution:** rebuild body mass from surviving material; not resurrection after permanent character death.
- **Adaptive Membrane:** develop resistances to observed hazards through compatible exposure, samples, and evolution choices.
- **Organic Arsenal:** shape limbs, tendrils, spikes, shields, or simple tools from available biomass.

### Cognition and control
- **Parallel Cognition:** process multiple known tasks up to a defined control bandwidth.
- **Threat Simulation:** estimate likely actions from observed evidence, not hidden player data.
- **Autonomous Defense:** trigger eligible defensive responses when prerequisites, resources, and reaction windows permit.
- **Memory Palace:** organize discovered species, materials, abilities, and evolution dependencies.
- **Synthesis Engine:** propose combinations from known compatible components; the player must still meet requirements and learn mastery.

### Energy, barriers, and high-tier evolution
- **Energy Assimilation:** absorb eligible energy types with capacity, compatibility, and overload rules.
- **Elemental Conduit:** manipulate a researched elemental affinity; different elements require separate discovery chains.
- **Layered Barrier:** construct a barrier with selectable coverage and durability, consuming energy or biomass.
- **Spatial Cache:** store eligible objects/materials in a bounded fictional space; cannot bypass inventory rules or contain unrestricted living targets by default.
- **Sovereign Pressure:** influence nearby eligible creatures through a visible aura; resistance, range, intent, and narrative agency remain relevant.
- **Core Fusion:** fuse selected traits/abilities into a new ability after compatibility and stability requirements.
- **Cosmic Adaptation:** progressively withstand vacuum, radiation, temperature extremes, and stellar hazards.
- **Godlike Assimilation:** after the project's three-planet conquest requirement and other open ascension checks, increase eligible absorption yield from evolved targets. This does not remove eligibility, multiplayer, or permanent-death rules.

## Exactness and licensing boundary

The reference anime may contain particular named skills, character-specific forms, and story-gated abilities. For the unlicensed design:
- Record the *mechanical behavior* the user wants in neutral terms.
- Create original skill names, visual language, animation, lore, and progression gates.
- Avoid copying exact dialogue, character models, costumes, signature move names, story scenes, or a one-to-one character build.
- If the user wants the exact franchise character and its exact named powers as depicted, treat that as a licensed-content path and seek appropriate rights before including those assets or distinctive expression.

The goal is to preserve the desired feeling of action-gated growth, selective absorption, analysis, transformation, ability synthesis, and escalating power—not to promise unlicensed reproduction of the anime itself.

## Player-facing UI requirements

For every ability node, the Evolution Atlas should show:
- Current state: unknown, discovered, researched, eligible, acquired, stabilizing, mastered, equipped, or unavailable.
- Exact known prerequisites and progress counters.
- Which actions count and how the player can verify them.
- Trait source and confidence level.
- Compatibility, body-plan needs, resource cost, risk, counters, and interactions.
- Whether the node is mandatory for the chosen route, optional, mutually exclusive, or a costly respec.
- A preview of the body/animation/gameplay change before committing where feasible.
- Clear feedback when a condition is not met; no hidden failure without explanation after the condition has been discovered.

## Acceptance criteria

1. A new character can start as a weak blob and cannot immediately access endgame powers.
2. Each major slime milestone has a logged, reproducible action or achievement gate.
3. Unlocking is not tied only to character level.
4. Absorption records what was offered, accepted, rejected, and why.
5. Trait acquisition does not automatically grant a target's full skill set or mastery.
6. The player can view known prerequisites and track progress in the Evolution Atlas.
7. Slime abilities interact consistently with anatomy, movement, combat, resources, environment, and multiplayer validation.
8. The route supports several valid playstyles and does not force every gate to be a kill.
9. Permanent character death remains permanent; reconstitution cannot be used as a loophole.
10. The exact implementation/test status is documented separately from this design specification.

## Open decisions

- Whether the slime route is a main progression branch, an optional starting lineage, or an early mutation path available to other lineages.
- Exact numeric costs, cooldowns, capacity limits, and stage thresholds.
- Which elemental and energy systems are present in the first playable scope.
- How companions or AI-like internal assistants are represented without copying a franchise character's distinctive identity.
- Whether official franchise licensing will ever be pursued.
- Which exact abilities are required for the initial vertical slice versus later expansions.
