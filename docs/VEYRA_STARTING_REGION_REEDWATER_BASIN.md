# Lethal Absorption — Veyra Starting Region: The Reedwater Basin

> **Status:** Regional design specification; proposed, not implemented or tested.
> **Planet:** Veyra, defined in `docs/BASE_PLANET_MASTER_ATLAS.md`.
> **Region ID:** VEY-REG-START-001.
> **Working region name:** Reedwater Basin.
> **Purpose:** Build the first connected, ecology-first playable region where the Slime's initial senses and movement can be learned naturally.

## 1. Regional design goals

The starting region must teach the game through environmental evidence rather than a large tutorial wall. It needs safe observation opportunities, low-risk food sources, readable threats, multiple routes for different body plans, and enough ecological logic that player actions have visible but proportionate consequences.

The region is a compact vertical slice of Veyra, not the entire planet. It links a temperate river, wet meadow, woodland edge, shallow marsh, rocky upland and a small cave system. Each neighboring habitat must connect physically and ecologically.

## 2. Regional layout

The river flows from the northwestern uplands toward a broad southeastern floodplain. A tributary enters from the wooded east. The river forms oxbow pools, gravel bars, reed beds and a shallow delta fan before leaving the region. The forest occupies the higher eastern ground; the western grassland rises gradually into rocky bluffs. A small karst opening sits above the floodplain, with a shallow entrance chamber and one narrow, optional passage.

### Named subregions

| Region ID | Working name | Physical features | Main biome links |
|---|---|---|---|
| VEY-START-01 | First Drip Hollow | Moist rock pocket, biofilm, shallow trickle, narrow exits | Wet rock, cave mouth |
| VEY-START-02 | Reedwater Run | Shallow river margin, gravel, pools and submerged cover | Upland/lowland river |
| VEY-START-03 | Reedglass Marsh | Reeds, soft mud, standing water and hummocks | Marsh, floodplain |
| VEY-START-04 | Mossbank Edge | Rooted banks, leaf litter, shrubs and fallen wood | Temperate forest edge |
| VEY-START-05 | Longgrass Shelf | Open grass, seed heads, burrows and low rises | Temperate grassland |
| VEY-START-06 | Flintback Rise | Exposed rock, cracks, short ledges and wind | Rocky upland, canyon margin |
| VEY-START-07 | Quietroot Grotto | Shallow karst chamber, drip water and echoing stone | Karst cave |
| VEY-START-08 | Siltbend Oxbows | Cut-off river loops, fine sediment and seasonal pools | Floodplain, wetland |
| VEY-START-09 | Elderbank Stand | Older trees, deadwood and deep leaf litter | Ancient woodland edge |
| VEY-START-10 | Southwash Fan | Gravel/silt deposits, braided channels and seasonal flooding | Delta / river floodplain |

## 3. Environmental envelope

These are initial gameplay tuning ranges, not validated planetary climate data.

- **Climate:** temperate, humid near water; warmer and drier on exposed rises.
- **Seasonal state:** mild baseline season for the opening route; other seasons will change water depth, mud, food availability and migration.
- **Day/night:** 26-hour local day. Exact sunrise/sunset and calendar are OPEN.
- **Weather:** clear, overcast, light rain and fog are baseline states. Flood, severe storm, drought and wildfire are later regional events, not forced into the first minutes.
- **Water:** clean-looking water is not automatically safe. Water chemistry and biological contamination are data-driven; the opening area should communicate any relevant risk through evidence.
- **Terrain:** soft mud impedes some movement; wet rock improves moisture access but can reduce adhesion; gravel creates vibration cues; dense reeds block direct sight and create scent/chemical traces.
- **Acoustics:** rock and enclosed spaces carry echoes; open grassland exposes vibration paths differently from loose mud or flowing water.

## 4. Opening progression: Stage 0 to early Stage 1

### Stage 0 — cellular survival
The player begins as a small living cell. The first loop introduces nutrient gradients, membrane integrity, local currents, competing microbes and simple environmental danger. The player must infer nearby conditions from chemical and contact cues rather than conventional vision.

