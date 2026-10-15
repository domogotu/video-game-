# Lethal Absorption — The Slime: Complete Evolutionary Character Blueprint

> **Status:** Foundational design specification; design-only, not implemented or tested.
>
> **Working identity:** The Null Sovereign (temporary codename). Final name, visual identity, origin, and secret-boss reveal remain editable.
>
> **Purpose:** Establish the first end-to-end life path and master reference for future species. The slime begins without limbs or conventional organs and earns every new capability through survival, absorption, adaptation, discovery, training, and deliberate evolution.

## 1. Design mandate

This is an original Lethal Absorption character built from broad slime-game design patterns—not a reproduction of any single copyrighted slime, character, named skill, visual design, or progression tree. The research inspiration spans absorption and evolution, elemental acquisition, splitting, merging, physics-based movement, digestion, status effects, slime companions, skill mastery, and late-game transformations. No search can establish a literal inventory of every slime ability in every game; this document defines a broad, extensible taxonomy and a coherent original implementation target.

**Character fantasy:** Begin as vulnerable living gel. Survive by sensing, moving, hiding, feeding, and learning. Gradually become a flexible combat organism that can reconfigure its anatomy and use the world's biology as a library of possibilities. At the end of the path, become an apparently unbeatable secret-boss entity whose powers are formidable but whose combat logic remains readable and counterable.

**Non-negotiable rules**
- No limbs at the start. Early movement and combat must be designed for a limbless body.
- No ability is granted merely because it appears on the tree. It has prerequisites, a learning source, a cost, a limitation, and counterplay.
- Absorption is not automatic mastery. Eating, safely digesting, analyzing, adapting, and mastering are separate steps.
- The slime can learn broadly, but cannot run every power at full strength simultaneously. Internal capacity, energy, heat, stability, attention, anatomy, and loadout constraints preserve choices.
- A player's secret-boss build is an authored extreme of the same rules used by ordinary species—not a separate system with arbitrary immunity.
- PvP can never permanently kill the player or steal assets/progression. Boss challenge does not override this rule.
- The existing level cap remains 1050; main-story completion does not require reaching the cap.
- Planetary completion precedes space survival; space progression uses biological Living Ship Form, not conventional ships or vehicles.
- This is a master design reference. It does not expand or replace the frozen initial vertical slice.

## 2. Life path overview

| Stage | Form / role | Core problem | Signature unlock |
|---|---|---|---|
| 0 | Dormant cell | Wake, sense, avoid lethal conditions | Pulse, contract, roll |
| 1 | Primitive slime | Feed without limbs; avoid predators | Adhesion, engulf, nutrient processing |
| 2 | Adaptive gel | Survive contact and learn from threats | Elastic recoil, gel armor, first trait choice |
| 3 | Mobile slime | Navigate difficult terrain and escape pursuit | Launch, wall cling, fluid flow |
| 4 | Hunter slime | Fight creatures using body shape, not weapons | Pseudopod strike, tendril, acid / enzyme options |
| 5 | Composite slime | Combine acquired traits safely | Trait slots, limited fusion, resistance adaptation |
| 6 | Intelligent slime | Observe, plan, imitate patterns, support allies | Sensory web, decoy, controlled split |
| 7 | Apex slime | Compete with evolved predators and bosses | Shape-shifting body plans, counters, signature ability |
| 8 | Sovereign slime | Control an ecosystem and survive extreme habitats | Territory-scale adaptations, advanced fusions |
| 9 | Planetary apex | Finish planetary evolution and confront world-scale threats | Planetary-scale biology and transformation |
| 10 | Living Ship organism | Survive and move through space biologically | Vacuum shell, propulsion, navigation, cosmic feeding |
| 11 | Cosmic aberration | Interact with exotic energy, dimensions, and reality | Highly gated cosmic adaptations |
| 12 | Secret-boss ultimate | Test a complete build against its own principles | Null Sovereign form, adaptive encounter phases |

Stages are evolutionary milestones, not rigid level brackets. A character can reach a milestone early through a rare discovery or later through a safer route. Access to a branch does not imply it is safe to attempt.

## 3. Starting body and base statistics

### Stage 0: Dormant cell
- **Body:** tiny single cellular mass; no limbs, eyes, mouth, skeleton, lungs, or separate hands.
- **Perception:** chemical gradients, contact, temperature, pressure, light/dark intensity, and fluid vibration at very short range.
- **Movement:** membrane contractions and passive drift. No conventional jump, sprint, or attack.
- **Survival loop:** detect safe nutrients → pulse toward them → absorb small particles → stabilize membrane → evade environmental hazard.
- **Threats:** drying, extreme temperature, toxins, violent currents, crushing pressure, and larger organisms.
- **First lesson:** sensory information is partial; moving toward food may expose the cell to danger.

### Stage 1: Primitive slime
- **Body:** one soft mass with a central nutrient core and outer membrane.
- **Movement:** contract, flatten, roll, ooze through gaps, cling briefly to rough surfaces.
- **Attack:** weak body bump, adhesive contact, engulf tiny resources. No standard melee combo yet.
- **Defense:** compress under some attacks, but piercing, drying, heat, and membrane disruption are dangerous.
- **Progression:** nutrient storage, membrane integrity, basic digestion, and first safe absorption.
- **Failure recovery:** early tutorial setbacks are recoverable; no permanent death before the core movement, absorption, and evasion lessons are taught.

Base metrics should be qualitative in early prototypes. Exact HP, damage, speed, resource caps, and multipliers are balancing decisions, not yet established.

## 4. Slime-specific body systems

Every ability is supported by one or more body systems. Body systems may be passive, toggled, or active.

1. **Membrane:** shape control, adhesion, permeability, water retention, surface tension, impact distribution.
2. **Gel matrix:** elasticity, viscosity, density, damping, rebound, structural memory.
3. **Nutrient core:** digestion, energy conversion, storage, emergency reserves, overload warning.
4. **Distributed sensory web:** chemical, vibration, pressure, thermal, electrical, optical, and later exotic-energy sensing.
5. **Pseudopod architecture:** temporary protrusions, tendrils, hooks, striking lobes, grasping pads, stabilizers.
6. **Digestive chemistry:** enzymes, acid, neutralizers, selective breakdown, toxin isolation, material processing.
7. **Repair lattice:** local sealing, controlled regrowth, replacement of damaged mass, emergency survival mode.
8. **Trait archive:** stores analyzed biological patterns and learned adaptations, not an unlimited set of simultaneous active mutations.
9. **Cognitive lattice:** distributed processing, memory, tactical modeling, deliberate body control, later parallel attention.
10. **Fusion regulator:** evaluates compatibility, stabilizes combinations, rejects dangerous trait conflicts.
11. **Environmental interface:** heat exchange, water balance, pressure tolerance, atmospheric and vacuum adaptations.
12. **Exotic interface:** late-game energy, dimensional, and reality-interaction adaptations; unavailable until their own rules are discovered.

