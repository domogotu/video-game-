# Lethal Absorption — Veyra / Reedwater Basin Integrated Ecosystem Simulation Contract

> **Status:** Authoritative proposed implementation contract, **design only**. No simulation runtime, code tests, performance benchmark, or validated ecology is claimed. Applies to the first planet Veyra, first region Reedwater Basin.
> **Inputs:** [Genetics Pass 1](VEYRA_REEDWATER_FOUNDING_GENETICS_DOSSIERS.md), [Pass 2](VEYRA_REEDWATER_GENETICS_PASS_2.md), [Pass 3](VEYRA_REEDWATER_GENETICS_PASS_3.md), [Genetic Catalogue](GENETIC_INHERITANCE_CATALOGUE_AND_COMPATIBILITY_MATRIX.md), [Landscape Restoration](LANDSCAPE_RESTORATION_AND_ECOLOGICAL_BALANCE_SYSTEM.md), and canonical species dossiers.

## 1. Scope and immutable gameplay boundaries

Implement one playable ecological vertical slice before scaling across planets. The 12 genetics-profiled organisms are Null Slime, Glassfilm Microbe, Reed Skipper, Silt Burrower, Glass-Eyed Pouncer, Mire Needle, Moss-Horn Browser, Root-Crown Forager, Current Dart, Reedstalker, Bark Lantern, and Gloam Moth.

Null Slime begins largely blind with **manually switchable chemical and vibration sensory modes**, moves by crawling, squeezing, short hops, and limited climbing, and may evolve eye-bearing branches only through appropriate anatomy/progression. Absorption is **not reproduction**. Predation does not establish breeding compatibility. All interspecies reproduction is CX unknown unless later supported. No permanent player death from PvP; existing game rules on NPC-caused permanent death remain separate from ordinary ecological mortality.

The ecological system must not assume an unlimited population, free instant respawns, infinite prey, or world-wide perfect animal perception. Species dossiers take precedence over examples in this contract where biology is more specific.

## 2. Spatial representation and update cadence

Partition Reedwater Basin into **habitat cells** with stable IDs and graph edges for traversable land, connected water, airborne dispersal, and sheltered corridors. A cell has habitat type, area, elevation, water depth/flow/oxygen, moisture, temperature, light, substrate, vegetation biomass by resource group, detritus, deadwood/shelter slots, disturbance, and accessibility flags. Values have units and bounds in implementation; no specific numerical balance constants are canonized here.

Use three layers:
- **Near-player agents:** individual creatures with position, health, stamina, stage, sensed evidence, AI state, territory and current actions.
- **Far-field populations:** aggregated cohorts by species, life stage, cell and lineage/trait distribution. Conserve individuals and resources when converting between individual and cohort representation.
- **Environmental processes:** slower habitat changes, nutrient and vegetation renewal, flood/drought, shelter damage, and recolonization through valid connectivity.

Simulation tick groups: immediate interactions (movement, attacks, perception); short ecology updates (feeding, resource consumption, migration); long ecology updates (growth, breeding, senescence, vegetation succession). Exact tick rates are engineering parameters to profile, not canon. Offline catch-up must be bounded, deterministic and never grant infinite births or resources.

## 3. Canonical entity and event schema

**SpeciesDefinition**: species_id, anatomy slots, developmental stages, reproduction_mode (including unknown), habitat requirements, diet links with confidence, sensory modalities, locomotion constraints, candidate genetics, behavioral state machine, carrying-capacity factors.

**Individual**: unique ID, species_id, lineage ID, developmental stage, age, cell, position when active, phenotype, trait-expression records with evidence status, health, energy, hydration/oxygen as applicable, injury, reproductive eligibility, current AI state, local memory, owner/authority context where relevant.

**PopulationCohort**: species_id, habitat_cell, life_stage, count, bounded trait-frequency distribution, resource demand, average condition, lineage summary. Cohorts must not invent traits absent in their source population.

**HabitatCell**: stable cell ID, terrain and water variables, resource stocks and regrowth capacities, nesting/shelter availability, connectivity edges, disturbance/restoration state.

**Event**: unique ID, simulation time, event type, cell, actor and target IDs, quantities with units, preconditions, before/after deltas, provenance, deterministic random seed, authority and replay reference.

Event families: feed, move, migrate, attack, capture, absorb, reproduce, hatch/birth, metamorphose, grow, age, die, decompose, pollinate, disperse seed, dig, collapse shelter, flood, drought, restore, mutate, speciate (only after separate validation).

## 4. Lifecycle state transitions

Common conceptual path: viable offspring/egg -> juvenile/larva -> subadult/pupa as species-specific -> reproductive adult -> senescence -> death -> decomposition. Never force every organism through the same anatomy or stages.

