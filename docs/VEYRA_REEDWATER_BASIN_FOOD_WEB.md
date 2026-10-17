# Lethal Absorption — Reedwater Basin Food-Web and Biome Linkage Specification

> **Planet:** Veyra  
> **Region:** Reedwater Basin  
> **Status:** Design specification; relationships are hypotheses unless explicitly marked as a physical dependency. Not implemented or simulated.

## 1. Purpose

This document links the starting region's habitats, seasonal states, candidate species, player discovery, and resource renewal. It is a design contract for future implementation, not evidence that a functioning ecosystem simulation exists.

The region is a compact vertical slice: First Drip Hollow, Reedwater Run, Reedglass Marsh, Mossbank Edge, Longgrass Shelf, Flintback Rise, Quietroot Grotto, Siltbend Oxbows, Elderbank Stand, and Southwash Fan. Each area should support at least one ecological role and a navigable route into a neighboring habitat.

## 2. Link types and evidence labels

Every proposed connection must be stored as one of:
- **Consumes:** organism A eats organism B or its specified resource.
- **Predates:** A can capture and consume B under defined conditions.
- **Competes:** A and B use a limiting shared resource.
- **Mutualism:** both receive a measurable benefit.
- **Habitat dependency:** a species requires a specified physical feature or condition.
- **Material flow:** waste, remains, or detritus move into a decomposer/resource pool.
- **Behavioral clue:** one organism's behavior reveals a nearby resource or threat without proving a trophic interaction.

Evidence state:
- **Design hypothesis:** plausible concept awaiting validation.
- **Mechanic specified:** requirements written but not built.
- **Implemented:** code exists and is connected.
- **Tested:** reproducible test evidence exists.
- **Rejected:** interaction is disallowed or unsupported.

No hypothesis should be displayed to players as a proven biological fact until validated.

## 3. Starting-region habitat matrix

| Subregion | Dominant conditions | Anchor roles | Seasonal pressures |
|---|---|---|---|
| First Drip Hollow | Damp shaded source hollow | Slime start, wet rock microbial film, sheltered small prey | Drying, cold, source-flow variation |
| Reedwater Run | Flowing freshwater and vegetated banks | Current Dart, Reed Skipper, shoreline hunters | Flood speed, turbidity, channel connectivity |
| Reedglass Marsh | Shallow channels, reeds, saturated soil | Reed Skipper, Mire Needle, Reedstalker | Flooding, oxygen swings, dry-down |
| Mossbank Edge | Woodland–marsh transition | Moss-Horn Browser, Bark Lantern, Gloam Moth | Humidity, flowering, cover changes |
| Longgrass Shelf | Open grassland with damp margins | Grazers, flying invertebrates, small predators | Drought, fire-like disturbance if introduced, exposure |
| Flintback Rise | Rocky upland and scrub | Glass-Eyed Pouncer, exposed-route refuge | Temperature, wind, scarce cover |
| Quietroot Grotto | Small cave with damp stone and sediment | Glassfilm Microbe, Silt Burrower where substrate permits | Humidity, oxygen, entrance disturbance |
| Siltbend Oxbows | Slow water, mud banks, disconnected pools | Current Dart, Silt Burrower, marsh prey | Pool isolation, low oxygen, crowding |
| Elderbank Stand | Mature woodland and retained deadwood | Moss-Horn Browser, Bark Lantern, Gloam Moth | Drought, deadwood removal, host-plant cycle |
| Southwash Fan | Seasonal channels, deposits and shallow pools | Opportunistic small prey, Current Dart when connected | Flood deposition, channel shift, dry-down |

Species in the matrix are intended presences, not a claim of final population numbers or guaranteed encounters.

## 4. Provisional interaction ledger

| Source | Target/resource | Link type | Conditions and constraints | Evidence |
|---|---|---|---|---|
| Glassfilm Microbe | Wet rock / suitable dissolved nutrients | Habitat dependency | Needs damp, suitable surfaces and resources; not universal on every rock | Design hypothesis |
| Reed Skipper | Surface plant/microbial food | Consumes | Exact diet source must be selected and documented in its dossier | Design hypothesis |
| Silt Burrower | Sediment organic matter / small prey | Consumes | Oxygen, moisture, and substrate stability limit activity | Design hypothesis |
| Glass-Eyed Pouncer | Small ground prey | Predates | Only prey within reach and capture capabilities; failed strikes have recovery | Design hypothesis |
| Mire Needle | Small shallow-water prey | Predates | Requires suitable water depth, concealment, and strike range | Design hypothesis |
| Moss-Horn Browser | Woodland vegetation | Consumes | Browsing pressure constrained by plant renewal and herd density | Design hypothesis |
| Root-Crown Forager | Roots, detritus, small soil organisms | Consumes / material flow | Digging and caching costs; cannot feed on unspecified resources | Design hypothesis |
| Current Dart | Drifting microscopic food / tiny aquatic prey | Consumes | Food density, current, oxygen and connectivity limit population | Design hypothesis |
| Reedstalker | Small shoreline prey | Predates | Current Dart link remains disabled until aquatic capture is designed and tested | Design hypothesis |
| Bark Lantern | Fungal film and decaying plant material | Consumes / material flow | Needs humid crevices and retained deadwood | Design hypothesis |
| Gloam Moth adult | Compatible night-opening flowers | Potential mutualism | Only if pollen transfer and plant reproduction benefit are demonstrated | Design hypothesis |
| Gloam Moth larva | Specified host plant | Consumes | Host plant must be named before simulation | Design hypothesis |
| Organism remains | Detrital resource pool | Material flow | Conversion must be finite and avoid infinite resource loops | Mechanic specified |
| Flood pulse | River/marsh/oxbow connections | Habitat dependency | May connect isolated habitats temporarily; does not guarantee survival or migration | Mechanic specified |