## 5. Core resource model

Keep resources distinct so that one generic mana bar does not erase the biology.

- **Biomass:** physical material used for growth, body parts, splitting, repair, and some constructs.
- **Metabolic energy:** immediate movement, attacks, active skills, and maintaining forms.
- **Stability:** how well the current body plan and fused traits remain coherent under stress.
- **Thermal / chemical load:** accumulated heat, acid, toxins, or other process strain from specific abilities.
- **Cognitive load:** number and complexity of simultaneous controlled actions, later improved by evolution.
- **Knowledge / mastery:** persistent learning state, not a spendable combat resource.
- **Evolution points:** optional progression accounting for the Atlas; exact generation and costs remain open.

Resource interactions: low biomass limits regrowth and splitting; low energy slows movement and active powers; low stability can disable incompatible fusions; overload creates telegraphed symptoms before a catastrophic failure. Never silently remove a power without communicating why.

## 6. Complete ability catalogue by family

The following is a broad original ability catalogue. These are design candidates, not all unlocked from the beginning. Each requires appropriate biological systems, discoveries, mastery, and costs.

### A. Movement and locomotion
- **Pulse Crawl:** alternating membrane contractions move the body across a surface.
- **Roll / Flow:** move as a compact rolling mass or low-profile fluid layer.
- **Compression Slip:** squeeze through a gap if body volume and material properties permit.
- **Adhesion:** cling to suitable surfaces; performance depends on texture, moisture, gravity, and contamination.
- **Wall Ooze:** slowly traverse walls and ceilings, with grip and energy limits.
- **Elastic Launch:** compress then release to leap; landing stability matters.
- **Rebound Step:** bounce off a valid surface to redirect movement.
- **Tendril Pull:** anchor a pseudopod and pull the body toward it.
- **Tether Swing:** later, use multiple anchors to swing or change direction.
- **Surface Skim:** travel quickly across suitable liquid or smooth terrain.
- **Buoyancy Control:** float, sink, or hover in fluid within density limits.
- **Current Riding:** detect and exploit fluid or air currents.
- **Burrow Ooze:** pass through loose material only if particle size, pressure, and oxygen/energy rules allow it.
- **Impact Cushion:** deform to reduce fall or collision damage; cannot cancel arbitrarily large impacts.
- **Aerial Glide:** broad membrane shape creates limited glide, not true flight.
- **Wing / Fin Mimic:** acquired anatomical adaptation for environments where a dedicated structure is viable.
- **Vector Recoil:** use a controlled mass ejection or energy pulse to change trajectory; expensive and dangerous near hazards.
- **Microflow:** split the outer body into tiny connected flows to pass around obstacles; high control cost.
- **Biological Propulsion:** advanced, form-specific movement for deep water, atmosphere, and eventually space.

### B. Sensing and perception
- **Chemoreception:** detect food, toxins, trails, pheromones, and disturbed surfaces.
- **Vibration Map:** infer nearby movement through ground or connected fluid.
- **Pressure Sense:** detect contact, approaching force, and structural stress.
- **Thermal Sense:** detect heat sources and temperature gradients.
- **Light Sensitivity:** distinguish illumination and movement; not full vision at first.
- **Optical Organ:** optional later organ for direction, silhouettes, and detail.
- **Electrical Sense:** detect bioelectric signals or powered systems at a limited range.
- **Echo Pulse:** emit a pulse and interpret returning disturbances; noisy environments degrade it.
- **Scent Memory:** retain and compare chemical signatures.
- **Trail Reconstruction:** combine scent, vibration, damage, and environmental evidence into a probable path.
- **Threat Signature Archive:** remember a creature's observed movement or attack pattern after sufficient exposure.
- **Energy Gradient Sense:** late-game detection of unusual energy sources, with decoys and blind spots.
- **Distributed Awareness:** monitor several nearby directions by allocating cognitive capacity.
- **Weakness Hypothesis:** suggest likely vulnerabilities from evidence; never guarantee an unknown target's weakness.
- **False-Signal Detection:** compare inconsistent cues to recognize possible decoys.

### C. Feeding, absorption, and digestion
- **Particle Absorption:** absorb compatible small nutrients through the membrane.
- **Engulf:** envelop an object or sufficiently vulnerable target; size, struggle, armor, and interruption matter.
- **Selective Intake:** choose what enters the digestive system.
- **External Digestion:** release enzymes to soften compatible material before intake.
- **Biomass Conversion:** turn digestible material into usable body mass.
- **Energy Extraction:** obtain metabolic energy from appropriate nutrients.
- **Mineral Assimilation:** incorporate compatible minerals into armor, density, or specialized tissues.
- **Organic Pattern Analysis:** study an organism's biological structure from credible evidence.
- **Trait Imprint:** unlock an eligible adaptation after enough analysis and a valid source; it does not automatically copy the target's full power.
- **Toxin Isolation:** quarantine and process known toxins; unknown toxins remain dangerous.
- **Purification:** remove or neutralize selected contaminants at a cost.
- **Emergency Digestion:** convert stored reserves into energy, with long-term biomass loss.
- **Stored Nutrient Sac:** retain limited food for travel or recovery.
- **Prey Disassembly:** safely process eligible material; sapient beings are not ordinary loot, ingredients, or property.
- **Living Target Resistance:** intelligent or powerful targets can fight engulfment, escape, injure the slime, or force disengagement.
- **Digestive Overload:** too much incompatible matter causes instability, toxin buildup, or temporary shutdown.
- **Absorption Recall:** review the source, evidence, and confidence behind a learned trait.
- **Memory Digestion:** late-game conversion of nonphysical patterns into knowledge only when supported by explicit world rules; not a blanket ability to steal identity or memories.

