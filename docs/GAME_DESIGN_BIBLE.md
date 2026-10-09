# Lethal Absorption — Game Design Bible

> **Working title:** Lethal Absorption  
> **Tagline:** “Consume. Evolve. Survive.”  
> **Status:** Living design specification. This repository documents concepts and design decisions; it does not imply that game systems have been implemented, tested, or production-certified.

## 1. Vision and pillars

Lethal Absorption is an original open-world multiplayer action RPG about evolving from a single cell into a creature, apex organism, sapient/superhuman being, planetary apex, cosmic entity, and potentially godlike existence. The player’s biology, anatomy, abilities, discoveries, environment, diet, combat history, and choices shape their individual evolution. There are no fixed classes.

Design pillars:
1. **Evolution through action:** consume, observe, survive, research, create, and master to discover possible evolutionary routes.
2. **Player-authored combat:** chain, modify, transform, and fuse abilities within coherent world rules.
3. **A persistent reactive ecosystem:** creatures, NPCs, habitats, wounds, evidence, damage, growth, and repairs can continue after players leave.
4. **Meaningful risk:** permanent character death, dangerous hunting, and explicit high-stakes PvP coexist with safeguards against technical unfairness.
5. **Scale with purpose:** cellular play, comparable-scale standard combat, optional Battle Mode, titan encounters, and biological spaceflight each have distinct mechanics.
6. **Discoverability without false certainty:** the Evolutionary Codex distinguishes observed, confirmed, researched, mastered, and hypothesized information.
7. **Original expression:** inspirations inform broad design goals only; all characters, species, art, story, and implementation should be original.

Inspirational reference points include Dragon Ball Z: Kakarot, Borderlands 4, Marvel’s Spider-Man 2, Hogwarts Legacy, No Man’s Sky, Suicide Squad: Kill the Justice League, Naruto Shippuden: Ultimate Ninja Storm Generations, Watch Dogs 2, The Division, That Time I Got Reincarnated as a Slime, Spore, Overlord, Black Myth: Wukong, Path of Exile, and Star Wars Outlaws. Do not copy protected characters, assets, stories, or signature expression.

## 2. Core progression model

### Character levels and stages

Normal character level cap: **1–1050**. Character level is separate from evolutionary path, ability level, and mastery. Completing the main story unlocks NG+ immediately; players do not need to reach level 1050 first.

Proposed level bands (the XP curve and thresholds remain to be balanced):
- **1–25:** Cellular Survival
- **26–100:** Primitive Creature
- **101–200:** Apex Organism
- **201–350:** Sapient Evolution
- **351–500:** Superhuman Evolution
- **501–650:** Planetary Apex
- **651–800:** Cosmic Adaptation / biological spaceflight preparation
- **801–950:** Cosmic Entity
- **951–1050:** Transcendent Being

The bands are a design proposal, not a finalized experience curve. Reaching level 1050 does not automatically master every ability or unlock every mutation.

### New Game Plus

NG+ becomes available on main-story completion. It restarts the main story/world progression while retaining the character’s earned powers and evolution. It should add meaningful enemy behaviors, boss variants, new discoveries, alternate story decisions, new mechanics, and further mastery—not merely inflate health and damage. Exact inventory/equipment carryover and post-1050 progression remain open design decisions. A proposed approach keeps the normal level cap and adds mastery/evolution milestones and NG+-exclusive content.

## 3. The Evolution Atlas

The **Evolution Atlas** is the unified, zoomable progression system—conceptually “Path of Exile × 1,000”—that begins as a cellular tree and can expand into planetary, stellar, dimensional, and universal routes. Each character’s actual history changes which branches and connections become available.

Node families include:
- Biological structures, organs, anatomy, and traits
- Mutations and environmental adaptations
- Abilities, delivery methods, modifiers, and subskills
- Fusion nodes, transformation/evolution nodes, and keystones
- Secret discoveries, cosmic powers, dimensions, time, reality manipulation, and creation

Planned Atlas tools: zoom from individual nodes to regions/galaxies/universe; search by desired capability (flight, regeneration, time manipulation, creation); evolution previews; build planner; discovery log; ability-combo view; and evolution history. Menus adapt to the player’s stage: Character, Evolution Tree, Abilities, Inventory/Equipment, Traits/Genetics, Consumption/Discovery, Knowledge/Mastery, and Evolution History.

Scale is aspirational, not a claim that millions of nodes already exist. Use authored branches plus controlled generated variations, evaluate only relevant combinations, retain progression history, and provide understandable explanations rather than overwhelming players.

## 4. Ability growth and free-flow combat

### Four progression dimensions

Each ability has a proposed level range of **1–20**. Ability level unlocks new mechanics, combo steps, move variants, advanced techniques, alternate uses, modifiers, fusion access, and signature/ultimate combinations—not just higher damage.

Progress is separated into:
1. **Ability level:** unlocks moves and mechanics.
2. **Skill branches:** specialize the ability.
3. **Mastery:** grows through effective use, timing, and application.
4. **Fusion rank:** develops combined techniques.

A level-1050 character can possess many abilities at different levels and mastery. Ability progression is inspired by the idea of individually developing moves, while combat aims for free-flow action with aerial movement, weapons, melee, ranged powers, dodges, blocks, counters, mobility, summons, gadgets, transformations, ultimates, and fusions.

### Input and combo model

A proposed configurable controller layout:
- Hold LT + X: power
- Hold LT + Y: shield, healing, counter, or summon
- Hold LT + B: mobility/utility
- Hold LT + A: signature technique
- Transformation and ultimate have separate configurable controls.

These are placeholders, not final bindings. Inputs may include tap, hold/release charge, double tap, directional inputs, and sequences. Example combo progression:
- Square ×1: quick strike
- Square ×2: double strike
- Square ×3: strike–strike–kick
- Square ×4+: unlocked extended chains that may transition into power attacks, launchers, aerial attacks, weapon techniques, or signature finishers
- Hold Square: charged heavy
- Directional input: alter attack
- Square → Triangle: transition from melee into a power
- Mobility may enable aerial follow-ups

There is no arbitrary fixed maximum combo count; the chain must remain valid under input timing, animation state, stamina/energy, ability rules, and unlocks. Earlier moves remain available. Skill, timing, position, and aim matter at max level. Prevent endless stun loops with recovery, interruption, resource, cooldown, and PvP-balancing rules.

### Ability interaction and fusion

There should be no arbitrary ban on combining powers. Combinations work when their physical properties, supernatural rules, environment, costs, and constraints permit them. Examples:
- Fire + wind → spreads fire / firestorm
- Fire + barrier → burning protective field
- Water + ordinary fire → extinguishing; sufficiently heated water may produce steam
- Lightning + water → conductive hazard/field
- Life + death → revival-like, reanimation, or soul effects only under relevant rules
- Gravity + time → temporal compression field

Abilities are built from components: core effect (damage, healing, movement, control, creation, summoning), source/element, delivery method, modifiers, and evolutionary traits. Three interaction layers: basic interactions, advanced fusion, and emergent/discovered powers. The data-driven interaction model considers properties, environment, resistance, traits, and explicit exceptions; do not hardcode every conceivable combo.

Players can save effective discoveries as custom techniques. Each build receives at least one evolution-appropriate ultimate. Transformations can be temporary or permanent, alter form, moves, controls, and playstyle, and are not just stat multipliers.

### Resonance Fusion (co-op)

When consenting players activate compatible abilities in a timing window, **Resonance Fusion** creates a distinct enhanced effect. Example: one player summons one zombie and another summons three; coordinated timing may unlock a Unified Undead Legion with formations, improved command, elite servants, or shared buffs based on ability level, upgrades, mastery, and traits. This is more than adding the summon counts.

Possible pairs include fire + wind, ice + water, lightning + metal, necromancy + shadow, healing + regeneration, gravity + teleport, and compatible transformations. Players retain their original abilities and both receive appropriate credit. Fusion ranks may develop with use. It is optional and consent-based.

## 5. Adaptive anatomy and body-as-weapon

The character’s body is a modular combat platform, not a fixed class. Anatomy changes visible silhouette, animation, reach, movement, hitboxes, and combo branches.

Examples:
- **Tendrils:** reach, grabs, multi-direction attacks, anchoring, swinging, climbing, shields, whips, spears.
- **Transforming limbs:** blades, hammers, claws, cannons, shields; alter reach, speed, impact, and combo routes.
- **Armor/spikes:** counters, charging, area damage, altered dodge/block/heavy attacks, with mobility trade-offs.
- **Energy organs/supernatural attachments:** elemental projectiles, healing, energy blades, gravity effects.
- **Additional parts:** wings, tail, extra arms, living weapons, armor plates, and specialized organs.

The same input can produce different attacks depending on anatomy. Example agile hunter: claw slash → tendril pull → spinning kick → aerial pounce. Example heavy bruiser: armored fist → ground slam → spike eruption → crushing grab.

Attachments can interact: electrified blade-tendril, armored-wing dive, fire organ powering claws, or regeneration repairing appendages. Asymmetry is allowed when compatible. Players can control attachments and save anatomy configurations/forms where allowed. The Atlas tracks what each body part enables: a tail adds balance/sweeps/grabs/counters; wings enable flight/aerial branches; multiple arms allow simultaneous attacks; living weapons add moves; mutations combine with elements and cosmic powers.

## 6. Standard combat scale, Battle Mode, and Titans

### Standard Form

The Stage V superhuman evolved warrior is the **visual and scale baseline** for ordinary player combat. Player standard forms should remain within a controlled, broadly comparable combat-height range. This does **not** require every player to be humanoid: alien anatomy, asymmetry, tendrils, wings, and unique body plans remain possible. The goal is to avoid ordinary same-level fights between a roughly 6-foot character and a 30-foot character by default.

Standard Form maintains a comparable combat scale, with reach, hitboxes, movement, and anatomy balanced within the form. Contextual exceptions must be supported by explicit encounter rules.

### Battle Mode

Battle Mode is an optional transformation that expands a character’s size and capabilities based on evolved biology. It may increase height, reach, physical power, and unlock new attacks, animations, heavy finishers, grapples, and body-weapon interactions. It is not a class:
- Tendril builds gain longer/stronger tendrils.
- Armored builds gain plates and heavier limbs.
- Aerial builds gain wings and dive attacks.
- Energy builds expand energy organs.
- Multi-limbed builds gain simultaneous-attack options.

### Titan Form and encounters

Titan Form is an advanced large-scale transformation for characters whose evolution supports it. Titan-scale fights belong in dedicated encounters/arenas; they should not be ordinary combat with an oversized health bar. They use sweeping limbs, ground impacts, grapples, area hazards, terrain changes, anatomical targets (armor plates, organs, tendrils, wings), and scale-aware movement/range.

Players can dodge/counter, grapple or climb where possible, target weaknesses, use ranged powers, transform, or coordinate fusion attacks. Rewards can include rare genetic material, large-organism adaptations, signature techniques, and Atlas discoveries. Titan fights are designed for titan-scale characters, groups, or a clearly supported strategy.

### Threat clarity and fair matching

