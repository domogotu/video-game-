# Ability Weaving and Multi-Tree Progression

**Status:** Design specification only; not implemented or tested.

## Required progression trees

Lethal Absorption uses connected, distinct trees:
- **Skill Tree:** technique, timing, movement, crafting, and execution.
- **Ability Tree:** learned active actions and variants.
- **Power Tree:** elemental/supernatural sources, domains, and power control.
- **Mutation Tree:** anatomy, organs, body plans, resistances, and biological trade-offs.
- **Trait Tree / Trait Ledger:** passive properties, compatibility, expression, stabilization, and suppression.
- **Mastery Tree:** improvements earned through successful use in varied contexts.
- **Synthesis Tree:** recipes that combine compatible abilities, powers, mutations, and traits.
- **Form / Evolution Tree:** transformations, lineage branches, form-specific slots, and stage progression.

The trees must interact, but players should always be able to tell whether they are learning a technique, gaining a power source, changing anatomy, acquiring a passive trait, mastering use, or synthesizing a new result.

## Four-component ability set

A player may assign up to **four compatible abilities, powers, or traits to one input set**. Example: hold **LT** and press **X**. The combination is a registered “weave” with up to four ingredients/stages. It does not mean all four attacks fire at once. It produces one resulting technique at a time, with clear cost, startup, recovery, and counters.

Illustrative elemental progression:
1. **One component — Fire:** LT+X emits a basic fire attack.
2. **Two components — Fire + a learned fire-refinement ability:** produces a refined flame with improved control, density, or delivery.
3. **Three components — refined Fire + Wind:** produces a wind-fed flame with changed range, spread, travel, or pressure.
4. **Four components — Fire + refinement + Wind + Water:** may produce a steam/thermal-pressure reaction if the recipe is compatible. If not compatible, the recipe can fail, destabilize, or require another ingredient/order.

Adding ingredients does not automatically mean more damage. A later stage might add control, mobility, defense, efficiency, or a status interaction. A fourth component can conflict, require a stabilizing trait, or produce a different branch. Repeating Fire requires a distinct learned refinement/amplification component; it cannot be counted twice for free.

## Input and UI

- **LT held + X tap:** activate the selected/base weave output.
- **LT held + X charge:** advance to a higher stage only when the registered recipe supports charging and the player has resources.
- Optional alternate branches may use timing, sequential taps, directional input, target context, terrain, or current form; exact controller mapping remains configurable.
- UI previews show the ingredients, current and next stage, expected output, cost, compatibility warnings, and cancel path.
- Provide remapping and accessible alternatives to charge timing; support controller and keyboard/mouse without requiring frame-perfect inputs for basic use.

## Learning through use

New techniques and recipes can be discovered through meaningful use as well as through menus. Evidence can include repeated controlled use, successful combinations, trying abilities in varied environments, solving a combat/traversal problem, adapting to a counter, analysis, research, mentor guidance, or an evolution trial.

Learning stages:
1. **Exposure:** observe or attempt the interaction.
2. **Hypothesis:** the system records a plausible recipe.
3. **Discovery:** perform a qualifying sequence or complete a trial.
4. **Stabilization:** practice or pay required resources/materials/biomass.
5. **Mastery:** successful use improves reliability, efficiency, control, or branch options.
6. **Synthesis/evolution:** milestones unlock new recipes, traits, variants, or form-specific techniques.

Use alone does not instantly grant every power. The Evolution Atlas can show clues and ingredients without granting the personal unlock. Shared Discovery shares verified knowledge, not a player's mastery or unlock ownership.

## Recipe record requirements

Every weave must define ingredients and order; required power source, trait, mutation, form, and mastery; input gesture and stage selection; outputs and branch conditions; costs, cooldown/recovery, range/area/duration; failure, interruption, overload, and incompatibility; counters, PvP rules, environmental and NPC effects; discovery clues; and test cases.

More complex recipes need meaningful costs, startup, risk, or counter windows. Anatomy, resource limits, permanent-death rules, and server-side validation still apply. In multiplayer, the server validates learned recipe, stage, timing, resources, cooldown, and effects. Use curated recipes and bounded interaction rules rather than allowing unlimited combinatorial exploits.

## How trees interact

- Skill Tree: timing windows, cancel routes, stance options, and combo control.
- Ability Tree: base techniques and active variants.
- Power Tree: energy shaping, source control, and elemental reactions.
- Mutation Tree: body-dependent delivery, organs, resistance, and physical forms.
- Trait Tree/Ledger: passive modifiers, compatibility, stabilization, and suppression.
- Mastery Tree: execution improvements and use-earned branches.
- Synthesis Tree: discovered recipes and upgrades.
- Evolution Tree: major form changes, new capacity, and late-game tiers.

Players must be able to inspect why an ability is locked and which tree, trait, form, action, or mastery is missing.

## Initial acceptance scope

Before expanding broadly, specify and test one complete four-stage elemental weave, one incompatible recipe, trait stabilization, use-based discovery, UI feedback, accessibility alternatives, and server-authoritative validation. Expand the recipe library in staged groups while keeping deferred content tracked.

**Status:** design specification only. No controller behavior, skill trees, emergent abilities, or runtime tests are claimed implemented.
