# Lethal Absorption — Cooking, Equipment, Stats, and Build Synergy

**Status:** Design requirement; implementation and balance testing are outstanding.  
**Purpose:** Combine meal-based bonuses, equipment/set bonuses, stamina progression, energy systems, anatomy, and evolutionary customization into one coherent build system without introducing fixed classes.

## 1. Design rule

The character's performance comes from multiple interacting layers:

1. **Core attributes** — health, stamina, energy, recovery, strength, defense, mobility, and control.
2. **Training and level growth** — durable progression earned through play.
3. **Food and cooking** — temporary or meal-duration bonuses, recovery, preparation, and resistance.
4. **Equipment and gear sets** — protection, specialized bonuses, trade-offs, and playstyle incentives.
5. **Anatomy and body plan** — natural capabilities and limitations of the current form.
6. **Genetics, traits, mutations, and absorbed powers** — biological or supernatural modifiers.
7. **Mastery and execution** — how efficiently the player uses a move, weapon, form, or ability.
8. **Environment and condition** — heat, cold, toxins, pressure, exhaustion, injuries, and other situational effects.

No single layer should replace all the others. A powerful build is a set of meaningful synergies, not a mandatory best-in-slot checklist.

## 2. Core attributes

- **Health / Vitality:** How much damage the character can survive before being incapacitated or defeated.
- **Stamina / Endurance:** Budget for sustained physical effort, including sprinting, dodging, climbing, swimming, gliding corrections, physical combos, blocking, and other explicitly stamina-costed actions.
- **Energy / Power Reserve:** Fuel for energy attacks, supernatural techniques, transformations, and other abilities that explicitly use an energy pool.
- **Focus / Control:** Optional shared or route-specific resource for precision, concentration, complex techniques, or maintaining difficult effects. Do not force every ability to use it.
- **Strength / Force:** Influences appropriate physical attacks, grapples, lifting, and impact effects.
- **Defense / Resilience:** Reduces or mitigates appropriate damage types; must not become universal immunity.
- **Mobility / Agility:** Influences acceleration, turning, evasion, and traversal within animation, anatomy, and balance constraints.
- **Recovery:** Influences stamina/energy regeneration and recovery windows; it does not erase costs or remove all downtime.
- **Mastery / Efficiency:** Earned familiarity with a specific ability, weapon, form, or discipline; separate from character level and raw attributes.
- **Condition:** A changing state such as fed, exhausted, injured, overheated, chilled, poisoned, or well-rested. Condition is not a substitute for permanent progression.

The exact attribute list, formulas, caps, and display names remain subject to prototype testing. Do not create redundant stats that have no clear player-facing consequence.

## 3. Stamina must matter without making play tedious

Stamina creates decisions and prevents unrestricted action spam, but it should not interrupt every few seconds.

- Sprinting, repeated dodges, sustained blocking, strenuous traversal, and selected physical techniques can consume stamina.
- Different body plans use stamina differently. A serpent, flier, swimmer, heavy quadruped, many-limbed creature, and biped should not be forced into identical movement costs.
- Stamina improves through level progression, deliberate training, compatible traits, evolution, gear, food, and mastery—but these sources have different durations and trade-offs.
- Stamina regenerates according to action state, condition, injuries, terrain, body plan, and selected effects. Heavy exertion may delay regeneration.
- Strong attacks may cost more stamina, energy, or both. Cost should communicate power, range, duration, control, or utility rather than follow a universal rule.
- Exhaustion should create readable consequences such as slower recovery, reduced sprint duration, or a vulnerable recovery window—not arbitrary input lockouts.
- Enemies and NPCs obey the same understandable resource logic, adapted to their biology and AI role.
- Late-game evolution can greatly expand endurance or change how effort is paid for, but should preserve readable limits, counterplay, and meaningful build choices.
- Never let a permanent stamina investment make the player immune to every resource-management decision.

## 4. Cooking and meals

Cooking is a meaningful preparation system inspired by the appeal of meal-based RPG bonuses, but it must be original to Lethal Absorption.

### Ingredient sources

Ingredients may come from foraging, hunting, fishing, farming, gathering, trade, exploration, and compatible creature materials. Ingredients can carry qualities such as nutrition, heat, moisture, toxicity, rarity, freshness, and discovered biological properties.

Sapient species are not treated as ordinary ingredients or interchangeable loot. Their agency and rights remain protected by the game's governing design rules.

### Meal effects

