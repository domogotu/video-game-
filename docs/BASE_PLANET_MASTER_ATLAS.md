# Lethal Absorption — Canonical Base Planet Master Atlas

> **Status:** Foundational design specification; design-only, not implemented, simulated, or tested.
> **Role:** The canonical reference planet used to validate world rules, biome construction, species ecology, absorption, evolution, trainers, resources, and future procedural planet generation.
> **Working planet name:** Veyra (editable working name; do not treat as a final lore lock until reviewed).
> **Core rule:** Every later planet inherits the shared world schema and simulation contracts, not Veyra's exact geography or species placements.

## 1. Mission and source of truth

Veyra is the first end-to-end planetary reference for Lethal Absorption. It is not meant to be the largest possible world; it is the **complete systems reference** against which later worlds are generated and audited.

This atlas links to:
- `docs/GAME_DESIGN_BIBLE.md`
- `docs/ECOLOGY_AND_CROSSLINKED_EVOLUTION_ATLAS.md`
- `docs/SPECIES_SKILLS_AND_TRAINERS_ATLAS.md`
- `docs/SLIME_MASTER_CHARACTER_BLUEPRINT.md`
- `docs/SKILL_TREE_AND_EVOLUTION_ATLAS.md`
- `docs/LIVE_PREY_CAPTURE_AND_STAMINA_ABSORPTION.md`
- `docs/COHABITATION_BREEDING_AND_HERITABLE_TRAITS_SYSTEM.md` — planet-wide relationship, breeding, inheritance, and population-selection rules

Those documents remain the authority for their respective system-level rules. This document defines the first shared planetary reference and the contracts every planet-generation pass must obey.

### Canon labels

- **FOUNDATION:** a rule other systems must respect.
- **PROPOSED CANON:** a concrete initial world-design choice that can be revised deliberately.
- **OPEN:** requires further design, simulation, or playtesting.
- **NOT IMPLEMENTED:** documented only; do not describe it as a working game feature.

## 2. Planet identity card

| Property | Veyra reference value | Status / rationale |
|---|---|---|
| Planet class | Temperate, water-bearing terrestrial world | PROPOSED CANON |
| Star | One stable, Sun-like main-sequence star | PROPOSED CANON |
| Natural satellites | One large moon and one small irregular moonlet | PROPOSED CANON |
| Surface gravity | 0.92 g | PROPOSED CANON; movement and mass tuning reference |
| Day length | 26 standard hours | PROPOSED CANON |
| Year length | 412 local days | PROPOSED CANON |
| Axial tilt | 21 degrees | PROPOSED CANON; supports seasons |
| Surface water | Approximately 64% | PROPOSED CANON |
| Atmosphere | Nitrogen/oxygen-dominant, water-bearing, breathable to baseline human-like visitors only after local contaminant screening | PROPOSED CANON; not a safety claim |
| Magnetic field | Present, with regional auroral activity | PROPOSED CANON |
| Main landmasses | Four major continents, two polar caps, archipelagos and island arcs | PROPOSED CANON |
| Planetary age | Mature world with ancient geology and extant active tectonic zones | PROPOSED CANON |
| Civilization baseline | Multiple sapient societies; no single global empire | PROPOSED CANON |
| Starting region | A temperate river basin adjoining woodland, wetland and upland transitions | PROPOSED CANON |
| Player start | Cellular origin / Stage 0, with the Slime route as a supported early path | FOUNDATION |

All numbers above are reference parameters, not scientific validation or implemented simulation values. Future revisions must be recorded with rationale and checked against gravity, climate, movement, biology, and world-generation assumptions.

## 3. Planetary structure and geography

### 3.1 Planet-scale layers

1. **Core and mantle:** internal heat drives tectonics, geothermal fields, volcanism and mineral distribution.
2. **Crust:** old continental shields, young mountain belts, rift valleys, volcanic arcs, sedimentary basins and oceanic crust.
3. **Hydrosphere:** open ocean, inland seas, lakes, rivers, aquifers, wetlands, seasonal floodplains, glaciers and brine pockets.
4. **Atmosphere:** circulation cells, prevailing winds, storm tracks, cloud systems, seasonal monsoons, dust transport and high-altitude jet streams.
5. **Biosphere:** linked terrestrial, freshwater, marine, subterranean, aerial and extremophile food webs.
6. **Noosphere / built environment:** settlements, ruins, roads, farms, industrial sites, research stations, sacred or restricted places, and contested frontiers.

### 3.2 Continental planning template

Each major continent must have a distinct climate spine and connected watersheds, not a random collection of isolated biome tiles.

