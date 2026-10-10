# Core Gameplay Loop and Player Feedback

**Project:** Lethal Absorption  
**Status:** Gameplay design specification; not implemented or play-tested.  
**Purpose:** Define the repeatable moment-to-moment loop that connects survival, exploration, combat, consumption, discovery, evolution, and persistent-world consequences.

## 1. The Core Promise

Every meaningful encounter should give the player a choice: survive with what they have, learn something, take a risk to acquire something new, or change their body and strategy. Growth should come from actions and discoveries—not solely from filling an experience bar.

The loop is:

**Read the situation → Choose an approach → Act and adapt → Survive or suffer consequences → Recover evidence/resources → Interpret discovery → Evolve or prepare → Re-enter a changed world.**

This loop must work at cellular scale and remain recognizable in later stages, even as the available actions become more complex.

## 2. The Seven-Step Play Loop

### Step 1 — Read the situation
The player gathers information through sight, sound, scent, vibration, energy sensing, tracks, environmental clues, and learned knowledge. Which signals are available depends on anatomy, abilities, conditions, and stage.

The game should distinguish:
- **Observed:** directly perceived now.
- **Recorded:** previously witnessed or logged.
- **Inferred:** a plausible conclusion, not yet proven.
- **Confirmed:** tested or corroborated.
- **Mastered:** reliably understood and usable by this character.

NPCs and creatures do not receive omniscient knowledge of the player. They respond to what they could perceive, infer, or learn.

### Step 2 — Choose an approach
Players can evade, stalk, distract, negotiate, defend territory, gather resources, investigate, fight, capture, flee, or cooperate. Not every encounter needs to become combat.

Choices should account for:
- Current body plan and available movement.
- Health, stamina, energy, hunger, and relevant mutation costs.
- Target awareness, behavior, defenses, and escape routes.
- Terrain, weather, nearby hazards, witnesses, and structures.
- Potential evolutionary value versus the danger and ethical/social consequences.

### Step 3 — Act and adapt
Combat and traversal share the same body, physics, and resource rules. The player chains compatible melee, movement, defense, weapons, powers, transformations, and environmental interactions. Inputs must remain responsive, and clear telegraphs should help players understand high-impact threats.

During action, the player may learn timing, resistance, attack patterns, material properties, or a new interaction. Discovery must be earned through a legible cause-and-effect relationship, not granted randomly without feedback.

### Step 4 — Resolve the encounter
Resolution includes more than victory. Possible outcomes include escape, stalemate, negotiated withdrawal, capture, injury, territorial displacement, defeat, or permanent character death.

The world should preserve relevant outcomes: damaged structures, displaced creatures, tracks, alarms, witnesses, consumed resources, broken paths, and changes in faction or predator behavior. Persistent changes should have readable boundaries and a recovery policy.

### Step 5 — Collect and interpret
The player may gather biomass, nutrients, specimens, materials, genetic information, traces, records, or social knowledge. The available result depends on what happened, the player's tools and anatomy, the target, the environment, and whether the sample or evidence survived.

Consumption is not a universal button that grants every trait. A new trait or power may require compatible biology, sufficient analysis, repeated exposure, a special condition, a learned technique, or a risky evolution trial. Sapient beings retain agency, culture, rights, and consequences; they are not interchangeable loot containers.

### Step 6 — Make a meaningful build decision
At a safe or suitable opportunity, the player can review discoveries and choose whether to:
- Develop an existing ability or mastery branch.
- Add or refine a trait, organ, mutation, or movement option.
- Stabilize a new body plan or save a compatible form.
- Research a hypothesis before committing resources.
- Synthesize compatible powers into a new technique.
- Preserve flexibility instead of specializing.
- Delay evolution because the current form better suits the next challenge.

The interface must explain prerequisites, expected benefits, costs, incompatibilities, trade-offs, and whether a result is certain or experimental. Avoid irreversible choices without explicit warning and a clear reason.

### Step 7 — Return to a changed world
The next expedition should reflect the player's choices and the world’s response. A cleared nest may be reclaimed; a burned route may remain blocked; prey may change its movement; a community may strengthen defenses; an ally may share information; a repaired area may reopen. The player should be able to observe or investigate important changes.

The loop repeats with expanded capabilities, more complex decisions, and larger consequences.

## 3. How the Loop Changes by Evolution Stage