| Species | Supported reproduction or development fact | Unknown / guardrail |
|---|---|---|
| Null Slime | Natural reproduction not established | Absorption is not breeding |
| Glassfilm Microbe | Clonal division / fragmentation | No assumed sexual reproduction |
| Reed Skipper | Sheltered reed-base egg clusters | No assumed inheritance mode |
| Silt Burrower | Sediment egg capsules | No assumed fertility with other species |
| Glass-Eyed Pouncer | Concealed litter in dry den | Gestation and genetic mechanism unknown |
| Mire Needle | Protected egg masses/clutches in marsh | Water and oxygen constrain survival |
| Moss-Horn Browser | Dependent young, seasonal reproduction | Offspring count/gestation not finalized |
| Root-Crown Forager | Protected nest chamber, seasonal reproduction | Litter size/gestation not finalized |
| Current Dart | Eggs in oxygenated shallows/vegetation | Silt, flooding, anoxia reduce survival |
| Reedstalker | Elevated concealed nest | Egg vs live-birth **unknown** |
| Bark Lantern | Eggs in humid bark crevices | Deadwood/humidity constrain survival |
| Gloam Moth | Egg -> larva -> pupa -> adult | Reedlace Hostleaf is a host **hypothesis** |

Reproductive eligibility requires species-compatible adults, viable habitat, sufficient energy, resource and shelter capacity, and a documented reproduction mode. For species with unresolved reproduction, do not silently invent offspring production; mark the rule disabled/pending authoring or explicitly simulate only a documented abstract cohort recruitment assumption labeled noncanonical. Mutation is not guaranteed per birth and cannot create a fully functional anatomy without developmental gates.

## 5. Resource-conserving feeding and food-web edges

A feeding event checks target accessibility, species diet eligibility, available biomass, encounter/attack success when applicable, energy gain bounded by consumed biomass, and waste/decomposition outputs. Predator kills reduce real prey counts; prey do not instantly reappear.

| Consumer | Candidate resource/prey | Confidence / gate |
|---|---|---|
| Glassfilm Microbe | light/nutrients in suitable film substrate | Existing dossier physiology; resource balance TBD |
| Reed Skipper | species-specific food per dossier | Verify food item before enabling edge |
| Silt Burrower | species-specific sediment resources per dossier | Verify food item before enabling edge |
| Glass-Eyed Pouncer | exposed suitable Reed Skipper | Size, line of sight, footing, pounce and recovery |
| Mire Needle | accessible wetland prey, possibly Current Dart | Water depth, strike range, turbulence |
| Moss-Horn Browser | leaves, shoots, fruit, soft bark | Browse stock and regrowth |
| Root-Crown Forager | roots, fruit, fungi-like material, small invertebrates | Soil accessibility and food availability |
| Current Dart | drifting microfauna/particles | Flow and water quality |
| Reedstalker | accessible shoreline prey; Current Dart conditional | Actual aquatic capture mechanic required |
| Bark Lantern | fungal films, decaying plant matter | Humid deadwood and fungal food |
| Gloam Moth adult | nectar / compatible plant secretions | Flower availability and flight weather |
| Gloam Moth larva | Reedlace Hostleaf candidate | Host interaction unverified; disabled until validated |

No prey edge is promoted to confirmed implementation solely by its appearance in this table. Explicitly preserve negative constraints: Reedstalker cannot catch submerged Current Dart without aquatic capture logic; Glass-Eyed Pouncer cannot locate buried Silt Burrower by omniscience; Bark Lantern is not automatically a moth predator.

## 6. Local ecological feedback loops

**Aquatic:** precipitation -> water level and connectivity -> dissolved oxygen, flow and nursery suitability -> Current Dart recruitment/foraging -> wetland predator opportunity. Isolated pools lose oxygen/food and cannot repopulate from a disconnected river.

**Woodland:** plant production -> Moss-Horn browse and Root-Crown feeding -> seed deposition, soil disturbance and nutrient cycling -> conditional plant recruitment. Overbrowsing and excessive digging may damage regeneration.

**Deadwood:** standing/fallen wood and humidity -> fungal films -> Bark Lantern survival and signaling -> local detritus turnover. Deadwood removal has persistent shelter consequences.

**Flowers:** suitable host plant + larval survival + adult flight weather -> Gloam Moth flower visits -> actual pollen transfer to compatible flowers -> possible plant seed production. High larval density can suppress host leaves. No automatic pollination bonus.

**Predation:** prey abundance and concealment -> predator feeding -> predator condition and future reproduction -> changed prey survival/behavior -> local vegetation and nutrient effects. No universal predator-is-good/bad flag.

**Disturbance:** player attacks, absorption, trampling, digging, habitat removal and flood damage -> changed habitat/resource stocks -> altered AI movement, recruitment and recovery. Disturbance repair and biological succession use different clocks; previously established ~5-minute repair initiation and ~20-minute ordinary repair limit must not be misread as instant ecological maturity.

## 7. AI, sensing and counterplay

Every creature detects evidence rather than omniscient actor coordinates. Perception channels include sight, sound, chemistry, vibration, water pressure and contact with range/occlusion/noise limits. Sensory confidence is not guaranteed identification. AI state changes consume energy/time, and missed attacks have recovery. Group alarm is local, not telepathic. All threats need at least one feasible early-Slime nonvisual warning cue (chemical, vibration, substrate/water disturbance) with counterplay and false positives.