### D. Defense and recovery
- **Elastic Damping:** distribute blunt impact across the body.
- **Membrane Hardening:** temporarily increase surface resistance at the expense of flexibility.
- **Gel Armor:** form layered dense gel; increases mass and may reduce speed.
- **Viscoelastic Guard:** absorb and slow some attacks, but prolonged force can overwhelm it.
- **Surface Shedding:** discard a damaged or contaminated outer layer at a biomass cost.
- **Damage Seal:** close cuts and leaks quickly if sufficient material and energy remain.
- **Regeneration:** rebuild damaged tissue over time; cannot be free, instantaneous, or limitless.
- **Emergency Core Shield:** protect the vital nutrient/cognitive core while sacrificing outer biomass.
- **Shock Dispersion:** distribute a shock through a larger body volume; may stun the slime if overloaded.
- **Chemical Neutralizer:** counter a known acid, toxin, or corrosive agent after analysis.
- **Thermal Buffer:** temporarily absorb or redirect heat within a defined capacity.
- **Cryoprotectant:** survive cold conditions within a limit; does not grant universal immunity to freezing.
- **Desiccation Seal:** retain moisture in dry areas at an energy cost.
- **Pressure Adaptation:** reinforce body structure for deep water or high-pressure environments.
- **Reflective Film:** redirect some light or energy interactions only where the physical rule permits; no universal damage reflection.
- **Reactive Membrane:** changes response after observing a repeated attack; has adaptation delay and a finite set of maintained responses.
- **Status Purge:** expel or metabolize one known status agent, with resource cost and cooldown.
- **False Death / Dormancy:** reduce activity to evade some predators; vulnerable to discovery and environmental hazards.
- **Last-Mass Survival:** preserve a small viable core after catastrophic damage only if the encounter rules allow it; not a loophole against protected PvP or scripted permanent-death rules.

### E. Body shaping and anatomy
- **Pseudopod:** create a temporary protrusion for reaching, pushing, striking, or gripping.
- **Multi-Pseudopod:** maintain multiple temporary limbs within a control limit.
- **Tendril:** thinner, longer reach with lower impact strength and vulnerability to severing.
- **Hook / Barb:** anchor or snag suitable targets; difficult to use against some materials.
- **Suction Pad:** attach to compatible surfaces or targets.
- **Grip Pad:** hold an object without conventional fingers.
- **Impact Lobe:** concentrate mass for a blunt strike.
- **Blade Ridge:** create a hardened cutting edge if compatible material and stability are available.
- **Spine Burst:** expose defensive projections; reduces flexibility and can shed material.
- **Cushion Dome:** broaden the body to shield an ally or absorb a fall.
- **Armor Plates:** form rigid regions with gaps and mobility trade-offs.
- **Sensory Cilia:** improve environmental detection and fluid interaction.
- **Mouth Aperture:** create a controlled intake opening without requiring a permanent face.
- **Temporary Eye:** specialize a region for optical perception.
- **Gill / Gas Exchange Membrane:** support suitable aquatic or atmospheric environments.
- **Respiratory Organ Mimic:** use only after studying a viable biological pattern; each organ has maintenance needs.
- **Tail / Fin / Wing Mimic:** acquire a functional shape only if the underlying structure and energy budget support it.
- **Tool Grip:** create a stable grasping form for carried equipment where compatible with the world and body plan.
- **Body Density Shift:** redistribute density for floating, impact, or anchoring; costs energy and changes vulnerability.
- **Body Split:** separate into controlled sub-bodies only after a specialized control node.
- **Body Merge:** reunite compatible sub-bodies and recover shared mass; lost or damaged pieces may not be recoverable.
- **Shape Memory:** retain a learned form template to switch between saved body plans.
- **Anatomy Loadouts:** save compatible forms; transformation time, mass, and available resources still apply.

### F. Offense and combat techniques
- **Body Bump:** short-range attack using mass and momentum.
- **Pseudopod Jab:** quick reach attack with low commitment.
- **Hammer Lobe:** slower, heavier blunt strike.
- **Elastic Whip:** long reach, telegraphed sweep.
- **Multi-Tendril Lash:** several attacks with a high control cost.
- **Engulfing Clamp:** hold a target briefly to set up a follow-up; powerful targets can break free.
- **Adhesive Snare:** restrict movement on a successful hit; surface, mass, and resistance matter.
- **Acid Spit:** ranged corrosive attack; limited ammunition/chemical reserve and counterplay.
- **Enzyme Mist:** weaken selected materials or defenses gradually; not a universal instant dissolve.
- **Corrosive Pool:** place a hazard that can affect the slime too if incompatible.
- **Gel Projectile:** eject a blob that slows or marks a target; costs biomass.
- **Spore / Irritant Cloud:** status effect against susceptible targets; wind and filtration are counters.
- **Toxic Secretion:** use only after developing and storing a defined toxin; risks self-contamination.
- **Pressure Burst:** release a short-range concussive pulse; high energy cost.
- **Ground Pulse:** transmit a shock through a suitable surface; weak across discontinuous terrain.
- **Elastic Counter:** absorb a manageable hit and return momentum; timing and force limit apply.
- **Body-Check Launch:** compact, high-speed ram; dangerous if missed.
- **Pseudopod Parry:** deflect a defined class of attack with timing and angle.
- **Recoil Dodge:** shed or shift mass to evade, with a temporary stability penalty.
- **Tendril Bind:** briefly bind a target or object; cannot hold every size class.
- **Pin-and-Strike:** use adhesion and body shaping to create a combo opening.
- **Split Flank:** controlled sub-body distracts or attacks from another angle; shared biomass and attention are divided.
- **Decoy Shedding:** leave a moving or scented mass to misdirect a pursuer; costs biomass and may reveal the slime's signature.
- **Feint Shape:** simulate a vulnerable opening or change attack silhouette; only works against observers that can read the cue.
- **Adaptive Combo:** link a learned movement, attack, and counter; requires timing mastery.
- **Execution Compression:** high-risk finisher against a sufficiently staggered, eligible target; not guaranteed instant death.
- **Boss Breaker:** a situational attack that punishes a telegraphed boss vulnerability, not a universal boss-kill button.

### G. Elemental and material adaptations
Elements are acquired as traits with resistance, output, and environmental interactions—not simply color swaps. A slime can store many analyzed patterns but has a limited active loadout and stability budget.

