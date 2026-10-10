# Progressive Stage Transitions: From Cell to Cosmic Explorer

**Project:** Lethal Absorption  
**Status:** Core progression design specification; not implemented or play-tested.  
**Purpose:** Define the game's central identity as a seamless-feeling progression through several distinct gameplay experiences, each revealed through earned evolution. Keep the opening simple and protect performance by expanding world complexity in stages.

## 1. Core Vision

Lethal Absorption is one game whose gameplay changes substantially as the player evolves. The opening should not expose the full catalogue, every menu, or every advanced system. The player learns a small set of actions, survives, gathers, and gradually discovers that the game is much larger than it first appeared.

Each major evolution is a deliberate transition:
1. The player completes a meaningful survival and growth milestone.
2. A cinematic shows the character's actual evolution, shaped by accumulated biomass, absorbed traits, mutations, abilities, and prior choices.
3. The game changes its controls, camera, movement, world scale, threats, and goals to fit the new stage.
4. A short, contextual onboarding teaches only the new actions needed now.
5. Previously learned abilities remain useful when biologically and mechanically compatible.

The transitions should feel like the world has opened up—not like the player has been forced to start an unrelated game. The through-line is always **explore, survive, gather, learn, evolve, and adapt**.

## 2. Stage One — Cellular Survival

### Intended feel
A simple, colorful, futuristic, highly readable micro-world. The player begins as a single cell, and the first minutes teach the core verbs without overwhelming the player.

### Initial controls and objectives
Teach only:
- **Move:** steer the cell through the environment.
- **Gather/absorb:** collect safe nutrients and eligible biomass.
- **Dodge:** avoid predators, hazards, and dangerous currents.
- **Attack:** unlock or teach a simple attack when appropriate to the opening.
- **Grow:** fill a clear growth meter and reach a meaningful evolution threshold.

At first, the player sees a clean play screen, a few resources, immediate threats, and simple feedback. Advanced menus and complex skill trees are introduced gradually, not all at once. The player learns the inventory, evolution view, skill tree, and discovery log through short contextual introductions as each becomes relevant.

### Keep it simple without making it empty
The initial loop is deliberately repetitive and readable: gather, avoid, learn the safe routes, and grow. Its purpose is to teach movement, risk, resource awareness, and the satisfaction of visible growth. The grind should feel steady, not needlessly slow. Short-term milestones, changing local hazards, rare nutrients, and small discoveries keep the loop from becoming pure waiting.

The first stage should be compact, with a limited number of entities and effects. Its scale and visuals can be striking without requiring a vast simulation.

### Transition trigger
When the player reaches a designed combination of growth, survival, and evolution requirements, trigger a cinematic. The transformation is generated from the player's recorded path and eligible acquired traits—not a generic cutscene that ignores the build. The scene reveals the next body plan and previews the abilities or sensory changes that will matter.

## 3. Stage Two — Animal-Scale Exploration and Survival

### Intended feel
The player is no longer a cell. The world opens into a bounded but expansive ecosystem, and the camera and movement shift toward immersive animal exploration with first-person or close immersive perspective where it serves gameplay.

This stage borrows broad survival-game qualities: habitat exploration, tracking, hunting, hiding, gathering, territory, environmental danger, and the need to grow. It is not a copy of any existing game.

### Core loop
Explore habitat → find food/materials and evidence → avoid or confront predators → learn local ecology → unlock or refine traits → survive long enough to evolve.

The player has a creature body plan shaped by earlier choices. Movement, senses, attack, dodge, stamina, swimming, breath-holding, and abilities should all reflect the player's anatomy. The player is an animal or evolved organism, not a cell with a larger model.

### World scope
Use a designed region rather than a seamless planet-sized simulation at this stage. The region can feel vast through sightlines, landmarks, layered paths, caves, waterways, vertical routes, and distant silhouettes, while keeping active AI, pathfinding, physics, and persistent state within a controlled budget.

Start with a small number of distinct biomes and add complexity only where it supports the survival loop. Local areas may include forests, rocky highlands, rivers, caves, coastlines, wetlands, or alien terrain. Not every biome must be available in every world seed.

## 4. Stage Three — Apex Creature / Alien-Hunter Survival

### Intended feel
The next transition expands the player into a more capable, potentially frightening creature with a stronger identity and more expressive powers. The intended mood is tense predator-versus-prey survival in a dangerous ecosystem, with the player able to become hunter, scavenger, ambush predator, territorial defender, or another viable species route.

