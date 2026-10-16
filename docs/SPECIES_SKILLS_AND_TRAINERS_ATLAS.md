# Lethal Absorption — Species Skills, Trainers, and Evolution Reference

> **Status:** Design framework and initial Slime reference; design-only, not implemented or tested.
>
> **Purpose:** Establish a comprehensive Outward-style skills-and-trainers reference for every playable and discoverable species in Lethal Absorption. This is an original game-design system, not a reproduction of another game's skills, trainers, tables, or progression.

## 1. Scope and coverage

Every species entry in the Species Atlas must eventually have a dedicated skills-and-training page using the schema in this document. Coverage includes:
- Playable species and the Slime's evolutionary stages.
- Ordinary wildlife, prey, predators, and environmental specialists.
- Subspecies, regional adaptations, mutations, and rare variants.
- Alpha, apex, ancient/elder, anomalous, named/unique, friendly/bonded, and migratory/event creatures.
- Sapient species and factions, including agency-respecting training relationships.
- Planetary, Living Ship, cosmic, and secret-boss forms.

The target is exhaustive **coverage of all species defined by the project**, not an invented claim that a fixed number of species already exists. When the species roster grows, the index must grow with it. Do not silently omit a species or mark a placeholder as complete.

## 2. Skills and acquisition routes

A skill can be acquired through one or more clearly distinguished routes:

| Route | Meaning | Typical requirements |
|---|---|---|
| Species-native | Part of the species' baseline biology or inherited repertoire | Species/body plan and life stage |
| Trainer / mentor | Learned from a qualified NPC, creature mentor, faction, bonded ally, or specialist | Discovery, trust, quest, fee/trade, demonstration, or challenge |
| Observation | Learned by studying a creature performing the ability | Sufficient safe observation, correct clues, analysis |
| Absorption / trait imprint | A compatible biological pattern becomes eligible after an absorption and analysis process | Valid source, compatibility, processing, integration |
| Practice / mastery | Improves execution or unlocks an already eligible variant | Meaningful use, training drills, timing, performance |
| Environment / discovery | Learned from a habitat, anomaly, ruin, elemental source, or ecological event | Evidence, survival, puzzle, resource, or world-state condition |
| Quest / bond | Earned through a story, faction, ally, or species relationship | Quest outcomes and ethical/agency rules |
| Evolution Atlas | Unlocks an anatomical prerequisite, ability branch, or mutation route | Stage, prerequisites, evolution resources, trade-offs |
| Craft / research | Created or adapted from studied materials and knowledge | Recipe, research, compatible anatomy, resources |
| Fusion | Combines two or more already eligible traits or abilities | Compatibility, stability, control, costs, counterplay |

A trainer is not necessarily humanoid. A teacher can be a creature, bonded companion, recorded biological pattern, ecological process, or research construct. Pages must distinguish a **trainer** (teaches a skill), **source species** (provides a trait pattern), **mentor** (teaches technique or judgment), and **unlock location/event** (where the condition can be fulfilled).

## 3. Mandatory skill entry format

Every skill must include the following fields. Use “Not established” when the design has not decided the value; never invent a canon price, coordinate, percentage, cooldown, or unlock condition and present it as final.

- **Skill name and ID**
- **Species / forms supported**
- **Category:** active, passive, toggle, reaction, movement, sensory, defense, attack, support, survival, crafting, transformation, ultimate, or utility.
- **Effect:** exact gameplay behavior and readable feedback.
- **Acquisition route:** native, trainer, observation, absorption, practice, discovery, quest/bond, Atlas, research/craft, or fusion.
- **Teacher / source:** named trainer, source species, item/material, quest, location, event, or “not established.”
- **Unlock prerequisites:** evolutionary stage, anatomy, prior skill, trait compatibility, level if relevant, knowledge, quest, bond/trust, environmental conditions, and other gates.
- **Cost:** stamina, metabolic energy, biomass, stability, health risk, consumable, time, currency/trade, or none. Keep these distinct.
- **Cooldown / recovery:** exact only when designed; include charge, recovery, and interruption behavior where relevant.
- **Range / target / area:** include line-of-sight or sensing requirements and target-size limits.
- **Scaling:** anatomy, body mass, stats, mastery, environmental factors, target resistance, or other defined variables.
- **Mastery progression:** what use teaches, ranks/tiers, execution changes, and what mastery does not grant automatically.
- **Variants / branches:** alternative outcomes and trade-offs.
- **Synergies / conflicts:** compatible traits, anatomy, skills, and incompatible combinations.
- **Counters / failure states:** how the move can be avoided, resisted, interrupted, escaped, or countered.
- **World / AI response:** sound, scent, evidence, alert, ecosystem effect, allies, or no response where appropriate.
- **PvP / agency safeguards:** relevant rules for player characters, sapient NPCs, and permanent progression.
- **Implementation status:** design-only, implemented, tested, or verified, with evidence before upgrading status.