- **Heat / Flame:** heat storage, thermal pulse, flame projection where a valid fuel/energy mechanism exists, burn resistance, heat vent.
- **Cold / Ice:** heat extraction, frost coating, brittle terrain interaction, cryoprotection, ice shaping where moisture permits.
- **Water / Fluid:** water storage, flow form, pressure jets, moisture restoration, aquatic movement.
- **Wind / Gas:** airflow sensing, pressure pulse, glide assistance, gas dispersal, wind-assisted projectiles.
- **Earth / Mineral:** mineral armor, anchoring, burrowing in suitable soil, crystal/mineral shaping where material is available.
- **Electricity:** charge storage, bioelectric pulse, conductive surface interaction, grounding vulnerability.
- **Acid / Corrosion:** selective dissolution, corrosive coating, neutralization, corrosion-resistant membrane.
- **Poison / Toxin:** controlled secretion, toxin sensing, antidote research, susceptibility and self-contamination risk.
- **Light:** illumination, optical signaling, refraction/flash, limited energy interactions.
- **Shadow / Obscurity:** concealment in suitable light conditions, signature suppression, decoy shadowing; not literal invulnerability.
- **Sound / Vibration:** sonic pulse, resonance sensing, vibration damping, frequency-specific weaknesses.
- **Metal / Alloy:** mineral-metal assimilation and rigid structures where compatible; mass and conductivity trade-offs.
- **Crystal:** hard facets, resonance storage, brittle failure modes, refractive effects.
- **Plant / Fungal:** root-like anchoring, spore interactions, nutrient exchange, habitat-specific growth.
- **Gravity:** late-stage mass and movement manipulation with steep energy cost, range limits, and counterplay.
- **Magnetic:** interaction with compatible ferromagnetic materials, not universal control over all matter.
- **Radiant / Plasma-like energy:** highly gated, with containment and thermal burden.
- **Void / Exotic:** interact with explicitly defined anomalous matter or energy; must have rules and tells.
- **Temporal / Dimensional:** late-game branches only, constrained by the game's time, causality, and world-state rules.
- **Reality / Creation:** ultimate-tier capabilities requiring explicit costs, limitations, narrative gates, and testable rules; never an unlimited wish system.

### H. Control, support, and utility
- **Adhesive Mark:** mark a target with a detectable trace.
- **Scent Tag:** track a target within environmental limits.
- **Gel Bridge:** create a temporary crossing or foothold using stored mass.
- **Gel Cushion:** protect an ally from a fall or impact.
- **Seal / Plug:** temporarily block a leak, vent, or narrow passage.
- **Neutralizing Film:** protect a small surface or ally from a known hazard.
- **Resource Capsule:** carry or share a limited amount of nutrient/chemical reserve.
- **Signal Pulse:** communicate a simple learned signal to compatible allies.
- **Rescue Tendril:** pull an ally out of danger if strength and geometry allow.
- **Barrier Blob:** create a short-lived obstacle; can be destroyed or bypassed.
- **Temporary Platform:** place a mass-limited platform that degrades.
- **Scent Mask:** suppress or falsify a scent trail at a resource cost.
- **Environmental Sample:** collect a small specimen for later analysis.
- **Nest / Recovery Pool:** create a temporary recovery location where world rules allow it.
- **Ally Coat:** provide a protective gel layer; may impede movement or alter heat exchange.
- **Companion Bud:** create a limited autonomous helper only after a dedicated branch; it is not a free army.
- **Shared Sensory Link:** receive partial cues from a bonded ally; range and cognitive load limit it.
- **Habitat Repair:** assist local ecological recovery through appropriate biological processes; does not instantly reverse major destruction.

### I. Cognition, mimicry, and adaptation
- **Pattern Learning:** improve an ability after repeated valid use.
- **Attack Read:** learn wind-up and recovery cues after observing them.
- **Trait Compatibility Map:** predict likely fusion conflicts.
- **Temporary Mimicry:** imitate a limited physical property or silhouette after analysis; does not grant the target's full skills, identity, or authority.
- **Surface Camouflage:** adjust color, reflectance, and texture within available pigments/materials.
- **Thermal Camouflage:** reduce thermal signature within a limited range, with heat storage trade-offs.
- **Scent Mimicry:** imitate a studied chemical signature imperfectly.
- **Voice / Signal Mimicry:** later, produce learned sounds or simple signals; does not automatically deceive intelligent targets.
- **Movement Imitation:** reproduce observed locomotion or an attack rhythm if anatomy permits.
- **Behavior Model:** predict likely actions from observed evidence, with uncertainty.
- **Tactical Split Attention:** monitor multiple threats at a cognitive cost.
- **Memory Lattice:** store routes, creature signatures, and learned form templates.
- **Threat Adaptation:** develop a bounded counter to a repeatedly observed attack after a delay; opponents can vary tactics.
- **Counter-Adaptation:** revise a learned defense when an enemy changes tactics.
- **Environmental Research:** identify why a habitat is dangerous and what trait could help.
- **Evolution Preview:** simulate plausible build consequences in the Atlas without granting the outcome.
- **Trait Synthesis:** develop an original adaptation from compatible known traits, requiring experimentation and stability.
- **Cognitive Partition:** late-stage independent processing channels; each channel consumes capacity and can be disrupted.
- **Perfect Recall:** retain learned data with defined capacity and provenance; not omniscience.

### J. Splitting, merging, and distributed body
- **Microbud:** shed a tiny piece for sampling or decoy use; low survival chance and biomass loss.
- **Controlled Split:** create a limited second body with divided mass, energy, and durability.
- **Remote Scout:** a sub-body explores nearby routes and returns evidence; range, signal, and vulnerability limits.
- **Dual-Vector Attack:** attack from two angles while attention is divided.
- **Sacrificial Decoy:** distract a threat at a permanent or recoverable mass cost.
- **Recombine:** reunite compatible parts; recovery is not guaranteed if a part is destroyed or contaminated.
- **Emergency Budding:** preserve a small fragment when a defined survival threshold is met; rare, costly, and not a universal extra life.
- **Multi-Body Coordination:** control several bodies only after cognitive evolution, with increasing coordination cost.
- **Distributed Core:** spread critical functions across several masses; reduces single-point failure but creates coordination vulnerabilities.
- **Collective Form:** combine several compatible allied slime organisms only with consent and a defined bond/merge rule; no forced permanent assimilation of sapient allies.
- **Mass Reconstitution:** recover a large body from surviving pieces only if sufficient viable biomass and energy remain.
- **Sovereign Colony:** late-game networked organism with bounded radius, communication delays, and identifiable nodes; not simultaneous omnipresence.

