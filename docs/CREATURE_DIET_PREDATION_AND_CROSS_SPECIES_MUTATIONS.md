# Creature Diet, Predation, and Cross-Species Mutation System

**Project:** Lethal Absorption  
**Status:** Design specification — proposed, not implemented or tested  
**Purpose:** Make NPC diets and wild predation a core part of the living ecosystem. What creatures eat can change their growth, behavior, traits, and mutations; rare cross-species interactions can create abilities that neither species normally develops alone.

## 1. Core rule

Creatures are not static entries placed in the world. They eat, hunt, scavenge, compete, adapt, reproduce where appropriate, and respond to the environment. Diet is a meaningful input to growth and mutation for both NPC creatures and the player.

A creature's resulting traits depend on a combination of:
- Species biology and inherited baseline traits.
- What it eats and how often.
- Nutritional value, toxins, elemental/material/biological properties, and compatibility.
- Age, growth stage, health, environment, stress, and seasonal conditions.
- Rare random events and the creature's individual history.

Eating a creature does **not** automatically copy all its powers. Diet changes probabilities and opens compatible development paths; biology, exposure, and adaptation determine the outcome.

## 2. Wild predation and food webs

Wild creatures must hunt and eat one another where their ecology supports it. Food webs should include:
- Producers and nutrient sources.
- Grazers and other primary consumers.
- Predators that hunt suitable prey.
- Scavengers and decomposers that use remains.
- Omnivores with flexible diets.
- Parasites, symbionts, and mutualistic species where appropriate.
- Apex predators that affect local behavior and population distribution.

Predators choose prey based on detection, scent or other senses, hunger, size, vulnerability, opportunity, territory, risk, and learned behavior. Prey may flee, hide, group together, defend themselves, distract a predator, or use terrain. Hunting should have readable tells and counterplay rather than arbitrary instant kills.

NPCs do not need full simulation at all times. Nearby encounters use detailed behavior; distant regions use bounded population and food-web updates. The same rules must remain coherent across both levels of simulation.

## 3. Diet-to-growth and mutation pipeline

A diet event can pass through these stages:

1. **Ingestion:** the creature consumes a compatible food source or prey.
2. **Assimilation:** the body processes useful nutrients and properties, subject to digestion and resistance.
3. **Growth and condition:** biomass, energy, health, stamina, size, or recovery changes as appropriate.
4. **Exposure:** repeated or unusual intake creates exposure to biological, elemental, material, or energetic properties.
5. **Adaptation opportunity:** the system checks eligibility, accumulated exposure, current form, environment, and existing traits.
6. **Outcome:** ordinary growth, a clue, a temporary effect, a trait refinement, a new mutation candidate, an ability interaction, or no mutation.
7. **Stabilization:** significant changes may require rest, a safe environment, research, or deliberate use before they become reliable.
8. **History update:** the creature's diet and notable adaptations are recorded where the game exposes that information.

Not every meal triggers a mutation. Common diets should mainly sustain the creature; unusual combinations and sustained exposure can create meaningful opportunities.

## 4. Cross-species interaction example: fire dragon eats water dragon

A fire-aligned dragon consumes a water-aligned dragon. The result is not a guaranteed Fire + Water ability. The game checks anatomy, compatibility, the consumed creature's properties, existing traits, prior exposure, and chance.

Possible outcomes include:
- No new mutation; the dragon gains ordinary nutrition.
- A research clue about the interaction between thermal and aquatic traits.
- Improved resistance to steam, scalding, or thermal shock.
- A **Steam-Vent Mutation** that releases controlled vapor to obscure vision or alter pressure.
- A **Thermal-Mist Ability** that combines heat and water into a short-range area effect.
- A rare **Phase-Change Adaptation** that changes how the creature stores or releases heat and moisture.
- An unstable mixed trait that must be stabilized before reliable use.

The precise result depends on the species and the world rules. The outcome should be biologically or magically legible within the setting, not a random unrelated power.

## 5. Normal, refined, hybrid, and exceptional outcomes

Diet-related outcomes have distinct categories:

- **Nutrition:** supports health, energy, biomass, and growth.
- **Conditioning:** gradually improves an existing compatible trait, such as endurance or environmental tolerance.
- **Refinement:** changes the behavior of an existing mutation or ability rather than simply increasing its numerical strength.
- **Trait clue:** reveals a potential adaptation without granting it.
- **Hybrid interaction:** creates a new effect by combining properties from different species.
- **Exceptional mutation:** a rare, coherent adaptation that would not normally occur from either species' ordinary diet alone.
- **Adverse response:** sickness, toxin buildup, instability, or temporary impairment if the food is unsuitable.

