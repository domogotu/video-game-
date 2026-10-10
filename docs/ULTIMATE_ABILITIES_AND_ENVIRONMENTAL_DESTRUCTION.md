# Ultimate Abilities and Persistent Environmental Impact

**Status:** Design specification only; not implemented or tested.

## Core requirement

Lethal Absorption must treat the environment as part of combat. As an ability gains levels, mastery, compatible traits, mutations, synthesis stages, and evolutionary support, its impact can increase in scale and persistence—not only in direct target damage.

A maxed ability should feel meaningfully more powerful through a combination of reach, force, environmental interaction, duration, complexity, and world consequences. The scale must still follow the ability's nature: a perfected stealth, healing, control, or precision ability need not become a larger explosion.

## Environmental impact tiers

These tiers describe potential scope, not a universal level-to-destruction formula.

1. **Localized:** scorch marks, frost, displaced debris, damaged props, small craters, broken weak objects, moved foliage, and brief elemental residue.
2. **Encounter:** cracked floors, breached eligible walls, toppled trees, spread fire, localized flooding, ice sheets, smoke, toxic clouds, debris hazards, and altered cover.
3. **Battlefield:** collapsed eligible structures, blocked or opened routes, trenches and craters, redirected water, persistent storms, widespread fire or frost, unstable ground, and chained environmental reactions.
4. **Regional:** large landslides, major flood paths, wildfire fronts, prolonged storms, extensive terrain scars, changed local ecosystems, and persistent strategic map consequences.
5. **Planetary / transcendent:** only for powers, forms, and story milestones explicitly capable of this scale; possible continental devastation, major geological disruption, atmospheric effects, or other planet-level consequences. These are rare, expensive, telegraphed, and governed by world-state and narrative rules.

A power does not advance to a higher tier just because its numeric ability level is high. Its defined effect family, mastery, form, recipe, resources, target material, and world rules must support the result.

## Ability progression and maximum potential

Track separately:
- **Ability level:** expands a defined technique's capabilities and upgrade choices.
- **Mastery:** improves precision, efficiency, reliability, timing, control, and advanced applications.
- **Power development:** increases source capacity and shaping/control.
- **Mutation and traits:** enable anatomy, resistance, stabilization, or environmental adaptations.
- **Synthesis / weaving:** changes the interaction between compatible components and may create a new effect family.
- **Form / evolution:** permits higher output ceilings or larger-scale techniques where appropriate.
- **Ultimate authorization:** explicit prerequisites, resource burden, cooldown/recovery, and world-scale permission for rare high-impact effects.

Maximum level should unlock a technique's designed potential, not unlimited power. Further improvement can change behavior and environmental reach rather than simply multiplying damage without limit.

## Elemental and physical examples

- **Fire:** singes vegetation at low levels; ignites eligible objects at advanced levels; spreads according to fuel, wind, moisture, and containment at high levels; can create large fire fronts only when the environment and power tier support them.
- **Water / ice:** freezes puddles or surfaces; forms slippery zones and barriers; redirects local flows or creates flood hazards; large-scale flooding requires actual water, terrain, and a defined source of force.
- **Wind:** moves loose objects and disrupts aim; pushes targets and projectiles; breaks eligible structures or uproots trees at high force; major storms need sustained output and atmospheric conditions or an explicitly supernatural source.
- **Lightning / energy:** strikes targets and conductive objects; damages equipment and eligible structures; overloads connected systems or starts fires when supported by the simulation; regional effects require an appropriate ultimate source.
- **Earth / impact:** cracks surfaces; breaks weak walls and creates cover-changing craters; triggers local collapses or landslides when terrain stability supports it; planetary-scale geological effects are reserved for explicit transcendent powers.
- **Poison / spores / biological powers:** contaminate defined areas, affect organisms according to resistance, and alter local ecology only under tracked spread and persistence rules. Avoid instant, unlimited ecosystem takeover.
- **Gravity / telekinesis:** moves small objects; throws heavy debris; crushes or displaces eligible structures; high-tier area control can alter movement and cover without requiring every effect to be an explosion.
- **Shadow / spatial powers:** create movement paths, zones, or localized distortions; advanced forms may affect larger areas or battlefield positioning. Their impact should remain distinctive rather than being reduced to generic destruction.
- **Healing / protection / creation:** high mastery may restore terrain, erect large barriers, stabilize structures, redirect hazards, or create lasting safe zones. Maximum power is expressed by scale and persistence, not destruction alone.

## Physical world response

Each destructible object or terrain class needs material properties and a response profile: hardness/strength, mass, damage thresholds, resistance, structural dependencies, flammability, conductivity, permeability, and repair or regeneration behavior where relevant.