Bosses are visibly marked dangerous before engagement and display threat tier, recommended evolution, known attack characteristics, and current-form suitability. Major attacks are telegraphed; surprises come from new mechanics, not invisible damage. Beginners should not be randomly placed in an unwarned titan fight.

Encounter-scale defaults:
- Standard vs. standard: comparable height
- Standard vs. ordinary enemy: suitable encounter tier
- Battle vs. Battle: comparable transformation scale where the encounter supports it
- Titan vs. Titan: dedicated large-scale encounter
- Player vs. boss: explicit threat classification and mechanics

Player choice of form remains central. Size grants tactical options; level alone does not make a 30-foot player automatically beat a 6-foot player.

## 7. Consumption, genetics, diet, and environments

Core loop: encounter and study an organism → consume/absorb → gain nutrients, biomass, genetic patterns, or organs → analyze compatibility → choose an evolution → test and master it.

Consumption does not automatically grant every power of the target. Requirements may include data, compatibility, repeated encounters, rare specimens, research, environmental conditions, and mastery.

Examples:
- Armored predator: hardened skin/bones, claws, jaw, plates
- Flying insect: wings, flight, sensors, venom
- Aquatic/deep organism: pressure resistance, oxygen storage, temperature tolerance, bioluminescence
- Supernatural organism: shadow adaptation, soul sensitivity, regeneration, energy channels, dimensional traits

Diet influences opportunities, not guaranteed outcomes:
- Protein-rich food: muscle/strength potential
- Minerals: bones, armor, claws
- Toxins: resistance or toxin organs
- Energy-rich sources: reserves/channels
- Plants/fungi: resilience/regeneration
- Aquatic prey: water adaptations
- Supernatural prey: rare magical/cosmic routes

Poor or incompatible diet can create understandable drawbacks or instability, not arbitrary punishment. Environments such as volcanic heat, frozen regions, toxic swamps, deep oceans, high gravity, and dimensional anomalies unlock adaptations. Some traits require both genetic data and survival in the relevant environment.

Body parts can be independently upgraded. Examples: left arm armor → claws → blade → energy blade; right arm strength → hammer → gravity-impact limb; back tendrils → reinforced → elemental → dimensional; chest nutrient processing → regeneration → energy conversion; eyes normal → thermal → biological scan → supernatural perception; legs run → jump → wall-run → extreme mobility/flight.

### Evolutionary Codex

The Codex records species and variants, observed vs. absorbed traits, materials, compatible organs/mutations/hybrids, environmental requirements, unlocked combinations, research progress, and unknown traits. It answers questions such as “What organisms might help me grow wings?” and labels confirmed information separately from hypotheses. Research should not pretend unverified traits are certain.

### Hybridization example

Armored predator + electric organism + climbing creature may yield conductive armored tendrils that grab/anchor and electrify. Mastery may enable charge spread between connected targets, interaction with water/metal, and combinations with other powers. Hybrids must be supported by the trait interaction system and balanced for PvP.

## 8. Hunting and predation

A kill is not automatically a successful hunt. How a target is found, approached, killed, handled, preserved, carried, and absorbed affects the opportunities it creates.

### Hunt styles
- **Stalk/ambush:** stealth, silent movement, scent masking, pounce
- **Apex takedown:** dominance, armor breaking, grappling
- **Pursuit/interception:** tracking, endurance, turning, trail retention
- **Secure/transport:** carrying, preserving, efficient absorption

Categories can overlap; they are not a mandatory linear quest.

### Evaluation factors

Hunt evaluation may consider target detection, witnesses, target behavior, method, condition of remains, claim control, carry capacity, absorption rate, compatibility, and environment. No one factor decides every reward.

Witness states: unobserved; suspected; witnessed but not identified; identified; reported/investigated. Being seen does not automatically remove all rewards. Hunting mastery, secrecy achievements, social consequences, and access to the catch are distinct.

### Claim and absorption phase

After a kill, the player chooses whether to absorb, defend, move, or abandon the catch. Carry/drag capacity depends on strength, size, anatomy, grips, appendages, and target mass. Tendrils may drag; multiple limbs may carry more; small specialists may absorb in sections. Weight, terrain, stamina, absorption organs, energy reserves, target size, preservation, and tissue deterioration affect transport and absorption. Predators, scavengers, rivals, defenders, and hazards can interrupt the process. Full absorption is not mandatory.

### Feat-gated traits

Exclusive traits require qualifying feats, not random drops or ordinary grind alone. Proposed examples:
- **Ghost Predator:** hunt a target that never detects the player → stealth branch
- **Apex Challenger:** defeat a superior predator under qualifying conditions → dominance/armor-breaking
- **Unbroken Pursuit:** maintain a difficult trail → tracking/interception
- **Perfect Specimen:** preserve required tissues → rare-organ/precision absorption
- **Claim Keeper:** secure a contested catch → claim defense/rapid processing
- **Living Harvester:** absorb in a dangerous environment → environmental absorption adaptation
- **Unseen Extraction:** qualifying hunt and secured catch without witnesses → secrecy-related evolution
- **Apex Assimilator:** rare target plus compatibility/research/absorption → unique branch

A feat may unlock a research opportunity rather than granting the final power immediately. The Codex records hunt conditions, witness status, remains, timing, interruptions, environment, eligible traits, mastery, and unmet requirements. It labels confirmed and speculative outcomes.

Example: a raptor hunt that damages key tissue may yield ordinary resources but not Perfect Specimen. A specialized, unwitnessed ambush may reveal a new discovery. If the catch is too heavy, the player chooses partial absorption, dragging, or securing it. Local creatures or settlements may react later if evidence reaches them.

## 9. Dominance, individual awareness, and reputation

Creatures assess strength, size, body language, visible mutations, scent/energy signature, territory, hunger, offspring, loyalty, and prior encounters. Weaker creatures may retreat, hide, submit, or test; rivals may challenge. Dominance is contextual, not a universal fear meter: territory, desperation, or protection of young can override fear.

NPCs recognize individuals only when they have encountered, witnessed, tracked, or learned about them through credible reports. Recognition may use markings, scent, energy signature, or behavior; radical form changes can weaken recognition. Same species does not imply same individual.

Knowledge stages may include unknown, seen once, survived an encounter, observed abilities, received a report, or established a repeated peaceful/hostile relationship. Reputation spreads locally through travelers, communications, scouts, wildlife signals, or faction networks where those systems exist—not instantly everywhere. Rumors may be wrong. NPCs can counter abilities only if observed or credibly learned; they cannot magically know hidden builds, private Codex data, or unobserved actions.

Possible Atlas branches: Predator Presence, Territorial Instinct, Adaptive Concealment, Scent and Signature Control, Intimidation Display, Social Intelligence, Counter-Hunter Instinct. These influence awareness but do not guarantee control or invisibility.

Public profiles may reveal chosen details such as level, NG+ history, form, transformations, ability levels/mastery, fusion combos, rating, win/loss, tournaments, gear/traits, and public build. Players control privacy. Public reputation and NPC reports must not expose private world coordinates.

## 10. Evidence, investigations, and consequences

**Being seen ≠ identified ≠ reported ≠ caught.** Separate what happened from what any observer or community knows happened.

If nobody survives and no witness exists, there is no immediate witness report. Evidence may later be found by visitors, scouts, neighboring settlements, or intelligent investigators. Evidence does not automatically identify a culprit.

Investigation methods depend on the group:
- Animals: scent, tracks, missing members, territory changes; flee, follow, or alarm the group.
- Sapient societies: interviews, wounds/material analysis, records, trackers, researchers.
- Advanced technology: cameras, sensors, forensics, electronic records, only if present and relevant evidence exists.
- Supernatural/psychic abilities: residual energy, memory, soul, or event fragments only when supported by powers; results may be limited, misleading, or concealed.

Evidence and knowledge are stored separately. Tracks fade with weather/traffic; biological traces degrade or are scavenged; structural damage persists; electronic records last until damaged/erased; memories may be unreliable; supernatural traces can fade, be hidden, or misread. An undiscovered clue is not a public accusation.

Possible outcomes: unresolved mystery, lead, suspect identified, or confirmed threat. Consequences may include patrols, evacuation, better defenses, researchers, bounty, or ecological change. Investigators can be wrong. Cases may persist as investigators travel, gather evidence, interview witnesses, request help, abandon, or reopen them. If an investigator dies, another may continue if records survive; if all knowledge is destroyed, the case may end. Player actions can evade immediate detection; discovery is neither guaranteed nor impossible.

## 11. Permanent death and PvP

When a character dies, that character starts over completely. There is no resurrection or restoration of that same living character. Healing cannot reverse permanent death.

PvP is allowed, including consensual high-stakes lethal absorption matches. The loser’s character is absorbed by the winner; the winner gains some eligible abilities/traits/materials, not the full build or mastery. High-stakes challenges require clear acceptance and explicit stakes; ordinary practice/nonlethal matches may exist. A lethal match must never be disguised as a routine visit.

Absorption rewards depend on actual defeated development, eligible genetic data/materials, compatible traits, selected abilities, research, and winner compatibility. Incompatible abilities require organs, mutations, research, or environmental conditions. Knowledge can be partial; no automatic copy of all levels/mastery.

Technical safeguards must protect against confirmed server failure, disconnect edge cases, and cheating so a bug does not unfairly delete a character. Server-authoritative combat and anti-cheat/anti-boosting are required.

Leaderboard categories: global PvP, solo duels, team PvP, ability mastery, fusion mastery, evolution discovery, and seasons. Skill matters, not just level.

## 12. Evolution Vault

The **Evolution Vault** is an NPC or machine that stores specimens and research:
- Preserved specimens and organs/limbs
- Genetic archive and mutation library
- Ability research
- Saved anatomy designs

Proposed upgrade tiers: basic preservation; genetic analysis; adaptive engineering; cosmic archive. The Vault preserves research/materials, not a living character and not resurrection.

Death-loss model proposed: active body, equipped anatomy, carried resources, and unbanked discoveries may be subject to death-loss rules; eligible deposited specimens/research may persist. New characters start at the beginning of their own biology. Archived research guides discovery but never automatically grants the previous character’s level, body, or mastery.

Open decision: whether the Vault is account-persistent or world-based/raidable/capturable. Hybrid option: limited research archive persists, while physical specimens and rare organs can be at risk.

## 13. Persistent worlds and world discovery

Worlds persist: planetary conditions, creatures and food chains, bosses/lairs/encounter state, resources/genetic traits, structures/world changes, and history. A world address/seed identifies a procedural baseline; persistent state stores changes. Boss respawn/recovery rules remain to be defined.

Players can enter world names or coordinates to locate an active player's world and load into it, subject to privacy/discovery settings and any access permissions. A world address is a destination identifier, not automatic disclosure of a private location or a guarantee of access.

New characters spawn on different worlds and may encounter each other later. Beginner spawn selection must place a new player a defined distance away from any player above level 5, checking nearby player levels and also local threats, bosses, and environmental hazards. This is a spawn-distance rule, not a guarantee that players will never meet. Consider beginner-world protections and warnings before high-risk areas.

Possible visit modes: exploration, cooperation, PvP challenge, public frontier, and beginner origin.

### Planet completion before space