### Transition to Stage 1 — primitive Slime
After qualifying survival and development conditions, the player can form the primitive Slime body plan. The transition is a designed progression gate, not an automatic reward for time alone. Exact thresholds remain OPEN and must later be balanced.

### Stage 1 movement and perception
- Flow-crawl across compatible surfaces.
- Flatten and squeeze through suitable gaps.
- Make short compression hops over small obstacles.
- Climb limited surfaces only where adhesion, moisture, texture, slope and mass permit.
- Manually switch among available sensory interpretations.
- Use chemical sampling, contact/pressure and ground/fluid vibration as primary early information.
- Do not grant conventional image-forming vision or through-wall identity detection by default.

## 5. Initial ecology and teaching encounters

All species below are candidates from `docs/VEYRA_CANONICAL_SPECIES_INDEX.md`. Their roles are encounter intentions until individual dossiers confirm exact behavior.

| Species ID | Role in the starting region | First encounter purpose | Counterplay / clue |
|---|---|---|---|
| LA-PLN-MIC-001 Glassfilm Microbe | Biofilm / nutrient source candidate | Teach chemical gradients and microscopic competition | Follow gradients; avoid treating every patch as unlimited food |
| LA-PLN-INV-001 Reed Skipper | Small wetland prey | Teach movement traces and short pursuit | Track disturbed reeds and water ripples; can escape into cover |
| LA-PLN-INV-004 Silt Burrower | Sediment feeder / prey | Teach vibration cues through mud and bank substrate | Detect digging pulses; soft sediment blurs distance/direction |
| LA-PLN-AMP-001 Glass-Eyed Pouncer | Small ambush predator | Teach threat evidence and hiding | Disturbed cover, scent concentration and movement pauses precede attack |
| LA-PLN-AMP-002 Mire Needle | Wetland ambush predator | Teach water-edge danger and alternate routes | Ripple/pressure cues; avoid crossing its concealed strike zone |
| LA-PLN-HER-001 Moss-Horn Browser | Larger non-hostile herbivore | Teach scale, territory and non-combat observation | Footfall vibration and feeding traces; keep distance when alarmed |
| LA-PLN-OMN-002 Root-Crown Forager | Soil-engineering omnivore | Teach burrow networks and habitat modification | Fresh soil displacement and root disturbance reveal activity |
| LA-PLN-AQU-001 Current Dart | Schooling aquatic prey | Introduce current-dependent movement and aquatic life | Group movement and water displacement; current and depth constrain approach |
| LA-PLN-PRE-001 Reedstalker | Regional predator candidate | Later opening-region threat, not an unavoidable first encounter | Track, avoid, use cover, or escape; must have readable commitment and recovery |
| LA-PLN-SYM-001 Brushback Cleaner | Mutualist candidate | Demonstrate that not every creature is a target | Observe cleaning behavior; relationship and benefit require a later dossier |

Do not force every listed species into the player's immediate path. Encounters should depend on time, local conditions, population state and player disturbance.

## 6. Food-web hypotheses to validate

The following edges are **hypotheses**, not established facts until the species dossiers explicitly confirm them:

- Glassfilm Microbe provides a potential nutrient source for qualifying microscopic consumers, including the early Slime under compatible conditions.
- Reed Skipper may consume wetland plant matter or microbial films; a definitive diet is OPEN.
- Silt Burrower may process sediment detritus and serve as prey for wetland predators.
- Glass-Eyed Pouncer and Mire Needle may prey on smaller organisms in different cover and moisture conditions.
- Moss-Horn Browser may consume foliage and disperse seeds/spores; exact diet and plant species are OPEN.
- Root-Crown Forager may alter soil and root habitat while consuming mixed organic matter.
- Current Dart is a prey candidate for Siltjaw and other aquatic predators; Siltjaw's dossier must verify its diet before that edge is used.
- Reedstalker may prey on Reed Skipper or other appropriately sized fauna; body-size compatibility and hunt behavior are OPEN.
- Brushback Cleaner may remove parasites from compatible hosts; the parasite/host species and benefit model are OPEN.

No population simulation should use these hypotheses as hard data before the relevant species entries are reconciled.

