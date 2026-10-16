# Lethal Absorption — Species Dossier: Reedstalker

> **Stable ID:** LA-PLN-PRE-001  
> **Planet:** Veyra  
> **Status:** Designed — concept dossier; not implemented or tested  
> **Primary region:** Reedwater Basin's marsh edges and vegetated channels

## 1. Identity and ecological role

**Role:** Medium wetland predator; patient shoreline stalker.  
**Originality:** Original fictional animal; anatomy and behavior are provisional.

The Reedstalker is a long-legged, low-profile predator that moves through shallow water and dense reeds. It uses stillness, concealment, and deliberate steps to approach small animals along shorelines. Unlike the Mire Needle, which specializes in a short waterline lunge, the Reedstalker is a mobile shoreline hunter that can patrol between pools and reed beds. Unlike the Glass-Eyed Pouncer, it does not depend on an explosive leap from rocky cover.

## 2. Anatomy and life stages

- **Body plan:** Four long, narrow limbs with splayed toes, flexible neck, tapered muzzle, directional ears, and a laterally compressed tail for balance in reeds. Sparse sensory bristles around the muzzle help it navigate at close range.
- **Scale:** Medium predator; exact dimensions, mass, health, and strike values await world scale and balancing.
- **Life stages:** Hidden juvenile → learning subadult → territorial or pair-bonded adult (social system unresolved) → senescent adult.
- **Reproduction:** Concealed nest above normal waterline in dense vegetation. Breeding timing responds to prey availability and flood risk; clutch/litter size remains undefined.
- **Diet:** Small shoreline animals and aquatic prey that can be captured within the Reedstalker's reach. Reed Skipper is a plausible prey candidate; Current Dart is only prey if the hunter's capture animation and mechanics support it.
- **Mortality:** Injury, prey shortage, flooding of nesting sites, contamination, larger predators, and habitat fragmentation.

## 3. Habitat and distribution

**Habitat anchors:** Reedglass Marsh, Reedwater Run's vegetated banks, Siltbend Oxbows, and sheltered Southwash Fan pools.

**Preferred conditions:** Dense reeds, shallow margins, multiple approach routes, and cover for resting or nesting.  
**Poor conditions:** Deep open water, bare dry ground, strong currents, and broad exposed flats with no stalking cover.

Floods may open new hunting routes but also wash away nests and make movement noisy. Dry periods concentrate prey around persistent pools, increasing hunting opportunities while intensifying competition. Habitat carrying capacity must constrain predator abundance.

## 4. Senses and movement

- **Senses:** Close-range vision, hearing, smell, and pressure/vibration through the feet when in contact with substrate.
- **Movement:** Slow stalk, careful wading, short rush, brief strike, and retreat into reed cover.
- **Limits:** Poor concealment in open ground, high energy cost when wading through deep mud, and limited maneuverability in dense roots.
- **Player clues:** Reed stems part without wind, a low ripple against current, a narrow track along the waterline, a brief silhouette behind stems, or small prey abruptly scattering.
- **Sensory fairness:** Vibration and chemical cues may suggest a moving large animal nearby, but the Slime does not receive a perfect outline through opaque reeds or unlimited water.

## 5. Behavior and AI contract

Minimum states: patrol shoreline → inspect prey traces → select concealed approach → stalk → strike when range and footing are suitable → secure prey or recover → feed/rest → relocate after disturbance.

- Detection confidence depends on line of sight, noise, scent, cover, and wind/water conditions.
- The Reedstalker should abort a stalk when the target is too large, the route is blocked, or its own exposure becomes excessive.
- A missed strike requires recovery and reassessment; no endless instant attacks.
- It may compete with the Mire Needle near marsh edges, but it should not automatically coordinate attacks with it.
- It does not know the player's position through walls, solid ground, or disconnected water.

## 6. Ecology and proposed food-web links

- **Potential prey:** Reed Skipper and other small shoreline animals; Current Dart only if capture capability is explicitly implemented.
- **Competition:** May overlap with Mire Needle at shallow margins, but differs in movement, detection, and hunting strategy.
- **Indirect links:** Predator abundance responds to prey availability, nesting success, and connected reed habitat.
- **Scavenger support:** Leftover prey may feed detritivores and scavengers, but this should not produce unlimited resources.
- **Excluded assumption:** The Reedstalker cannot excavate Silt Burrower tunnels or catch deep-burrowing animals without a specified behavior and cost.

Food-web edges remain hypotheses pending ecology review and simulation.

## 7. Resources and nonlethal study

- **Study:** Track shoreline patrol routes, observe abort decisions, map concealed approaches, and compare behavior across water levels.
- **Nonlethal route:** Observe from cover, use prey movement as indirect evidence, and identify nesting zones without disturbing them.
- **Possible resource:** A small sample only if collection mechanics and ecological costs are established; no guaranteed drop.
- **Harvest impact:** Removing adults or destroying nests can reduce local predator density and alter prey pressure.
- **Renewal:** Population recovery depends on prey, nesting cover, reproduction, and survival; no instant respawn.

## 8. Absorption and compatibility

The Reedstalker is a meaningful threat to an early Slime. Capture depends on relative size, stage, terrain, stamina, target condition, and relevant mastery. Dense reeds may help the player hide but also obscure the predator's approach; shallow water can transmit vibration while turbulent flow masks it.

Potential learning branches:
- **Shoreline Trace Reading:** Interpret track and reed disturbance patterns.
- **Concealed Approach Analysis:** Learn how cover, noise, and water depth affect detection.
- **Wading Balance Insight:** A possible later movement adaptation after compatibility and cost review.

Absorption does not automatically grant long legs, predator strength, perfect camouflage, or aquatic breathing. Traits must be evaluated and mastered individually.

## 9. Skills and training

The Reedstalker is not a sapient trainer. Observation may contribute to:
- **Shoreline Tracking:** Read the age and direction of tracks using multiple clues.
- **Stalk Detection:** Recognize changes in reed motion, sound, and prey behavior.
- **Ambush Route Planning:** Identify routes that preserve cover while limiting escape options.

These are learning candidates, not finalized unlocks. Formal skill records must define prerequisites, training conditions, costs, mastery levels, and counterplay.

## 10. Variants and discovery

Provisional regional forms:
- **Oxbow Reedstalker:** More patient around still pools and submerged root cover.
- **Runbank Reedstalker:** More likely to patrol firmer, elevated banks and avoid fast channels.

They remain regional forms of one species. Discovery can start with tracks, reed movement, prey alarm, or waterline ripples; visual detection should not be mandatory.

## 11. Simulation and validation checklist

- [x] Identity, anatomy, life stages, habitat, senses, movement, behavior, ecology hypotheses, and absorption limits documented.
- [ ] Implement cover-aware stalking, prey selection, energy costs, strike recovery, and retreat.
- [ ] Validate pathing through reeds, mud, shallow water, and flood states.
- [ ] Confirm Current Dart capture capability before establishing that food-web edge.
- [ ] Test fair warning cues for vision-limited Slime players.
- [ ] Connect finalized learning hooks to skill records.

**Evidence status:** Design authored; not implemented or tested.