## 4. Trainer and mentor entry format

Each trainer/mentor page must specify:
- Name/ID and species or organization.
- Exact location or discovery method, region, access conditions, and whether they move.
- Skills taught and their full skill entries.
- Required relationship: neutral, reputation, trust, bond, faction, quest, challenge, or trade.
- Cost type and amount only when established; biological trades and services are valid alternatives to currency.
- Whether teaching is permanent, repeatable, limited, exclusive, or mutually exclusive.
- What happens if the teacher is absent, hostile, killed, relocated, or unavailable; do not assume permanent-death rules permit killing sapient teachers for skills.
- Evidence clues, dialogue/behavior hints, and navigation support.
- Version and verification state.

Trainer information must not force every species into a humanoid shop model. A territorial predator might teach through nonlethal sparring; a herd species through observation; an Alpha through a trial; a symbiotic organism through bonding; an ancient being through a costly negotiation.

## 5. Species page structure

Each species page must contain:
1. Identity, taxonomy, habitats, life stages, and body-plan variants.
2. Baseline anatomy and innate skills.
3. Full active, passive, toggle, reaction, movement, sensory, defense, survival, support, and ultimate ability tables as applicable.
4. Acquisition and training index.
5. Skill prerequisites and branching tree.
6. Skill-specific costs, cooldowns, ranges, target constraints, and mastery.
7. Species-specific trait sources, absorption compatibility, and integration limits.
8. Anatomy requirements and what breaks or changes when a body part is injured, lost, or evolved.
9. Environmental adaptations, weaknesses, counters, and status interactions.
10. Combat roles, AI behavior, pack/herd/ally behavior, and encounter consequences.
11. Cooking, diet, crafting, material, and non-combat interactions where applicable.
12. Evolution routes, mutations, subspecies, rare branches, and cross-species fusions.
13. PvP protections, sapient agency, companion/bond rules, and multiplayer edge cases.
14. Known gaps, unresolved balance values, and implementation/test status.

Species without a skill in a category should explicitly mark it “not applicable” rather than leave an unexplained omission.

## 6. Shared skill systems and balance rules

- No fixed class lock: species anatomy and evolution open routes, but players can build in multiple directions where prerequisites permit.
- A learned trait is not automatically mastered. Eating, analyzing, integrating, equipping, practicing, and mastering remain separate states.
- Every ability needs a purpose, resource cost or clear reason it is free, a limitation, readable feedback, and counterplay.
- Stamina, health, biomass, metabolic energy, stability, cognitive load, environmental condition, injury, and recovery remain separate variables. No single meter replaces the others.
- Trainer teaching and biological acquisition are different systems. A creature may teach a technique without donating an organ; absorption may reveal a trait without teaching its tactical use.
- Costs and numbers remain data-driven and tunable. Label unbalanced or undecided values as proposals, not established canon.
- Species AI uses only credible sensory evidence and plausible knowledge. Trainers and enemies do not become omniscient because the player learned a skill.
- Anatomy-aware skills require the appropriate structures or an explicitly designed substitute. Broken wings, legs, arms, sensory organs, or propulsion organs alter available actions according to severity and species.
- Live-target absorption drains health only once the active absorption process has begun; the target can resist, break free, and resume combat.
- Sapient beings retain agency and cannot be treated as ordinary loot. PvP cannot permanently kill player characters or permanently steal progression/assets.

## 7. Slime master reference — initial skill catalogue

This is the initial Slime index to be expanded into complete individual skill entries. It reflects the approved base-form choices: mostly blind initially, chemical and vibration senses, manual sensory switching, no starting conventional eyesight, species-specific eye evolution, and crawling/squeezing/short hops/limited surface climbing.

### Starting form and innate skills