No planet travel until the player:
1. Explores every continent.
2. Defeats every designated planetary boss.
3. Completes planet-specific conquest/objective requirements.
4. Has leveled/evolved enough to survive space travel.

Completion does not require exterminating every living creature unless a future planet-specific objective explicitly says so.

### No vehicles or spaceships

There are **no spaceships or vehicles**. The player’s own evolved body provides propulsion and survival. Space travel unlocks only when evolution supports breaking atmosphere and surviving vacuum; stolen or purchased ships cannot bypass the progression.

Biological spaceflight requirements may include atmospheric resistance, vacuum survival, oxygen independence, temperature regulation, propulsion, energy reserves, navigation, and re-entry adaptation. Space is a dangerous ecosystem with radiation, temperature, gravity wells, hazardous atmospheres, cosmic predators, reserves, and rare organisms.

## 14. Living Ship Form and space exploration

**Living Ship Form** is a true biological transformation of the character into an organic spaceflight body, not a piloted mechanical craft. The same individual, history, and permanent-death rules persist. The player directly controls full 3D movement and can travel from atmosphere into space and re-enter where evolved capabilities allow.

Evolution routes may include propulsion organs, navigation senses, vacuum-adapted tissue, armor/regeneration, energy reserves, maneuvering appendages, and dimensional adaptations. Proposed specialization examples:
- **Interceptor:** speed and turning
- **Armored Form:** durability and hazard resistance
- **Leviathan:** long trips and energy capacity

Hybrids are possible when biology supports them. Some powers remain usable in flight; others require another form. Inspirations include open-space exploration and traversal, but there is no cockpit or conventional ship.

Three traversal layers:
1. Planetary flight: fly through atmosphere and dive to surface.
2. Local space: planets, moons, asteroids, organisms, resources, signals.
3. Interplanetary: travel between planets and star systems after survival and navigation unlocks.

Controls should support 3D acceleration, braking, turning, rolling, diving, climbing, and maneuvering through biological propulsion. Atmosphere, gravity, radiation, and temperature affect flight. Forms may be energy-based, winged (vacuum survival separately required), armored, tendril-based, gravity-evolved, or dimensional/cosmic.

## 15. Reactive environment, persistent damage, growth, and recovery

Environment reacts to form, size, abilities, evolutionary stage, and actions without automatically scaling every enemy to the player or erasing challenge.

- **Standard Form:** consistent terrain scale; small organisms may hide in cracks; movement through tight spaces depends on anatomy.
- **Battle Mode:** vegetation bends/breaks under weight; jumps leave impact marks; fragile terrain reacts; tight passages may require reverting.
- **Titan Form:** large-scale terrain deformation, shockwaves, collapsing structures, arena hazards; some changes persist or recover over time.

Interactions follow world rules: fire burns fuel/vegetation and creates smoke/heat; water and ice change surfaces; electricity follows conductivity; gravity affects loose objects; wind redirects smoke/spores/debris/fire; regeneration applies to living systems, not ordinary rock; necromancy requires eligible remains; dimensional powers respect range, cost, and stability.

Combined abilities affect the world when justified, e.g. fire + wind spreads fire; water + electricity creates conductive zones; gravity + ground strike may collapse terrain if the structure supports it.

Regions can change with weather, season, drought, storms, migration, and anomalies. The world remembers meaningful actions: overhunting reduces prey, NPCs defend/relocate/adapt, fires alter habitats, resources deplete/regenerate, boss battles leave damage, and structures persist. Bound destruction and recovery so griefers cannot permanently erase worlds.

### Growth and damage over time

Plants spread, roots expand, and fungi colonize dead wood according to resources, temperature, energy, and space. Burned forests progress from shoots to shrubs to young trees to mature forest where conditions allow. Craters, rocks, and structures may persist and need repair. Water contamination/channels can change and recover. Creatures retain wounds/scars and heal according to biology/energy; lost limbs regrow only if capable. Populations recover or migrate; bosses and arenas change. Cosmic radiation/spatial scars may dissipate or require powers.

Damage-over-time effects may include burns, poison/infection, bleeding, corruption, and soul damage. Each has duration, visible consequences, counters, and interactions. Fire may intensify burns; water may wash away some toxins; cold may slow biological processes; regeneration may close wounds without removing poison. There is no universal cure. Character death remains permanent.

The same environmental model applies from microscopic nutrient/habitat scale to cosmic gravity wells and reality changes. Shared multiplayer history means a fire’s damage remains for other players; communities can repair. Example timeline (illustrative): forest burns day 1, clears and scavengers return day 3, new growth appears day 10, partial recovery occurs weeks later. Simulation detail tiers: active area detailed, nearby/recent simplified, distant areas summarized.

## 16. NPC agency and habitat improvement

NPCs actively repair and improve surroundings:
- Wildlife rebuilds nests/burrows, collects food, relocates young.
- Civilizations repair homes, bridges, roads, defenses; farm; improve water; and expand.
- Advanced/supernatural communities restore networks, study threats, and create living architecture.

An NPC/community detects needs, prioritizes survival/repairs, gathers materials, assigns work, repairs or improves, and evaluates results. They learn from repeated attacks, floods, fires, and corruption. Solutions depend on resources, intelligence, and knowledge; NPCs do not magically know unseen events.

Settlements may develop through survival camp → stable habitat → established settlement → advanced civilization, but not every species needs a settlement. Near NPCs simulate in detail; distant activity is summarized. Habitat work persists while players are away.

## 17. Original base species roster (100 concepts)

These are proposed original species concepts, not a claim that they are implemented. Not every species appears on every planet. Variants must change gameplay, not just recolor a model. Each future species entry should define habitat, diet/prey, behavior, combat anatomy, absorption data, mutation conditions, evolutionary role, and confirmed/speculative Codex discoveries. The dedicated [Species and Body-Plan Catalogue](SPECIES_AND_BODY_PLAN_CATALOGUE.md) expands this roster and defines how players encounter, analyze, absorb, and evolve compatible traits. The player does not select a fixed species class or automatically copy an entire organism: eligible body-plan traits can be combined under explicit compatibility rules. Bipedal, quadrupedal, serpentine, aquatic, aerial, many-limbed, amorphous, crystalline, and hybrid bodies are all valid directions; humanoid anatomy is not mandatory. The roster remains design-only until species, AI, animation, and gameplay are implemented and verified.

### Family 1 — Cellular and primitive
1. Nucleon Slime
2. Cilia Drifter
3. Sporeling
4. Microburrower
5. Pulse Jelly
6. Threadfeeder
7. Crystivore
8. Lumen Plankter
9. Hitchling
10. Splitcell

### Family 2 — Small terrestrial
11. Moss Hopper
12. Razor Beetle
13. Wallstalker
14. Dune Scrabbler
15. Bellfrog
16. Threadspider
17. Splitfox
18. Rollback
19. Crest Runner
20. Glowmollusk

### Family 3 — Predators and pack hunters
21. Blade Hound
22. Veilcat
23. Crownmaw
24. Sickle Raptor
25. Carrion Splitter
26. Coilstriker
27. Gravetusk
28. Fourblade Stalker
29. Sky Reaver
30. Chorus Hunter

### Family 4 — Giants, armored and territorial
31. Worldback
32. Trihorn Charger
33. Bastion Tortoise
34. Dune Colossus
35. Crown Grazer
36. Mire Titan
37. Cragbreaker
38. Spirespine
39. Riftclaw
40. Hearth Guardian

### Family 5 — Aerial and gliding
41. Glasswing
42. Cliff Glider
43. Silent Mantle
44. Arcfeather
45. Cloud Drifter
46. Echo Bat
47. Sky Manta
48. Needlewing
49. Ash Phoenix
50. Wind Serpent

### Family 6 — Aquatic and deep ocean
51. Abyssal Fang
52. Grasp Leviathan
53. Reef Sentinel
54. Volt Eel
55. Song Titan
56. Flood Stalker
57. Lantern Devourer
58. Trench Breaker
59. Razor Ray
60. Thermal Drake

### Family 7 — Insectoid, parasitic and colony
61. Hive Regent
62. Scythe Mantis
63. Burden Ant
64. Needle Wasp
65. Tunnel Crown
66. Veil Moth
67. Blood Anchor
68. Stone Termite
69. Mimic Cicada
70. Brood Bastion

### Family 8 — Intelligent and sapient
71. Veyari
72. Kharuun
73. Threx Collective
74. Nymari
75. Aeralith
76. Dromek
77. Umbrin
78. Sylvaran
79. Orunai
80. Prismborn

### Family 9 — Supernatural, undead and dimensional
81. Grave Stalker
82. Wraith Grazer
83. Rift Fiend
84. Soul Serpent
85. Cinder Demon
86. Rotbound Giant
87. Spectral Crown
88. Null Crawler
89. Echo Wisp
90. Aberrant Chimera

### Family 10 — Cosmic and space
91. Nebula Leviathan
92. Star Reaver
93. Orbital Bastion
94. Void Medusa
95. Astral Crystalis
96. Orbit Serpent
97. Pulsar Wing
98. Eventide Behemoth
99. Chronophage
100. Genesis Apex

Illustrative mutation-tree concept: Blade Hound variants could include Frostfang, Emberfang, Stormfang, and Riftfang, with a convergence apex such as Primal Tempest when conditions support it. This is a proposed example, not a finalized tree. World archetypes may include temperate, volcanic, frozen, oceanic, and anomalous, with procedural variation beyond those examples.

Taxonomy layers: base species, subspecies, regional variants, mutation species, hybrids, ascended/cosmic forms. Not every species needs every layer. The Codex tracks observed, studied, absorbed, researched, mastered, and hypothesized states.

## 18. Multiplayer and large-scale architecture goals

A persistent universe targeting very large populations is an aspiration, not a present capacity claim. A million-player-scale goal would require distributed regional/zoned architecture, authoritative combat, partitioned persistent world state, and coarse simulation of distant worlds/regions. Active encounters need detailed simulation; distant ecology and NPC activity can be aggregated. Server authority, privacy controls, anti-cheat, anti-boosting, and safe persistence are core requirements.

## 19. Open decisions / unresolved specifications

Do not silently treat these as settled:
- Exact XP curve, level thresholds, and balance for 1–1050
- Inventory/equipment carryover in NG+
- Post-1050 progression beyond proposed mastery/evolution milestones
- Exact Vault persistence model: account archive vs. physical world Vault risk
- Death-loss rules for carried resources, unbanked discoveries, and equipped anatomy
- Boss respawn/recovery rules and precise planet-completion criteria per world
- Spawn distance, beginner protection duration, and high-risk area warning thresholds
- Final controller bindings and per-ability resource/cooldown rules
- Exact standard-form height range, hitbox/reach compensation, and Battle/Titan transformation limits
- Final list and detailed behavior for the 100 base species and their variants
- Exact world privacy, invitation, coordinate discovery, and access controls
- Investigation evidence decay timings and case persistence rules
- Server scale, regional sharding, persistence, and recovery architecture
- Title/trademark availability for “Lethal Absorption”

## 20. Governing rules

