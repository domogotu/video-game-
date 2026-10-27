# Lethal Absorption — Cohabitation, Breeding, and Heritable Traits System

> **Status:** Design specification; not implemented, simulated, or tested.  
> **Scope:** Planet-wide system for Veyra and every later generated world.  
> **Design principle:** Species relationships and inherited traits must change observable behavior, population outcomes, and player decisions—not exist only as flavor text.

## 1. Goals

1. Let species share habitats, tolerate one another, cooperate, compete, avoid, hunt, or fight according to ecology and individual state.
2. Make breeding depend on reproductive biology, maturity, health, habitat, season, and mate compatibility.
3. Give offspring inherited variation with understandable trade-offs, not arbitrary stat rolls.
4. Let environmental pressures and player actions influence populations across generations.
5. Keep the system extensible from microbes and Slimes to animals, plants, sapient species, and bosses.
6. Keep the simulation bounded, legible, deterministic under test, and performant in a large multiplayer world.

## 2. Relationship model

Every species pair can have one or more relationship dimensions. Do not force every pair into a single permanent label.

### Relationship dimensions

- **Tolerance:** willingness to remain near another species.
- **Predation:** whether one species can hunt and consume the other, under which life-stage and size conditions.
- **Competition:** overlap in limited food, water, shelter, nesting sites, territory, or mates.
- **Mutual benefit:** a specified exchange in which one or both parties gain a measurable benefit.
- **Fear / threat response:** whether the other species triggers hiding, flight, mobbing, defense, or aggression.
- **Reproductive compatibility:** whether reproduction is biologically possible; this is independent from tolerance.
- **Disease / parasite interaction:** only where a defined transmission route and host compatibility exist.
- **Habitat dependency:** whether one species requires another organism or its products to survive or reproduce.

### Player-facing summary labels

The interface may summarize a relationship as **Compatible**, **Neutral**, **Hostile**, **Symbiotic**, or **Conditional**. These are summaries of underlying rules, not substitutes for them. A pair may be neutral while feeding, hostile during breeding season, and mutually beneficial in a specific life stage.

Each relationship record must include:
- Stable relationship ID and the two species IDs.
- Directionality (A affects B, B affects A, or reciprocal).
- Relationship type and conditions.
- Life stages and sex/reproductive states to which it applies, when relevant.
- Trigger, range, confidence, cooldown, and possible response.
- Ecological effect and resource/population consequences.
- Evidence state: design hypothesis, mechanic specified, implemented, tested, or rejected.

## 3. Individual and context modifiers

Relationship response is calculated from species rules plus the individual and local context. Relevant modifiers include:

- Hunger and access to alternative food.
- Health, injury, stamina, age, and life stage.
- Body size, anatomy, defensive traits, and escape ability.
- Group size, offspring nearby, social bonds, and learned experience.
- Territory ownership, nest/den proximity, and breeding season.
- Resource abundance, crowding, shelter, and habitat suitability.
- Weather, visibility, wind, water flow, noise, and sensory access.
- Previous encounters and memory, where the species' cognition supports it.

A predator must not attack solely because a prey species is present if it is satiated, injured, outmatched, or lacks a plausible capture opportunity. A herbivore must not become permanently aggressive because one encounter occurred. AI must use valid sensory cues and cannot know exact player or creature positions without a supported detection event.

## 4. Cohabitation outcomes

Species sharing a biome do not automatically form a stable community. Outcomes include:

- **Stable coexistence:** adequate separate or shared resources, acceptable risk, and enough habitat.
- **Spatial separation:** species use different depths, heights, times of day, or microhabitats.
- **Temporal separation:** feeding, nesting, or breeding schedules reduce conflict.
- **Resource competition:** one or both populations lose condition or reproduction when a shared resource becomes scarce.
- **Displacement:** repeated conflict or depletion causes individuals to leave if a viable route and destination exist.
- **Predator-prey pressure:** predation changes survival, behavior, and population recruitment.
- **Mutualism:** measurable benefit only when the mechanism is specified (for example, parasite removal or successful pollen transfer).
- **Local exclusion or collapse:** a species can disappear from a patch when pressure persists and recolonization is not possible.

No species should teleport to a preferred habitat. Migration and displacement require a traversable route, tolerable conditions, and destination capacity.

## 5. Breeding lifecycle

A reproductive attempt follows explicit gates rather than a universal timer:

