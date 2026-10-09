# Character-Specific Powers, Traits, and Unlock Requirements

**Status:** Approved product requirement for design and content planning. The game remains design-stage; this document does not claim implementation.

## Non-negotiable requirement

The six requested character routes must not be reduced to generic archetypes or loose inspiration. The intended experience is to have a dedicated progression route for each named character, with a character-specific ability and trait catalogue, unlock conditions, passives, active abilities, transformations/forms, upgrades, and late-game powers. The design must preserve the user's stated requirement that the actual requested character-specific power sets are represented in the game.

**Requested characters/routes**
1. Sung Jinwoo — *Solo Leveling* and relevant game adaptations.
2. Goku — *Dragon Ball* anime/show and relevant games.
3. The central goblin protagonist from *Re:Monster* (Gobrou/Rou; verify the intended adaptation/name before content is finalized).
4. Sun Wukong — mythic source material and the specific Wukong games/adaptations the project chooses to reference.
5. Rimuru Tempest — *That Time I Got Reincarnated as a Slime* anime/show and relevant games.
6. Ainz Ooal Gown — *Overlord* anime/show and relevant games.

For each route, the content team must create a source-by-source inventory of the powers, traits, passives, skills, transformations/forms, equipment-linked techniques, summons, resistances, and evolution states the user expects. Do not treat a broad family label such as “energy attack” or “shadow power” as satisfying the requirement by itself.

## Required character-specific catalogue structure

Each route must have:
- A source/version register stating which anime seasons, films, game titles, and/or official references are in scope.
- An individual row for every in-scope ability, passive trait, skill, transformation/form, and meaningful upgrade.
- The source character's name for internal traceability, plus an in-game availability status.
- Acquisition method: starting selection, story unlock, action-gated discovery, training, absorption, evolution, quest/trial, equipment, or mastery.
- Prerequisites, exact route/form dependencies, and whether it is active, passive, conditional, or transformation-bound.
- Gameplay effect, cost/upkeep, range, duration, startup/recovery, counterplay, and compatibility.
- Upgrade/evolution chain and interactions with other abilities.
- Implementation status: not specified, specified, prototyped, implemented, or tested, with evidence required for status changes.

## Route completeness checklist

### Sung Jinwoo — Shadow Sovereign route
Track the character-specific shadow extraction/army and command progression, shadow soldiers and their roles, shadow storage/recall and movement, combat and dagger techniques, stealth/perception, growth and rank progression, monarch/sovereign powers, and relevant forms/upgrades from the chosen official sources. Individual shadows and named techniques should be separately catalogued when in scope; “summons” alone is not enough.

### Goku — Saiyan / martial-artist route
Track the source-specific martial techniques, ki sensing/control, signature energy attacks, flight and high-speed movement, defensive and counter techniques, transformations and their variants, Ultra Instinct-related states/techniques where in scope, recovery/strain trade-offs, and training-driven improvements. Treat forms and named techniques as separate entries rather than one generic “power-up.”

### Re:Monster goblin protagonist — adaptive evolution route
Track the protagonist's goblin-to-higher-lineage evolution, absorption/consumption-derived abilities, acquired skills and resistances, learned combat/crafting/survival capabilities, named evolutions and major skill upgrades, and the progression logic from the selected anime/show and official game sources. Confirm source-specific spelling and adaptation scope before treating any name as canonical.

### Sun Wukong — mythic staff route
Track the chosen source version(s) explicitly. Inventory the relevant staff techniques, shape/size manipulation, mobility, transformation/disguise abilities, duplicates/clone techniques, cloud/sky traversal, enhanced physical traits, supernatural resistances, and mythic forms/powers included in the selected source. Distinguish classical myth, television/anime portrayals, and individual games rather than merging their versions into one supposedly canonical list.

### Rimuru Tempest — adaptive slime route
Track analysis/appraisal, predation/absorption, storage and internal-space functions, skill acquisition and synthesis, unique/ultimate skill progression, resistances, body/form changes, magic/elemental abilities, barriers, clones/parallel processing, summons/servants where applicable, and later evolution states from the chosen official sources. Each skill and evolution upgrade must be an individual catalogue entry.

### Ainz Ooal Gown — undead spell sovereign route
Track the source-specific spell catalogue, spell tiers, preparation/casting limits, summons and undead servants, buffs/debuffs, barriers/resistances, instant-death and control effects where applicable, equipment-linked abilities, rituals/domain effects, racial/class traits, and forms/states from the chosen official sources. Distinguish known spells, prepared spells, equipped effects, passive traits, and actually castable abilities.

## Availability requirement

The project plan must not quietly demote these routes to optional generic inspiration. Each route must be planned as a specific character-content package and included in the roster/content roadmap. The game may stage delivery across releases, but every deferred entry must remain tracked, with an explicit reason and planned milestone. If exact franchise characters, names, visuals, dialogue, or signature expression are to appear commercially, the project must establish appropriate rights/licensing or use a separately approved original adaptation; do not assume permission exists.

## Acceptance criteria

A route is considered **content-specified** only when:
1. The source/version scope is recorded.
2. The route-specific ability/trait/form inventory is complete against that scope.
3. Each entry has acquisition/unlock rules and gameplay behavior.
4. Cross-ability interactions and balance/counterplay are specified.
5. The route appears in the README, roster, and Game Design Bible.
6. Missing, disputed, version-specific, or unverified powers are explicitly marked rather than guessed.

A route is considered **implemented** only when the corresponding game code/content exists. It is considered **tested** only after recorded test evidence. Documentation alone is not implementation.

## Current status

This file locks the product requirement and defines how to satisfy it. The six routes still need a source-by-source canonical inventory and the actual gameplay implementation. Do not claim that all exact abilities are already in the playable game.