### K. Transformations and ultimate abilities
- **Dense Core Form:** compact, heavy, durable body for close combat.
- **Flow Form:** spread low and thin to move through tight routes, vulnerable to drying or area hazards.
- **Bulwark Form:** defensive mass distribution and ally shielding, slower movement.
- **Predator Form:** optimized tendrils, launch movement, and pursuit.
- **Aerial Form:** temporary lift/glide structures if acquired; energy-intensive.
- **Aquatic Form:** efficient fluid movement and pressure adaptation.
- **Elemental Mantle:** temporarily emphasizes one compatible elemental trait; increases output and strain.
- **Composite Form:** activate a stable set of fused traits with visible trade-offs.
- **Split Sovereign:** control multiple sub-bodies for a limited time; high cognitive and biomass burden.
- **Adaptive Apex Form:** switch among a small number of prevalidated responses during combat; cannot instantly invent counters.
- **Planetary Apex Form:** organism optimized for world-scale environmental challenges, not literal unlimited size.
- **Living Ship Form:** biological propulsion, shielding, life support, sensing, and navigation; requires prior planetary milestones.
- **Cosmic Interface Form:** interact with exotic environments under explicit survival constraints.
- **Null Sovereign Form:** final secret-boss form that uses the full system—absorption, shape control, fusions, counter-adaptation, split bodies, and arena interaction. Each phase has visible tells, resource demands, and windows to punish overextension.

## 7. Complete Evolution Atlas path and unlock gates

### Path I — Wake and survive
1. **Membrane Pulse** — unlock first movement.
2. **Contact Sense** — register nearby contact and pressure.
3. **Chemoreception I** — detect simple nutrient gradients.
4. **Particle Absorption** — collect safe micro-nutrients.
5. **Nutrient Core** — store limited energy.
6. **Membrane Seal** — slow moisture loss.
7. **Contract / Flatten** — evade a simple hazard and pass a narrow gap.
8. **First Trait Choice** — Current-Sensitive Membrane or Impact-Resistant Membrane. This early tutorial choice is recoverable.

### Path II — Feed and move
9. **Pulse Crawl** — controlled movement.
10. **Roll / Flow** — choose compact or low-profile travel.
11. **Selective Intake** — avoid known contaminants.
12. **Digestive Enzymes I** — process simple organic material.
13. **Biomass Conversion** — grow body mass.
14. **Adhesion I** — cling briefly to a surface.
15. **Elastic Damping** — survive small falls and impacts.
16. **Scent Memory** — remember a known food source.
17. **Emergency Retreat** — spend energy to burst away from danger.

### Path III — First defense and attack
18. **Damage Seal** — close small membrane injuries.
19. **Pseudopod I** — create a temporary striking/reaching lobe.
20. **Body Bump** — first reliable attack.
21. **Elastic Launch** — jump through compression/release.
22. **Gel Guard** — briefly harden surface.
23. **Toxin Isolation I** — safely test known low-grade hazards.
24. **Threat Signature I** — record one observed attack pattern.
25. **Counter Timing I** — unlock a timed recoil or dodge after observation.
26. **Engulf Small Target** — attempt absorption of eligible small organisms, with struggle risk.

### Path IV — Adapt and hunt
27. **External Digestion** — soften compatible material.
28. **Scent Tag** — track a marked target.
29. **Tendril I** — extend reach at lower impact strength.
30. **Adhesive Snare** — briefly slow a target.
31. **Acid / Enzyme Specialization** — choose corrosive offense or controlled digestion first; the other can be researched later.
32. **Gel Armor** — trade speed for protection.
33. **Thermal Sense** — detect heat cues.
34. **Vibration Map** — detect movement through suitable surfaces.
35. **Adaptive Combo I** — link movement, attack, and retreat.
36. **First Major Absorption** — earn one eligible biological trait through encounter evidence, analysis, digestion, and stabilization.

### Path V — Build identity and hybridization
37. **Trait Archive** — store analyzed trait blueprints.
38. **Compatibility Map** — preview conflicts before fusion.
39. **Trait Slot I** — maintain one active acquired adaptation.
40. **Fusion Stabilizer I** — fuse two compatible low-complexity traits.
41. **Saved Body Plan I** — record a valid form template.
42. **Pseudopod II** — maintain two controlled protrusions.
43. **Elemental Research I** — unlock a single discovered elemental route.
44. **Resistance Adaptation I** — partial protection from a studied threat.
45. **Ability Mastery I** — improve timing or control through use.
46. **Loadout Preset I** — save a combat configuration.

### Path VI — Intelligence and distributed body
47. **Distributed Sensory Web** — track multiple local cues.
48. **Pattern Learning II** — learn a second move pattern.
49. **Camouflage I** — blend with a suitable environment.
50. **Microbud** — shed a small decoy/sample at a biomass cost.
51. **Controlled Split** — unlock a fragile second body; both bodies share a finite resource budget.
52. **Remote Scout I** — sub-body returns local evidence within range.
53. **Recombine I** — reunite compatible pieces.
54. **Multi-Pseudopod** — increase controlled anatomy.
55. **Tactical Split Attention** — coordinate a limited second action.
56. **Trait Synthesis I** — create one tested hybrid adaptation from known compatible traits.

### Path VII — Apex combat
57. **Counter-Adaptation** — adjust to repeated attacks after a learning delay.
58. **Boss Breaker** — exploit a clearly telegraphed recovery or weak point.
59. **Elastic Counter II** — stronger counter with a force limit.
60. **Tendril Bind** — control a target briefly.
61. **Body Density Shift** — trade speed for anchoring or impact.
62. **Shape Memory II** — store multiple body plans.
63. **Composite Form** — activate a limited stable trait combination.
64. **Adaptive Combo II** — chain attack, defense, and movement.
65. **Emergency Core Shield** — protect vital structures by sacrificing outer mass.
66. **Apex Signature Ability** — one unique signature selected from the player's actual path, not a mandatory single best power.

### Path VIII — Sovereign and planetary evolution
67. **Advanced Fusion Regulator** — stabilize more complex combinations with increased upkeep.
68. **Multi-Body Coordination** — coordinate a bounded number of sub-bodies.
69. **Distributed Core** — reduce single-point failure while adding coordination weaknesses.
70. **Habitat Adaptation Suite** — prepare for extreme local environments.
71. **Territory Sensory Network** — read changes within a bounded region using credible cues.
72. **Ecological Interface** — interact with habitat recovery, resources, and local organisms.
73. **Planetary Survival Adaptations** — meet actual planet completion/survival prerequisites.
74. **Planetary Apex Form** — a transformation suited to planetary threats and large-scale environments.
75. **World-Scale Signature** — unlock only after a defined story and evolution milestone.