A prepared meal may grant one or more clearly described effects, for example:
- increased maximum health or temporary protection;
- improved stamina capacity, regeneration, or recovery delay;
- improved energy reserve or energy regeneration;
- resistance to a named damage type or environmental condition;
- improved healing, recovery, focus, or status-effect resistance;
- improved resource yield or research insight for a limited activity;
- a temporary boost to a compatible body plan or trait.

Meals can provide a mix of direct nourishment and specialized effects. They should not all be generic percentage boosts.

### Preparation and duration

- Cooking quality can depend on recipe knowledge, ingredient quality, tools, heat control, and cooking mastery.
- Recipes are discovered through observation, experimentation, culture, exploration, and research; essential progression must not depend on one rare random drop.
- Meal effects need readable durations, stacking rules, and refresh behavior.
- Multiple dishes may combine only within explicit categories or a meal plan. Prevent unlimited stacking of identical or multiplicative buffs.
- Food buffs are generally temporary; learned recipes, cooking mastery, and discovered ingredient knowledge can persist.
- Bad preparation, spoiled ingredients, or toxic materials may create a warning, a manageable risk, or a research opportunity. Avoid opaque punishment.
- Eating is optional for basic play. Food should enhance preparation and playstyle rather than become constant busywork or a mandatory tax.
- Different species may digest, tolerate, or benefit from ingredients differently. This can create discoveries without making common content inaccessible to certain builds.

### Food and biological evolution are separate but connected

Eating to satisfy nutrition or gain a cooked-meal buff is not the same as absorbing genetic material or evolving from a creature. Raw diet, cooked dishes, biological absorption, and research each have separate rules. Some foods may reveal clues or temporarily support a compatible trait, but a meal must not silently grant a complete species, signature ability, or permanent mutation.

## 5. Equipment, armor, and set bonuses

Equipment can modify offense, defense, mobility, resource economy, resistances, and specialized effects. Sets should reward a coherent style without making all other gear inferior.

- **Individual piece stats:** Each item communicates defense, weight or movement impact, durability/condition if used, resistances, and any unique effect.
- **Set bonuses:** Equipping a defined number of compatible pieces can unlock a bonus. Partial bonuses should be visible, and full sets should be a meaningful option rather than an automatic requirement.
- **Trade-offs:** Heavy protection may reduce mobility or increase stamina costs; light equipment may improve evasion but offer less protection; energy-focused equipment may trade physical defense for energy control.
- **Slot clarity:** Define equipment slots by function and form compatibility. Avoid creating numerous nearly identical slots purely to inflate loot.
- **Anatomy compatibility:** Gear must fit or adapt to the current body plan. A quadruped, serpent, winged form, amorphous body, or many-limbed creature cannot be forced to wear a human-shaped armor set without an explicitly supported adaptation.
- **Adaptive gear:** Later technology, crafting, mutation, or evolution may produce modular, morphing, symbiotic, or body-conforming equipment. This must remain distinguishable from the character's natural anatomy and abilities.
- **Durability and repair:** If durability is implemented, it must be readable, repairable through clear means, and must not erase a rare item's identity or permanently destroy core progression without an explicit separate design decision.
- **Loadouts:** Players can save compatible equipment/trait/ability loadouts where feasible. Changing loadouts should respect combat, encounter, and multiplayer rules.
- **Acquisition:** Gear can come from crafting, exploration, quests, rivals, bosses, trade, discovery, and PvP reward pools. PvP rewards never require stealing another player's owned equipment.
- **Visual identity:** Stats and visuals should be separable where possible. Players can preserve a preferred appearance while using compatible earned stats, subject to anatomy and readability.

## 6. Armor sets and evolved anatomy

Equipment is only one path to protection. A character may use natural scales, plates, shells, chitin, energy barriers, regeneration, phasing, agility, or other compatible defenses. These must not all be treated as identical armor values.

- Physical armor should primarily address the damage types it plausibly protects against.
- Energy shields, magical barriers, elemental resistance, evasion, regeneration, and damage redirection have distinct counterplay and costs.
- Stacking multiple defenses must have diminishing returns or explicit interaction rules where necessary.
- A natural body trait and an armor item may synergize, but neither should accidentally multiply into invulnerability.
- Armor and anatomy should remain useful across different body sizes, including the stage-five height-normalization rule, without creating collision or hitbox exploits.
- A form change may disable, adapt, or reconfigure incompatible gear; communicate this before confirming a loadout change.

## 7. Build synergy and balance

The design goal is a broad space of viable builds, not one mathematically dominant combination.