| Skill | Type | Initial behavior | Limits / counterplay | Status |
|---|---|---|---|---|
| Chemical Sampling | Passive / sensory | Detect nutrient traces, toxins, and familiar biological signatures through contact or nearby chemistry | Wind, water, contamination, unfamiliar substances, competing traces | Design-only |
| Vibration Sense | Passive / sensory | Detect movement and impacts transmitted through connected ground or fluid; estimate direction/intensity | Soft terrain, suspended movement, noise, careful movement | Design-only |
| Contact / Pressure Sense | Passive / sensory | Detect touch, pressure, and local body/surface stress | Limited to contact and transmitted forces; does not provide visual identity | Design-only |
| Manual Sensory Switch | Utility / interface | Player manually selects an available sensory view; the view emphasizes valid cues without revealing hidden entities arbitrarily | Only discovered/evolved senses are selectable; each has blind spots and interference | Design-only |
| Flow Crawl | Movement | Limbless movement through membrane contractions | Terrain, exertion, injury, body condition | Design-only |
| Flatten and Squeeze | Movement / utility | Reduce profile and pass through physically traversable openings | Gap size, mass, core placement, membrane condition | Design-only |
| Short Compression Hop | Movement / evasion | Short launch across small obstacles or for brief evasive repositioning | Stamina, recovery, landing surface, body condition | Design-only |
| Limited Surface Adhesion | Movement / utility | Cling to and climb some suitable surfaces | Texture, moisture, slope, contamination, gravity, mass, stamina, injury | Design-only |
| Elastic Membrane | Passive / defense | Distributes some blunt impacts and enables deformation | Does not grant immunity to piercing, heat, chemicals, or concentrated force | Design-only |
| Basic Absorption | Active / feeding | Absorbs eligible biological material; live-target health drain begins only once active absorption starts | Size, anatomy, resistance, interruption, compatibility, stamina, health, defenses | Design-only |
| Basic Nutrient Processing | Passive / survival | Converts compatible intake into defined stored resources | Digestive capacity, toxins, incompatible matter, overload | Design-only |

### Slime sensory evolution branches

| Branch | Candidate skills / outcomes | Source / prerequisite concept | Trade-offs |
|---|---|---|---|
| Chemical specialist | Scent Memory, Trail Reconstruction, Toxin Discrimination, Pheromone Parsing | Repeated exposure, compatible sensory tissue, analysis, practice | Weather and contamination still interfere; complex traces may cost attention |
| Vibration specialist | Directional Vibration Map, Footfall Classification, Subsurface Pulse Reading | Specialized mechanosensory structures and training | Weak on disconnected/soft surfaces; noisy environments create ambiguity |
| Light-sensitivity branch | Light/Dark Detection, Directional Light Response | Photoreceptor-bearing source and compatible integration | Detects illumination before forming detailed images |
| Directional-eye branch | Silhouette Sight, Motion Recognition, Basic Depth Estimation | Eye-bearing source with directional/image-forming structures; analysis and integration | Limited acuity, range, field of view, or color |
| Compound-eye branch | Broad Motion Coverage, Fast-Movement Tracking | Compatible compound-eye species | May sacrifice fine detail and depth precision |
| Low-light branch | Dim-Light Sight, Contrast Preservation | Species adapted to darkness | Bright-light overload or reduced color/detail may apply |
| Color branch | Expanded Color Discrimination | Appropriate receptor diversity and visual processing | Color range depends on source; not universal color vision |
| Specialized optical branch | Ultraviolet or Polarized-Light Detection, where biologically supported | Rare source species, discovery, or later adaptation | Specialized information only; environmental interference and processing costs |
| Thermal branch (optional, not default) | Temperature Gradient Sense, Heat-Source Localization | Separate thermal adaptation or discovery | Heat sources can mislead; opaque barriers remain opaque |

Different eye-bearing species unlock different branches; absorbing one species does not grant all branches. A complete image-forming system may require multiple compatible structures and evolution steps. Chemical and vibration senses remain useful after eyesight evolves. The player manually switches among unlocked sensory views by default.

### Slime locomotion evolution index