1. Kill ≠ successful hunt.
2. Witnessed ≠ identified ≠ reported ≠ caught.
3. What happened and what a community knows happened are separate.
4. Consumption creates opportunities; it does not grant every power automatically.
5. Traits and fusions obey anatomy, properties, compatibility, environment, costs, and explicit supernatural rules.
6. Player size is controlled by form and encounter context, not level alone.
7. Bosses communicate danger; titan fights are designed for titan-scale play.
8. The environment persists, grows, heals, decays, and is repaired according to rules.
9. NPCs can only act on knowledge they could reasonably acquire.
10. Death is permanent for the character; the Vault is not resurrection.
11. PvP lethal stakes are explicit and accepted; technical failures must not unfairly delete characters.
12. No vehicle or spaceship can bypass biological spaceflight progression.
13. Codex information must distinguish confirmed knowledge from hypotheses.
14. Large-scale simulation is an architectural goal, not a current implementation claim.
15. Keep the project original and do not reproduce copyrighted characters, designs, or assets.

## 21. Ongoing repository maintenance and status discipline

This repository is the central source of truth for Lethal Absorption. For each continued design or implementation session:

1. Record each newly agreed feature and material rule change in the relevant section of this bible during the same work sequence.
2. Update the README when a change affects the project overview, major systems, or project status.
3. Keep system dependencies, constraints, examples, and unresolved decisions synchronized across documents.
4. Distinguish **proposed**, **approved/design-specified**, **in progress**, **implemented**, and **verified** states. Approval of a design is not implementation; code changes are not verified until relevant checks have actually run.
5. When implementation work occurs, document the affected code areas, configuration/dependencies, migration or compatibility concerns, and verification evidence where applicable.
6. Do not fabricate test results, completed work, files, commits, or runtime capabilities. State blockers and unverified items explicitly.
7. After updating a repository file, retrieve it from the target branch to confirm the update landed.
8. Preserve unresolved decisions in the open-decision list until they are explicitly resolved.

Documentation updates are part of the ongoing workflow; they do not imply the game systems themselves have been built.


## 22. Character identity, creation, and development

**Status: design-specified concept; not implemented or play-tested.** Character development must produce a recognizable individual, not merely a level number or a collection of interchangeable statistics. The character begins as simple life and accumulates a visible, mechanical, and historical identity through evolution.

### Character identity layers

1. **Life origin:** starting organism and its initial survival constraints. Starting origin changes the first available survival options, but does not lock the player into a permanent class.
2. **Body plan:** symmetry/asymmetry, locomotion, sensory organs, feeding structures, defense, and initial appendages. The body plan must be physically legible and supported by movement/combat rules.
3. **Evolution history:** recorded origins of acquired organs, mutations, adaptations, and major transformations. The character can retain recognizable inherited features even after major changes.
4. **Combat expression:** preferred attack ranges, mobility, defense, control, summons, support, and ability combinations emerge from anatomy and choices—not a class-selection screen.
5. **Ecological identity:** habitat adaptations, diet patterns, hunting methods, environmental tolerances, and known relationships with species/factions can shape opportunities and reactions.
6. **Personal signature:** players may name their character and saved forms/techniques; names must not grant mechanical power. The interface should surface a concise identity summary, such as key anatomy, defining traits, and known signature techniques.

### Character creation and early play

Character creation should be short enough to avoid overwhelming a new player. It establishes an initial life form and optional visual preferences where those are meaningful at the starting stage. Players should learn anatomy and survival by doing rather than selecting from a large list of late-game powers. Early choices introduce trade-offs and opportunities, not irreversible traps.

As the organism develops, the player reviews a **Character Profile** with:
- Current form and evolutionary stage
- Active anatomy and body-part functions
- Acquired traits, adaptations, resistances, and vulnerabilities
- Abilities, branches, mastery, and saved techniques
- Diet/environmental adaptations and relevant research
- Transformation forms and their costs/requirements
- A chronological Evolution History and Codex discoveries

Information should be separated into active, unlocked-but-inactive, researched, and hypothesized states. The interface must not imply a trait is equipped or usable just because it was discovered.

### Anatomy loadouts and form continuity

Players should be able to save compatible anatomy configurations as named forms/loadouts once the necessary system is unlocked. A loadout records its anatomy, ability assignments, compatible traits, and transformation configuration; it cannot bypass genetic compatibility, resource costs, form-size rules, or unlock requirements. Switching forms should communicate any unavailable parts, ability changes, energy costs, and risks before confirmation.

Major transformations should preserve continuity: body shape and combat behavior change, but the character’s history, learned mastery, and earned discoveries remain traceable. If an evolution replaces or suppresses an organ, the interface should explain which capabilities are lost, retained, or converted. Avoid silently deleting a player’s earned progress.

### Respecialization and evolutionary consequences

Evolution should allow experimentation without making every choice consequence-free. Reconfiguration may require compatible genetic data, research, biomass/energy, a suitable environment, or a safe adaptation window. Minor loadout changes can be more accessible than rebuilding an entire body plan. The precise costs and reset rules remain open for balancing.

A respec must never create an impossible body state, duplicate unique resources, bypass permanent-death rules, or grant unearned traits. The system should preview downstream effects and offer a clear confirmation before committing major irreversible changes. If a choice is reversible only through a rare process, that restriction must be communicated before selection.

### Strengths, weaknesses, and fair identity

Every major specialization should offer a meaningful advantage and a readable limitation. Examples: heavy armor improves defense but can impair acceleration; extensive tendrils improve reach/control but expose more vulnerable appendages; powerful energy organs increase burst potential but require energy and may reveal a detectable signature; extreme sensory organs improve tracking but may be overwhelmed by interference. These are examples, not universal rules: exact trade-offs depend on anatomy and system balance.

Do not use arbitrary weaknesses solely to punish unusual builds. A weakness must follow from the body, power source, environment, resource demand, or counterplay rule and should be understandable to the player and opponent. PvP fairness should focus on telegraphs, costs, counterplay, and server-authoritative resolution—not forcing every character into the same shape or move set.

### Death, legacy, and the next character

Permanent death ends the current character; it does not restore that same body. The Evolution Vault may preserve eligible deposited research/specimens according to the unresolved Vault rules. A new character begins at the beginning, while any permitted archive provides knowledge or planning context—not the dead character’s level, active body, mastery, or full build. The profile and Vault UI must make this distinction explicit.

### Character development acceptance criteria

Before calling this system implemented, verify that:
- Two characters can share an origin yet develop meaningfully different anatomy and combat options.
- The profile distinguishes active traits from discovered, inactive, or speculative traits.
- Replacing anatomy explains what abilities are gained, lost, or changed.
- Saved forms cannot bypass compatibility, costs, unlocks, or scale constraints.
- Evolution choices have previews and clear confirmation for consequential changes.
- Death and permitted Vault persistence do not duplicate or restore the same character.
- UI, save data, combat rules, Codex, and evolution history agree on the character’s current state.

These criteria are design targets, not evidence that tests have been run.


## 23. Modular anatomy workshop and body upgrades

**Status: design-specified concept; not implemented or play-tested.** This system uses the broad appeal of individually upgrading body regions and adding specialized parts found in character-focused action RPGs, but Lethal Absorption's expression is original: anatomy is grown, absorbed, engineered, evolved, or bonded to compatible supernatural/cosmic structures rather than being limited to cybernetic implants.

### Anatomy Workshop

A dedicated **Anatomy Workshop** lets the player inspect a full-body model, select a body region, compare compatible upgrades, preview visual and gameplay changes, and apply or save a configuration. It is a design target, not a built screen. Regions include:
- **Arms/hands:** claws, gripping structures, tendril launchers, shields, transforming blades/hammers, ranged organs, precision manipulators.
- **Legs/locomotion:** sprinting, jumping, pouncing, climbing, wall-running, impact landings, specialized aquatic movement, and later-stage propulsion.
- **Torso/core:** armor, reinforced skeleton, energy reserves, regeneration, metabolism, toxin filtering, oxygen processing, and elemental organs.
- **Head/senses:** vision modes, hearing, scent, thermal detection, biological scanning, threat perception, jaws, horns, and specialized communication.
- **Back/auxiliary anatomy:** wings, tails, extra limbs, tendrils, dorsal armor, auxiliary organs, and propulsion structures.
- **Skin/skeleton:** surface armor, flexible plating, camouflage, insulation, pressure resistance, and structural reinforcement.
- **Special slots:** rare supernatural, dimensional, or cosmic structures where the character's stage and body plan permit them.

These are logical regions, not a promise that every character has every slot. A character can have non-humanoid anatomy, and a slot only appears when the body plan supports it. Some upgrades occupy multiple slots or conflict with others. Extra limbs, large wings, and heavy armor must be represented in silhouette, collision, animation, traversal, and combat—not merely as inventory icons.

### Upgrade sources and installation

Parts may become available through consuming eligible organisms, researching specimens, surviving an environment, completing a feat, finding rare material, or developing an Evolution Atlas branch. Acquisition does not automatically install or master a part. A typical flow is: discover source → obtain required biological/genetic data → check compatibility → preview the result and trade-offs → pay the relevant resources or meet adaptation conditions → install/evolve → test and master.

Use in-world language such as **graft, grow, adapt, integrate, evolve, or bond** according to the part's origin. Cybernetic-style visual motifs can be used as broad genre inspiration, but do not copy Cyberpunk 2077's proprietary implants, names, visual designs, interface, or lore. Tech-like function may arise from evolved organs, mineral structures, living armor, symbiotic organisms, or supernatural mechanisms.

### Upgrade depth and progression

A part may have a small number of meaningful development tiers rather than endless flat-stat ranks. Example forelimb path: reinforced limb → clawed limb → transforming blade → energy-conductive blade. Example leg path: spring tendons → pounce adaptation → wall-running anatomy → advanced propulsion. Example sensory path: low-light vision → thermal perception → biological scan → specialized supernatural perception. Branches may diverge, converge, or require traits from multiple species and environments.

An upgrade should change at least one meaningful property where appropriate: animation, move set, reach, movement option, defensive response, perception, resource behavior, environmental resistance, or interaction with other abilities. Purely cosmetic variations may exist, but must be labeled cosmetic and must not imply mechanical benefits.

### Open-ended mix-and-match combinations

**Design rule: the number of viable anatomy combinations is open-ended, not capped by a fixed catalog of hand-authored builds.** The game should support an effectively unbounded combination space as the library of body parts, mutations, organs, traits, abilities, delivery methods, materials, environments, and evolutionary stages expands. “Unlimited” describes creative combination potential; it does not mean every combination is physically compatible, free, automatically unlocked, or guaranteed to be equally powerful.

The system must be **compositional and data-driven**, not a giant list of individually scripted recipes. Each part exposes structured properties and interfaces—such as attachment points, tissue/genetic requirements, shape and scale, movement effects, damage types, energy use, environmental interactions, tags, and supported actions. The interaction resolver evaluates the properties of the selected components and composes their effects. Authored special cases may provide memorable signature results, but they must extend the general rules rather than become the only combinations that work.

Examples of player-authored builds include a blade-arm paired with a grappling tendril, toxin delivery through a winged dive, an armored tail that conducts electricity, a regeneration organ supporting extra limbs, or a gravity effect routed through a living ranged organ. These are examples, not an exhaustive list. New valid combinations should emerge from shared properties even if designers did not name that exact build in advance.

