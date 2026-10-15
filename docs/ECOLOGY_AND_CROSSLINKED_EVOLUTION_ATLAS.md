# Lethal Absorption — Ecology and Cross-Linked Evolution Atlas

> **Status:** Design-only. This specifies intended architecture; it does not claim that a species catalogue, procedural character generator, Atlas UI, or gameplay system has been implemented or tested.

## 1. Core concept

Build one interconnected evolution network that can support millions of distinct character outcomes without hand-authoring millions of separate skill trees. Characters begin at the cellular scale and develop through acquired traits, environment, diet, research, training, survival, mutations, and deliberate choices.

The network is **connected but not linear**:
- Routes can branch into specialized body plans.
- Compatible traits can cross-link between distant branches.
- Shared biological systems can reconnect routes.
- Conflicting traits, anatomy requirements, costs, and instability prevent every combination from working.
- Each character's history explains why its available routes and resulting body plan are different.

Real taxonomy informs the reference catalogue; fictional game evolution follows explicit game rules. Do not present fantasy transformations as real-world biology.

## 2. Example: one cell, many futures

A starting cell first develops the systems its stage can support: membrane behavior, nutrient processing, basic sensing, energy use, movement, and survival responses.

As it advances, its history and acquired traits may qualify it for different routes:
- **Terrestrial predator:** structural support, powerful locomotion, hunting senses, jaws or other suitable feeding anatomy.
- **Serpentine lineage:** elongated body plan, undulatory movement, flexible structure, specialized sensory traits.
- **Aquatic lineage:** water-compatible respiration, propulsion, pressure tolerance, and aquatic sensing.
- **Fantasy draconic lineage:** a compatible body plan plus explicit fictional prerequisites such as a specialized energy organ, heat management, flight structures, and rare discoveries.
- **Hybrid phenotype:** a combination of compatible traits from multiple routes, with costs and trade-offs.

A cell does not literally turn into a dinosaur, eel, or dragon by selecting one node. These are staged game outcomes assembled from prerequisites, templates, trait combinations, and—where fantasy is involved—clearly identified fictional rules.

## 3. Four layers

### A. Real-world reference catalogue

Maintain a versioned catalogue of known organisms and sourced ecological information. Candidate fields include:
- Stable internal ID, scientific name, common names, synonyms, and taxonomy.
- Habitat, range, diet, locomotion, anatomy, life stage, and ecological role where reliable sources provide them.
- Relevant capabilities and environmental tolerances.
- Source, version/date, licence/usage terms, provenance, confidence, and review status.
- A mapping to game traits that distinguishes the real-world fact from its gameplay abstraction.

Use datasets and sources whose licences permit the intended use. Preserve attribution and licence obligations. Do not assume a catalogue entry grants rights to reuse protected descriptions, images, models, or recordings. Taxonomy changes, so the catalogue must be updateable rather than described as permanently complete.

### B. Canonical trait ontology

Normalize reusable capabilities into trait records instead of duplicating every trait for every species. Trait families can include:
- Body architecture: soft-bodied, segmented, exoskeletal, endoskeletal, serpentine, winged, finned.
- Locomotion: crawl, undulate, swim, burrow, glide, fly, cling, jump, propel.
- Senses: chemical, vibration, visual, thermal, pressure, electrical, magnetic, echolocation-like, fictional/anomalous.
- Physiology: respiration, metabolism, water retention, thermal regulation, regeneration, toxin processing, energy storage.
- Defense: armor, camouflage, decoy, insulation, secretion, escape response, counterforce.
- Offense and interaction: bite, grasp, tendril, venom, projectile, elemental channel, absorption, tool use.
- Ecology: diet, habitat needs, symbiosis, territory, migration, social behavior, predator/prey role.

Every trait needs a stable ID, prerequisites, effects, anatomy requirements, costs, compatibility/conflict rules, environmental fit, counterplay, and provenance.

### C. Cross-linked evolution graph

Use a typed graph rather than a single strict tree:
- **Prerequisite:** one node requires another.
- **Alternative path:** multiple credible routes can qualify a character.
- **Compatibility:** traits can combine if conditions are met.
- **Conflict:** traits compete for anatomy, metabolism, stability, or slots.
- **Discovery:** evidence reveals a hypothesis or route without granting the ability.
- **Mastery:** use, training, and trials unlock advanced execution.
- **Transformation:** a compatible set of traits enables a new body plan.
- **Cross-scale:** early biology can remain relevant to later combat, planetary, and cosmic systems.

Validate deliberate loops and cross-links so they cannot bypass prerequisites or create infinite resources.

### D. Phenotype and character variation

Assemble the resulting character from a body-plan template, acquired traits, anatomy constraints, mutations, environment, diet, training, mastery, active form, and cosmetic choices. Cosmetic choices must not falsely grant mechanical capabilities.

