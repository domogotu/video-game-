# Lethal Absorption — Genetic Inheritance Catalogue and Compatibility Matrix

> **Status:** Design specification only. No breeding simulation, trait engine, or gameplay implementation is verified.
> **Applies to:** Veyra first; reusable for later planets.
> **Related:** [Cross-Species Hybridization](CROSS_SPECIES_HYBRIDIZATION_AND_SPECIES_EMERGENCE_SYSTEM.md), [Cohabitation and Breeding](COHABITATION_BREEDING_AND_HERITABLE_TRAITS_SYSTEM.md), [Landscape Restoration](LANDSCAPE_RESTORATION_AND_ECOLOGICAL_BALANCE_SYSTEM.md).

## 1. Purpose and design boundary

Build a traceable trait-inheritance engine rather than a random creature blender. Every expressed offspring feature needs a plausible origin, compatible body plan and developmental pathway, a cost, and an ecological consequence. The catalogue distinguishes **canonical facts**, **design hypotheses**, and **undiscovered/unknown** information. No Veyra pairing is declared canonically fertile merely because the species coexist.

## 2. Trait families and stable IDs

Each heritable module has a stable ID of the form `GEN.<family>.<trait>`; use versioned revisions without reusing retired IDs.

| Family | Examples | Required checks |
|---|---|---|
| MOR — morphology | limbs, shell, membrane, body size, root structures | attachment, skeletal/support architecture, development |
| LOC — locomotion | hopping, burrowing, gliding, swimming, climbing | anatomy, medium, energy cost |
| SEN — senses | chemical sensing, vibration, eyes, echolocation | organs, neural processing, sensory conflicts |
| MET — metabolism | digestion, heat/cold tolerance, dormancy | nutrition, oxygen, temperature, growth cost |
| DEF — defense | armor, camouflage, toxins, regeneration | material supply, activation costs, vulnerabilities |
| OFF — offense | claws, stingers, constriction, discharge | anatomy, reach, energy, friendly-fire risk |
| REP — reproduction | spores, eggs, live birth, budding, symbiont transfer | parent role, developmental environment, fertility |
| BEH — behavior | migration, pack cooperation, nesting, territoriality | learning versus inheritance, social triggers |
| ECO — ecological role | seed dispersal, soil turnover, pollination, browsing | actual mechanism and habitat conditions |
| ANO — anomalous biology | explicitly supported exotic trait mechanisms | source, rarity, counterplay, limits |

Behavioral predisposition is not the same as a learned skill; ecological roles are *outcomes* of anatomy, behavior, and environment, not magic traits that instantly restore a landscape.

## 3. Per-trait record

Required fields:
- `trait_id`, `revision`, `name`, `family`, `origin_lineage_ids`, `source_mechanism`.
- `inheritance_mode`: dominant, recessive, codominant, polygenic, cytoplasmic/symbiotic, conditional, or nonheritable.
- `alleles_or_modules`, `expression_range`, `penetrance_conditions`, `latent_state`, `mutation_bounds`.
- `developmental_prerequisites`, `body_plan_slots`, `required_organs`, `incompatible_trait_ids`.
- `environmental_requirements`, `metabolic_cost`, `movement_cost`, `fertility_effect`, `counterplay`.
- `transmission_route`, `heritability_confidence`, `evidence_refs`, `discovery_visibility`.
- `ecological_functions` and `ecological_harms`, each with causal mechanism, biome, and density thresholds.
- `balance_budget` and `rarity_gate`; no guaranteed stacking of the strongest parental traits.

The record must distinguish genotype (inherited potential), phenotype (expressed features), acquired modifications, and active symbionts.

## 4. Combination rule matrix

| Relationship | Rule | Example, illustrative only |
|---|---|---|
| Independent | Both may express if slots and resources permit | Chemical sensing and reinforced skin |
| Compatible with cost | Both express with an explicit trade-off | Armor plus climbing increases mass and stamina use |
| Conditional | Expression depends on an environment or organ | A light-sensitive eye requires a functioning visual organ |
| Dominance / codominance | Expression follows documented allele interaction | Two pigment alleles yield one or mixed patterns |
| Latent / recessive | Trait can remain unexpressed and reappear in descendants | Dormancy tendency manifests under defined inheritance |
| Prerequisite | Feature cannot express without supporting anatomy | Gliding membrane requires attachment surfaces and control |
| Mutually exclusive | Conflicting structures cannot occupy the same anatomical role | Two incompatible limb-joint architectures in one slot |
| Developmentally incompatible | Embryo/offspring fails a documented viability gate | Contradictory respiratory development |
| Symbiont-dependent | Trait persists only if partner is transmitted and maintained | Host protection from an inherited microbial partner |
| Nonheritable | Cannot enter breeding inheritance by default | Learned combat technique or absorbed temporary buff |

Conflicts are evaluated in order: reproduction mechanism → development → structural compatibility → physiological capacity → expression → ecological fitness. An invalid combination cannot be rescued by a lucky roll.

## 5. Offspring resolution pipeline