The system should:
- Let players combine all components whose explicit compatibility and world rules permit them, without an arbitrary fixed number of named recipes.
- Resolve interactions consistently across combat, traversal, defense, senses, resource costs, environmental effects, animations, and NPC/world reactions.
- Support multi-part and chained interactions, not just pairs, while preventing recursive effects, infinite resource generation, duplicated unique components, and unbounded server work.
- Explain which properties combine, which are suppressed or conflict, what the result costs, and what counters or drawbacks apply.
- Offer a preview or safe test where practical; if a combination is unknown, show a hypothesis or uncertainty instead of falsely claiming a guaranteed result.
- Preserve player discoveries in the Codex and let players save named techniques or anatomy loadouts when the configuration is valid.
- Use reusable animation/action families, procedural composition, and graceful fallback behavior so an open-ended design space does not require a bespoke animation or script for every possible build.
- Keep compatibility, resource, progression, and PvP rules authoritative and deterministic where needed for multiplayer.

A combination can be novel without being compatible. When parts conflict, the interface must explain the reason and, where possible, suggest a valid alternative or a route to evolve the required support anatomy. It must never silently remove a selected part. Balance should emerge from readable costs, counters, timing, risk, and situational strengths—not from arbitrarily forbidding creative combinations.

### Compatibility, capacity, and trade-offs

The body has finite compatibility and maintenance capacity. Upgrades may require a compatible tissue type, genetic pattern, energy channel, anatomical space, structural support, or adaptation period. Conflicting structures should be blocked or offered as explicit alternatives; never silently discard an existing feature. Costs and limits should follow from the fiction and balance model, not arbitrary restrictions designed to suppress creative builds.

Examples of readable trade-offs:
- Heavy armor improves protection but may reduce acceleration, climbing, or stamina efficiency.
- Long tendrils improve reach and control but may expose appendages to severing, restraint, or energy drain where those counters exist.
- High-output organs increase burst damage but consume more energy and may reveal a detectable signature.
- Extra arms enable additional attack or utility routes but increase animation complexity and may require more energy/coordination.
- Specialized senses reveal certain targets or traces but can be disrupted by relevant environmental interference.

Every part must have understandable strengths, limitations, counters, and UI descriptions. No upgrade should be universally best across all situations.

### Active, stored, and saved anatomy

The interface distinguishes **installed/active**, **owned or researched but not installed**, **incompatible**, and **speculative/unconfirmed** parts. Where storage is supported, eligible organs/specimens or genetic patterns can be kept in the Evolution Vault; storage rules remain subject to the open Vault persistence and death-loss decisions. Saved forms reference known anatomy configurations, but cannot duplicate unique parts, bypass resources, or equip mutually exclusive structures.

Swapping parts must show what changes in the character's silhouette, movement, attacks, defenses, resource costs, and compatible abilities. Major changes may require a safe adaptation window, resources, or a suitable location. The player confirms significant changes after reviewing effects. Earned mastery and Evolution History remain recorded even when a part is not currently active; the system must clearly state whether a mastery effect requires the corresponding part to be equipped.

### Combat, traversal, and world integration

The same anatomy definition must drive character appearance, animation, hitboxes/reach, traversal, combat moves, damageable appendages, NPC recognition, environmental interaction, and save data. Examples:
- A grappling tendril can pull an enemy, anchor to a surface, retrieve eligible objects, or enable a traversal route if the environment supports a valid anchor.
- Wing upgrades affect flight and aerial attacks, but do not grant vacuum survival without the required space adaptations.
- A toxin organ creates and stores a defined toxin; resistance and delivery depend on target biology and world rules.
- A regeneration organ repairs eligible living tissue according to resource and damage rules, but does not reverse permanent character death.
- Conductive anatomy interacts with electricity, water, and metal according to the existing ability-interaction model.

Damage to appendages may temporarily disable their functions where the combat system supports localized injury. Recovery depends on anatomy, time, energy, treatment, and available resources. Avoid randomly removing a player's permanent build without clear rules, warning, and recovery design.

### Implementation acceptance criteria

Before calling this system implemented, verify that:
- The player can inspect supported body regions and compare compatible parts.
- Applying an upgrade updates the visual model and all dependent movement/combat behaviors.
- Unsupported body plans and incompatible combinations are rejected with a clear reason.
- Upgrade previews state meaningful benefits, drawbacks, resource costs, and lost/replaced functions.
- Active, stored, researched, and speculative parts are clearly distinguished.
- Saved forms cannot duplicate unique items or bypass compatibility, cost, progression, or death rules.
- Character saves, Codex records, Evolution History, NPC awareness, and combat state agree after an upgrade or swap.

These are acceptance targets only; no playable implementation or test pass is claimed.

## 24. Shared discoveries and player-legacy NPCs

**Status: approved design specification; not implemented or play-tested.** These are two related but distinct systems: shared discoveries make knowledge available across the player community, while player-legacy NPCs let defeated characters leave a world presence without undoing permanent death.

### Global boss-defeat ability unlocks

A qualifying boss defeat is a global progression event. When any player defeats a boss and earns or reveals an ability, that ability and its connected branch are added to the shared Evolution Atlas/skill tree for all players. This is a real shared skill-tree unlock, not merely a Codex note. Credit the first discoverer and meaningful collaborators, but do not reserve the branch for the winning player or party.

The boss's full verified dossier is added to the Evolutionary Codex and made available to all players. Record, where known: identity and variants; habitat and location; appearance and anatomy; behavior and encounter phases; attacks, ability effects and telegraphs; resistances, weaknesses and counters; environmental interactions; eligible organs, genetic material, drops and rewards; newly unlocked ability nodes; prerequisites, costs, compatibility, risks and known combinations; supporting evidence; version history; and contributor attribution. Label unknown or unverified details clearly rather than inventing them.

Global availability does not grant every player the ability automatically. All players can see and pursue the newly available branch, while each character must meet the stated personal requirements to learn, acquire, install, evolve, or master it. The shared unlock expands community progression options without erasing individual progression. **Each player must still personally locate and encounter the relevant boss or creature** to activate that source's personal discovery path. The shared tree may show the newly available branch and Codex may show community-known information, but a player cannot claim the creature's discovery, gain its personal source credit, or bypass its encounter simply because another player found or defeated it. Use clues and research to help players track it down; do not auto-mark it found, teleport players to it, or grant the creature's encounter reward globally. If the creature has moved, migrated, or become inaccessible, the player must follow the world's valid tracking and encounter rules.

The event and dossier must be stored in an authoritative shared record and remain consistent across supported worlds and future sessions. Repeated kills may grant eligible personal rewards or new verified findings, but cannot duplicate the global unlock or create a false first-discovery claim. Patches must preserve history and identify the current version. Unconfirmed kills or disputed events must not be published as verified.

Acceptance criteria: one qualifying boss defeat exposes the ability branch beyond the winning group; all eligible players can inspect the full dossier; personal prerequisites still apply; shared records persist; duplicate events and invalid reward claims cannot corrupt global progression; and evidence, unknowns, credit, and version history are retained.

### Shared Discovery Network

When a player discovers a previously unknown species, mutation, anatomy combination, ability interaction, environmental adaptation, or Evolution Atlas route, the game may record a verified discovery in a **Shared Discovery Network**. Once the discovery meets its verification requirements, it becomes discoverable by other players through the Codex, research terminals, community records, or other appropriate in-world interfaces. A discovery should not remain permanently exclusive merely because one player found it first.

Sharing knowledge is not the same as granting everyone the resulting power. Other players may learn the recipe, evidence, location clues, or research method, but they must still meet the applicable personal requirements: obtain the necessary specimens or materials, satisfy anatomy compatibility, complete required research or feats, survive required environments, pay costs, and master the result. If a discovery is account- or world-specific by design, its scope must be stated clearly rather than presented as universal.

Discovery states:
- **Unverified lead:** a player's observation or hypothesis; clearly labeled and not presented as confirmed fact.
- **Verified discovery:** enough repeatable evidence exists to publish the finding.
- **Community-known:** the verified record is available to eligible players through the Shared Discovery Network.
- **Personally researched:** a player has independently obtained the required evidence or completed the required research.
- **Personally acquired/mastered:** the player has met the separate acquisition, compatibility, installation, and mastery requirements.

The network should preserve attribution where appropriate, credit the original discoverer and meaningful collaborators, and record subsequent refinements. Players may choose a display name or anonymous credit where supported. Prevent false submissions, duplicated records, exploit recipes, fabricated evidence, and maliciously misleading reports through server-side validation, corroboration rules appropriate to the discovery, versioning, and moderation/rollback tools. Do not require every discovery to be verified by a large crowd; rare or dangerous discoveries may use a suitable evidence standard.

Shared records should explain what is known, how confidence was established, prerequisites, known risks, and whether the result is reproducible. New combinations can be published as discoveries without becoming mandatory recipes: the underlying compositional system must still allow other valid, unlisted combinations to emerge. If a later update changes a rule, mark affected records as revised or version-specific rather than silently treating obsolete instructions as current.

### Defeated-player legacy NPCs

When a player character is defeated under a rule that permanently ends that character—such as a valid accepted lethal PvP match—the game may preserve an eligible **legacy imprint** of that character as an AI-controlled NPC. This NPC can appear in an appropriate world role: a wandering predator, rival, guardian, bounty target, faction recruit, arena challenger, local legend, or other role justified by the character's history and the world. It is a memorial/continuation of the character's recorded influence, **not resurrection** and not a second playable copy of the dead character.

The legacy NPC may be built from permitted, recorded aspects of the defeated character: visible anatomy, eligible abilities, combat tendencies, evolution history, signature techniques, known affiliations, and relevant public reputation. It must not automatically inherit private account data, chat logs, hidden player information, or unearned powers. The NPC's capabilities must be reconstructed from a validated snapshot of the character at the point of defeat and obey normal compatibility, resource, progression, and AI rules. It must not gain abilities the character did not have.

Rules and safeguards:
- Only a qualifying defeat triggers a legacy NPC; ordinary knockdowns, nonlethal practice, disconnects, server errors, or invalid/cheating outcomes do not.
- Permanent death remains final for the player character. The NPC cannot restore the same character, its inventory, its level, or its mastery to a new playable life.
- Use the defeated character's recorded world history to select a plausible role and location; do not spawn the NPC instantly everywhere or grant it knowledge the original character never had.
- Clearly label it as an AI legacy when appropriate, while allowing an anonymized or lore-based presentation if the player’s privacy settings permit.
- Provide transparent player settings for whether eligible character appearance, public name, and combat style may be used in legacy NPCs. The precise default and any consent requirements remain an open product/privacy decision; no private account information may be used.
- Avoid reproducing real-player harassment or humiliation. Provide reporting and removal/appeal handling for impersonation, abusive names, or sensitive appearance concerns.
- Legacy NPC difficulty must reflect the recorded build and intended encounter tier, with readable threat warnings. It must not receive hidden stat boosts simply because it represents a former player.
- Defeating a legacy NPC may grant only explicitly eligible rewards. It must not recursively generate unlimited copies, duplicate unique items, repeatedly grant the same discovery, or recreate a permanently dead playable character.
- A legacy NPC may persist, travel, learn, be defeated, or be removed according to world rules. Whether the same legacy can reappear after a second NPC defeat, and whether a defeated player's legacy is available across worlds, remain open decisions.