1. **Reproductive eligibility:** species reproduces by the relevant method; compatible reproductive types and mature life stages exist.
2. **Condition:** sufficient health, nutrition, energy/stamina reserve, and acceptable stress level.
3. **Environmental suitability:** required water, temperature, shelter, host plant, substrate, nest/den site, or other species-specific conditions.
4. **Mate or reproductive event:** mate choice, courtship, spawning, budding, fission, egg laying, seed production, or another documented process.
5. **Gestation / incubation / development:** time and survival depend on the species and environmental conditions.
6. **Birth / hatch / germination:** offspring or new organism enters the appropriate life stage; no guaranteed survival.
7. **Juvenile survival:** food, shelter, predation, disease, parental care, crowding, and weather affect survival.
8. **Maturity and dispersal:** mature individuals may remain, form territories, join groups, or disperse if conditions allow.

A species dossier must specify its reproductive mode before the system enables breeding. Do not assume all species have sexes, pair bonds, live birth, or sexual reproduction. Plants, microbes, Slimes, and alien organisms may use other documented modes.

### Breeding controls and limits

- Reproduction consumes or depends on finite resources and available habitat capacity.
- Population growth is limited by food, shelter, territory, juvenile survival, and environmental constraints.
- Inbreeding effects are species-specific and should not be applied as a universal penalty without defined biology.
- Cross-species breeding and genetic/trait exchange are supported possibilities, but each pairing must use a documented compatibility class and mechanism.
- Sharing a habitat, being visually similar, or having a friendly relationship does not establish reproductive compatibility.
- Hybrid offspring may be viable, nonviable, sterile, reduced-fertility, or fertile according to the documented lineage rules.
- A single hybrid individual is not automatically a new species; stable derived species require multi-generation lineage and population criteria.
- Trait transfer, symbiosis, grafting, and player absorption must remain distinct from ordinary hybrid reproduction unless a specific species rule connects them.
- Player-controlled breeding must not bypass compatibility, resource costs, population limits, or world ecology.
- See the [Cross-Species Hybridization and Species Emergence System](CROSS_SPECIES_HYBRIDIZATION_AND_SPECIES_EMERGENCE_SYSTEM.md) for compatibility classes, mechanisms, lineage tracking, and acceptance tests.
- Population management may include protection, selective pairing, habitat restoration, or removal, with visible consequences.

## 6. Heritable trait model

Each species declares a list of heritable trait loci or trait modules. The schema supports continuous values, discrete alleles, and multi-gene traits, but does not require real-world genetics to be copied literally.

Candidate trait families:
- **Morphology:** body size, limb proportions, jaw or feeding structures, shell/skin/scale properties, horn/crest structures.
- **Movement:** burst speed, endurance, turning, climbing, swimming, burrowing, gliding, flight efficiency.
- **Senses:** chemical range, vibration sensitivity, low-light vision, hearing, heat or pressure detection.
- **Physiology:** temperature tolerance, water retention, oxygen tolerance, digestion, toxin resistance, recovery.
- **Behavior:** caution, aggression threshold, sociality, territoriality, curiosity, parental investment, activity schedule.
- **Reproduction:** maturity timing, clutch/litter range, incubation tolerance, courtship preference, host dependence.
- **Appearance:** pattern, coloration, markings, body ornamentation; appearance alone must not silently grant a gameplay advantage.

Every trait definition needs:
- Stable ID, allowed species/lineages, expression range, inheritance mode, and mutation limits.
- Environmental effects and measurable gameplay/ecology effects.
- Costs, trade-offs, incompatibilities, and possible failure states.
- Whether the trait is heritable, acquired, learned, temporary, or player-installed.
- UI explanation and validation test.

### Inheritance and variation

Offspring inherit only traits supported by their lineage and reproductive mechanism. For cross-species offspring, the [Cross-Species Hybridization and Species Emergence System](CROSS_SPECIES_HYBRIDIZATION_AND_SPECIES_EMERGENCE_SYSTEM.md) defines compatibility, allowed trait transfer, viability, fertility, parentage, and the criteria for recognizing a derived species. The model may combine parental values, dominance, recombination, and bounded variation when appropriate. Mutation is possible but uncommon, bounded, and explainable; it is not a free upgrade roll.

Traits should have trade-offs. Examples:
- Larger body may improve intimidation and defense but require more food and make hiding harder.
- High burst speed may improve escape but consume more energy and reduce sustained pursuit.
- Thick armor may resist injury but increase resource needs or reduce movement in mud.
- Better drought tolerance may reduce performance in cold or permanently wet conditions.
- Higher reproductive output may increase juvenile competition and parental/resource demands.
- Aggression may improve territorial defense while increasing injury risk and resource use.

