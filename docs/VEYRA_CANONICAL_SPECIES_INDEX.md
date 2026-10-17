# Lethal Absorption — Canonical Species Index for Veyra

> **Status:** Working inventory; two species dossiers authored as design records; runtime remains unimplemented and untested.
> **Purpose:** One index for species references used by Veyra's biome, ecology, skill, trainer, and evolution documents.
> **Authority:** `docs/BASE_PLANET_MASTER_ATLAS.md` defines the planet template; `docs/SPECIES_SKILLS_AND_TRAINERS_ATLAS.md` defines species-skill and trainer coverage.

## 1. Rules for maintaining this index

1. Every species/lineage receives one stable ID. Display names may change without changing IDs.
2. A character, faction, culture, regional form, life stage, and individual creature are not automatically separate species.
3. Existing repository concepts must be inventoried before the roster is called exhaustive. This document records known sources and reconciles the initial Veyra candidates; it does not claim all possible species have been authored.
4. Mark each record as Candidate, In design, Designed, Implemented, or Tested. At creation, all entries below are **Candidate** except the foundational Slime lineage, whose separate blueprint exists.
5. Do not invent exact stats, reproduction, compatibility, trainer knowledge, or ecological relationships without adding a reasoned design record.
6. Each completed record must cross-link biome instances, food-web edges, skills, trainer sources, resources, and evolution compatibility.

## 2. Repository source inventory

| Source | What it contributes | Reconciliation rule |
|---|---|---|
| `docs/BASE_PLANET_MASTER_ATLAS.md` | Initial Veyra species candidates and required biome families | This index is the stable roster location; keep candidate IDs synchronized |
| `docs/SLIME_MASTER_CHARACTER_BLUEPRINT.md` | Foundational Slime anatomy, perception, movement and evolution | Use as authority for established Slime decisions |
| `docs/SPECIES_SKILLS_AND_TRAINERS_ATLAS.md` | Species-page, skill-entry and trainer-entry schema | Every species must eventually receive coverage |
| `docs/LIVING_CREATURE_ECOSYSTEM_AND_COLLECTION.md` | Creature identity, behaviors, discovery, bonding and ecology rules | Apply to non-sapient fauna; distinguish sapient agency |
| `docs/ECOLOGY_AND_CROSSLINKED_EVOLUTION_ATLAS.md` | Cross-linked evolutionary architecture | Trait compatibility is not automatic |
| `docs/CHARACTER_INSPIRATION_AND_ORIGINAL_ROSTER.md` | Fourteen character archetypes | These are character concepts, not automatically biological species |
| `docs/EXPANDED_ABILITY_COVERAGE_MATRIX.md` | Ability-family coverage goals | Does not establish any species or ability as implemented |

### Character concepts that must not be miscounted as species

The existing character roster includes The Threshold Duelist, The Relic Symbiote, The Storm Choir, The Hollow Sovereign, The Wayfinder Organism, The Unfinished Apex, The Archive-Born Envoy, The Planetary Gardener, The Counter-Evolver, The Last Form Artisan, The Umbral Successor, The Limit-Breaker Disciple, The Scrap-Crowned Goblin, and The Mythic Staff Ascendant.

Treat these as individuals/archetypes until their records establish species, culture, lineage, or faction relationships. In particular, **The Storm Choir** is described as a multi-bodied aerial concept coordinated through vibration and electrical pulses; it may become a species, collective organism, or culture after explicit design review, but this index does not decide that prematurely.

## 3. Canonical Veyra candidate roster

All rows marked Candidate need a full species dossier. Habitat anchors are intended distribution clues, not final spawn coordinates.