### Integration and acceptance criteria

The Shared Discovery Network must integrate with the Evolutionary Codex, Evolution Atlas, research requirements, attribution, anti-exploit validation, and versioned world rules. Legacy NPCs must integrate with permanent death, combat snapshots, NPC awareness/investigation, world persistence, privacy controls, and reward validation.

Before either system is called implemented, verify that:
- A verified discovery appears to other eligible players while personal prerequisites remain enforced.
- Unverified hypotheses are not misrepresented as confirmed, and attribution/version changes are retained.
- A defeated character creates a legacy NPC only after a qualifying permanent-death event.
- The NPC uses a validated snapshot of eligible character features and cannot restore or duplicate the original playable character.
- Privacy settings, identity presentation, rewards, spawn rules, and removal/appeal handling are enforced.
- Repeated defeats or exploits cannot create infinite NPCs, duplicate unique rewards, or repeatedly grant the same unlock.
- Codex, Atlas, player saves, NPC state, and shared records remain consistent.

These are design acceptance targets only; no playable implementation or tests are claimed.

## 25. Movement, camera, and world interaction

**Approved direction:** hybrid responsive action movement with anatomy and terrain effects; hybrid contextual and direct physical interactions; adaptive third-person camera. This is a design specification, not an implementation claim.

### Movement principles
Movement should feel responsive like an action RPG while preserving readable momentum, body weight, traction, collision, and terrain consequences. Acceleration, braking, turning radius, jump arc, landing recovery, grip, and stamina/energy use depend on anatomy, mass distribution, movement specialization, condition, and surface. Avoid making every build feel identical or making complex anatomy sluggish by default.

Support applicable locomotion modes: walk/run/sprint, crouch/crawl, jump, dodge/evade, slide, climb, wall-cling or wall-run, swim/dive, glide/flight, burrow, tendril grapple/swing, and later biological spaceflight. These are capability-based, not universal moves. Each mode requires appropriate anatomy/ability and environmental conditions. Bodies can transition fluidly between compatible modes without unnecessary mode menus; incompatible transitions give clear feedback.

Movement is compositional: wings plus tendril anchors can support dive-grapple-release-flight; claws plus extra limbs can support climbing while carrying eligible objects; a heavy body may break fragile terrain but turns more slowly; aquatic anatomy can swim efficiently while being less agile on dry land. These outcomes use data-driven properties and interaction rules, not bespoke scripts for every combination. Preserve accessibility and input consistency across body plans.

### Adaptive camera
Use third-person as the baseline with camera framing that adapts to the active body, movement mode, and encounter. Pull back or shift framing for large forms, wide wings, long tails, aerial flight, fast traversal, and Titan-scale encounters; move closer for precision inspection, tight spaces, and detailed interactions. Keep the target and movement direction readable, reduce obstruction and clipping, and avoid sudden camera motion that causes discomfort. Provide player options for sensitivity, camera distance, shake, motion effects, target framing, and manual override. Camera changes must not secretly change hitboxes, grant information through walls, or alter gameplay collision.

### Hybrid contextual and physical interaction
Contextual interaction offers clear available actions when aiming at or approaching a supported target. Direct physical interaction lets the player deliberately reach, grab, push, pull, carry, throw, climb, harvest, open, or manipulate an object when anatomy, reach, strength, target state, and environment permit it. Both use the same authoritative action rules and object state; neither is a separate exploit path. The interface should show only plausible actions, explain why an action is unavailable when useful, and never promise actions that the body cannot perform.

Objects and organisms may support distinct affordances: observe/scan, communicate, feed, track, harvest, consume, carry, rescue, capture, or attack, as appropriate. Context and player intent should determine the prompt; direct controls should allow skilled play without requiring a radial menu for every small action. Holding an object can occupy limbs or appendages and affect movement, combat, climbing, and carrying capacity. Multiple limbs can enable concurrent actions only when animation, physics, and game rules support them.

### Persistent world response
Movement and interactions update the same persistent world state used by other players: displaced objects, broken vegetation, damaged structures, tracks, harvested resources, opened paths, creature injuries, alarms, and NPC reactions. Materials respond according to defined properties; do not simulate arbitrary destruction for every asset. Changes persist or recover according to world rules and bounded simulation budgets. NPC knowledge must come from observation, evidence, reports, or supported senses—not omniscience.

### Unified action validation
Every movement or interaction checks: (1) body/ability capability and reach; (2) target and environmental affordances; (3) collision, terrain, and current body state; (4) resource/time costs and interruption rules; (5) authoritative result and consequences; and (6) what nearby players and NPCs can observe. Reuse these checks for combat, traversal, harvesting, object manipulation, and ability effects to keep the rules consistent.

### Acceptance criteria
- Different anatomy produces visibly and mechanically distinct movement options.
- Hybrid traversal chains work when every required ability, anchor, surface, and resource is valid.
- Context prompts and direct physical controls resolve to the same valid world actions.
- The adaptive camera frames small, standard, aerial, and large forms without persistent clipping or loss of directional readability.
- Objects, terrain, resources, creatures, and NPCs respond consistently and persist according to world rules.
- Unsupported actions fail clearly; no interaction bypasses costs, compatibility, collision, permissions, or multiplayer authority.
- Input remapping and camera comfort options are supported.
- All rules are tested before the system is described as implemented.

## 26. Object handling, creature handling, and physical manipulation

**Status: approved design specification; not implemented or tested.** This section extends the movement and interaction rules in Section 25. Objects and creatures use shared interaction rules, while their distinct properties determine which actions are possible.

### Interaction targets and affordances

Each interactable target exposes data-driven properties rather than a fixed universal action list:
- **Physical properties:** mass, size, shape, material, durability, center of mass, grip/anchor points, fragility, and whether it can be moved or broken.
- **State:** fixed, loose, held, carried, damaged, harvested, consumed, captured, unconscious, dead, decaying, or otherwise unavailable, as applicable.
- **Biological properties:** species, anatomy, vital state, defenses, danger, eligible tissues, preservation needs, and known/unknown research status.
- **Context:** terrain, nearby obstacles, water/current/wind, temperature, permissions, witnesses, and relevant world/NPC reactions.
- **Player capability:** reach, appendage type, grip strength, limb availability, body size, movement mode, learned technique, and required resources.

The interface offers only actions supported by these properties. If an action is unavailable, explain the main reason when useful—insufficient reach, incompatible grip, excessive mass, protected target, dangerous condition, or missing ability—rather than displaying a misleading prompt.

### Grab, carry, drag, and throw

Direct physical controls should let the player intentionally reach for, grab, release, push, pull, drag, carry, place, and throw supported objects. Contextual prompts provide an accessible alternative to precise manual targeting. Both paths resolve through the same rules and world state.

- A held object occupies the appendage or grip used to hold it. That appendage cannot simultaneously perform incompatible actions.
- Extra limbs, tails, jaws, feet, or tendrils may provide alternate grips only if their anatomy definition explicitly supports that function.
- Carrying limits depend on mass, leverage, grip, body structure, movement style, stamina/energy, and terrain—not only a single inventory number.
- Dragging a heavy object may be possible when lifting is not. It is slower, noisier, may leave tracks, and is affected by friction, slope, obstacles, and the object's shape.
- Throwing depends on grip, mass, momentum, body mechanics, aim, and available space. Large or awkward objects may be pushed or dropped rather than thrown accurately.
- Carrying changes movement, climbing, dodging, swimming, flight, combat options, and visibility where physically appropriate. The UI should show significant restrictions before the player commits.
- Objects cannot pass through solid geometry, be duplicated by releasing/re-grabbing, or be moved through access restrictions without a valid ability or rule.

### Anatomy creates different handling styles

The same target can support different interactions based on the player's evolved body:
- **Hands or gripping forelimbs:** precise manipulation, tool use, turning mechanisms, handling small specimens, and careful placement.
- **Jaws or mouthparts:** carry suitable objects or prey while sacrificing eating, biting, speech, or other incompatible actions.
- **Tendrils or prehensile tails:** reach around obstacles, anchor, pull, swing, or hold multiple objects if the number, strength, and control of those appendages support it.
- **Claws and hooks:** attach to valid surfaces or grip suitable materials, but may damage fragile samples or lack fine manipulation.
- **Heavy limbs, horns, armor, or body mass:** shove, brace, break, pin, or move large objects without implying delicate grip.
- **Telekinetic, gravity, or other powers:** manipulate only within their defined range, line-of-effect, mass limit, energy cost, and resistance rules.

These are capability examples, not exclusive classes. Compatible features can combine through the general interaction resolver. Animation and feedback should make clear which appendage is doing the work.

### Creature handling and post-encounter choices

Living creatures are not ordinary physics props. Interactions must consider their awareness, movement, strength, size, danger, social behavior, and current condition. A player may observe, lure, feed, restrain, capture, carry, defend against, hunt, or communicate with a creature only when the relevant anatomy, abilities, target state, and world rules permit it. A creature may struggle, flee, attack, call for help, or attract other predators. Restraints and captures require valid control and can fail if the player cannot maintain them.

After a qualifying kill, the player can assess the remains and choose among supported actions such as securing the area, harvesting, preserving, carrying/dragging, absorbing/consuming, researching, or leaving the remains. These actions can compete for time and resources. They are not all guaranteed to be available on every species or body plan.

- **Harvesting** extracts eligible materials or tissues and updates the specimen's remaining state; it does not create unlimited copies of the same part.
- **Preservation** protects eligible tissues for later research or Vault storage, using suitable organs, containers, environment, or abilities where specified.
- **Absorption/consumption** follows the existing biology, compatibility, research, and progression requirements; it does not automatically grant every trait.
- **Transport** depends on target mass/shape, player capacity, route, grip, terrain, and interference. A large body may require dragging, cutting an eligible section, using multiple appendages, or abandoning the attempt.
- **Deterioration and scavenging** may change the value or availability of remains over time according to the world's decay rules. Valuable specimens can attract scavengers, rivals, investigators, or territorial creatures where justified.
- **Living capture** and **dead specimen handling** are separate states with different risks, affordances, and outcomes.

The interface must communicate meaningful trade-offs before irreversible actions, especially when consuming, damaging, or harvesting a rare specimen could remove a research opportunity. Never silently destroy an eligible unique specimen or permanently remove a player's earned build.

### Persistence, multiplayer, and fairness

Object and creature state is authoritative and shared. If a player moves a crate, breaks a barrier, harvests a rare organ, or leaves a carcass, other players should encounter the corresponding world state subject to the persistence and simulation rules. Concurrent attempts to grab or harvest the same target must resolve safely: one valid state transition wins, or the action is explicitly contested; neither player receives duplicated objects or rewards.

Important safeguards:
- Server-authoritative validation for contested, valuable, or combat-relevant interactions.
- No item duplication through latency, disconnects, repeated inputs, death, or save/load transitions.
- Clear ownership, access, and permission rules for protected objects, player-built structures, and private spaces.
- No hidden player knowledge: witnesses and NPCs react only to what they could observe, infer, or learn.
- Bounded physics and simulation budgets; distant objects and creatures may use simplified simulation without changing important outcomes unfairly.
- Safe handling of server interruption so a failed request does not consume a unique specimen without recording the result or award it twice.