Environmental effects should support:
- Impact deformation, cracks, breakage, collapse, and debris.
- Heat, burning, smoke, steam, melting, and ignition.
- Cold, freezing, brittleness, and thawing.
- Wind pressure, displacement, projectile deflection, and falling objects.
- Water movement, erosion, flooding, buoyancy, and drying.
- Electrical conduction, overload, and secondary ignition.
- Toxic/biological spread with bounded exposure and persistence.
- Gravity, force, pressure, and spatial effects when supported by the ability.
- Persistent scars and hazards that can affect later traversal, combat, NPC behavior, and resource availability.

Do not promise universal real-time destruction of every surface. Define material classes, simulation budgets, destructibility boundaries, and fallbacks. The visual effect, collision state, navigation, and server world-state must agree.

## Chain reactions and combination effects

Environmental combinations should be authored and bounded:
- Fire + Wind can intensify spread or redirect flame if fuel and conditions permit.
- Fire + Water can produce steam, suppress flames, or create a thermal-pressure effect only when the recipe defines it.
- Water + Electricity can create a conductivity hazard under explicit rules and counterplay.
- Ice + Impact can fracture frozen surfaces or alter footing.
- Wind + debris can create projectile hazards with mass, range, and damage limits.
- Earth + Water can destabilize slopes or create mud only where material and terrain allow.
- Ultimate combinations may trigger multi-step reactions, but every step needs clear prerequisites, limits, costs, and interrupt/counter opportunities.

Use the registered ability-weaving system. Four components are not four unlimited effects fired simultaneously; the output is a validated recipe with defined stages and a single current output.

## Costs, telegraphs, and counterplay

The more world-altering an effect is, the more carefully its risk must be specified:
- Biomass, energy, stamina, charge, rare resources, or other appropriate costs.
- Startup, charge time, cooldown, recovery, and potential self-exposure.
- Visible or audible telegraphs appropriate to the ability.
- Interruptions, escape routes, resistance, cover, counter-elements, grounding, insulation, suppression, or other ability-specific answers.
- Consequences for allies, neutral NPCs, player structures, objectives, and the user.
- Defined limits on repeat casting, overlapping persistent effects, and resource generation from destruction.

Costs should fit the fiction and progression; avoid a single generic penalty applied to every ability.

## Persistence and world ownership

The world must distinguish:
- Short-lived combat effects.
- Encounter-persistent hazards.
- Persistent structural damage or terrain changes.
- Strategic regional changes.
- Rare narrative/planetary changes.

World changes must be authoritative, saved where intended, and replicated consistently. The game must define who can cause permanent changes, who can repair them, how changes affect shared navigation and objectives, and whether they reset at a world lifecycle boundary. Do not allow players to grief protected areas or permanently erase required content without explicit world rules.

NPCs should respond based on what they could observe or investigate; they must not gain magical omniscience. Ecological effects need bounded propagation, recovery, and resource consequences. Server performance must be protected with spatial limits, effect budgets, aggregation, and deterministic rules where feasible.

## Multiplayer fairness and safeguards

- Server validates ability level, mastery, form, recipe, resources, cooldown, area, targets, and world effects.
- Clients cannot dictate final damage, destruction, or persistent world state.
- Competitive modes require readable telegraphs, consistent collision, counterplay, and defined limits on map-altering effects.
- Protect spawn areas, required traversal routes, mission-critical objects, and consent-controlled spaces through explicit rules.
- Handle overlapping attacks and chain reactions without multiplying damage or effects unintentionally.
- Include performance caps and graceful degradation for large battles; presentation may simplify, but authoritative outcomes must remain consistent.

## UI and player feedback

Before activation, show or communicate the expected footprint, affected material types, cost, duration/persistence class, allied/neutral impact, and major risks when the ability is charged or world-altering. The preview is an estimate when the result depends on dynamic material or weather conditions; do not promise exact outcomes where the simulation cannot guarantee them.

After activation, show the cause-and-effect chain clearly enough for players to understand why terrain, structures, hazards, and NPCs changed. The Evolution Atlas should record discovered environmental interactions and their prerequisites without granting missing powers or mastery.

## Acceptance criteria for the first implementation slice

Before broad rollout, implement and verify a small controlled sample:
1. One destructible material class and one indestructible boundary.
2. One low-level ability that causes localized impact.
3. One mastered/ultimate version with visibly larger, persistent environmental consequences.
4. One elemental combination that produces a defined chain reaction.
5. One incompatible combination that fails safely with clear feedback.
6. Collision, navigation, visual effects, and authoritative world state remain synchronized.
7. Costs, cooldowns, interruption, counterplay, and environmental persistence are validated.
8. NPC and multiplayer behavior, protected areas, and performance limits are tested.
9. Save/load or world persistence behavior is verified for each intended persistence class.
10. Automated tests and a reproducible runtime/playtest record are stored before marking the feature tested or verified.

## Status policy

This is a design specification only. Do not describe environmental destruction, ultimate abilities, persistent terrain deformation, chain reactions, or these tests as implemented until code and test evidence exist.