Behavior states must be auditable: current state, observed cue, confidence, decision reason, cost, target, cooldown and result. Species-specific behaviors remain defined in their dossiers.

## 8. Population dynamics and migration

Births/recruitment are bounded by breeding eligibility, habitat capacity, parental/offspring resources, and juvenile survival. Deaths include predation, starvation, hazard and age; avoid unconditional spawn/despawn cycles. Migration requires a valid habitat edge and capacity at the destination. For population aggregation: N_after = N_before + births + immigration - deaths - emigration, accounting for individual/cohort conversion exactly once. Each feeding/absorption kill is counted once, even under multiplayer contention.

Local extinction is possible. Recovery requires viable neighboring populations or a separately authored recolonization event, not a hidden respawn timer. Planet-wide extinction rules require separate design review.

## 9. Genetics, hybridization and lineage authority

Keep genotype hypotheses separate from observed phenotype and learned skill. A lineage record includes parent references when known, reproduction type, trait origin, developmental gating, expression costs, mutation evidence and confidence. No cross-species fertile offspring unless the compatibility system establishes C3/C4, and no stable new species until C5 criteria are satisfied. All currently proposed pairings are CX. Reproduction cannot be inferred from predation, shared habitat, absorption, symbiosis or morphology alone.

## 10. Multiplayer and persistence contract

Use **server-authoritative** event resolution for feeding, kills, absorption, reproduction, migration, loot and resource changes. Resolve contested events atomically: one prey cannot be consumed twice; one nest cannot issue duplicate offspring on reconnect; resource stocks cannot go negative. Persist stable IDs, species lineage, habitat state, ecological events and time markers. Replay must be deterministic from state, inputs and seeded randomness. Validate client inputs, bound update frequency and preserve save-schema version migrations. Do not design for 1 million fully simulated agents per server without profiling and a proven architecture; near/far simulation and interest management are mandatory scalability candidates.

## 11. Vertical-slice player journey

1. Start as a Null Slime in Reedwater; manually switch chemical and vibration senses and locate safe microhabitats.
2. Observe Glassfilm Microbe and a Reed Skipper through evidence; study before choosing an absorption opportunity.
3. Approach a waterline; sense Current Dart movement and distinguish current noise from a possible Mire Needle.
4. Observe Reedstalker stalking cues and escape using terrain and sensory information.
5. Find Moss-Horn browse damage and Root-Crown digging; witness differing consequences for plant recovery.
6. Inspect humid deadwood for Bark Lantern glow and follow Gloam Moth activity to a candidate flowering patch.
7. Cause one bounded disturbance; watch local resources, animal decisions and later recovery change persistently.
8. Revisit after time passes; observe population changes and habitat state rather than arbitrary respawn.

Each step needs player-readable feedback, accessible nonvisual alternatives, explicit success/failure conditions, and telemetry.

## 12. Engineering acceptance tests (not yet executed)

- **Conservation:** no negative biomass or creature counts; kills and absorption remove exactly one valid target.
- **Reproduction:** no offspring from unknown reproductive modes; eligible eggs fail in unsuitable oxygen/humidity/host conditions.
- **Flow:** disconnecting a pool blocks river immigration and can reduce Current Dart survival.
- **Predation:** Reedstalker cannot capture inaccessible submerged Current Dart; Pouncer cannot pounce through opaque walls.
- **Climate:** drought lowers Bark Lantern surface activity; moth flight responds to rain/wind; flood threatens nests and burrows.
- **Vegetation:** browser seed dispersal requires viable seeds and suitable establishment; overbrowsing can suppress saplings.
- **Deadwood:** clearing occupied wood reduces Bark Lantern shelter, with no instant population refill.
- **Genetics:** CX pairings cannot produce confirmed fertile offspring; learned skills do not become germline traits.
- **Sensing:** early Slime can detect some valid nearby hazards nonvisually without exact x-ray outlines.
- **Multiplayer:** simultaneous capture attempts yield at most one committed consumption event.
- **Persistence:** save/reload and event replay preserve population counts, lineage and habitat state.
- **Performance:** measure agent/cohort transitions and server tick budgets on target hardware before declaring scale targets achieved.

## 13. Delivery sequence and status gates

**Gate A — authored schema:** data models, event contracts, species dependencies, and unresolved biology documented (**this document only**).
**Gate B — executable deterministic simulator:** habitat cells, resources, cohorts, events, invariants and persistence.
**Gate C — 12-species integration:** individual AI, species reproduction modes that are actually defined, resource webs, climate, player sensing.
**Gate D — gameplay vertical slice:** playable Null Slime journey and persistent world effects.
**Gate E — verified release candidate:** automated invariant/regression tests, multiplayer contention tests, save migration, ecological balancing, visual and accessibility playtests, and measured performance.

**Current state:** Gate A design authored; B–E not implemented or verified. The next concrete engineering artifact should be machine-readable species/habitat/event schemas and a minimal deterministic simulation runner with conservation tests.