### Acceptance criteria

Before this system is described as implemented, verify that:
- Different anatomies expose distinct, understandable handling options.
- Contextual and direct controls produce the same valid state changes.
- Grip occupancy, mass, reach, terrain, and resource costs constrain carrying and manipulation consistently.
- Living creatures can resist or respond when their behavior and condition allow it.
- Harvesting, preservation, consumption, and transport update one consistent specimen state.
- Shared world state remains consistent under simultaneous interactions, latency, disconnects, and save/load.
- Unique specimens, objects, and rewards cannot be duplicated or silently lost through invalid state transitions.
- The game explains important restrictions and irreversible trade-offs before commitment.

## 27. Bottom-up evolution stages and planetary ascension

**Status: approved design specification; not implemented or tested.** This section establishes the intended macro-progression sequence. It refines the existing level bands, Evolution Atlas, transformation, and space-travel systems; exact XP thresholds and implementation remain open.

### Stage progression principle

Progression is experienced as a series of meaningful biological and perceptual transitions, not just a level number or menu unlock. Each stage changes the player's available movement, sensory reach, body plan, interactions, survival needs, and scale of challenges. Transitions should be visible in the world and in the player's body, with clear requirements and a brief, readable explanation of new capabilities.

Evolution is based on the player's accumulated discoveries, consumed organisms, genetic information, environmental adaptations, and selected mutations. The game does not force every player through an identical final anatomy. Bipedal, quadrupedal, serpentine, multi-limbed, aquatic, aerial, and other viable body plans remain possible when supported by the player's acquired traits and compatible anatomy.

### Stage 1 — Cellular life: amoeba survival

The player begins as a simple amoeba-like organism at the smallest scale of the progression.

- Move with limited, low-speed cellular locomotion such as drifting, crawling, and extending pseudopod-like structures where appropriate.
- Gather and absorb compatible nutrients or microscopic life; avoid threats that are dangerous at this scale.
- Learn the core loop through play: detect, approach, absorb, survive, mutate, and adapt.
- Perception is limited and close-range. The environment should feel vast and only partly understood.
- Early adaptations may improve sensing, movement, membrane defense, energy storage, absorption, or resistance, but should not instantly grant complex creature powers.
- The first transition occurs when the organism meets a defined evolutionary threshold through survival, absorption, and compatible development.

### Stage 2 — Primitive organism: first complex mobility and clearer perception

The player evolves beyond the single-cell stage into a primitive multicellular or otherwise more complex organism.

- Movement becomes more deliberate but remains limited. The player may struggle to travel, turn, climb, or cross difficult terrain until relevant structures evolve.
- Sensory range and environmental clarity improve, revealing more of the nearby habitat, food sources, hazards, tracks, and organisms.
- New structures may include basic locomotor tissue, primitive sensory organs, attachment/gripping structures, and specialized absorption or defense organs.
- This stage teaches how body structures affect mobility and survival. It should feel meaningfully different from cellular drifting, not like the same controls with a larger model.
- Progression into the main creature stage depends on suitable biological complexity and survival milestones, not simply a cinematic timer.

### Stage 3 — Main creature stage: open-ended body plans and core gameplay

This is the primary long-running creature gameplay stage. The player develops a recognizable organism while retaining freedom over anatomy.

- Viable forms may be bipedal, quadrupedal, serpentine, multi-limbed, winged, aquatic, burrowing, or other compatible plans. No default humanoid form is mandatory.
- What the player has consumed, researched, survived, and adapted to influences which body parts, organs, traits, movement modes, and skill branches become available.
- Players develop individual body regions and organs, learn and master abilities, form custom techniques, and discover combinations.
- The world opens up to deeper exploration, hunting, rival creatures, territorial behavior, harvesting, specimen preservation, and more complex environmental interactions.
- Body-plan choice changes reach, grip, locomotion, carrying, combat chains, sensory strengths, weaknesses, and which actions are possible. The game explains compatibility and trade-offs rather than silently removing parts.
- The player may continue evolving within this stage for a substantial portion of the game. It is not a narrow mandatory humanoid tutorial.
- This stage includes the previously established standard-form scale principle: ordinary player forms remain broadly comparable in overall scale for fair baseline encounters; specialized transformations and titan-scale activities are governed by their own rules.

### Stage 4 — Species-dependent transformation

After meeting evolutionary prerequisites, the player receives an important transformation that reflects their species, anatomy, and evolution history.

- The transformation is earned through a defined combination of progression, relevant discoveries or mastery, compatible anatomy, and any specified environmental or material requirements.
- Transformations differ by body plan and evolutionary route. A winged organism may become an aerial combat form; an armored organism may gain a defensive siege form; a serpentine or multi-limbed organism develops a form suited to its own structure.
- A transformation may change anatomy, movement, control options, combat chains, defenses, resource use, sensory abilities, and available techniques—not only health, size, or damage.
- Clearly distinguish temporary transformation, persistent anatomical evolution, and saved compatible forms/loadouts. A temporary transformation does not silently overwrite the player's base anatomy.
- Transformations require clear activation, duration or persistence rules, costs, counters, and recovery conditions. Exact values remain open for balancing.
- The first transformation is a major progression milestone, but it does not automatically grant space survival or space travel.

### Stage 5 — Spacefaring life and biological space combat

Spacefaring progression becomes available only after the player satisfies the existing planetary departure requirements: explore every continent, defeat all designated planetary bosses, complete the planet-specific conquest objectives, and develop enough evolution to survive space. This preserves the prior rule that space is not an early-game shortcut.

- The player evolves their own body for spaceflight. No vehicle or spaceship is required or introduced.
- Necessary adaptations may include biological propulsion, three-dimensional maneuvering, navigation senses, vacuum survival, radiation/temperature protection, resource reserves, and defenses against cosmic organisms.
- Spaceflight controls support acceleration, braking, turning, rolling, climbing, diving, and sustained travel, with anatomy and environmental physics shaping handling.
- Players can explore planets, moons, asteroids, cosmic organisms, and points of interest, and can fight in space where encounters support it.
- Space combat uses the same anatomy, ability-combination, telegraphing, resource, damage, and multiplayer-authority principles as ground combat, adapted for three-dimensional movement and space hazards.
- The transition should show a clear change in scale and perspective, but keep the player's identity, history, anatomy, and permanent-death rules continuous. This is the same character evolving, not a separate ship or new character.
- Conquering one planet does not by itself unlock godlike evolution. The player must complete the three-planet condition below.

### Stage 6 — Godlike evolution after three planetary conquests

After the player has conquered three qualifying planets, the game unlocks a godlike evolutionary stage. The conquest requirements and proof must be recorded in persistent world/player progression so the milestone cannot be duplicated or granted by an invalid state transition.

- Godlike evolution represents accumulated biological knowledge and mastery of absorption. It improves the evolutionary return from creatures, specimens, and mutations.
- **Gathering itself does not become faster by default.** The player continues to find, approach, gather, and absorb through the established world loop at its normal rate; the increased benefit comes from greater enhancement yield, deeper mutation opportunities, improved compatibility insight, or access to advanced branches.
- Enhanced returns must be communicated before a meaningful consumption choice. Results still depend on the target, rarity, compatibility, research, anatomy, and applicable progression rules.
- Godlike progression may unlock powers that influence large-scale processes, environments, travel, or reality according to explicit ability rules. It is not permission to skip all costs, instantly collect every resource, ignore other players, or bypass world simulation.
- Gathering and absorption remain relevant after ascension. The player still discovers organisms and mutations; the rewards become more profound rather than making the core loop obsolete.
- Godlike power must preserve meaningful challenge, counters, multiplayer fairness, and server-authoritative validation. No ability may silently erase other players' earned progression or grant automatic victory.
- Godlike stage does not undo permanent death. If the character dies under the established rules, the character is lost; any retained research or archive follows the separately defined Vault rules.

### Stage transitions and feedback

Every transition should include:
1. A clear preview of the requirement and the player's current progress.
2. A visible anatomical and sensory change appropriate to the new stage.
3. A concise explanation of newly available movement, interactions, organs, abilities, and survival needs.
4. A comparison of important capabilities gained, lost, or changed.
5. An updated Evolution Atlas, Character Profile, Codex, and Evolution History.
6. A safe opportunity to learn changed controls and movement before facing a major lethal threat.
7. Persistent, server-authoritative recording of the transition and its prerequisites.

Transitions must not grant abilities whose prerequisites are missing, silently discard earned traits, or imply that concept art or design documentation means a feature is already implemented.

### Acceptance criteria

Before this progression is called implemented, verify that:
- Cellular, primitive, main-creature, transformation, spacefaring, and godlike stages have distinct gameplay and readable transition criteria.
- Main-stage body plans are determined by compatible evolution and are not forced into one humanoid template.
- Sensory and mobility improvements across the first two transitions are perceptible in play.
- Transformations reflect the player's species/anatomy and distinguish temporary forms from permanent evolution.
- Space access respects the previously specified planetary prerequisites and biological spaceflight rule.
- Godlike evolution requires three qualifying planetary conquests and increases enhancement/mutation returns without silently increasing the underlying gathering rate.
- Stage state, unlocks, prerequisites, and history persist consistently across supported sessions and multiplayer.
- Death, Vault persistence, resource costs, and unresolved rules remain consistent with the rest of the design.

### Open decisions retained

Exact XP thresholds and transition timing, the formal definition of a qualifying planetary conquest, whether godlike powers include time/reality manipulation at launch or later, the numerical increase in absorption yield, transformation duration/costs, and the final stage-specific UI remain open for explicit design and balancing.

## 28. Master Power and Ability Catalogue

**Status: initial design inventory documented; powers are not thereby implemented or balanced.** The dedicated catalogue at [docs/POWER_ABILITY_CATALOGUE.md](POWER_ABILITY_CATALOGUE.md) is the broad index for potential powers and abilities across biological, physical, elemental, psychic, magical, technological, dimensional, cosmic, and godlike systems. It includes locomotion, senses, defense, combat techniques, transformations, absorption, creation, support, and combinations.

The catalogue is intentionally expandable rather than a claim that any finite list captures every imaginable power. It draws on broad genre concepts across games, anime, television, comics, mythology, fantasy, science fiction, and speculative biology. It must not copy another franchise's protected character, art, narrative, text, or distinctive implementation.

Every detailed ability must distinguish its source/mechanism, effect, delivery, eligible targets, applications, prerequisites, body-plan compatibility, costs, range, duration, recovery, environmental dependencies, counters, failure modes, combinations, visual feedback, world/NPC consequences, multiplayer validation, stage-specific evolution, and acceptance tests. Separate generation, control, absorption, conversion, resistance, immunity, sensing, and movement when they have distinct gameplay.

Abilities are candidates, not automatic launch commitments. No power is unrestricted by default. Range, duration, targets, energy, compatibility, counterplay, permanent-death rules, and server-authoritative fairness must remain coherent. New and untested combinations are hypotheses until their outcomes are verified and recorded in the Codex. The next design pass will deduplicate the index, define full ability records, classify rarity, map abilities to progression stages, and document interactions.