| Stage | Primary play verbs | Main pressure | Typical reward |
|---|---|---|---|
| Cellular survival | Sense, drift, absorb, evade, divide or adapt where permitted | Nutrient scarcity, hazards, predators | Survival adaptations and basic biological understanding |
| Primitive organism | Crawl, swim, cling, hide, feed, escape | Exposure, inefficient movement, competing organisms | Functional anatomy and reliable survival traits |
| Apex organism | Hunt, track, ambush, defend, traverse | Territory, rival predators, resource competition | Specialized traits, combat options, ecological influence |
| Sapient evolution | Investigate, craft, communicate, plan, cooperate or compete | Factions, tools, social consequences, complex objectives | Knowledge, techniques, allies, crafted solutions |
| Superhuman evolution | Chain powers, transform, counter, rescue, pursue | Enemy combinations, timing, resource control | Ability branches, signature techniques, fusion opportunities |
| Planetary apex | Alter habitats, defeat regional threats, protect or dominate territories | Large-scale ecology and faction response | Planetary progression and access to space-readiness requirements |
| Cosmic adaptation and beyond | Survive extreme environments, traverse, manipulate advanced forces | Vast scale, rare rules, high-cost powers | Cosmic systems and increasingly consequential synthesis |

These are play-pattern guidelines, not rigid classes. Players may retain low-stage abilities and use them creatively later. Early-stage actions must not become meaningless simply because the player has reached a higher level.

## 4. Rewards and Feedback

Every significant action should communicate four things:
1. **What happened?** Clear animation, sound, interface, and world response.
2. **Why did it happen?** A concise explanation based on the relevant rule.
3. **What changed?** Resources, evidence, knowledge confidence, relationships, anatomy, mastery, or world state.
4. **What can I try next?** One or more optional leads—not a mandatory arrow for every discovery.

Use multiple reward types so the loop does not reduce to loot:
- Immediate: survival, position, resource, successful counter, opened route.
- Learning: confirmed weakness, new sensory clue, recipe hypothesis, behavior insight.
- Build: ability variant, mutation, organ, form, synergy, saved technique.
- World: safer passage, changed territory, broken obstacle, rescued group, faction response.
- Legacy: recorded discovery, authored knowledge, new-character research after death.

Rewards should be proportionate to risk and effort. Repeating a trivial action must not generate unlimited biomass, mastery, destruction materials, or progression.

## 5. Failure, Recovery, and Permanent Death

Ordinary setbacks should create new decisions rather than only punish the player with lost time. Depending on the event, consequences may include injury, depleted resources, lost position, damaged equipment or anatomy, alerted enemies, lost samples, or a changed local world.

Permanent character death is final for that character. There is no resurrection. The player may retain only the explicitly designed legacy or research information allowed by the game; this information guides a new life but does not transfer the dead character's identity, body, or complete power set.

Death should be attributable to understandable rules and reliable simulation. Server failures, desynchronization, exploit abuse, or other technical faults must not be treated as legitimate in-world causes of death without a fair review and recovery policy.

## 6. Multiplayer Fairness and Shared Discovery

The Shared Discovery Network shares verified knowledge, not automatic ownership or mastery. Receiving a discovery may reveal a hypothesis, prerequisites, or a location to investigate; the receiving character still needs the required compatibility, materials, exposure, training, or trial.

Cooperative play should reward complementary roles and coordinated power weaving without requiring every player to use the same build. Competitive play should expose clear costs, telegraphs, counterplay, and consent rules for explicitly lethal encounters. Persistent world changes must have attribution, ownership/permission rules where needed, and limits against griefing or monopolizing essential routes.

## 7. Design Guardrails

- Do not make absorption the optimal answer to every problem.
- Do not award a complete ability solely because a player touched or consumed a target once.
- Do not force a single route through a fixed class system.
- Do not make high-level play only larger numbers or larger explosions.
- Do not let a maxed destruction ability permanently erase mission-critical content or trap other players without counterplay.
- Do not let knowledge sharing bypass individual prerequisites or mastery.
- Do not let NPCs know facts they could not perceive or reasonably infer.
- Do not let random generation hide essential progression requirements.
- Do not let persistent ecology create infinite resource, experience, or chain-reaction loops.
- Preserve accessibility options for sensory clues, telegraphs, camera motion, and complex inputs.

## 8. Acceptance Criteria for Future Prototypes

A prototype of this loop should be considered successful only when playtesting demonstrates that:
1. A new player can identify an immediate survival goal without needing a full-system tutorial.
2. At least two viable approaches exist for a representative encounter.
3. An action produces a readable, causally connected result.
4. A discovery clearly distinguishes observation from confirmation.
5. The player can inspect the prerequisites and trade-offs of an evolution before committing.
6. A non-combat choice can produce a meaningful reward or world-state change.
7. The next visit reflects at least one prior world consequence.
8. Failure teaches a rule or creates a recoverable decision; permanent death remains final when legitimately triggered.
9. A shared discovery does not automatically grant the receiving character the associated ability.
10. Repeated low-risk actions cannot generate unlimited resources or progression.

**Next design dependency:** Define the first playable vertical slice around one small ecosystem, a handful of species with distinct behaviors, one basic body plan, a small set of interacting abilities, one persistent environmental change, and one visible evolution decision. This should validate the core loop before expanding the catalogue or scale.