1. Validate lineage IDs, reproductive roles, maturity, compatibility class (C0–C5 or CX), and applicable conditions.
2. Choose the **documented mechanism**: genetic cross, alien analogue, symbiotic transfer, graft/composite, or other permitted path. Do not silently equate them.
3. Assemble inherited allele/module candidates with provenance, recombination limits, and any inherited symbiont.
4. Resolve developmental prerequisites, mutually exclusive modules, and viability; record why a cross failed.
5. Determine expressed and latent traits from genotype plus age, health, environment, and development.
6. Apply mass, stamina, nutrition, fertility, and ecological trade-offs; no cost-free maximal offspring.
7. Determine offspring reproductive compatibility independently of parental compatibility.
8. Register a unique individual, parents, generation, lineage graph, trait provenance, and evidence state.
9. On later generations, measure stable inheritance, population persistence, and reproductive identity before considering C5 species recognition.

Use a deterministic server-authoritative seed for resolution and retain a replayable event record; clients may preview only outcomes supported by their discovery level. Never rely on client-provided genotype or trait outcomes.

## 6. Veyra compatibility research queue

The following are **research candidates, not established compatible pairs**. Default status is **CX unknown** until dossiers document reproductive biology and evidence.

| Candidate interaction | What to investigate | Do not assume |
|---|---|---|
| Reed Skipper × Silt Burrower | Reproductive mechanisms, body-plan support, shared life stages | Both living in Reedwater means fertile hybrids |
| Moss-Horn Browser × Root-Crown Forager | Reproductive roles, size, development, ecological traits | Both helping soil/vegetation means crossbreeding |
| Gloam Moth × other compatible flying lineage (not yet selected) | Life-cycle stages, gamete/spore analogue, flight morphology | Flight or pollination proves reproductive compatibility |
| Glassfilm Microbe × Null Slime | Whether any symbiotic gene transfer exists | Contact or absorption creates offspring |
| Duskbell Bloom × Reedlace Hostleaf | Pollination, plant-like reproduction, host relationships | Shared habitat implies genetic compatibility |

If the research supports only symbiosis, ecological interaction, or C1 overlap, record that result instead of manufacturing a hybrid.

## 7. Worked hypothetical offspring (NOT canonical species)

**Armored climber:** A future C4-compatible pair contributes a climb-capable limb module and armor. The offspring expresses both only if load-bearing joints support the mass. Gains protection; pays extra stamina and loses some vertical speed. Recessive sensory variation may remain latent.

**Wetland seed carrier:** A future compatible lineage combines seed-carrying fur with wetland mobility. It may move seeds between habitat patches, but only viable seeds in suitable soil contribute to restoration. In a fragile habitat it could instead spread an invasive plant. Ecological role must be simulated, not assigned by label.

**Symbiotic sensor host:** A microorganism enables improved chemical detection in a host through symbiosis. The host is *not* automatically a hybrid; descendants retain the function only if the symbiont transfers and persists. This must not be counted toward C5 speciation without additional evidence.

## 8. Derived-species registry

State machine: `individual hybrid → recurring hybrid lineage → candidate derived population → verified derived species (C5)`. A lineage can also fail, backcross, become extinct, or remain unresolved.

Store `lineage_id`, founder individuals, parent lineages, reproductive mechanism, generation history, trait-stability evidence, viable population trend, ecological niche, reproductive boundaries, geographic distribution, and approval evidence. Thresholds are per-lineage configurable; no global fixed generation count.

A newly recognized species gets a permanent unique ID and dossier; discoveries are shared as knowledge under existing discovery-network rules, not as free player traits.

## 9. Player-facing tools

- **Field Codex:** observed pairings, confidence levels, inherited/latent traits, habitat evidence.
- **Breeding and lineage viewer:** family tree, developmental risks, offspring phenotype, fertility observations.
- **Anatomy preview:** compatible slots, costs, conflicts, required organs; distinguish hypothetical from verified.
- **Ecology overlay:** seed dispersal, browsing, pollination, soil disturbance, spread risks, restoration/counter-restoration outcomes.
- **Research progression:** unknown → suspected → observed → replicated → established, without revealing undiscovered rare traits in advance.

## 10. Acceptance criteria before implementation can be called complete

- C0/C1 never yield ordinary hybrid offspring; CX is not treated as C4.
- C2 trait transfer does not automatically create hybrid offspring or a new species.
- C3 offspring fertility restrictions persist through save/load and multiplayer replication.
- Mutually exclusive anatomy never co-expresses; prerequisites and costs apply.
- Latent inherited traits can be tracked without being displayed as active abilities.
- Learned, absorbed temporary, and symbiotic traits never silently become germline.
- Hybrid births do not automatically register C5 species.
- Population/ecology effects occur locally with resource and carrying-capacity checks.
- Restoration and counter-restoration outcomes depend on causal interactions, not moral labels.
- Identical authoritative inputs reproduce outcomes; client-side tampering is rejected.
- Species discovery and parentage remain auditable across generations.

## 11. Next content pass

For each Veyra species, write a reproductive biology dossier, a minimum of five traceable trait records, developmental prerequisites, ecological functions and costs, and explicit pairwise compatibility evidence. Start with the Reedwater Basin species; keep uncertain entries as CX. Only then promote example crosses into canon.