Exceptional outcomes must be rare and context-sensitive. Randomness may decide between eligible outcomes but cannot bypass biology, world rules, or required progression.

## 6. Mutation inheritance and individual ecology

Where breeding or offspring exist, parental traits and environmental conditions may influence offspring within the world's rules. Do not guarantee exact copies or perfect trait inheritance. Some adaptations may be learned through diet; others may be inherited, symbiotic, temporary, or unique to an individual.

This creates emergent ecological stories: a population that feeds on mineral-rich prey may become more resilient; a predator repeatedly hunting electrically adapted prey may develop partial electrical tolerance; a fire creature living near volcanic vents may become more heat-resistant. Such shifts must be bounded and communicated through observable evidence.

## 7. Player interaction

The player can learn from NPC dietary adaptations through:
- Observing a hunt or feeding event.
- Finding tracks, remains, nests, dens, or feeding grounds.
- Studying the creature before and after its diet changes.
- Comparing related species in the journal.
- Researching unusual traits or testing compatible samples.
- Absorbing or consuming an eligible organism, subject to the existing absorption rules.
- Helping, protecting, or redirecting creatures to alter their food access where gameplay supports it.

A player can therefore discover an unusual mutation without being the first creature to develop it. NPCs become part of the world's research and evolutionary storytelling.

## 8. Food availability and ecosystem consequences

Food sources must affect creature decisions and population behavior:
- Prey scarcity can make predators migrate, compete, switch to alternate prey, or enter settlements.
- Abundant food can support population growth within defined limits.
- Removing a key predator can cause prey populations to increase and change vegetation or resources.
- Overhunting by the player can reduce local opportunities until populations recover or creatures migrate back.
- Contaminated or unusual food sources can create localized mutation patterns or hazards.
- Fire, flooding, freezing, destruction, and other world-state changes can alter food access and migration.

Consequences must be proportionate, signaled, and recoverable where appropriate. Do not simulate every organism individually at world scale.

## 9. Rules and safeguards

- No mutation is guaranteed merely because one species eats another.
- Diet cannot grant traits that violate the recipient's basic compatibility without an explicitly defined transformation route.
- Cross-species abilities must have coherent effects, costs, limits, and counterplay.
- Harmful dietary outcomes should be telegraphed through behavior, visual signs, journal clues, or known properties where practical.
- Avoid endless feeding loops that create unlimited stats, biomass, mutation rolls, or ability strength.
- Use exposure thresholds, diminishing returns, cooldowns, or unique-event limits where needed.
- Keep essential progression achievable without obtaining a rare NPC mutation.
- Track notable NPC changes consistently through save/load and region transitions.
- Avoid expensive full-world simulation; define update budgets and test performance.
- Sapient species remain agents with culture and rights, not ordinary food-table entries. Any conflict involving them must be handled by the game's separate narrative and ethical rules.

## 10. Initial vertical-slice scope

Do not build the entire food-web simulation into the first playable slice. The initial implementation should demonstrate:
- A small nutrient/food source.
- One predator and one prey species with readable hunt and escape behavior.
- One diet-driven growth or condition change.
- One possible, clearly communicated adaptation clue or mutation outcome.
- A journal record showing what was observed and what remains uncertain.
- A bounded simulation budget and a test that the loop does not run indefinitely.

The fire-dragon/water-dragon hybrid is a later-stage design example, not a requirement for the opening slice.

## 11. Verification requirements

When implemented, verify:
- NPCs select valid prey and food sources according to species rules.
- Hunting, escape, feeding, digestion, and recovery states transition correctly.
- Diet changes growth and eligible mutation outcomes as specified.
- Repeated meals do not cause uncontrolled stat or mutation escalation.
- Hybrid outcomes are possible only when the documented conditions are met.
- The player can discover clues through observation, not only consumption.
- Population and food availability respond coherently to major changes.
- Nearby and distant simulation produce compatible outcomes within defined tolerances.
- Save/load preserves significant NPC history and player discoveries.
- Automated simulation runs test common, rare, adverse, and edge-case diets.
- Performance remains within the target budget at the intended ecosystem scale.

**Current state:** Specified at design level. Not implemented, playtested, or verified in a playable build.