The experience may include a forest at night, subterranean dens, nests, ruins, abandoned facilities, settlements, or other locations suited to the generated world. These should be selected by the player's species, world history, and active region rather than all loaded everywhere at once.

### Core loop
Scout → track or hide → gather and hunt → fight or evade → use powers tactically → secure a den or safe route → study threats → evolve.

The player now combines basic physical actions with a manageable number of powers and mutations. Powers should enrich survival and combat, not erase hunger, threat, navigation, or meaningful choices. Bosses, elite enemies, dens, bases, and contested areas act as regional challenges with readable telegraphs, tactics, and rewards.

### Species and social behavior
Different evolutionary paths should create distinct movement, senses, hunting methods, defensive options, and environmental needs. Enemies and neutral creatures have readable routines, territories, escape responses, and group behaviors. Friendly or allied creatures can communicate, assist, trade information, or share territory when the world fiction supports it.

The environment remembers relevant outcomes, but persistence is budgeted: preserve important changes and summarize distant low-priority simulation rather than running every creature at full detail continuously.

## 5. Stage Four — Main Form, Action Adventure, and Planetary Roaming

### Intended feel
This is the main high-expression action stage: a powerful, readable player form with responsive combat, free roaming, mobility, boss fights, exploration, and a larger catalogue of abilities. Visual ambition should emphasize strong art direction, readable silhouettes, animation quality, atmospheric lighting, varied terrain, and memorable locations—not only polygon count.

The feel can draw from broad qualities of cinematic action adventures and mythic action games without copying protected characters, moves, designs, or signature presentation.

### Core loop
Travel through a region → discover a threat, secret, activity, or boss → fight using chains and ability combinations → gather discoveries and materials → unlock mastery or evolution → explore a newly reachable area.

The player can run, climb, jump, dodge, fight, use abilities, and gain flight or other traversal when their build supports it. Not every character should automatically fly or use every movement mode. Anatomy and earned abilities define access.

### World design
Each planet or large destination should be built from purposeful regions rather than relying on endless empty land. Use landmarks, vertical layers, hidden paths, caves, bases, enemy territories, underwater routes, and aerial threats to create discovery density. Region boundaries can be concealed by terrain, weather, caves, traversal, or transition sequences.

Support both ordinary-sized combat and optional large-scale encounters. Large forms should not automatically win against smaller opponents; positioning, mechanics, counters, and encounter rules still matter.

## 6. Stage Five — Living Ship Form and Space Exploration

### Intended feel
After the player meets the relevant biological, mastery, and planetary progression requirements, another cinematic introduces a Living Ship Form: the character evolves into a life-form capable of traversing space. This is a transformation of the player, not an unlock of a conventional vehicle.

### Core loop
Prepare the living form → travel through space → detect a planet, anomaly, hazard, or encounter → choose a landing/entry approach → explore at planetary scale in an appropriate body form → gather, investigate, fight, and evolve → return to space.

Space gameplay must have its own readable movement model, threats, resource constraints, and discovery rhythm. The player should not be required to use the Living Ship Form for ordinary surface exploration; they can return to a compatible base form on a planet. Form changes need clear rules and must not make equipment, anatomy, or powers silently disappear.

### Scale and performance
Do not simulate every planet, creature, and structure at full detail at once. Load only the active destination and the relevant nearby simulation. Use streaming, authored points of interest, procedural variation under design constraints, and persistence tiers. Distant worlds retain key state summaries and reload meaningful changes when visited.

## 7. The World Evolves with the Player

The world should offer appropriate opportunities for each stage, while still allowing old environments to remain meaningful.

- **Cellular stage:** micro-scale currents, nutrient pockets, cell predators, and clear hazards.
- **Animal stage:** cover, food webs, tracks, burrows, water, climbing, and hiding places.
- **Apex stage:** dens, territorial borders, complex prey/predator behavior, power-aware hazards, and regional bosses.
- **Main-form stage:** vertical traversal, ruins, enemy bases, secrets, caves, aerial routes, underwater regions, and major encounters.
- **Space stage:** planetary entry, extreme environments, orbital-scale dangers, and rare destinations.

Terrain is gameplay: mountains provide climb routes and vantage points; trees and vegetation provide cover and ambush opportunities; caves create shelter, traversal, and danger; water supports swimming, breath management, aquatic life, and submerged discoveries; the sky supports flying enemies and aerial encounters when the player and region can support them.