- **Northreach:** cool temperate forests, boreal belts, alpine chains, glacial lakes and subpolar coast.
- **Serevan:** warm grasslands, seasonal forests, broad river basins, dry interior and monsoon-facing coasts.
- **Ashkar:** arid plateaus, dune seas, salt basins, canyon networks, volcanic uplands and scattered oases.
- **Myrdeep:** humid equatorial forests, high-rainfall mountains, extensive deltas, peat wetlands and coastal mangroves.
- **Polar caps and island arcs:** ice shelves, tundra margins, geothermal refugia, stormy islands and isolated endemic habitats.

These are geographic planning anchors. Exact map shapes, borders, settlement coordinates and travel distances remain OPEN until a world map is authored.

### 3.3 Geology-to-biome rules

- Mountain rain shadows create plausible wet-to-dry transitions.
- Rivers flow downhill from headwaters to lakes, wetlands, deltas or ocean.
- Soil fertility depends on parent rock, organic cycling, water and disturbance.
- Volcanic and geothermal regions cluster around plausible tectonic structures.
- Glaciers and permanent snow follow elevation, latitude and climate.
- Caves connect to geology, groundwater, fissures, lava tubes or karst; not every cave network connects to every other.
- Biome boundaries can shift over seasons and long timescales; ecological zones are not immutable painted borders.

## 4. Canonical biome atlas

The list below defines the **required biome families** for Veyra. Each individual biome instance must receive a unique ID, region, elevation/depth band, climate envelope, seasonal profile, hydrology, substrate, hazards, species population, resource table, transition neighbors and discovery state.

### 4.1 Surface terrestrial biomes

| Biome ID | Biome | Environmental identity | Typical ecological roles |
|---|---|---|---|
| SUR-TEM-FOR | Temperate broadleaf forest | Seasonal canopy, layered understory, leaf litter and streams | Browsers, small prey, ambush predators, decomposers |
| SUR-CON-FOR | Conifer / boreal forest | Cold winters, resinous canopy, acidic soils, snow and bog edges | Cold-adapted grazers, burrowers, pack hunters |
| SUR-RAI-EQU | Equatorial rainforest | High humidity, dense vertical layers, rapid decomposition | Arboreal feeders, gliders, parasites, specialist predators |
| SUR-MON-FOR | Seasonal monsoon forest | Wet/dry seasons, flood pulses, seasonal fruiting | Migratory herds, amphibious species, ambush hunters |
| SUR-GRA-TEM | Temperate grassland | Deep-rooted grasses, fire cycles, open sightlines | Herd grazers, pursuit predators, burrowers |
| SUR-SAV-TRO | Tropical savanna | Seasonal water scarcity, scattered trees and tall grasses | Large grazers, scavengers, pack predators |
| SUR-SHR-MED | Mediterranean scrub | Dry summers, wet winters, aromatic shrubs and fire adaptation | Browsers, small omnivores, heat-tolerant hunters |
| SUR-DES-HOT | Hot desert | Low rainfall, high thermal range, sparse cover | Nocturnal foragers, water conservers, burrowers |
| SUR-DES-COLD | Cold desert | Low precipitation, freeze-thaw stress, sparse vegetation | Cold-tolerant scavengers, seasonal specialists |
| SUR-PLA-ALP | High plateau | Thin air, intense radiation, large daily temperature swing | Endurance specialists, cliff fauna, hardy grazers |
| SUR-TUN-POL | Tundra | Permafrost, short growing season, low shrubs and seasonal pools | Migratory grazers, burrowers, cold-adapted predators |
| SUR-ALP-MEA | Alpine meadow | Elevation-driven cold, summer bloom, steep terrain | Climbers, pollinators, small predators |
| SUR-ALP-ROC | Alpine rock / scree | Exposed stone, unstable slopes, thin soil | Crevice dwellers, gliders, ambush specialists |
| SUR-WET-MAR | Marsh / freshwater wetland | Saturated soils, emergent plants and shallow channels | Amphibious species, filter feeders, waders |
| SUR-BOG-PEAT | Peat bog | Acidic water, slow decay, soft substrate and gas pockets | Small specialists, decomposers, ambush predators |
| SUR-FEN-MIN | Mineral-rich fen | Groundwater-fed wetland, mineral gradients | Grazers, amphibians, mineral-seeking organisms |
| SUR-MAN-MNG | Mangrove / tidal forest | Brackish tides, aerial roots and shifting mud | Juvenile marine fauna, climbers, detritivores |
| SUR-RIV-FLD | Floodplain / river delta | Seasonal inundation, fertile silt, shifting channels | Fish-spawning species, grazers, scavengers |
| SUR-SAL-FLT | Salt flat / saline basin | Evaporation, salt crust, brine pockets and scarce shade | Salt-tolerant microbes, brine feeders, migratory visitors |
| SUR-DUN-SEA | Dune sea | Mobile sand, buried habitats, wind exposure | Sand burrowers, nocturnal hunters, surface skimmers |
| SUR-CAN-DRY | Dry canyon / badlands | Erosion channels, cliffs, flash floods and thermal stress | Climbers, nesters, ambush predators |
| SUR-VOL-ASH | Volcanic ash field | Unstable ash, toxic gases near vents, mineral-rich soils | Extremotolerant microbes, opportunistic scavengers |
| SUR-GEO-FLD | Geothermal field | Hot springs, mineral crusts, steam vents and temperature gradients | Thermotolerant specialists; unsafe zones require warning cues |
| SUR-BUR-OLD | Ancient woodland / old-growth refuge | Long-lived canopy, deadwood, deep soils and rare niches | Long-lived species, rare symbionts, ancient lineages |
| SUR-ANT-DIS | Disturbed / recovering land | Fire, storm, landslide or abandoned development succession | Pioneer species, scavengers, invasive-risk populations |