| Stable ID | Working name | Functional role | Habitat anchors | Status |
|---|---|---|---|---|
| LA-PLN-SLM-001 | Null Slime | Player-capable flexible opportunist | Wet woodland edge, river basin, caves | Designed — [species dossier](species/LA-PLN-SLM-001_NULL_SLIME.md); runtime not implemented |
| LA-PLN-MIC-001 | Glassfilm Microbe | Biofilm producer | Wet rock, lake shallows, caves | Designed — [species dossier](species/LA-PLN-MIC-001_GLASSFILM_MICROBE.md); ecology links are hypotheses |
| LA-PLN-MIC-002 | Ember Mat | Heat-tolerant microbial producer | Geothermal field, volcanic ash | Candidate |
| LA-PLN-MIC-003 | Brine Lace | Salt-tolerant microbial producer | Salt flat, brine pool | Candidate |
| LA-PLN-INV-001 | Reed Skipper | Small wetland grazer / prey | Marsh, river delta | Designed — [species dossier](species/LA-PLN-INV-001_REED_SKIPPER.md); food-web links provisional |
| LA-PLN-INV-002 | Bark Lantern | Nocturnal detritivore / prey | Forest, scrub, canopy | Designed — [species dossier](species/LA-PLN-INV-002_BARK_LANTERN.md); ecological links provisional |
| LA-PLN-INV-003 | Stoneback Grazerling | Armored detritivore / prey | Grassland, woodland edge | Candidate |
| LA-PLN-INV-004 | Silt Burrower | Sediment feeder / prey | Riverbank, wetland, estuary | Designed — [species dossier](species/LA-PLN-INV-004_SILT_BURROWER.md); food-web links provisional |
| LA-PLN-INV-005 | Gloam Moth | Night-flying flower visitor / prey | Forest edge, marsh margin, old growth | Designed — [species dossier](species/LA-PLN-INV-005_GLOAM_MOTH.md); pollination links provisional |
| LA-PLN-AMP-001 | Glass-Eyed Pouncer | Small ambush predator | Scrub, canyon, rocky woodland | Designed — [species dossier](species/LA-PLN-AMP-001_GLASS_EYED_POUNCER.md); prey links provisional |
| LA-PLN-AMP-002 | Mire Needle | Wetland ambush predator | Marsh, bog, river edge | Designed — [species dossier](species/LA-PLN-AMP-002_MIRE_NEEDLE.md); prey links provisional |
| LA-PLN-HER-001 | Moss-Horn Browser | Medium herbivore / seed disperser | Temperate forest, old growth | Designed — [species dossier](species/LA-PLN-HER-001_MOSS_HORN_BROWSER.md); ecology links provisional |
| LA-PLN-HER-002 | Longstride Grazer | Herd grazer / migration driver | Grassland, savanna, floodplain | Candidate |
| LA-PLN-HER-003 | Frostveil Grazer | Cold-adapted herd grazer | Boreal forest, tundra, alpine meadow | Candidate |
| LA-PLN-OMN-001 | Cinder Rummager | Omnivorous scavenger | Ash field, dry canyon, scrub | Candidate |
| LA-PLN-OMN-002 | Root-Crown Forager | Burrowing omnivore / soil engineer | Forest, grassland, root labyrinth | Designed — [species dossier](species/LA-PLN-OMN-002_ROOT_CROWN_FORAGER.md); ecology links provisional |
| LA-PLN-PRE-001 | Reedstalker | Medium pursuit / ambush predator | Wetland, floodplain, river edge | Designed — [species dossier](species/LA-PLN-PRE-001_REEDSTALKER.md); prey links provisional |
| LA-PLN-PRE-002 | Duskcoil | Serpentine predator | Scrub, canyon, dry forest | Candidate |
| LA-PLN-PRE-003 | Ridge Prowler | Pack hunter | Alpine foothills, plateau, grassland | Candidate |
| LA-PLN-APX-001 | Thunder-Crest Colossus | Regional apex / territorial titan | Mountain pass, storm corridor | Candidate |
| LA-PLN-APX-002 | Mire Crown | Wetland apex | Deep marsh, delta channel | Candidate |
| LA-PLN-AQU-001 | Current Dart | Schooling aquatic prey | River, lake, estuary | Designed — [species dossier](species/LA-PLN-AQU-001_CURRENT_DART.md); food-web links provisional |
| LA-PLN-AQU-002 | Siltjaw | Aquatic ambush predator | Lowland river, estuary | Candidate |
| LA-PLN-AQU-003 | Lantern Drift | Deep-water lure feeder / predator | Twilight ocean, deep lake | Candidate |
| LA-PLN-AQU-004 | Ventroot Colony | Chemosynthetic symbiotic colony | Hydrothermal vent, cold seep | Candidate |
| LA-PLN-AIR-001 | Windglass Glider | Gliding omnivore / seed disperser | Canopy, cliff, island wind zone | Candidate |
| LA-PLN-AIR-002 | Stormwing Hunter | Aerial pursuit predator | Updraft corridor, storm-belt margin | Candidate |
| LA-PLN-CAV-001 | Echo Mite | Cave detritivore / prey | Karst cave, lava tube | Candidate |
| LA-PLN-CAV-002 | Pale Threader | Cave ambush predator | Subterranean stream, root labyrinth | Candidate |
| LA-PLN-EXT-001 | Sulfur Veil | Extremophile colony | Geothermal subterrane, vents | Candidate |
| LA-PLN-EXT-002 | Frostglass Crawler | Cold specialist | Subglacial cavern, polar cave | Candidate |
| LA-PLN-SYM-001 | Brushback Cleaner | Mutualistic parasite-remover | Reef, large-herbivore range | Candidate |
| LA-PLN-SAP-001 | Veyran River Communities | Sapient society concept; species unresolved | River basins, coasts, trade corridors | Candidate; resolve species/culture boundary |
| LA-PLN-SAP-002 | Canopy Concords | Sapient society concept; species unresolved | Rainforest, old-growth canopy | Candidate; resolve species/culture boundary |
| LA-PLN-SAP-003 | Deep Archive Enclaves | Sapient society concept; species unresolved | Cave cities, buried ruins | Candidate; resolve species/culture boundary |
| LA-PLN-ANC-001 | Rootbound Elder | Ancient lineage / possible keystone | Ancient woodland refugium | Candidate |
| LA-PLN-ANM-001 | Rift-Touched Organism | Anomalous rare lineage | Anomalous reserve, if physics rules permit | Candidate |