### Path IX — Living Ship and cosmic survival
76. **Vacuum Seal** — prevent immediate exposure failure, with finite endurance.
77. **Radiation / Energy Buffer** — tolerate a defined range of space hazards.
78. **Biological Propulsion** — move through space without conventional vehicles.
79. **Organic Navigation Sense** — navigate through learned celestial cues and instruments/organisms as defined by the world.
80. **Life-Support Metabolism** — recycle limited energy and matter.
81. **Living Ship Form** — transformation into a self-propelled organism; requires planetary progression.
82. **Cosmic Feeding** — process explicitly defined cosmic resources with severe overload risk.
83. **Exotic-Environment Adaptation** — survive specific anomalous zones after research.
84. **Dimensional Interface** — enter defined dimensional systems only after story gating.
85. **Reality Interaction** — limited, rule-bound effects with costs, range, and counterplay.

### Path X — Secret boss: Null Sovereign
86. **Perfect Trait Index** — access the archive of traits actually acquired or discovered by this character.
87. **Parallel Cognition** — maintain several controlled processes, limited by focus and disruption.
88. **Adaptive Phase Engine** — choose from prelearned counters after observing player behavior; no instant omniscience.
89. **Sovereign Reconstitution** — rebuild from viable mass under defined arena and resource rules.
90. **Null Mantle** — suppress or distort a narrow class of incoming effects for a short, telegraphed window; not universal immunity.
91. **Apex Fusion State** — activate a carefully chosen set of compatible traits at high stability/energy cost.
92. **Split-Crown Bodies** — create multiple boss bodies, each with a distinct readable role and shared finite resources.
93. **Arena Assimilation** — temporarily reshape selected arena features using available material; players receive tells and counterplay.
94. **Evolution Reversal Feint** — temporarily abandon a visible adaptation to bait a counter, then reconfigure; has a cooldown and cannot undo player progression.
95. **Null Sovereign: Final Form** — complete boss phase set, built from the same body, resource, counter, and adaptation rules used throughout the game.

These numbered nodes are a planning scaffold, not a final UI layout. Additional optional nodes and branches can be added after the first complete progression pass and playtest.

## 8. Secret-boss identity and encounter design

### Encounter premise
The Null Sovereign is the endpoint of the slime life path and a secret-boss test of whether the player understands absorption, adaptation, resource pressure, and combat tells. It should not simply have unlimited health or ignore every attack.

### Boss phases
1. **Assessment:** uses basic movement, pseudopod strikes, and defensive gel; reads player behavior through visible observation.
2. **Predator:** adds pursuit, tendril binds, acid/enzyme zones, and punishable launch attacks.
3. **Composite:** switches among a small set of announced body plans; each form has a clear strength and weakness.
4. **Split Crown:** separates into a few coordinated bodies with shared finite reserves. Disabling or forcing a merge creates openings.
5. **Adaptation Duel:** reacts to repeated player tactics after a delay. Alternating tactics, baiting, and breaking line/connection cues can defeat adaptation.
6. **Arena Assimilation:** changes parts of the arena with visible telegraphs. Players can interrupt a source, move to safe ground, or exploit unstable terrain.
7. **Null Sovereign:** combines prior mechanics, but every major defense has a readable condition, resource cost, duration, or counter. Final victory follows a fair vulnerability window, not a hidden instant-kill condition.

### Boss fairness rules
- Telegraph major attacks and phase transitions.
- No perfect response to every possible player build.
- Adaptation uses observed evidence, not player-only hidden data or omniscience.
- Counters take time to learn and can be baited.
- Never permanently kill a player or confiscate progression/assets through PvP.
- The secret-boss build can be more capable than a normal player build, but must obey legible resource and timing rules.
- If this boss is the narrative's ultimate body, tie its origin to the existing endgame consciousness/replica concept only after the story connection is deliberately approved.

## 8A. Secret ultimate skill: Absolute Nullification

**Purpose:** This is the slime's final defensive-offensive capstone. After mastering the connected defensive, resource-conversion, adaptation, and absorption branches, the slime can activate a state where all defined incoming hostile damage is nullified and converted into useful reserves. It is an earned, conditional endgame ability—not a passive buff available from the beginning.

### Core effect

When the ultimate is active and all activation conditions are satisfied, qualifying incoming damage causes **zero health loss**. Instead, the slime's core routes the absorbed attack into eligible resources:
- **Health / repair:** restores missing health or repairs viable body mass.
- **Mana / energy:** converts compatible energy, elemental, or spell-like attacks into power reserves.
- **Stamina:** converts compatible impact, momentum, and physical exertion into stamina.
- **Biomass:** recovers material from compatible physical or biological attacks when the correct trait is unlocked.
- **Stability / knowledge:** records unfamiliar attack signatures if the sensory and analysis branches are mastered.
- **Offensive charge:** stores surplus conversion for tendrils, counterattacks, pressure waves, or the final absorption sequence.

The general damage model does not need to be globally rebalanced. This skill changes how damage is handled by the slime; other characters' attacks continue to work normally against other targets.

### Conversion matrix

| Attack type | Main route | Required development |
|---|---|---|
| Blunt / kinetic melee | Stamina, kinetic charge, repair | Elastic damping and force routing |
| Cutting / piercing | Membrane repair, biomass if compatible | Membrane hardening and damage sealing |
| Physical projectiles | Momentum reserve, counterforce | Projectile observation and force routing |
| Energy beams / blasts | Energy or mana-like reserve | Energy buffer and energy routing |
| Elemental attacks | Matching elemental reserve | Acquired elemental trait and containment |
| Acid / corrosion | Corrosion buffer, repair reserve | Corrosion analysis and neutralizer |
| Poison / status damage | Detoxification and repair | Toxin isolation and status purge |
| Explosive / area damage | Distributed energy and impact routing | Multi-vector absorption and core shielding |
| Psychic / control effects | Specific cognitive/status protection | Relevant defensive branch; not covered by damage nullification alone |
| Gravity / dimensional / exotic attacks | Matching exotic reserve | Relevant late-game interface |
| Unknown or mixed attacks | Nullification plus signature analysis | Final capstone and trait archive |

At the final rank, every defined incoming damage class—including mixed and previously unseen types—is nullified during the active window. Non-damage effects such as forced movement, imprisonment, arena removal, or an objective are not automatically erased unless a separate ability explicitly covers them.

### Required skill-tree links