### 4.2 Marine and freshwater biomes

| Biome ID | Biome | Environmental identity | Typical ecological roles |
|---|---|---|---|
| AQU-COA-ROC | Rocky shore / tide pools | Tides, wave impact, pools and exposure cycles | Clingers, shell-like fauna, tide-window feeders |
| AQU-COA-SND | Sandy shore | Shifting substrate, surf, burrowing zones | Filter feeders, beach scavengers, nesting species |
| AQU-REE-COR | Coral-like reef | High structural complexity and symbiosis | Small grazers, ambush predators, cleaning symbionts |
| AQU-REE-COL | Cold-water reef | Low temperature, slower growth, deep structure | Cold-adapted filter feeders and hunters |
| AQU-KEL-FO | Kelp forest | Strong currents, layered vegetation, changing light | Browsers, stalkers, hiding prey |
| AQU-SEA-GRA | Seagrass meadow | Shallow sunlit substrate and nursery habitat | Grazers, juvenile fish-like species, burrowers |
| AQU-PEL-SUR | Open-ocean epipelagic | Sunlit water, currents, seasonal productivity | Schooling prey, pursuit predators, migrators |
| AQU-PEL-MES | Twilight ocean | Low light, pressure increase and vertical migration | Light-sensitive species, ambush hunters |
| AQU-PEL-BAT | Deep ocean / bathyal | Darkness, high pressure, sparse food | Slow-metabolism fauna, sensory specialists |
| AQU-ABY-PLA | Abyssal plain | Near-freezing darkness, sediment and food falls | Deposit feeders, scavengers, rare large fauna |
| AQU-HYD-VENT | Hydrothermal vent | Mineral-rich hot fluids, steep chemical gradients | Chemosynthetic base web and vent specialists |
| AQU-TRN-VENT | Cold seep | Methane/sulfide seepage and sediment mounds | Chemosynthetic symbionts and specialist feeders |
| AQU-TRE-FO | Ocean trench | Extreme pressure, darkness, isolated habitat | Pressure-specialized species; rare encounters |
| AQU-ICE-SEA | Under-ice sea | Seasonal ice cover, brine channels and limited light | Ice-associated feeders and cold specialists |
| AQU-EST-BRA | Estuary / brackish water | Salinity gradients, tidal exchange and nutrient pulses | Euryhaline species, nursery populations |
| AQU-RIV-UP | Upland river | Fast current, cold water, oxygenation and rock | Stream clingers, agile swimmers, insect-like prey |
| AQU-RIV-LO | Lowland river | Slower current, sediment, flood pulses and banks | Burrowers, ambush predators, migratory fauna |
| AQU-LAK-OLI | Oligotrophic lake | Clear water, low nutrients, layered temperatures | Specialized plankton feeders and deep-water fauna |
| AQU-LAK-EUT | Productive lake | Nutrient-rich water, blooms and seasonal oxygen shifts | Grazers, scavengers, bloom-dependent populations |
| AQU-CAV-UND | Underground lake / river | Darkness, stable temperature, mineral chemistry | Reduced-vision species, chemical/vibration specialists |
| AQU-BRI-POOL | Brine pool | Extreme salinity and density layers | Specialized microbes and highly restricted fauna |

### 4.3 Subterranean and enclosed biomes

| Biome ID | Biome | Environmental identity | Typical ecological roles |
|---|---|---|---|
| SUB-KAR-CAV | Karst cave | Dissolution chambers, groundwater and fragile formations | Blind or low-light specialists, bats/analogs, scavengers |
| SUB-LAV-TUB | Lava tube | Volcanic tunnels, dry chambers and local heat | Cave fauna, geothermal specialists, rare minerals |
| SUB-MYC-NET | Fungal / mycelial network | Organic substrate, moisture and spore transport | Decomposers, symbionts, parasites and predators |
| SUB-ROOT-LAB | Deep root labyrinth | Root networks, soil fauna and variable oxygen | Burrowers, root feeders, ambush species |
| SUB-CRY-ICE | Subglacial caverns | Ice, meltwater, pressure and low nutrients | Cold-adapted microbial webs and rare fauna |
| SUB-CRY-DEP | Crystal-bearing cavern | Mineral growth, reflective surfaces and acoustic echoes | Mineral grazers or nesters where food supports them |
| SUB-GEO-CHM | Geothermal subterrane | Heat, gases, mineral water and oxygen-poor pockets | Chemosynthetic or heat-tolerant specialists |
| SUB-ANX-RUI | Buried ruins / sealed complex | Artificial corridors, old hazards and altered microclimate | Opportunists, relic guardians, human/sapient traces |
| SUB-ABY-FIS | Deep fissure | Vertical drop, unstable ledges and localized airflow | Climbers, gliders, wall cling specialists |
| SUB-UNDER-AQF | Deep aquifer | Confined groundwater, mineral gradients and limited nutrients | Chemical-sense specialists and filter feeders |