## 4. Species-dossier completion checklist

For each ID, create a dedicated dossier with:
- [ ] Taxonomy, originality note, body plan, size/mass bands and life stages.
- [ ] Diet, energy source, reproduction, growth, lifespan class and mortality.
- [ ] Native range, biome-instance links, seasonal presence, dispersal barriers and migration.
- [ ] Senses, blind spots, detection clues, locomotion, shelter and activity cycle.
- [ ] Innate abilities, costs, range, prerequisites, counters and failure states.
- [ ] Temperament, social organization, threat response, AI evidence and recovery states.
- [ ] Food-web edges, competition, symbiosis, decomposition and habitat impact.
- [ ] Resources, nonlethal study options, harvest rules and renewal consequences.
- [ ] Absorption eligibility, compatibility, risks, trait conflicts and alternate discovery paths.
- [ ] Skills, observation sources, trainers/mentors, training conditions and mastery.
- [ ] Regional forms, life-stage differences, mutations, rare/alpha/apex/ancient variants.
- [ ] Player-facing discovery clues, accessibility, PvP/agency rules when applicable.
- [ ] Status, evidence, unresolved questions and links to tests/implementation tickets.

## 5. First vertical-slice priority

Complete the first local food web before trying to finish every planetary species. Priority order:

1. Null Slime — starting player organism and its Stage 0/Stage 1 rules.
2. Glassfilm Microbe — a defined nutrient/biofilm source that makes the first environment legible.
3. Reed Skipper and Silt Burrower — [Reed Skipper dossier](species/LA-PLN-INV-001_REED_SKIPPER.md) and [Silt Burrower dossier](species/LA-PLN-INV-004_SILT_BURROWER.md), small prey with contrasting wetland/river microhabitats.
4. Glass-Eyed Pouncer and Mire Needle — [Glass-Eyed Pouncer dossier](species/LA-PLN-AMP-001_GLASS_EYED_POUNCER.md) and [Mire Needle dossier](species/LA-PLN-AMP-002_MIRE_NEEDLE.md), early predator pressure with different warning cues and counters.
5. Moss-Horn Browser and Root-Crown Forager — [Moss-Horn Browser dossier](species/LA-PLN-HER-001_MOSS_HORN_BROWSER.md) and [Root-Crown Forager dossier](species/LA-PLN-OMN-002_ROOT_CROWN_FORAGER.md), larger herbivore/omnivore roles connecting plant matter, soil, and predators.
6. Current Dart and Reedstalker — [Current Dart dossier](species/LA-PLN-AQU-001_CURRENT_DART.md) and [Reedstalker dossier](species/LA-PLN-PRE-001_REEDSTALKER.md), freshwater food web and aquatic movement.
7. Bark Lantern and Gloam Moth — [Bark Lantern dossier](species/LA-PLN-INV-002_BARK_LANTERN.md) and [Gloam Moth dossier](species/LA-PLN-INV-005_GLOAM_MOTH.md), deadwood ecology, night activity, and flight-related sensory clues.
8. One non-hostile symbiont and one rare/ancient lineage only after the baseline network is coherent.

This order is a production priority, not a claim that these species have final mechanics. Any food-web edge must be supported in the species dossiers.

## 6. Audit rules

- No species may be marked complete merely because it has a name, concept art prompt or one-line role.
- Every biome instance must reference IDs from this index, and every species must have at least one justified habitat or an explicit off-planet/future-stage designation.
- Sapient cultures must not be misrepresented as species or loot categories.
- Candidate names can be changed during originality and naming review; preserve stable IDs and record aliases.
- Do not add exact drop rates, stats or reproduction rates without a design rationale and later balance validation.
- Completion counts must distinguish rostered, dossier-complete, implemented and tested entries.

**Current status:** Initial candidate roster reconciled with known repository documents listed above. The [Reedwater Basin Food-Web and Biome Linkage Specification](VEYRA_REEDWATER_BASIN_FOOD_WEB.md) defines provisional edge types, regional habitat links, seasonal scenarios, and validation gates. This is not yet an exhaustive repository-wide species inventory; population data, biome instances, and runtime simulation remain incomplete.