## 7. Resource and study sites

| Site ID | Resource/study focus | Intended constraint |
|---|---|---|
| VEY-RES-001 | Moist biofilm patch | Regrowth depends on moisture, substrate and local consumption |
| VEY-RES-002 | River-edge organic detritus | Renewed by upstream transport and seasonal floods |
| VEY-RES-003 | Reed fibers | Harvesting can damage shelter and nesting cover if excessive |
| VEY-RES-004 | Fallen wood / leaf litter | Decomposition is slow; removal changes small-animal shelter |
| VEY-RES-005 | Mineral seep at Flintback Rise | Finite/slow-renewing until geology defines the deposit |
| VEY-RES-006 | Cave mineral film | Study first; do not label it an evolution material without evidence |
| VEY-RES-007 | Freshwater sample point | Water quality is conditional, not a universal healing or stamina refill |
| VEY-RES-008 | Burrow and track observation sites | Nonlethal research path; rewards information rather than guaranteed trait theft |

## 8. Navigation and accessibility

- Provide at least two routes between key subregions where practical: a direct route with exposure or hazard, and a slower sheltered route.
- Narrow cracks are Slime-compatible only when the body is sufficiently small and flexible; they are not generic shortcuts for every form.
- Mud, current, steep wet rock and exposed grass create different movement and sensing trade-offs.
- The game must communicate lethal hazards with reliable cues and counterplay; early difficulty should not depend on hidden instant-death traps.
- Sensory mode changes are manual as approved for the Slime. Mode switching must be clear, accessible, and must not require color-only distinctions.
- Low-vision/nonvisual sensory feedback must use distinguishable shape, motion, text, sound or haptic patterns where supported by the platform.

## 9. Regional dynamic states

| State | Trigger examples | Consequences | Recovery / player-readable evidence |
|---|---|---|---|
| Normal flow | Baseline conditions | Standard river margin and shallow pools | Current direction, waterline and ordinary species activity |
| Rain-swollen river | Sustained rainfall upstream | Faster current, submerged paths, displaced prey | Rising waterline, debris, louder flow |
| Seasonal flood | Regional rainfall threshold | New temporary channels, resource deposition, burrow loss | Gradual rise where possible; recession leaves silt and altered routes |
| Dry spell | Low rainfall over time | Shrinking pools, changed migration, higher competition | Exposed mud, plant stress, reduced water depth |
| Fog bank | Humidity and cooling conditions | Reduced visual range; chemical and vibration cues gain relative utility | Visible fog edge and moisture cues |
| Predator disturbance | Hunt, injury, player action or prey migration | Temporary changes in local activity | Tracks, alarm calls, altered movement and later return |
| Local overharvest | Repeated removal of a slow-renewing resource | Lower yield and altered shelter/food | Visible depletion and measured recovery over time |

State triggers and thresholds require future tuning. The design should preserve causal explanations rather than random arbitrary flips.

## 10. Regional exit conditions and expansion hooks

The region is ready to expand only after:
- The Slime base-form rules are reconciled with its blueprint.
- Every species appearing in the opening encounter set has a completed minimum dossier.
- Every active food-web relationship is confirmed or explicitly marked hypothetical.
- Every resource has a source, yield rule, renewal behavior and ecological impact.
- All subregions have biome IDs, transition links, navigation constraints and hazards.
- The opening can be completed without requiring a rare spawn or forced cruelty.
- At least one safe observation/research route exists alongside combat/absorption routes.
- The regional layout can be represented as data without depending on prose-only rules.

Expansion connections: upstream uplands and conifer forest; downstream floodplain and estuary; eastward temperate forest and ancient woodland; westward grassland and dry canyon; downward into the karst/cave network.

## 11. Status

**Designed:** regional concept, named subregions, initial environmental envelope, opening progression intent, candidate encounter roles, resource/study sites and dynamic-state concepts.

**Not yet complete:** map geometry, exact coordinates/distances, finalized species dossiers, validated food web, population numbers, exact skill and trainer entries, runtime data, implementation, simulation, balance and tests.

The Reedwater Basin is a design slice to build next—not a claim of a playable region.