### 4.4 Atmospheric, aerial and high-altitude biomes

| Biome ID | Biome | Environmental identity | Typical ecological roles |
|---|---|---|---|
| AIR-CAN-FO | Forest canopy | Wind, branches, vertical routes and changing exposure | Climbers, gliders, arboreal predators |
| AIR-CLI-ROC | Cliff face / updraft corridor | Shear winds, nesting ledges and fall hazards | Flyers, climbers, cliff ambushers |
| AIR-MIG-ROU | Seasonal migration corridor | Predictable winds, thermal lift and resting sites | Migrators, aerial hunters and scavengers |
| AIR-ALP-THN | Thin-air high atmosphere | Low density, cold, strong UV and low oxygen | Specialized flyers; severe stamina and altitude constraints |
| AIR-STO-FRO | Storm belt | Lightning, turbulence, hail and rapidly changing pressure | Storm-avoiding fauna; rare storm-adapted species |
| AIR-CAV-VENT | Cave airflow network | Drafts, thermal gradients, spores and scent transport | Gliders in large chambers, flying cave fauna |
| AIR-ISL-SEA | Offshore island wind zone | Salt spray, strong gusts and nesting cliffs | Seabird analogs, gliders, island endemics |

### 4.5 Seasonal, transient, and anomalous ecological zones

| Biome ID | Biome | Environmental identity | Typical ecological roles |
|---|---|---|---|
| EVT-FLO-SEAS | Seasonal flood zone | Temporary wetlands, displaced prey and altered routes | Seasonal breeders, migrators, ambush hunters |
| EVT-FIR-REC | Recent burn scar | Heat-damaged soil, ash nutrients and sparse cover | Pioneer species, scavengers, opportunistic predators |
| EVT-STO-DAM | Storm-impact zone | Debris, changed channels and temporary shelter | Scavengers, displaced wildlife, rescue/repair opportunities |
| EVT-BLO-ALG | Algal / microbial bloom zone | Oxygen and toxin risks vary by organism and conditions | Bloom feeders, tolerant species, die-off scavengers |
| EVT-INV-POC | Invasive-species pocket | Ecological imbalance caused by introduction or disturbance | Competition, control or coexistence quest chains |
| EVT-ANM-RES | Anomalous ecology reserve | Explicitly fictional physics or biology with readable rules | Rare creatures, high-risk research and unique evolution clues |
| EVT-ARC-REF | Ancient refugium | Stable microclimate preserving old lineages | Relict species, rare traits and fragile conservation choices |

### 4.6 Biome completeness rule

A biome is not complete merely because it has a name or landscape art. Each biome instance must document:

1. ID, parent family, map footprint, elevation/depth and neighboring transitions.
2. Temperature, moisture, seasonal range, light, wind/current, substrate, water chemistry and hazards.
3. Producer/decomposer foundation, food availability and carrying-capacity assumptions.
4. Resident, migratory, breeding, transient and rare species; life stages and population evidence.
5. Food-web links, competition, symbiosis, disease/parasites where appropriate, and predator-prey response.
6. Resources, harvesting conditions, regeneration rates, scarcity, and consequences of overharvesting.
7. Navigation affordances, movement constraints, sensing conditions and visibility limits.
8. Weather/events, disturbance and recovery/succession rules.
9. Player discovery cues, danger communication, accessibility and counterplay.
10. Cross-links to species, skills, trainers, crafting, quests, evolution, and procedural-generation rules.

## 5. Species architecture and first-pass roster

**Important coverage rule:** The following is a starter roster of original design candidates, not a claim that all species are fully designed. Every named candidate needs a canonical species page before it can be marked complete. New species discovered during worldbuilding must be added to the index rather than hidden in prose.

### 5.1 Species record contract