Avoid one universally optimal genetic build. Local conditions should change which traits are advantageous.

## 7. Selection and population change

Across generations, trait frequencies may change through:
- Differential survival and reproductive success.
- Mate choice and reproductive compatibility.
- Migration and gene flow between connected populations.
- Genetic drift in small populations.
- Mutation within defined bounds.
- Player actions that alter habitat, mating access, predation, or selection pressure.

Do not evolve a population instantly in response to one weather event. Track generations and population state. For distant or low-relevance populations, use bounded aggregate simulation while preserving meaningful outcomes; simulate individuals in detail near active players or high-value events.

## 8. Veyra starter relationship examples

All entries below are design hypotheses or specified concepts, not validated simulation results.

| Pair / interaction | Initial rule | Conditions and limits |
|---|---|---|
| Glass-Eyed Pouncer → Reed Skipper | Predation | Only if size, line of sight/sensory cues, capture window, and terrain permit; pouncer is not a guaranteed winner. |
| Mire Needle → Reed Skipper | Predation | Shallow-water strike opportunity; deep or fast water may prevent capture. |
| Moss-Horn Browser ↔ Root-Crown Forager | Competition | Only for explicitly shared roots, fallen fruit, or soft vegetation; different foraging heights and methods reduce overlap. |
| Gloam Moth larva → Reedlace Hostleaf | Host feeding | Limited leaf stock; season, plant recovery, and larval survival govern recruitment. |
| Gloam Moth adult ↔ Duskbell Bloom | Potential mutualism | Adult food / potential pollination only; pollen transfer and plant reproductive benefit must be validated. |
| Reed Skipper ↔ Moss-Horn Browser | Conditional coexistence | Shared wetland/woodland edge does not imply direct benefit; disturbance and trampling may affect small-prey cover. |
| Slime ↔ any potential prey | Stage-dependent interaction | Capture/absorption depends on Slime stage, size, stamina, target condition, anatomy, and escape/counterplay. Absorption is not reproduction. |

Do not fill unknown pairs with invented friendliness or hostility. An unrecorded relationship remains **unknown**, not automatically neutral.

## 9. Cohabitation and genetics UI

A field guide / species panel should expose:
- Relationship summary and confidence/evidence state.
- Compatible, neutral, hostile, symbiotic, conditional, and unknown links.
- Known food, shelter, nesting, host, and territory dependencies.
- Breeding eligibility and environmental requirements when discovered.
- Trait profile, heritability, trade-offs, and how the trait was observed or inherited.
- Population trend and visible warning when a resource or breeding population is declining.

Discovery is gradual. The player may see tracks, calls, feeding damage, courtship, nests, territorial displays, or offspring before the full relationship is identified. Do not reveal all hidden genetics or ecosystem facts before the player has observed or researched them.

## 10. Multiplayer and performance constraints

- One authoritative world state governs population, breeding, and relationship outcomes.
- Do not allow each client to create duplicate offspring or harvest the same resource independently.
- Use stable entity IDs, server-authoritative reproduction events, and reproducible simulation steps.
- Cap population and breeding events through ecology-driven carrying capacity, not arbitrary invisible despawns.
- Preserve important named individuals and player-discovered lineages when using aggregate simulation.
- Apply detail levels by distance and relevance without changing major ecological outcomes.
- Record significant events for debugging: birth/hatch, failed reproduction, migration, predation, resource collapse, mutation, and local extinction.

## 11. Acceptance tests required before implementation is called complete

- [ ] Compatible species can coexist without forced interaction when resources are sufficient.
- [ ] Predators cannot capture prey without a valid size, sensory, movement, and terrain opportunity.
- [ ] Resource scarcity increases competition or displacement and can reduce reproduction.
- [ ] Species-specific breeding gates prevent reproduction when maturity, compatibility, or environmental conditions fail.
- [ ] Offspring inherit only allowed traits and remain within defined bounds.
- [ ] Trait trade-offs are observable and no trait dominates in every environment.
- [ ] Population growth respects food, shelter, and habitat capacity.
- [ ] Mutualism is not enabled without a measurable benefit to the required participant(s).
- [ ] Unknown relationships stay unknown until documented or discovered.
- [ ] Multiplayer tests prevent duplicate births, divergent population state, and infinite resource/population loops.
- [ ] Tests cover flood, drought, food shortage, predator increase, habitat fragmentation, and recovery.
- [ ] Distant population aggregation preserves bounded, reproducible ecological trends.

**Evidence status:** Design specification only. No breeding, cohabitation, inheritance, or population simulation has been implemented or tested.