1. **Membrane Mastery:** Membrane Seal → Membrane Hardening → Reactive Membrane → Perfect Structural Response.
2. **Impact Conversion:** Elastic Damping → Elastic Counter → Force Routing → Kinetic Assimilation.
3. **Core Recovery:** Nutrient Core → Damage Seal → Regeneration → Emergency Core Shield → Core Reconstitution.
4. **Energy Conversion:** Energy Buffer → Elemental Containment → Energy Routing → Multi-Channel Conversion.
5. **Trait Knowledge:** Threat Signature Archive → Compatibility Map → Counter-Adaptation → Unknown-Signature Analysis.
6. **Stability and Control:** Fusion Stabilizer → Advanced Fusion Regulator → Parallel Cognition → Null-State Control.
7. **Offensive Absorption:** Engulf → Adhesive Snare / Tendril Bind → Absorption Preparation → Sovereign Capture.
8. **Capstone:** **Absolute Nullification** → **Null Sovereign: Unanswerable State**.

These are linked progression prerequisites, not final numeric costs. Exact level gates, points, duration, and resource values require prototyping.

### Activation and resource rules

- The slime must be in a compatible body form with its core and membrane systems online.
- Required defensive and offensive branches must be unlocked and configured as specified by the final build.
- The core needs a minimum starting reserve and sufficient stability.
- The player deliberately activates the state; the startup has a readable animation and cue.
- While active, qualifying damage is nullified and routed to health, energy, stamina, biomass, analysis, or offensive charge according to a documented priority.
- Each resource has a cap. When full, its share routes to another eligible reserve or dissipates harmlessly; repeated weak attacks cannot generate infinite resources.
- The active state ends at its stated duration, when its reserve is spent, or when the player cancels it. A visible cooldown/recovery period follows.
- Fully mastering the skill can improve conversion and shorten setup, but permanent uninterrupted uptime is not assumed unless explicitly approved as a separate endgame rule.

**Design promise:** once properly unlocked and activated, the slime cannot be defeated by simply increasing damage, changing damage type, stacking damage-over-time, or repeating attacks. Those attacks feed the slime instead. The ability's activation window and resource limits are explicit; it does not require changing everyone else's base damage.

### Offensive link: Absorption Preparation → Sovereign Capture

1. **Receive:** stand still or hold position while qualifying attacks are nullified.
2. **Classify:** analyze signatures that the current build can understand.
3. **Charge:** convert incoming force into reserves and an offensive absorption meter.
4. **Prepare:** tendrils or an adhesive field telegraph the target entering capture range.
5. **Bind:** a successful, clearly signaled move briefly restricts the target.
6. **Sovereign Capture:** attempt to engulf an eligible target, subject to size, resistance, interruption, and story rules.
7. **Resolve:** award only validated material, knowledge, or trait rewards; sapient beings are not ordinary loot or ingredients.

### Secret-boss presentation

The Null Sovereign may stand motionless while the player attacks. A distinctive core/membrane effect, animation, sound cue, and resource feedback show attacks being absorbed rather than dealing damage. The boss then prepares a tendril bind, arena-control move, or capture attempt. Its timing and rules remain consistent and learnable.

### Acceptance tests

- Every defined attack class has a documented conversion route.
- During the fully qualified active window, qualifying attacks cause no health loss, including mixed or unfamiliar damage types.
- Resource caps and overflow rules prevent infinite-resource loops.
- The skill clearly explains missing prerequisites and never silently fails to activate.
- The active window and recovery period are communicated to the player.
- Bind/capture attacks are telegraphed and have a defined escape, interrupt, or objective response.
- The same classification and conversion rules support the player build and secret-boss version.
- PvP protections remain unchanged: no permanent player death and no theft of assets or progression.

**Implementation status:** Design-only. Damage routing, skill nodes, status classification, UI, and boss logic have not been implemented or tested.

## 9. Weaknesses and counterplay catalogue

| Weakness | Why it matters | Counterplay / adaptation |
|---|---|---|
| Desiccation | Membrane loses flexibility and cohesion | Moisture route, seal, water storage, shade |
| Extreme heat | Overloads thermal buffer and damages gel | Vent heat, change route, heat-resistant trait |
| Extreme cold | Reduces flow and can make the body brittle | Cryoprotectant, thermal source, controlled retreat |
| Piercing / cutting | Concentrated damage can bypass blunt damping | Hardening, angle change, decoy, counter |
| Toxins | Unknown compounds can corrupt metabolism | Sample cautiously, isolate, purify, retreat |
| Corrosives | Can damage the membrane or stored structures | Neutralizer, resistant layer, avoid prolonged exposure |
| Electrical conduction | Wet/conductive body can transmit current | Grounding, insulation, split route, avoid conductive pools |
| Low biomass | Limits repair, armor, split bodies, and constructs | Feed safely, conserve mass, recombine |
| Low energy | Weakens movement and active abilities | Reduce active effects, use efficient movement, recover |
| Fusion instability | Incompatible traits degrade performance | Disable one trait, stabilize, use saved safe build |
| Divided attention | Multiple bodies are harder to coordinate | Recombine, reduce sub-bodies, use prepared tactics |
| Sensory deception | Decoys and noisy terrain mislead perception | Cross-check cues, test hypotheses, observe |
| Adaptation delay | Repeated attacks may be countered only after observation | Vary attacks, bait the wrong response, exploit transition |
| Mass / size constraints | Large forms cannot enter every route | Save compact form, change body plan, use alternate route |
| Energy / exotic overload | Cosmic powers strain containment | Vent, interrupt, shorten exposure, exploit cooldown |
| Cognitive disruption | Distributed control can be confused or interrupted | Simplify active processes and protect key nodes |

No weakness must make the slime helpless. Each should create a decision and allow preparation, adaptation, or counterplay.

## 10. Signature progression examples

### Example A: Predatory gel
Adhesion → Pseudopod → Elastic Launch → Tendril Bind → Scent Tag → Adaptive Combo → Predator Form → Apex Signature.

Strength: pursuit, close-range control, punish windows. Trade-off: vulnerable when overextended and when targets deny close contact.

### Example B: Fortress gel
Impact-Resistant Membrane → Elastic Damping → Gel Armor → Emergency Core Shield → Density Shift → Bulwark Form → Distributed Core.

Strength: survival, body-blocking, counterattacks. Trade-off: slower movement, high mass and repair costs.

### Example C: Elemental synthesizer
Chemoreception → Elemental Research → Trait Archive → Compatibility Map → Fusion Stabilizer → Elemental Mantle → Composite Form.

Strength: situational damage and environmental interaction. Trade-off: resource and stability management; no universal elemental immunity.

### Example D: Phantom scout
Scent Memory → Vibration Map → Camouflage → Microbud → Remote Scout → Tactical Split Attention → Split Sovereign.

Strength: scouting, deception, multi-angle pressure. Trade-off: divided durability, biomass, and attention.

