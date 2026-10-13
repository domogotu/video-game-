# Lethal Absorption — Perception, Investigation, and Adaptive Hunter AI

**Status:** Design specification; runtime behavior, tuning, and automated verification are outstanding.  
**Design target:** Create tense, reactive adversaries inspired by the broad experience of being hunted and outsmarted in survival horror, while using original AI behavior and world systems rather than copying another game's implementation.

## 1. Core promise

Enemies should react to evidence the player actually creates. They can hear, see, smell, sense, infer, remember, investigate, search, adapt, retreat, coordinate, and lose the trail according to their species, anatomy, intelligence, condition, environment, and learned experience.

**No omniscient tracking:** an enemy does not know the player's exact current position merely because the AI has selected that player as a target. It acts on direct perception, a last-known location, a trace, an ally's report, or another explicitly defined source of information.

The player must be able to understand why the enemy reacted, mislead it, break contact, and learn how a given species hunts.

## 2. Perception channels

Each species receives only sensors justified by its biology, technology, mutations, and current condition.

- **Vision:** line of sight, range, lighting, movement, silhouette, contrast, obstruction, and whether the target is actually visible. Darkness may reduce detection without automatically making a visible target invisible.
- **Hearing:** sound source, intensity, distance, obstruction, ambient noise, and sound category. Running, impacts, attacks, dropped objects, doors, machinery, and environmental damage can create different cues.
- **Scent and biological traces:** only for species with appropriate senses. Wind, rain, water, terrain, time, contamination, and masking can alter the strength or direction of a trail.
- **Vibration and contact:** footsteps, movement through water or foliage, structural impacts, and nearby disturbances for species capable of detecting them.
- **Energy, heat, or supernatural signatures:** only when a creature or device has a justified sensor. These senses have ranges, interference, costs, and blind spots.
- **Environmental evidence:** disturbed vegetation, opened passages, broken objects, fresh damage, missing prey, blood or biological residue, and changed territory can suggest recent activity.
- **Social information:** allies can communicate a sighting or sound with source, time, direction, and confidence. They do not transmit perfect live coordinates unless the fiction and communication method explicitly support it.

Sensory modifiers must account for weather, terrain, walls, doors, noise, lighting, injury, fatigue, abilities, equipment, and mutations.

## 3. Detection and investigation states

Use a readable state model that may be adapted to different species:

1. **Unaware:** no actionable evidence of the player.
2. **Stimulus noticed:** a sound, movement, scent, or environmental change was detected.
3. **Suspicious:** evidence is incomplete or inconsistent; the enemy changes posture or behavior and begins checking possibilities.
4. **Investigating:** travels to a sound source, disturbed area, clue, or last-known position.
5. **Searching:** examines nearby routes, cover, hiding places, vertical spaces, escape paths, or alternative explanations.
6. **Pursuing:** has current reliable evidence or a strong, recent trail and attempts interception.
7. **Lost contact:** the player has broken reliable tracking; the enemy must search from its last evidence instead of continuing perfect pursuit.
8. **Reassessing / cooling down:** the enemy updates confidence, guards a likely route, resumes patrol, calls for help, feeds, rests, or returns to territory as appropriate.
9. **Recovering / displaced:** injuries, resource loss, fear, territory changes, or tactical defeat can alter its behavior before the next encounter.

Transitions are evidence-driven and species-specific. A mindless organism may follow simple stimuli; a cunning hunter may use decoys and routes; a sapient adversary may reason, communicate, or deliberately protect an objective.

## 4. Last-known-position search

When an enemy loses sight or another reliable signal, it should search intelligently rather than snap directly to the player.

