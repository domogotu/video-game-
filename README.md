# Lethal Absorption

**Tagline:** *Consume. Evolve. Survive.*

Lethal Absorption is an original open-world multiplayer action RPG concept in which a player begins as a single cell and evolves through increasingly complex life, superhuman forms, planetary apexes, cosmic entities, and potentially godlike existence. What the player consumes, studies, survives, creates, and masters shapes their body, abilities, and available evolution paths.

> **Project status:** This repository currently stores the game’s design documentation. The design systems described here are proposals/specifications, not claims that a playable game or these systems have been implemented or verified.

## Core pillars

- **The Evolution Atlas:** one massive, history-sensitive progression system spanning cellular biology through cosmic and reality-altering powers.
- **No fixed classes:** anatomy, abilities, mutations, discoveries, diet, environment, and player choices define each build.
- **Character identity and development:** body plan, evolution history, saved forms, active traits, and readable strengths/trade-offs create distinct characters.
- **Free-flow combat:** chain melee, weapons, powers, mobility, defense, summons, transformations, ultimates, and player-discovered combinations.
- **Adaptive body-as-weapon:** a modular Anatomy Workshop lets compatible limbs, organs, armor, senses, wings, tails, tendrils, and other evolved parts change combat and movement; the design is documented but not implemented.
- **Reactive persistent worlds:** ecosystems, NPCs, structures, wounds, evidence, environmental damage, plant growth, repairs, and recovery can continue after players leave.
- **Meaningful hunting:** stalking, pursuit, witness awareness, catch security, carrying, specimen preservation, and absorption circumstances can unlock rare evolutionary opportunities.
- **Dominance and investigation:** creatures and communities remember credible encounters, assess threats, and investigate evidence without magical omniscience.
- **Permanent character death:** a dead character starts over; stored research can guide a new life but cannot resurrect the old character.
- **High-stakes PvP and cooperative Resonance Fusion:** explicit lethal challenges can transfer eligible traits; compatible co-op abilities can form enhanced techniques.
- **Planetary-to-cosmic progression:** planetary completion and biological survival capabilities are required before space travel. There are no vehicles or conventional spaceships; the player evolves into a Living Ship Form.

## Progression overview

The proposed normal character-level range is **1–1050**, separate from ability levels, evolutionary paths, and mastery. Completing the main story unlocks NG+ immediately. Proposed stage bands are cellular survival (1–25), primitive creature (26–100), apex organism (101–200), sapient evolution (201–350), superhuman evolution (351–500), planetary apex (501–650), cosmic adaptation (651–800), cosmic entity (801–950), and transcendent being (951–1050). Exact experience curves and balance remain open.

The Stage V superhuman form is the visual and scale baseline for ordinary player combat. Standard forms should be comparably sized even when their anatomy is alien. Optional Battle Mode expands the character according to evolved biology; Titan Form is intended for dedicated large-scale encounters. Level alone does not make a much larger character automatically win.

## Key systems

| System | Purpose |
|---|---|
| Character profile & evolution history | Track current anatomy, active/inactive traits, forms, adaptations, and major changes |
| Modular anatomy workshop | Open-ended mix-and-match anatomy builds with data-driven part interactions, compatibility previews, trade-offs, and combat effects |
| Evolution Atlas | Discover and plan biology, abilities, fusion, transformations, and cosmic evolution |
| Ability growth | Individual ability levels, specialization branches, use-based mastery, fusion rank |
| Consumption & genetics | Absorb resources and compatible traits through research and evolution choices |
| Evolutionary Codex | Track species, traits, materials, requirements, combinations, and confidence of knowledge |
| Hunting & predation | Evaluate how a hunt is completed and what rare opportunities it qualifies for |
| Evolution Vault | Preserve eligible specimens, organs, research, and anatomy plans; never resurrection |
| Reactive world | Persist ecosystem changes, environmental damage, growth, healing, repairs, and NPC activity |
| Dominance & investigations | Track individual awareness, witnesses, evidence, reports, and plausible consequences |
| PvP & Resonance Fusion | Explicit high-stakes absorption matches and optional coordinated co-op abilities |
| Living Ship Form | Biological flight from planetary atmosphere to space after required evolution |

## Species roster

The current concept roster contains **100 proposed original base species** across ten families: cellular/primitive, small terrestrial, predators/pack hunters, giants/armored, aerial, aquatic/deep ocean, insectoid/colony, sapient, supernatural/dimensional, and cosmic/space. Species may have subspecies, regional variants, mutations, hybrids, and ascended forms where justified. Variants should change gameplay, not just appearance. These are concepts, not implemented content.

## Design principles

1. A kill is not automatically a successful hunt.
2. Being seen, identified, reported, and caught are separate states.
3. Consumption creates opportunities; it does not automatically copy every target ability.
4. Powers combine when their properties, rules, costs, anatomy, and circumstances allow.
5. NPCs can only react to knowledge they could reasonably obtain.
6. Bosses communicate danger; Titan fights are designed for Titan-scale play.
7. The world persists and recovers according to its ecology and physical/supernatural rules.
8. Character death is permanent; research persistence is not resurrection.
9. No ship or vehicle bypasses biological spaceflight progression.
10. Large-scale population support is an aspiration requiring distributed simulation and authoritative servers, not a current capability claim.

## Documentation

- **[Full Game Design Bible](docs/GAME_DESIGN_BIBLE.md)** — consolidated specification for progression, combat, evolution, anatomy, hunting, species, PvP, world persistence, investigations, NPC behavior, planetary completion, biological spaceflight, modular anatomy upgrades, unresolved decisions, and governing rules.

## Inspirations

Broad design inspiration includes action RPG combat, open-world exploration, procedural universe discovery, deep build customization, and evolving ecosystems. Referenced touchstones include Dragon Ball Z: Kakarot, Borderlands 4, Marvel’s Spider-Man 2, Hogwarts Legacy, No Man’s Sky, Watch Dogs 2, The Division, Spore, Black Myth: Wukong, Path of Exile, and Star Wars Outlaws. These are references only: Lethal Absorption should use original characters, species, art, narrative, and implementation.

## Open design decisions

The design bible identifies unresolved choices including the exact level curve, NG+ inventory carryover, post-1050 progression, Vault persistence/death-loss rules, boss recovery, spawn protection, controller bindings, standard-form scale limits, species details, world privacy/access, investigation timings, and the technical architecture required for persistent multiplayer.

The working title **Lethal Absorption** has not been checked for trademark or title availability.

## Ongoing documentation and implementation workflow

This repository is the central source of truth for the project. As development continues, record every agreed new feature or material design change in the relevant documentation during the same work sequence. Update this README when the project overview, major systems, or status changes. Keep the Game Design Bible synchronized with the detailed rules and dependencies. When features are implemented in code, update implementation-specific documentation and record what changed and what verification was actually performed. Clearly distinguish **proposed**, **approved/design-specified**, **in progress**, **implemented**, and **verified** work; never report a feature as implemented or tested without evidence. Preserve unresolved questions as open decisions rather than inventing answers. After repository changes, retrieve the changed files to confirm the updates landed.