Every species record requires:
- Stable species ID, display name, taxonomy/lineage, originality note, and status.
- Body plan, size range, mass, life stages, lifespan class, reproduction, diet and locomotion.
- Native and seasonal biomes; range, migration, shelter and nesting/breeding behavior.
- Primary senses, sensory blind spots, detection range bands and environmental interference.
- Baseline attributes and relevant physiological resources; injury, exhaustion, recovery and death rules.
- Innate abilities; skills learned through observation, trainer/mentor, practice, research or absorption.
- Predation, prey, competition, symbiosis, parasites/disease and scavenging relationships where relevant.
- Defensive behaviors, threat thresholds, flee/territorial/group responses and evidence-based AI perception.
- Absorption eligibility, biological compatibility, trait conflicts, processing risk and limits.
- Resource drops or nonlethal study outputs, crafting uses and ecological cost.
- Evolutionary relatives, regional variants, mutations, rare/alpha/apex/ancient/named variants.
- Counterplay, failure modes, accessibility/readability, PvP agency constraints where relevant.
- Discovery state, evidence source, unresolved questions, implementation status and test status.

### 5.2 Initial species families and candidates

Names below are original working names and may change during the naming pass. Species do not all need to be hostile or absorbable. Sapient beings have agency; a trainer relationship cannot imply ownership or automatic consent.

| Species ID | Working name / family | Ecological role | Native habitat anchors | Design status |
|---|---|---|---|---|
| LA-PLN-SLM-001 | Null Slime (base slime lineage) | Player-capable flexible omnivore / opportunist | Wet woodland edges, river basin, caves | FOUNDATIONAL; use existing Slime blueprint |
| LA-PLN-MIC-001 | Glassfilm Microbe | Primary producer / biofilm former | Wet rock, lake shallows, caves | Candidate |
| LA-PLN-MIC-002 | Ember Mat | Heat-tolerant microbial producer | Geothermal field, volcanic ash | Candidate |
| LA-PLN-MIC-003 | Brine Lace | Salt-tolerant microbial producer | Salt flats, brine pools | Candidate |
| LA-PLN-INV-001 | Reed Skipper | Small wetland grazer / prey | Marsh, river delta | Candidate |
| LA-PLN-INV-002 | Bark Lantern | Nocturnal pollinator / prey | Forest, scrub, canopy | Candidate |
| LA-PLN-INV-003 | Stoneback Grazerling | Small armored detritivore / prey | Grassland, woodland edge | Candidate |
| LA-PLN-INV-004 | Silt Burrower | Sediment feeder / prey | Riverbanks, wetlands, estuaries | Candidate |
| LA-PLN-INV-005 | Gloam Moth | Night pollinator / prey | Forest, cave mouths, old growth | Candidate |
| LA-PLN-AMP-001 | Glass-Eyed Pouncer | Small ambush predator | Scrub, canyon, rocky woodland | Candidate |
| LA-PLN-AMP-002 | Mire Needle | Wetland ambush predator | Marsh, bog, river edge | Candidate |
| LA-PLN-HER-001 | Moss-Horn Browser | Medium herbivore / seed disperser | Temperate forest, old growth | Candidate |
| LA-PLN-HER-002 | Longstride Grazer | Herd grazer / migration driver | Grassland, savanna, floodplain | Candidate |
| LA-PLN-HER-003 | Frostveil Grazer | Cold-adapted herd grazer | Boreal forest, tundra, alpine meadow | Candidate |
| LA-PLN-OMN-001 | Cinder Rummager | Omnivorous scavenger | Ash field, dry canyon, scrub | Candidate |
| LA-PLN-OMN-002 | Root-Crown Forager | Burrowing omnivore / soil engineer | Forest, grassland, root labyrinth | Candidate |
| LA-PLN-PRE-001 | Reedstalker | Medium pursuit / ambush predator | Wetland, floodplain, river edge | Candidate |
| LA-PLN-PRE-002 | Duskcoil | Serpentine predator | Scrub, canyon, dry forest | Candidate |
| LA-PLN-PRE-003 | Ridge Prowler | Pack hunter | Alpine foothills, plateau, grassland | Candidate |
| LA-PLN-APX-001 | Thunder-Crest Colossus | Regional apex / territorial titan | Mountain passes, storm corridors | Candidate; encounter rules needed |
| LA-PLN-APX-002 | Mire Crown | Wetland apex | Deep marsh, delta channels | Candidate |
| LA-PLN-AQU-001 | Current Dart | Schooling aquatic prey | Rivers, lakes, estuaries | Candidate |
| LA-PLN-AQU-002 | Siltjaw | Aquatic ambush predator | Lowland river, estuary | Candidate |
| LA-PLN-AQU-003 | Lantern Drift | Deep-water lure feeder / predator | Twilight ocean, deep lakes | Candidate |
| LA-PLN-AQU-004 | Ventroot Colony | Chemosynthetic symbiotic colony | Hydrothermal vents, cold seeps | Candidate |
| LA-PLN-AIR-001 | Windglass Glider | Gliding omnivore / seed disperser | Canopy, cliffs, island winds | Candidate |
| LA-PLN-AIR-002 | Stormwing Hunter | Aerial pursuit predator | Updraft corridors, storm-belt margins | Candidate |
| LA-PLN-CAV-001 | Echo Mite | Cave detritivore / prey | Karst caves, lava tubes | Candidate |
| LA-PLN-CAV-002 | Pale Threader | Cave ambush predator | Subterranean streams, root labyrinth | Candidate |
| LA-PLN-EXT-001 | Sulfur Veil | Extremophile colony | Geothermal subterrane, vents | Candidate |
| LA-PLN-EXT-002 | Frostglass Crawler | Cold specialist | Subglacial caverns, polar caves | Candidate |
| LA-PLN-SYM-001 | Brushback Cleaner | Mutualistic parasite-remover | Reef, large-herbivore range | Candidate |
| LA-PLN-SAP-001 | Veyran River Communities | Sapient societies (multiple cultures, not one species-wide faction) | River basins, coasts and trade corridors | Candidate; cultural and agency review required |
| LA-PLN-SAP-002 | Canopy Concords | Sapient forest-dwelling communities | Rainforest, old-growth canopy | Candidate; cultural and agency review required |
| LA-PLN-SAP-003 | Deep Archive Enclaves | Sapient subterranean communities | Cave cities, buried ruins | Candidate; cultural and agency review required |
| LA-PLN-ANC-001 | Rootbound Elder | Ancient lineage / rare ecological keystone | Ancient woodland refugium | Candidate |
| LA-PLN-ANM-001 | Rift-Touched Organism | Anomalous rare lineage | Anomalous reserve only where rules support it | Candidate; fictional anomaly contract required |