**Important exclusions:** Do not assume Current Dart is eaten by Reedstalker until capture is supported. Do not assume Bark Lantern predates Gloam Moth, or that Gloam Moth pollinates all flowers. Do not create predator alliances merely because species share a habitat.

## 5. Population and resource rules

1. Population is constrained by suitable habitat, food, reproduction, mortality, dispersal, and disturbance; no species should respawn instantly after harvest.
2. Each resource node has a finite stock, renewal conditions, and recovery interval. Harvest can reduce availability and should be recorded against the local patch.
3. Renewal can fail when its conditions fail: microbial films need suitable surfaces and moisture; aquatic prey need viable water; woodland organisms need cover and food plants.
4. A habitat may temporarily support fewer individuals after drought, flooding, contamination, nest loss, or repeated disturbance.
5. Population recovery must not be driven solely by a hidden global timer. Use local carrying capacity and viable source populations when runtime simulation is built.
6. Avoid simulating every individual at full fidelity at all distances. A future implementation may use high-detail nearby agents and aggregated population cohorts at distance, but it must preserve cause-and-effect and reproducible transitions.
7. No numeric birth rates, carrying capacities, drop rates, or recovery times are locked until playtesting and performance profiling.

## 6. Seasonal and disturbance scenarios

- **Rain-swollen river:** Current Dart can move into connected margins; high flow raises movement costs and may reduce visibility. Reedstalker routes shift toward suitable banks.
- **Seasonal flood:** Some subregions connect, but nests and small shelters may be lost. Flooding is not a universal benefit.
- **Dry spell:** Shallow pools shrink, oxygen may fall, prey can concentrate, and predators may become more successful while local populations become more fragile.
- **Fog:** Visual detection range changes; chemical and vibration cues retain their own limits.
- **Repeated predator disturbance:** Prey may shift refuge or feeding times, reducing encounter frequency in that patch.
- **Overharvest:** Local prey and harvestable materials decline; predator activity and player routes should respond only where the simulated dependency exists.
- **Deadwood removal:** Bark Lantern refuge and fungal substrate decrease; this should not automatically change unrelated river populations.

## 7. Player sensory fairness and discovery

The starting Slime begins mostly blind and relies on chemical and vibration senses, with manual sensory-mode switching. It must not receive omniscient species names or exact positions through walls.

- **Chemical mode:** Detect gradients and traces when wind, flow, distance, and contamination permit. It should not distinguish every species by smell automatically.
- **Vibration mode:** Detect local movement transmitted through connected ground or fluid; turbulence, soft substrate, distance, and competing movement reduce confidence.
- **Contact/pressure:** Reliable at close range but offers little advance warning.
- **Visual branches:** Unlocked through compatible eye-bearing species; each branch has explicit field of view, low-light limits, motion sensitivity, and tradeoffs.
- **Flying prey:** Provide sound, shadow, airflow, flower visitation, or landing clues so vision is not the sole valid method.
- **Predators:** Give readable but imperfect warning cues. No invisible unavoidable strikes in the starting region.

## 8. Validation gates before this becomes a runtime system

- [ ] **G1 — Dossier coverage:** Every active species has a dossier with diet, life stages, habitat, senses, behavior, and mortality.
- [ ] **G2 — Edge validity:** Every enabled food-web edge names its conditions, failure states, and evidence.
- [ ] **G3 — Conservation:** Resource creation and consumption reconcile; no unlimited harvest loop or free energy.
- [ ] **G4 — Seasonal transition:** Flood/dry transitions alter connectivity and survival without arbitrary instant resets.
- [ ] **G5 — Player fairness:** Sensory clues are discoverable and range-limited; predators allow counterplay.
- [ ] **G6 — Recovery:** Population and habitat recover only when viable conditions exist.
- [ ] **G7 — Performance:** Nearby and distant simulation tiers preserve comparable outcomes under repeatable test seeds.
- [ ] **G8 — Reproducibility:** Logs record seed, environmental state, population transitions, harvest, predation, and test outcomes.

## 9. Implementation boundary

This document and linked dossiers are authored design. No runtime food web, AI, population model, procedural biome generation, or ecological balancing is claimed implemented. Future code should be built from these contracts, with data-driven species and edge records, deterministic test fixtures, and explicit test results.

## 10. Immediate build order

1. Finalize at least one named plant/host resource for Reed Skipper, Moss-Horn Browser, and Gloam Moth larvae.
2. Create a single machine-readable schema for species, habitat, and interaction edges.
3. Implement a small deterministic Reedwater Basin sandbox with a handful of species and resource nodes.
4. Add test scenarios for flood, dry spell, overharvest, and predator disturbance.
5. Reconcile results against this ledger before expanding to the other continents of Veyra.