The world must not simply become larger and more expensive at every stage. Increase the density and sophistication of relevant interactions, while keeping active simulation bounded.

## 8. Land, Sky, and Water Rules

Each region should define which layers are present and supported:

- **Ground:** traversal, tracks, cover, burrows, structures, predators, prey, allies, and bosses.
- **Canopy/vertical terrain:** climbing, jumping, flight takeoffs, nests, ambushes, and elevated routes.
- **Sky:** flying creatures, weather, aerial hazards, and encounters only when aerial navigation is supported.
- **Surface water:** swimming, currents, shorelines, aquatic life, and crossings.
- **Underwater:** breath or oxygen limits, visibility, pressure or depth constraints where relevant, aquatic enemies and allies, submerged resources, and safe return routes.
- **Caves/interiors:** restricted sightlines, sound propagation, confined movement, nests, ruins, and special environmental hazards.
- **Settlements/bases:** inhabitants, defenses, patrols, services or interactions appropriate to the setting, and consequences for intrusion or alliance.

A creature can only use a layer when its anatomy and unlocked abilities permit it. If the player can swim and remain underwater long enough—or has suitable adaptations—the underwater world should be genuinely explorable, not a decorative plane. If not, it should remain a visible future opportunity with clear danger signals rather than a hidden instant-death trap.

## 9. Cinematic Transitions and Continuity

Each major stage transition should:
1. Be triggered by explicit, readable progression conditions.
2. Save the character's evolution history before transition.
3. Show how the previous form changes into the next form.
4. Reflect the player's actual traits, abilities, and mutations where technically feasible.
5. Introduce the new camera, movement, threats, and immediate goal.
6. Teach the new mechanics through safe, short interactions.
7. Preserve compatible learned skills and explain any changed controls.
8. Provide a recap and accessible summary if the player skips or replays the cinematic.
9. Avoid permanently interrupting play with repeated unskippable scenes.
10. Offer a clear first objective in the new stage.

Transitions must not erase the player's agency. The cutscene communicates the result of the player's path; it should not secretly replace their build with a fixed character.

## 10. Scope and Performance Guardrails

- Begin with one compact cellular environment, not a galaxy.
- Build the first animal-scale region from a small, authored set of creatures and ecological roles.
- Add species and biomes only when they support a tested gameplay loop.
- Keep active AI and physics limited to the relevant area; use lower-cost simulation for distant regions.
- Stream or load later stages only when the player earns the transition.
- Avoid placing every creature, building, effect, and biome into memory at once.
- Use visual ambition through art direction, composition, lighting, animation, effects, and carefully authored landmarks.
- Establish performance budgets for active enemies, destructible objects, effects, AI updates, and persistent state before scaling content.
- Ensure world generation creates navigable and playable regions, not just large maps.
- Avoid grind based only on inflated resource requirements; provide varied but coherent routes to growth.

## 11. Acceptance Criteria for the Stage-Transition Design

The design is ready for a vertical-slice handoff when:
1. Each stage has a distinct player fantasy, camera/movement model, core loop, and growth objective.
2. The opening teaches movement, gather/absorb, dodge, and attack in a simple screen before revealing complex menus.
3. Skill tree, inventory, evolution, and discovery systems appear through staged onboarding rather than one overwhelming tutorial.
4. The first major cinematic reflects the character's earned evolution history.
5. The animal stage uses a bounded but expansive region with a limited active simulation.
6. The apex stage adds tactical powers while preserving survival and exploration.
7. The main-form stage supports expressive combat, bosses, roaming, and terrain-driven exploration.
8. The space stage is gated by progression and uses a biological Living Ship Form.
9. Ground, sky, water, underwater, and interiors have explicit traversal and threat rules.
10. At least one world-state consequence persists across a return visit in the designed slice.
11. A stage transition does not silently erase compatible abilities or overwrite the character's identity.
12. The first slice remains small enough to build and evaluate without requiring the full game world.

## 12. Current Work Ledger Update

This document captures the intended multi-stage experience and constraints. It does not complete the first gameplay vertical slice by itself.

- **Core gameplay loop and player feedback:** DONE — prior design document exists and was fetched back from GitHub.
- **Stage-transition vision:** DONE — this document created and fetched back from GitHub.
- **First gameplay vertical-slice boundaries:** IN PROGRESS — next action is to define the smallest testable opening segment, including the cellular opening and the first transition trigger; do not spec all five stages in implementation-level detail before that boundary is set.
- **Implementation:** DEFERRED — current focus is gameplay and design.