## 29. Character inspiration and original character roster

Lethal Absorption should include authored characters that deliver the broad appeal of the games and anime named in Section 1: distinctive combat identities, dramatic transformations, signature techniques, tactical tools, magic and supernatural systems, rivalries, memorable bosses, companions, factions, and cosmic-scale figures. These references define desired experience qualities only; the game must use original characters, species, stories, names, silhouettes, costumes, dialogue, animations, and signature techniques.

The detailed framework and first ten original character archetype seeds are maintained in [Character Inspiration and Original Roster](CHARACTER_INSPIRATION_AND_ORIGINAL_ROSTER.md). The framework uses an inspiration-to-originality pipeline: extract a broad design goal, abstract the mechanic, create a new premise and expression, define the character's role in the world, then review for excessive similarity to any single reference.

Character content has five distinct lanes:
- **Player characters:** open-ended body plans and builds assembled through eligible evolution choices, not permanent preset classes.
- **Authored NPCs:** original motivations, relationships, culture, and readable combat or non-combat roles.
- **Rivals and bosses:** advanced combinations and transformations with understandable tells, limits, weaknesses, and counterplay.
- **Companions and factions:** potential support for research, diplomacy, crafting, exploration, team abilities, and persistent world change.
- **World and cosmic characters:** beings whose ecological, planetary, or cosmic roles make their existence matter beyond being a source of loot.

Absorption from a character is not automatic copying of identity, complete power set, or mastery. Discovery, sample acquisition, analysis, compatibility, mutation selection, installation, and mastery remain separate. Sapient characters have agency and rights within the fiction; not every character should be an absorbable target, and not every encounter should resolve through combat. Any lethal PvP absorption remains governed by the existing high-stakes PvP and fairness rules.

Each major character needs an original visual read, motive, relationships, narrative role, combat rhythm or utility role, strengths, weaknesses, counterplay, world consequences, eligible absorption rewards if any, and acceptance criteria. Characters must react only to information they could reasonably observe or learn. Character concepts, approved designs, assets, code, and verified behavior must have separate status labels.

**Status:** design specification only. The framework and archetype seeds are not implemented character content. Open decisions include final roster size, story placement, companion boundaries, authored-versus-modular content ratio, and originality review.


## 30. Action-gated slime evolution route

The game should contain a **secret god-tier basic slime lineage** hidden among its many monsters, species, abilities, and transformations. At first, it appears to be an ordinary weak slime. Through rare, specific actions, discoveries, experiments, and hidden evolution conditions, a player can uncover a path toward godlike power. The secret is not advertised at character creation, is not guaranteed to every slime player, and must be discoverable through reproducible in-world actions once its clues are understood. The desired inspiration is the broad ability fantasy—absorption, analysis, shapeshifting, regeneration, adaptive resistance, rapid learning, ability synthesis, and escalating transformations—not a copy of the anime protagonist or exact named skills.

The detailed route, candidate milestone gates, original working ability suite, player-facing Atlas requirements, acceptance criteria, and open questions are maintained in [Slime Action-Gated Evolution](SLIME_ACTION_GATED_EVOLUTION.md). Candidate unlock families include selective assimilation, trait analysis, form mimicry, elastic morphology, distributed body, regeneration, adaptive resistance, parallel cognition, elemental/energy control, barriers, spatial storage, trait synthesis, sovereign-scale abilities, and cosmic adaptation. Early clues should look like ordinary adaptations; deeper branches remain concealed until discovered.

The secret slime must use original lore, identity, ability names, visuals, animations, and story placement. The detailed specification preserves the desired broad mechanics without copying a franchise character or its distinctive expression. This is not a claim that any ability is implemented.

The Evolution Atlas must show each known ability's unlock state, prerequisites, action progress, source, compatibility, costs, counters, and mastery separately. Absorption must not automatically copy all of a target's powers or expertise. The existing permanent-death and three-planet godlike-progression rules continue to apply.

**Status:** detailed design proposal; numeric balance, route placement, initial-scope selection, and implementation remain open.


## 31. Hidden god-tier skeleton ascendant

The world should contain a secret skeleton evolution route that can turn an apparently ordinary, weak skeleton into an exceptionally powerful undead sovereign. The path is concealed at character creation and uncovered through connected clues, grave/ruin exploration, magical research, survival feats, spell mastery, summon control, preparation, and high-risk evolution trials. It is not a copy of Ainz Ooal Gown or another existing character.

The desired broad ability fantasy includes necromancy, spell discovery and preparation, summoning and commanding undead, layered defenses, resistances, tactical counters, rituals, lair/domain development, and escalating transformations. All names, lore, character identity, visuals, animations, and specific presentation must be original. The route must keep spell discovery, acquisition, preparation, casting, and mastery distinct, and must define summon limits, upkeep, control bandwidth, counterplay, and world consequences.

The full milestone gates, working ability suite, secret-discovery rules, UI requirements, acceptance criteria, and open decisions are in [Hidden God-Tier Skeleton Ascendant](HIDDEN_SKELETON_ASCENDANT.md). The route must respect permanent character death; anchor-like lore cannot resurrect a player character. It must also align with the existing late-game and three-planet godlike progression requirements where applicable.

**Status:** detailed design proposal only; not implemented or tested. Open decisions include starting-lineage availability, magic-resource architecture, summon limits, domain ownership, and first-playable-scope selection.


## 32. Hidden shadow sovereign, limit-breaker, and goblin evolution routes

Add three original action-gated route concepts that evoke broad qualities associated with *Solo Leveling*, *Dragon Ball*, and *Re:Monster* without copying their protagonists, exact powers, names, designs, lore, dialogue, or signature presentation.

- **Hidden Shadow Sovereign:** a low-status survivor discovers residual traces, earns a first echo through a costly trial, and gradually learns bounded echo command, tactical formations, and late-game sovereign powers. Echo count, command bandwidth, duration, upkeep, counters, and recovery must be explicit. No echo or anchor can resurrect a player character.
- **Limit-Breaker Martial Ascendant:** a fighter earns techniques and transformations through training, readable combat challenges, energy control, rival encounters, and mastery. Overdrive has costs and vulnerability windows; transformations add choices and trade-offs rather than guaranteeing victory.
- **Goblin Reclaimer:** a fragile goblin grows through survival, selective consumption, crafting, technique learning, social or solo strategy, and compatible trait evolution. Consumption never grants every target skill automatically; crafting requires materials and learned competence, and NPC allies retain agency.

The complete proposed gates, original working ability names, limitations, counterplay, shared secret-route rules, and open decisions are maintained in [Shadow Sovereign, Limit-Breaker, and Goblin Evolution Routes](SHADOW_SOVEREIGN_LIMIT_BREAKER_GOBLIN_ROUTES.md). All three routes keep their endgame hidden at character creation and require discoverable, reproducible action gates. They must obey permanent character death, multiplayer fairness, privacy, server-authoritative validation, and the existing three-planet godlike progression condition where applicable.

**Status:** design proposal only; not implemented or tested. Open decisions include starting-lineage versus hidden-branch availability, exact costs and thresholds, resource architecture, solo/group route requirements, and first-playable scope.


## 33. Wukong-inspired mythic staff ascendant route

**Availability requirement:** Wukong-inspired gameplay is part of the planned Lethal Absorption roster and must not be omitted. The intended player experience is a mobile, technically expressive staff fighter with mythic trials, feints, staff-assisted traversal, counterattacks, and earned transformation options. The route may also inspire original mentors, rivals, and bosses.

The route must use original character identity, lore, silhouette, staff design, animations, effects, names, and signature techniques. Broad inspiration from mythic staff-fighter themes does not authorize copying Sun Wukong's specific portrayal or any particular game's/anime's protected character expression.

The detailed progression, original working abilities, strengths, weaknesses, counterplay, acceptance criteria, and open decisions are in [Mythic Staff Ascendant (Wukong-Inspired)](WUKONG_INSPIRED_MYTHIC_STAFF_ASCENDANT.md). The route supports a playable staff-focused build. Whether it is available from character creation, unlocked through a hidden branch, or both remains open. Its abilities must obey resource, recovery, anatomy, terrain, multiplayer fairness, and permanent-death rules.

**Status:** design specification only; not implemented or tested.


## 34. Expanded ability coverage across all approved inspiration routes

The game design must cover the complete intended range of ability families for the six approved inspiration routes: shadow-command sovereign, limit-breaking martial ascendant, adaptive goblin reclaimer, mythic staff trickster, hidden god-tier slime, and undead spell sovereign. The detailed matrix is maintained in [Expanded Ability Coverage Matrix](EXPANDED_ABILITY_COVERAGE_MATRIX.md).

Coverage includes perception and analysis; bounded echoes, summons, and command systems; melee, staff, ranged energy, and aerial combat; transformation and temporary amplification; crafting, salvage, selective absorption, trait synthesis, and adaptive anatomy; barriers, wards, resistance, spell research, rituals, domains, and counterplay; movement, decoys, reconstitution limits, endgame/cosmic progression, and eligible cross-route combinations.

This is an approved design baseline, not a claim that the powers have been coded, animated, balanced, or tested. Every ability must have a distinct catalogue record defining action gates, anatomy compatibility, costs/upkeep, range/duration, startup/recovery, mastery stages, counters, combinations, NPC/ecology effects, multiplayer/server-authority rules, accessibility/readability, and test cases. No infinite resources, unrestricted clones or armies, omniscience, universal immunity, free power stacking, or resurrection after permanent character death. Personal unlocks remain personal; the Shared Discovery Network shares knowledge only. Sapient species retain agency and rights.

Use original ability names, lore, silhouettes, animations, effects, and combinations. The project is targeting broad capability and gameplay coverage across its inspirations, not a move-for-move reproduction of licensed characters or their exact expression. A vertical slice may stage delivery, but it must not silently erase the approved roadmap. Runtime implementation and verification status must be reported honestly.

**Status:** design specification only; not implemented or tested.


## 35. Character-specific powersets are a required content target

The six named routes—Sung Jinwoo, Goku, the *Re:Monster* goblin protagonist, Sun Wukong, Rimuru Tempest, and Ainz Ooal Gown—must not be reduced to generic archetypes or loose thematic inspirations. The intended content target is a route-specific inventory of individual abilities, passive traits, skills, transformations/forms, upgrades, summons, resistances, and their unlock/progression conditions, based on a declared set of source versions. See [Character-Specific Powerset Requirements](CHARACTER_SPECIFIC_POWERSET_REQUIREMENTS.md).

Every ability must be individually catalogued, with source/version traceability, unlock method, active/passive/conditional status, route/form prerequisites, gameplay effects, costs, counters, upgrade chains, interactions, and implementation status. The roadmap may stage release, but deferred powers must remain tracked. Where exact franchise character names, signature expression, visuals, or other protected content is planned for commercial release, rights/licensing must be addressed or the content must be separately adapted into original expression.

**Status:** requirement documented; canonical source-by-source inventories and gameplay implementation remain outstanding. Documentation must not be represented as playable implementation.