This table is deliberately a starter set. It does **not** mean that Veyra currently has only these species, that each has final stats, or that any has been implemented. A species can have regional forms, sex/life-stage differences, non-hostile behavior, and population variants without those automatically becoming separate species. Create separate species IDs when the differences affect taxonomy, compatibility, ecology, or gameplay enough to warrant it.

## 6. Food-web and population contracts

### 6.1 Functional guilds

Every substantial biome needs enough ecological functions to support its inhabitants:
- Primary producers (photosynthetic or fictional energy-capturing base).
- Detritus and waste processors.
- Herbivores/grazers and other primary consumers.
- Small prey and mid-level consumers.
- Predators, scavengers and carrion processors.
- Pollinators, seed/spore dispersers, soil engineers and ecosystem modifiers where relevant.
- Parasites/pathogens only when their gameplay, spread and counterplay are documented.
- Keystone, symbiotic and habitat-forming organisms where the environment depends on them.

A biome with no plausible food/energy source cannot sustain a large permanent predator population without an explicitly documented external energy source.

### 6.2 Population model

Population simulation must be scale-aware and need not simulate every organism individually:
- Individual simulation for nearby, quest-critical, named, tracked or actively interacting creatures.
- Group/cohort simulation for distant herds, flocks, schools, colonies and burrows.
- Statistical regional updates for distant populations, with transitions preserving plausible population counts.
- Reproduction, maturation, migration, predation, starvation, disease, injury, weather and habitat change modify population state.
- Harvesting, hunting and absorption remove organisms or alter their condition; resources do not respawn instantly without an explicit mechanism.
- Simulated populations must not duplicate when switching between individual, group and regional representation.
- The world should retain meaningful ecological consequences while avoiding needless per-creature simulation everywhere.

### 6.3 Relationship graph

Every completed species page must link its relationships using stable IDs:
- eats / is eaten by;
- competes with;
- pollinates / disperses;
- cleans / is cleaned by;
- parasitizes / is host to;
- shelters / is sheltered by;
- migrates with / follows;
- changes habitat or resource availability;
- shares trait compatibility or incompatibility with;
- teaches, mentors, or can be studied for an ability.

Relationships must be directional where appropriate and should identify life stage or conditions if the relationship only applies sometimes.

## 7. Climate, weather, seasons, and hazards

### Climate and seasons
- Climate is driven by latitude, altitude, ocean currents, continentality, prevailing winds, water availability, axial tilt and seasonal orbital position.
- Weather is local and time-dependent; climate is the long-term range, not today's condition.
- Seasons alter breeding, migration, food, camouflage, water access, snow/ice, fire risk and biome accessibility.
- Extreme events should have lead-up signals where possible, meaningful counterplay, and persistent consequences followed by recovery.

### Hazard categories
- Thermal: heat, cold, thermal shock, burns, frost injury.
- Hydrological: flood, drought, currents, undertow, waterlogging, dehydration.
- Atmospheric: lightning, wind, low oxygen, altitude stress, toxic gas, airborne particulates.
- Geological: landslide, cave-in, unstable ice, lava, ash, sinkholes, geothermal vents.
- Biological: venom, irritants, parasites, disease, spores, bloom toxins.
- Anomalous: explicitly fictional effects with stable rules, warning cues and counters.

Hazards act through shared character condition and anatomy rules. Do not create a hazard that bypasses established defenses without explaining why.

## 8. Sensory and movement coherence