### Example E: Null Sovereign
Trait Index → Parallel Cognition → Adaptive Phase Engine → Apex Fusion State → Split-Crown Bodies → Arena Assimilation → Final Form.

Strength: versatile encounter control. Trade-off: finite shared reserves, visible phase windows, and punishable adaptation transitions.

## 11. Appearance and animation evolution

- **Dormant cell:** almost featureless translucent membrane; tiny internal pulse.
- **Primitive slime:** simple rounded mass; surface ripples communicate intention.
- **Adaptive gel:** clearer internal core and visible membrane response to temperature, damage, and feeding.
- **Hunter slime:** deliberate pseudopods, tendrils, compressed launch silhouette; no required humanoid face.
- **Composite slime:** different materials/traits remain visually readable through distinct surface patterns, internal particles, and localized effects.
- **Intelligent slime:** controlled sensory ripples, deliberate decoys, and coordinated sub-body movement.
- **Apex slime:** stable signature silhouette with multiple possible body plans; power is expressed through anticipation and precise shape control rather than constant visual noise.
- **Planetary apex:** environmental scale and movement communicate power without requiring arbitrary gigantic size in every scene.
- **Living Ship:** a continuous organic silhouette with propulsion, sensing, and protection integrated into the body.
- **Null Sovereign:** elegant, controlled, deceptively simple outer shape with internal signs of many mastered systems. Its visual changes telegraph the active trait and upcoming attack.

Accessibility: important attack tells cannot rely on color alone; use shape, motion, sound, and timing cues. Keep effects readable in busy combat.

## 12. Animation and input requirements

- Limbless locomotion must feel responsive, not like a humanoid sliding without legs.
- Inputs should map to intent: move/flow, evade, primary body attack, absorb/interact, ability slots, form switch, and lock-on/target focus.
- Contextual pseudopods may emerge automatically for an equipped move, but the player retains control over attack choice and timing.
- Shape changes need clear anticipation, active window, and recovery.
- Splitting/merging must communicate which body is controlled and how resources are divided.
- The UI must show current body plan, active traits, resource levels, stability, and disabled powers.
- Deep build planning occurs in the Evolution Atlas, not through mandatory menu navigation during active combat.

## 13. Implementation order and acceptance gates

### Phase A — First playable slime
1. Slime movement physics: pulse, roll, flatten, compression.
2. Absorb safe resources and grow a visible meter.
3. Basic sensory cue and hazard awareness.
4. Dodge/escape, body bump, and recoverable tutorial failure.
5. One early trait choice with clear differences.
6. Save/load for the character's current form and first trait.

### Phase B — Combat and body systems
7. Pseudopod, adhesion, elastic launch, damage seal.
8. Biomass, energy, stability, and visible overload behavior.
9. One predator/prey interaction and one boss-style telegraph.
10. Ability unlocks, prerequisites, and use-based mastery.
11. First elemental/material trait and one valid fusion.
12. Test controller, keyboard, accessibility, and combat readability.

### Phase C — Full evolutionary architecture
13. Trait archive and compatibility rules.
14. Body plan loadouts, respec, preview, and persistence.
15. Splitting, scouting, merging, and cognitive limits.
16. Environmental adaptation and world persistence.
17. Advanced forms and planetary milestone.
18. Living Ship biology and cosmic survival as later project milestones.

### Phase D — Secret boss
19. Build the Null Sovereign using the same trait and resource definitions.
20. Implement boss phase state machine, telegraphs, adaptation delay, and vulnerability windows.
21. Test against multiple player builds and tactics.
22. Validate save/load, performance, multiplayer authority, and anti-exploit rules.
23. Final boss tuning only after earlier systems are stable.

### Acceptance criteria
- A player can understand and control the slime before it gains limbs or humanoid features.
- Each ability lists unlock requirements, effect, cost, limitations, and counterplay.
- The character can move, feed, survive, fight, and recover using a coherent limbless body model.
- Absorbing a target never silently grants all its abilities.
- Trait combinations are validated and unstable combinations fail safely with an explanation.
- Split bodies share finite resources and can be tracked, controlled, and recombined consistently.
- Learned traits, discoveries, mastery, loadouts, and evolution history survive save/load.
- The Null Sovereign demonstrates every major system without becoming immune to counterplay.
- The character path is a reusable template for defining other species, not a reason to give every species identical mechanics.

## 14. Open decisions before final balance

These require prototype evidence and should not be invented as finished numbers:
- Exact numerical stats, ability damage, cooldowns, resource costs, and stage thresholds.
- Number of active trait slots by stage.
- Exact number of simultaneously controlled sub-bodies.
- Respec cost and restrictions.
- Which rare traits are permanent versus reversible.
- The slime's canonical name, origin, voice/personality, and visual motif.
- Whether the secret-boss encounter is the narrator's replica, an earlier failed vessel, the original slime, or a separate entity.
- Which cosmic/reality powers fit the final story and how their rules are constrained.
- Final list of all discoverable trait templates after playtesting.

## 15. Research notes: broad genre patterns

These public game descriptions and guides demonstrate several distinct slime mechanics that inform the *category* of design—not a license to reproduce any game's exact content:
- [Slime Evolution (Steam)](https://store.steampowered.com/app/2214010/) describes growth through eating resources, fighting monsters, and choosing among elemental paths.
- [Prime Slime (itch.io)](https://yrgo.itch.io/prime-slime) describes absorbing elemental orbs to gain abilities and using an elemental interaction hierarchy.
- [Slime:Evo (Steam community)](https://steamcommunity.com/app/1683060) describes an evolving slime learning attacks and dodges.
- [Slime King (itch.io)](https://whiteslime.itch.io/the-slime-king) describes staged evolution, elemental abilities, environmental traversal, and allied slimes.
- [Ambition of the Slimes strategy guide (GameFAQs)](https://gamefaqs.gamespot.com/pc/232549/ambition-of-the-slimes/faqs/79840) discusses splitting mechanics and the trade-off of dividing durability.
- [Slime Evolution design reference (Steam)](https://store.steampowered.com/app/2214010/) also illustrates survival pressure from stronger enemies as the slime grows.
- Additional community/mod descriptions discuss digestion, regeneration, acid, shielding, and multi-role abilities; these are useful as broad mechanic categories but are not treated as authoritative or copied verbatim.

This reference list is illustrative, not exhaustive. The original ability taxonomy above is intended to be expanded through systematic research and design review.

---
**Implementation status:** Design specification only. No abilities, animations, skill nodes, boss logic, saving, or balance are claimed to be implemented or tested.