- Record the last-known position or area, timestamp, evidence type, confidence, and direction of travel if observed.
- Estimate plausible escape routes using the enemy's actual map knowledge, mobility, and available senses.
- Search in a bounded pattern: inspect the stimulus point, nearby cover, likely exits, vertical routes, scent/vibration trails, and tactical choke points where appropriate.
- Expand, narrow, pause, or abandon the search based on new evidence, elapsed time, threat level, and the creature's goals.
- Investigate hiding places only if the creature has a reason and a plausible means to inspect them; do not make every hiding place fail automatically.
- Let the player distract, conceal, mask, misdirect, escape vertically, cross noisy terrain, or exploit the enemy's sensor limitations.
- Do not reveal hidden AI state through arbitrary UI markers unless the chosen difficulty/accessibility settings intentionally provide that information.

The enemy can make a reasonable prediction, but prediction is not knowledge. Search accuracy should reflect evidence quality and age.

## 5. Learning and bounded adaptation

Adversaries may remember patterns they plausibly witnessed or inferred, with confidence and recency.

Examples:
- A player repeatedly uses loud attacks, so a rival becomes more cautious around obvious sound cues.
- A creature escapes the same trap several times and begins inspecting similar hazards.
- A predator notices the player repeatedly uses one escape route and checks a nearby alternate route during a later encounter.
- An enemy that is repeatedly attacked from range seeks cover or changes approach timing when the environment supports it.
- A species learns that a particular food source, disturbance, or player action is associated with danger.
- A faction records a known tactic and may share a limited report with allies who could realistically receive it.

Adaptation must be bounded. Each counter has a tell, limitation, cost, and counterplay. Enemies cannot instantly know an unseen loadout, gain unexplained immunity, negate every favorite ability, or escalate forever. Repeated tactics may become less reliable, not categorically invalid.

Learning is per individual, group, species, or faction only where that level of sharing is justified. Do not make every creature globally omniscient because one rival met the player.

## 6. Encounter pacing and tension director

A separate, bounded encounter director may manage tension, quiet periods, clue placement, and the timing of possible threats in supported authored or procedural encounters.

The director may:
- choose among already valid encounter opportunities;
- vary quiet time and pressure within declared encounter bounds;
- avoid stacking several high-intensity events when the player is already under pressure;
- schedule a search, patrol, distant cue, or recovery window when world state permits;
- preserve authored beats and the player's earned safety or progress.

The director must not:
- secretly teleport an enemy into an impossible position;
- grant exact player coordinates to an enemy without a sensor or report;
- rewrite enemy perception or abilities solely to force a scare;
- spawn an unavoidable threat directly on the player;
- override safe zones, tutorial protection, encounter telegraphs, or PvP protections;
- silently alter the world to invalidate a solved encounter or required progression.

If the player notices the system, it should still feel like a coherent world rather than a hidden referee cheating to increase difficulty.

## 7. Species-specific intelligence and behavior

The AI architecture is shared, but behavior profiles differ:

- **Prey:** freeze, flee, hide, group, warn others, use burrows or water, and learn safe routes.
- **Pack hunters:** flank, signal, split pursuit, protect injured members, and coordinate only within communication range and group capability.
- **Territorial predators:** patrol, scent-mark, investigate intrusions, defend dens, stalk, disengage when injured, or return when conditions favor them.
- **Ambush hunters:** use cover, concealment, patience, and likely travel paths, but must obey their own sensory limits and cannot always know the player's route.
- **Alphas and named threats:** combine a small number of distinctive behaviors with readable tells and exploitable limitations. Rank is not a license for omniscience.
- **Sapient factions and rivals:** investigate evidence, guard goals, repair or alter territory, share credible reports, negotiate or withdraw when suitable, and respond to longer-term consequences.
- **Anomalous or cosmic entities:** may use unusual senses, but those powers need defined ranges, conditions, interference, and counterplay.

Species behavior should be influenced by hunger, injuries, fatigue, fear, pack/ally status, territory, environmental hazards, reproductive or migration cycles where appropriate, and local resource conditions.

## 8. Player counterplay and feedback