The base planet must honor Lethal Absorption's anatomy-dependent sensing and movement:
- The base Slime is mostly blind and initially relies on chemical sampling, contact/pressure and vibration cues; it has no default conventional image-forming vision.
- Sensory interpretation is manually switched by the player. Only unlocked senses are selectable, and every mode has blind spots, interference and costs where appropriate.
- Sight, echolocation, chemical tracking, electrical sensing, thermal detection and vibration perception are separate modalities, not a single omniscient detection channel.
- Through-wall detection requires a physically plausible signal path; sensing does not automatically reveal identity, health bars or intent.
- Crawling, squeezing, short compression hops and limited surface climbing are valid early Slime movement modes. Surface, moisture, slope, gravity, contamination, mass, injury and fatigue alter their reliability.
- Biome geometry must expose both accessible routes and anatomy-dependent routes, without assuming every build can traverse every space.

## 9. Absorption, traits, skills, and trainers

- A target's species record declares what can be consumed, studied, safely processed, absorbed, imprinted, or not acquired at all.
- Absorption is not automatic full-skill theft. Intake, survival, analysis, compatibility, integration, practice and mastery remain distinct steps.
- When active live-prey absorption begins, target health drains over time according to the existing capture/absorption rules; defenses, struggle, stamina, condition and compatibility matter.
- Trainers and mentors must have a documented location/access method, knowledge domain, prerequisites, cost or reciprocal exchange, trust/agency conditions, and unavailable-state behavior.
- Wildlife can teach by observation without being a trainer. Sapient beings cannot be reduced to a skill vending machine; consent, trust, exchange, culture and consequences apply.
- Skill pages use `docs/SPECIES_SKILLS_AND_TRAINERS_ATLAS.md` as the required schema.
- The Evolution Atlas remains cross-linked and history-sensitive; no fixed class system is introduced.

## 10. Resource, harvest, and crafting ecology

Each harvestable resource needs:
- Stable ID, source species/biome/geology, extraction method and required anatomy/tool/skill.
- Renewable, slow-renewing, finite or nonrenewable classification.
- Yield range, quality factors, seasonal availability, storage/decay and contamination.
- Ecological role: what is harmed or changed by extraction, and what recovers afterward.
- Crafting/research/evolution uses, substitutes and scarcity controls.
- Nonlethal study or sample routes where appropriate.
- Rules against unlimited repeat harvesting from one unchanged node.

Resources can include biological materials, mineral deposits, water, fibers, resins, toxins, food, energy-bearing organs, research traces and crafted salvage. Rare evolutionary materials must have discoverable logic, not arbitrary drops alone.

## 11. Settlement, ruins, trainers, and intelligent life

Every settlement or site must define:
- Population and governance model, culture, language/communication assumptions, needs and local ecology.
- Food, water, energy, waste, trade routes, defenses, transport and environmental footprint.
- Local relationships with species, hazards, resources and neighboring settlements.
- Trainers, mentors, healers, researchers, craftspeople and other service roles with availability conditions.
- Quest states, faction reputation, trust, conflict, consent, and consequences.
- Evidence-backed knowledge: residents know what their experience or culture supports; they are not omniscient quest databases.
- Ruins and sealed sites need an origin hypothesis, physical access logic, hazard model, and clues that allow players to reason about them.

No single sapient culture should be treated as internally uniform. Individuals and communities can disagree.

## 12. Base-planet world-generation contract

Veyra is the baseline reference, not a fixed mold. Future planet generation must separate **shared rules** from **planet-specific parameters**.

### Shared invariant layer
- Species/biome record schemas and stable ID requirements.
- Food-web and population conservation rules.
- Evolution, absorption, trainer and skill-acquisition contracts.
- Anatomy-dependent sensing, movement, injury and recovery.
- Resource renewal, harvesting consequences and scarcity.
- NPC knowledge limits, agency and social consequence.
- Hazard signaling, counterplay and accessibility expectations.
- PvP cannot permanently delete a player character or strip that character's progression/possessions, per the game design bible.
- Discovery confidence and evidence states in the Evolutionary Codex.
- Explicit separation of design, implementation, and test status.

### Planet-specific parameter layer
- Star system, orbit, gravity, day/year length, axial tilt, atmosphere and hydrosphere.
- Continents, oceans, elevation, bathymetry, watersheds, climate and biome map.
- Native species pool, endemic lineages, invasive introductions and species distribution.
- Local evolutionary pressures, resources, civilizations, histories, hazards and anomalies.
- Unique quests, trainers, ruins, apex encounters, discoveries and environmental events.