The same saved state and generation seed should reproduce the same phenotype. Use authored landmark forms for distinctive creatures and controlled procedural variation to expand variety without sacrificing silhouette, animation, readability, balance, or story quality.

## 4. Real, inspired, and fantasy content

The Codex should distinguish:
- **Real-world reference:** sourced organism information.
- **Inspired abstraction:** a game trait inspired by a real capability but adjusted for play.
- **Fantasy organism:** a fictional species with authored rules.
- **Hybrid phenotype:** a valid combination of compatible traits.
- **Hypothesis:** an unconfirmed in-world research idea, not an unlocked power.

A dragon, for example, is a fantasy lineage that can combine compatible concepts inspired by several animals plus explicit fictional systems. The game should not imply that such a creature exists in real taxonomy.

## 5. Unlock and discovery loop

A species entry is not a free trait vending machine. A route may require the player to:
1. Encounter an organism, trace, specimen, or credible record.
2. Observe relevant anatomy or behavior.
3. Gather enough evidence to record a hypothesis.
4. Research, train, absorb safely, or survive the relevant condition.
5. Prove compatibility with the current body.
6. Complete a defined feat or pay a clearly shown cost where appropriate.
7. Stabilize and master the trait before advanced combinations become reliable.

Where appropriate, alternate routes may include observation, cooperative research, environmental trials, crafting, or direct encounters. They may reveal the same knowledge without granting identical materials or mastery.

## 6. Compatibility, trade-offs, and balance

Evaluate body structure, required organs, anatomy slots, metabolic demand, environmental fit, trait conflicts, mass/scale, locomotion, animation feasibility, resource limits, and combat counterplay.

For example, heavy terrestrial armor combined with aquatic propulsion might increase energy demand and reduce turning speed. A fantasy energy organ might require heat management, compatible respiration, rare research, and recovery time. Combinations should not accidentally grant infinite regeneration, universal resistance, or an all-purpose best build.

## 7. Supporting millions of character outcomes

“Millions of characters” is a target for combinatorial variety, not a promise to hand-author millions of full species. Scale comes from:
- Curated real-organism references with source and licence metadata.
- Reusable trait definitions.
- Authored species/body-plan templates and landmark creatures.
- Validated compatibility rules and cross-links.
- Controlled variation in morphology, proportions, coloration, behaviors, traits, and evolution history.
- On-demand evaluation of relevant combinations, indexed by traits, prerequisites, anatomy, habitat, and stage.
- Persistent character state and generation seeds.

Do not enumerate every possible combination at once. Validate combinations when needed, cache results, and persist only the relevant character state. Any generated creature affecting combat or progression must pass the same compatibility and fairness rules as authored content.

## 8. Atlas interface

The Atlas should provide:
- A cellular-origin view that expands as the player discovers more.
- Zoom from cells and anatomy to species families, ecosystems, planetary adaptation, and cosmic evolution.
- Filters for real references, inspired traits, fantasy lineages, hybrids, habitat, locomotion, senses, role, and prerequisites.
- Visible divergence, reconnection, cross-links, compatibility, and conflicts.
- A detail panel with source confidence, effects, requirements, costs, trade-offs, and discovery method.
- A preview of predicted anatomy, silhouette, movement, strengths, weaknesses, and resource demand.
- State labels such as unknown, hypothesized, discovered, eligible, available, acquired, unstable, mastered, incompatible, and temporarily active.
- An evolution history explaining which discoveries and choices caused major changes.
- Optional recommendations without automatic irreversible evolution.

## 9. Acceptance gates

1. Real-reference records preserve provenance and usage/licence metadata.
2. Stable trait IDs are separate from source organism records.
3. The graph validates prerequisites, alternatives, conflicts, cross-links, and intentional loops.
4. Saved state and seed reproduce the character phenotype.
5. Invalid anatomy or prerequisite combinations are rejected with a clear explanation.
6. Real facts, inspired abstractions, and fictional rules are distinguishable in the Codex.
7. Preview does not mutate the live character or spend resources.
8. Save/load and multiplayer authority preserve evolution history and prevent forged or duplicated traits.
9. Generated creatures are reviewed for readability, animation, ecology, combat, and fairness.
10. Performance testing measures indexed route queries and on-demand combination evaluation rather than enumerating the entire possibility space.
11. Actual implementation tests and results are recorded before any feature is called implemented or verified.

## 10. Related documents

- [Skill Tree and Evolution Atlas](SKILL_TREE_AND_EVOLUTION_ATLAS.md)
- [Game Design Bible](GAME_DESIGN_BIBLE.md)
- [Ultimate and Secret Skill Framework](ULTIMATE_AND_SECRET_SKILL_FRAMEWORK.md)
- [Expanded Ability Coverage Matrix](EXPANDED_ABILITY_COVERAGE_MATRIX.md)

**Implementation status:** Design-only. The real-world reference catalogue, trait ontology, evolution graph, phenotype generator, Atlas UI, and validation suite are not claimed implemented or tested.