The player needs enough feedback to learn without exposing every internal calculation:
- audio and animation cues for suspicion, detection, searching, and renewed pursuit;
- consistent differences between a distant sound, confirmed sighting, scent trail, and ally alert;
- environmental evidence that can be inspected or misread according to skill and conditions;
- ways to reduce noise, conceal silhouette, mask or confuse traces, use decoys, create distractions, or exploit terrain where their build supports it;
- fair warning before an enemy uses a powerful ambush or special sensor;
- clear recovery opportunities after a successful escape;
- accessibility options for critical cues, visual indicators, sound alternatives, and adjustable intensity.

Counterplay must be available through more than one approach where feasible. Do not force a single mandatory stealth gadget or mutation.

## 9. Relationship to Rivalry, ecology, and permanent death

This specification extends the [Rivalry and Adaptive Adversary System](RIVALRY_AND_ADAPTIVE_ADVERSARY_SYSTEM.md); it does not replace it.

- Investigation memory can seed a persistent rival record when a capable individual survives a meaningful encounter.
- Ordinary creatures may retain only short-lived threat memory, while higher-intelligence rivals can preserve bounded, evidence-based histories.
- Predator and prey AI uses the same sensory and search principles to support the living ecosystem.
- Alpha status, rivalry status, species intelligence, and boss status remain distinct labels.
- Only eligible NPC-controlled threats can cause permanent character death. PvP encounters remain non-permanent regardless of rank, consent, ambush, or attribution.
- NPC-caused permanent death must still obey the project's fairness, readability, safe-start, and tutorial-protection rules.

## 10. Performance and persistence

- Use simulation tiers: full perception and tactical reasoning nearby; simplified state updates at medium distance; abstract ecological and memory updates far away.
- Use event-driven perception and bounded sensing intervals instead of evaluating every sensor for every actor every frame.
- Cap simultaneous high-cost searches, group communications, long-term memories, and active rivals.
- Persist important rival history and world consequences; use bounded summaries for routine creature memories.
- Save enough information to resume a search fairly, but do not serialize transient engine state unnecessarily.
- Memory must have confidence, recency, scope, and decay or archival rules. Avoid infinite growth and stale omniscient knowledge.
- Multiplayer authority, where added, must validate important perception-dependent outcomes server-side and prevent client manipulation of detection, targeting, or AI state.

## 11. Prototype sequence

1. One predator hears a sound, investigates its source, and searches the last-known area.
2. The player breaks line of sight and can escape by changing route or using a distraction.
3. A second encounter uses a bounded memory of a previously witnessed tactic.
4. Add one sensor variation, such as scent or vibration, with an understandable countermeasure.
5. Add a simple prey response and verify predator/prey interactions.
6. Add a tension director only after individual perception and search are fair and testable.
7. Expand to packs, factions, persistent rivals, and larger ecological simulations after the local loop works.

Do not put the full AI ecosystem into the first cellular-to-animal vertical slice. The initial slice may include only one readable threat and a small, bounded investigation behavior.

## 12. Acceptance criteria and required tests

The prototype must demonstrate:
- no target tracking without a valid perception or information source;
- sound investigation toward a plausible source rather than teleporting to the player;
- last-known-position searches with uncertainty and bounded duration;
- the player can break contact and successfully escape;
- sensory changes from obstruction, distance, noise, and environmental conditions;
- decoys and distractions affect only sensors that can plausibly detect them;
- adaptive counters are telegraphed, bounded, and have counterplay;
- memory scope prevents one enemy's knowledge becoming global knowledge without a valid communication path;
- the encounter director cannot bypass safe zones, tutorial protection, or PvP protections;
- save/load does not grant enemies impossible knowledge or erase required persistent rivalry state;
- performance remains bounded under multiple nearby actors and many off-screen creatures;
- all outcomes are repeatable enough to test, while behavior remains varied within explicit rules.

**Implementation state:** Design only. Runtime AI, performance measurements, balancing, and automated tests remain outstanding.