| Skill / branch | Unlock concept | Effect | Trade-off |
|---|---|---|---|
| Efficient Flow | Practice and gel-matrix evolution | Lower exertion on suitable terrain | Less benefit on hostile surfaces |
| Compression Control | Membrane/body control mastery | Narrower squeeze profile and more reliable traversal | Does not bypass solid geometry or body-volume limits |
| Elastic Launch | Gel matrix and controlled energy storage | Longer or more directional jumps | Higher stamina/energy demand and landing risk |
| Adhesion Upgrade | Compatible surface-binding trait | Better grip and more climbing surfaces | Contamination, moisture, and surface type still matter |
| Wall Ooze | Advanced adhesion and body control | Sustained traversal of suitable walls/ceilings | High exertion; failed grip can cause falls |
| Tendril Pull | Pseudopod/tendril anatomy | Anchor and pull body toward compatible surfaces | Requires a valid anchor and sufficient control |
| Aerial Glide | Broad membrane or compatible acquired anatomy | Controlled descent and limited gliding | Not true powered flight; wind and mass matter |
| Specialized aquatic movement | Compatible fin, cilia, or propulsion traits | More efficient swimming or current use | Requires water and anatomy; does not imply land performance |
| Advanced propulsion | Later evolutionary stage and appropriate anatomy/energy system | Form-specific rapid movement | High costs, environmental constraints, counterplay |

### Slime combat, defense, feeding, and utility index

The full individual entries must follow the mandatory schema in Sections 3 and 7. Current candidates from the master blueprint include:
- **Body shaping:** Pseudopod, Multi-Pseudopod, Tendril, Hook/Barb, Suction Pad, Grip Pad, Impact Lobe, Blade Ridge, Spine Burst, Cushion Dome, Armor Plates, Sensory Cilia, Temporary Eye, Body Density Shift.
- **Defense/recovery:** Elastic Damping, Membrane Hardening, Gel Armor, Surface Shedding, Damage Seal, Regeneration, Emergency Core Shield, Thermal Buffer, Desiccation Seal, Pressure Adaptation, Reactive Membrane, Status Purge, False Death/Dormancy.
- **Feeding/analysis:** Particle Absorption, Engulf, Selective Intake, External Digestion, Biomass Conversion, Energy Extraction, Mineral Assimilation, Organic Pattern Analysis, Trait Imprint, Toxin Isolation, Purification, Emergency Digestion, Stored Nutrient Sac, Digestive Overload, Absorption Recall.
- **Combat/control:** Pseudopod Strike, Adhesive Restraint, Counter-Engulf, Body Slam, Recoil Dodge, Acid/Enzyme options, Decoy, controlled split, compatible trait fusion.
- **Late evolution:** advanced sensory web, controlled multi-body systems, transformations, ultimate abilities, planetary adaptation, Living Ship biology, and gated cosmic branches.

These are catalogue candidates, not claims that every skill is balanced, unlocked, or implemented. Each must eventually receive prerequisites, exact effects, costs, counters, mastery, and source information.

## 8. Master index and completion tracking

Maintain a machine-readable or table-based index with one row per species and fields:
- Species ID / canonical name / taxonomy.
- Playable, NPC-only, companion, trainer, source, boss, or mixed role.
- Life stages and body plans.
- Species-page URL/path.
- Innate skill count and full-entry count.
- Trainer/mentor entries and source-trait entries.
- Sensory, locomotion, combat, defense, survival, support, and ultimate coverage.
- Missing sections and unresolved values.
- Last reviewed commit and status: planned, drafting, design-reviewed, implemented, or tested.

A species page is **design-complete** only when every applicable category is covered, every skill uses the mandatory schema, acquisition sources and prerequisites are documented, conflicts/counters are stated, and open values are explicitly labeled. It is **implemented** only with code evidence, and **tested** only with actual verification evidence. Do not mark the entire species roster complete while any defined species remains missing a page.

## 9. Work plan

1. Inventory the repository's existing species, ecology, evolution, ability, and master blueprint documents to establish the actual canonical roster.
2. Build a species coverage index from that roster, preserving canonical names and variants rather than inventing extra species.
3. Complete the Slime page first, using the approved base-form perception and locomotion rules.
4. Create consistent species pages for the existing roster, prioritizing species with playable forms, trainers, major trait sources, and key encounter roles.
5. Cross-link each species to the Evolution Atlas, ecology, absorption, anatomy/injury, combat, cooking/crafting, and AI specifications.
6. Audit for missing skills, contradictory prerequisites, ungrounded numeric values, missing counters, and false implementation claims.
7. Keep implementation and runtime verification as separate future gates after design coverage is complete.