- Show the player how bonuses combine and which resource each action consumes.
- Distinguish additive bonuses, multipliers, conditional triggers, flat mitigation, resistance, and damage conversion.
- Cap, diminish, or otherwise constrain runaway stacking, especially for regeneration, cooldown reduction, repeated triggers, damage reflection, evasion, and resource refunds.
- A bonus should have a stated scope: always active, while a set is equipped, after a dodge, against a certain threat, in a particular environment, or during a form.
- Strong effects need costs, cooldowns, exposure windows, environmental requirements, counters, or other meaningful limits.
- Avoid mandatory synergies. Multiple viable combinations should reach endgame through different strengths and weaknesses.
- Respecialization and gear changes must be understandable; permanent evolution choices may have consequences, but routine experimentation should not require restarting the character.
- PvP matchmaking and reward rules must account for build capability without guaranteeing wins. PvP remains non-permanent and cannot destroy owned progression.
- AI opponents can respond to repeated tactics, but must not gain unexplained hard counters to the player's entire build.

## 8. Example build combinations

These are illustrations of the system, not locked numerical balance values.

1. **Heavy predator:** High vitality, natural armor, a heavy gear set, and a stamina-costly charge. Excellent at holding ground, but slower and vulnerable to being kited or exhausted.
2. **Mobile hunter:** Lower armor, efficient dodge and sprint, stamina recovery, and light equipment. Strong at repositioning, but punished by mistimed evasion and sustained pressure.
3. **Energy specialist:** High energy reserve, controlled regeneration, and gear that improves technique stability. Powerful ranged options, but must manage energy costs and vulnerable recovery windows.
4. **Thermal survivor:** Heat-tolerant anatomy, a meal that improves environmental resistance, and gear optimized for hostile climates. Prepared for that region, but not universally resistant to every damage type.
5. **Adaptive hybrid:** A compatible absorbed trait, anatomy-specific equipment, and a meal that temporarily supports stamina recovery. Flexible but must balance multiple resource pools and avoid overextending.
6. **Mythic weapon master:** A compatible weapon/form, mastery-driven technique improvements, a set bonus for timing or counters, and a meal that improves short-term endurance. Power comes from execution and setup, not simply stacking attack numbers.

## 9. Player-facing information and feedback

The interface must make the system legible:
- current and maximum health, stamina, and any active energy/focus pools;
- regeneration state, exhaustion, and action costs where relevant;
- active meal effects, remaining duration, and stacking category;
- equipment piece stats, set progress, active bonuses, and trade-offs;
- anatomy/gear compatibility warnings before applying changes;
- source and scope of major stat changes;
- clear comparison of current versus proposed loadout;
- a readable explanation of why a technique is unavailable (insufficient resource, incompatible form, cooldown, status, or prerequisite);
- accessibility options for color, icons, text, timing, and effect intensity.

Do not flood the HUD with every hidden calculation. Put advanced breakdowns in a character/status screen and show immediate combat-relevant information in context.

## 10. First-slice boundary

The first cellular-to-animal vertical slice should demonstrate only a small, testable subset:
- one basic stamina-costed action or short exertion sequence;
- a readable stamina meter and recovery behavior;
- one simple food item or meal effect only if it can be taught without delaying the core tutorial;
- one basic equipment or natural-defense comparison only if appropriate for the animal-stage prototype;
- one status/trait explanation showing where a bonus comes from.

Do not expand the frozen first slice into the full cooking economy, dozens of armor sets, all attributes, or every species. The full design is a future system target; first-slice inclusion must be explicit and scope-controlled.

## 11. Acceptance criteria

The system is ready for implementation review when:
- every core stat has a distinct player-facing purpose;
- stamina costs, recovery, and exhaustion are readable and consistent;
- food effects have explicit duration, stacking, and species-compatibility rules;
- permanent diet/evolution changes are not confused with temporary meal effects;
- gear and set bonuses show benefits and trade-offs;
- equipment works with multiple body plans or clearly explains incompatibility;
- layered defenses and stat bonuses have anti-exploit limits;
- the interface shows active effects and source attribution;
- multiple viable builds remain possible without a single mandatory set;
- tests cover resource exhaustion, buff stacking, gear swaps, form changes, save/load persistence, and PvP protection;
- implementation and verification are evidenced separately from this design document.

## 12. Open tuning decisions

The following remain open until prototypes and playtests provide evidence:
- final stat names and exact number of core attributes;
- stamina/energy formulas, costs, regeneration, caps, and soft caps;
- meal duration, recipe complexity, freshness, and ingredient rarity;
- equipment slots, set sizes, durability, and repair economy;
- numerical stacking, diminishing returns, and resistance formulas;
- how much of cooking and gear appears in each evolution stage;
- accessibility defaults and advanced stat-detail presentation.

Do not invent final numbers in the design documentation before they are tested.