### Generation pipeline
1. Define orbital, geological and atmospheric parameters.
2. Generate tectonic plates, elevation, bathymetry and watersheds.
3. Solve broad climate bands and seasonal circulation.
4. Assign biome families and transition zones based on physical inputs.
5. Establish producer/decomposer bases and hydrological energy/material cycles.
6. Place viable species according to habitat needs, dispersal, barriers and history.
7. Validate food webs, population capacity, predator-prey links and migration paths.
8. Place settlements and sites using water, resources, routes, hazards and ecological limits.
9. Add trainers, discoveries, quests and rare encounters only where world logic supports them.
10. Run audits for impossible geography, unsupported species, broken food webs, resource exploits and contradictory lore.
11. Store seed, generator version, parameter set and change history for reproducibility.
12. Label output as generated/proposed until validated; never claim runtime success from documentation alone.

## 13. Validation gates for a completed base planet

A gate is not passed just because its checklist has been written. Record evidence and status.

- **Gate A — Geography:** coastlines, elevations, drainage, currents, climate and transitions are coherent.
- **Gate B — Biome coverage:** every required biome family has at least one defined instance or a documented reason it is absent.
- **Gate C — Species coverage:** every roster entry has a full species record, habitat distribution, life cycle, ecology and status.
- **Gate D — Food webs:** energy/food sources, prey, predators, decomposers and population constraints are coherent.
- **Gate E — Movement and senses:** each species' anatomy, senses and movement fit its habitat; player routes have readable constraints and counters.
- **Gate F — Absorption and progression:** each eligible trait has a source, compatibility, prerequisites, costs, risks, counters and learning route.
- **Gate G — Social systems:** sapient agency, trainers, settlements, knowledge limits and consequences are documented.
- **Gate H — Resources:** renewable and finite resources have extraction, regeneration and ecological-impact rules.
- **Gate I — Dynamic ecology:** seasonal changes, migration, disturbance and recovery are defined at individual/cohort/regional scales.
- **Gate J — Procedural portability:** a second planet can inherit the schema without copying Veyra's exact species placements or geography.
- **Gate K — Implementation and testing:** only mark complete after implementation exists and evidence from the relevant tests is recorded.

Current status for every gate: **NOT STARTED — design framework has been committed; detailed maps, individual species pages, populated biome instances, simulation and tests are not yet complete.**

## 14. Work breakdown: complete Veyra in order

1. **Planet map and region index:** define continents, watersheds, elevation/depth bands, climate zones, coastlines and travel scale.
2. **Biome instances:** turn the biome families in Section 4 into named, located regions with seasonal conditions, transitions and resources.
3. **Canonical species index:** inventory every species already mentioned across the repository; reconcile duplicates, retain original IDs, and map each to this planet or mark it as non-Veyra/cosmic/future-planet.
4. **Species dossiers:** complete one species at a time using Section 5.1, starting with the base Slime, its prey, its first predators and the starting river-basin ecosystem.
5. **Food-web audit:** verify that every species has a plausible energy source and relationships; include population and seasonal changes.
6. **Skills and trainer atlas:** enumerate innate skills and acquisition routes for each species; trainers and mentors receive individual records.
7. **Resources and crafting:** connect every material to a geological, biological or constructed source and a renewal model.
8. **Civilization and history:** establish settlements, cultures, ruins, trade routes and conflict without treating cultures as monoliths.
9. **World events and encounters:** add migration seasons, apex territories, rare variants, environmental disturbances and anomaly reserves.
10. **Generation template:** formalize the planet-independent schema, parameters, constraints, seeds and validation reports.
11. **Implementation plan:** split design contracts into code/data/runtime tasks; do not imply implementation before repository evidence exists.
12. **Verification:** execute and record validation only after relevant implementation is present.

## 15. Change control and status vocabulary

- Do not silently overwrite established Slime decisions, live-prey rules, skill schemas or PvP safeguards.
- When a new species conflicts with gravity, climate, food-web, anatomy, or resource assumptions, either correct the species design or record an explicit fictional exception with constraints.
- Use stable IDs. Display names may change without breaking cross-links.
- Record open questions instead of inventing precise balance values without evidence.
- Distinguish **designed**, **data-authored**, **implemented**, **tested**, and **verified** in all future status reports.
- Any later planet may deliberately differ from Veyra, but deviations must be represented as explicit parameters or world-history rules.

## 16. First-pass open decisions

- Final planet name, map projection, continent outlines and exact regional coordinates.
- Local calendar naming, season lengths and regional climate envelopes.
- Final roster after repository-wide species inventory and duplicate reconciliation.
- Full individual species stats, lifecycles, habitat ranges, skill lists and trainer identities.
- Exact population simulation parameters and performance budgets.
- Which sapient lineages are biological species versus cultures of one species.
- Whether each proposed anomalous biome belongs on Veyra or should be reserved for later planets.
- Runtime format and tooling for machine-readable planet/biome/species data.

**Current completion statement:** This file establishes the reference-planet contract, initial planet parameters, required biome families, and a first-pass species candidate list. It is a committed design artifact only. It does not mean that a planet map, complete species encyclopedia, biome simulation, procedural generator, playable world, or validation suite currently exists.
