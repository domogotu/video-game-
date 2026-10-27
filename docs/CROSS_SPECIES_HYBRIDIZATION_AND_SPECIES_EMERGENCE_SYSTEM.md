# Lethal Absorption — Cross-Species Hybridization and New Species Emergence

> **Status:** Design specification; not implemented, simulated, or tested.  
> **Parent system:** [Cohabitation, Breeding, and Heritable Traits](COHABITATION_BREEDING_AND_HERITABLE_TRAITS_SYSTEM.md).  
> **Purpose:** Let compatible organisms exchange heritable material, produce hybrids or composite lineages, and potentially give rise to genuinely new species over generations.

## 1. Core rule

Cross-species breeding is a real possibility in Lethal Absorption, not a blanket exception. But sharing a biome, being visually similar, or having a high relationship score does not automatically make two organisms reproductively compatible. Each pairing uses a documented biological, symbiotic, anomalous, or species-specific mechanism.

The system must support:
- Compatible species producing hybrid offspring.
- Partial compatibility that allows offspring but creates fertility, survival, or trait-expression limits.
- Stable hybrid lineages that can become distinct species over generations.
- Symbiotic or composite organisms that combine functions without being genetically identical to a hybrid.
- Unusual alien mechanisms such as spores, budding, grafting, gene-transfer symbionts, or controlled anomalous inheritance, where the species dossier defines them.
- Failed pairings, sterile offspring, unstable traits, and lineages that disappear when they cannot survive or reproduce.

Crossbreeding should create possibilities and trade-offs, not guaranteed upgrades.

## 2. Compatibility classes

Each pair of candidate parent lineages receives a stable compatibility record. Compatibility can be directional or depend on sex/role, life stage, season, habitat, health, anatomy, and reproductive method.

| Class | Meaning | Possible result |
|---|---|---|
| **C0 — Incompatible** | No known viable mechanism under current rules | No offspring through ordinary breeding; other interactions may still occur |
| **C1 — Environmental overlap only** | Species share space/resources but lack a supported reproductive pathway | Cohabitation only; no hybrid assumption |
| **C2 — Limited transfer** | A defined mechanism transfers a restricted set of genes, symbionts, or traits | Trait transfer, graft, symbiosis, or partial expression; not automatically a hybrid |
| **C3 — Viable hybrid, reduced fertility** | Offspring can develop but have low fertility, narrow viable conditions, or limited mating compatibility | Hybrid individuals; lineage may depend on repeated parent crosses or a different reproduction mode |
| **C4 — Viable fertile hybrid** | Offspring can survive and reproduce with compatible partners | Hybrid population can persist; a new species is not automatic |
| **C5 — Stable derived lineage** | A hybrid-derived population has a stable identity and reproducible traits across generations | Eligible for recognition as a new species after lineage criteria are met |
| **CX — Unknown / undiscovered** | Evidence is insufficient | Remains unknown until observed, researched, or tested in-world |

Do not assign a compatibility class from appearance or shared habitat alone. The field guide should distinguish "not compatible" from "not yet known."

## 3. Mechanisms for cross-species variation

Use only mechanisms supported by the organisms involved.

### 3.1 Conventional genetic hybridization
Compatible reproductive systems combine parental genetic material. Offspring receive a bounded combination of traits and may show dominance, incomplete dominance, recombination, or multi-gene interactions.

### 3.2 Alien reproductive compatibility
Species may use non-Earth reproductive strategies—spore fusion, compatible gamete analogues, budding exchange, colony fusion, or life-cycle stages that only meet under rare environmental conditions. Their rules must be specified per lineage rather than assumed universal.

### 3.3 Symbiotic gene or trait transfer
A symbiont, parasite, microbe, or engineered/anomalous organism may transfer a defined trait module to another host. This can change the host without creating a hybrid species. Transfer has compatibility limits, costs, risks, and possible loss across generations.

### 3.4 Grafting and composite bodies
Two organisms may physically cooperate, graft, or form a composite body. The result can be a symbiotic form or chimera-like individual, but must not be mislabeled as a genetically stable species unless the lineage meets species-emergence criteria.

### 3.5 Absorption and assimilation
Player absorption is a separate acquisition system. Absorbing a creature may grant a compatible biological ability, material, memory, or trait candidate under the existing absorption rules; it does **not** automatically create offspring, rewrite the player's germline, or create a new species. Heritable changes require a separately documented mechanism and explicit player-facing consequences.

### 3.6 Mutation and recombination
Mutation creates bounded new variation within a lineage. Recombination can combine compatible inherited traits. Neither is a license to produce arbitrary powers unrelated to parental biology, world rules, or established anomaly systems.

## 4. Offspring generation pipeline

A candidate cross should pass through explicit gates:

1. **Pair eligibility:** both organisms are mature and their species-specific reproductive roles permit the interaction.
2. **Compatibility:** the pair has a documented mechanism and a current compatibility state.
3. **Condition and environment:** health, nutrition, habitat, season, resources, and other lineage-specific requirements are met.
4. **Inheritance assembly:** choose only supported trait modules, alleles, or symbionts; record parentage and inheritance source.
5. **Development:** evaluate incubation, gestation, budding, spore growth, or another valid developmental process.
6. **Viability:** check developmental compatibility, physiology, anatomy, and environmental tolerance.
7. **Phenotype expression:** express inherited traits within bounded ranges, including recessive/latent traits where supported.
8. **Fertility and reproduction mode:** determine whether the offspring is sterile, fertile with one or both parent lineages, fertile only with similar hybrids, or capable of another documented reproductive method.
9. **Ecological integration:** evaluate food, habitat, predators, social acceptance, competition, disease, and carrying capacity.
10. **Lineage tracking:** preserve parentage, inherited traits, health outcomes, and offspring generation so the lineage can be studied over time.

Failure at a gate can result in no conception, failed development, nonviable offspring, a short-lived individual, or a viable but sterile hybrid. Failure outcomes should follow known rules and should not be rolled arbitrarily just to surprise players.

## 5. When does a hybrid become a new species?

A single unusual offspring is not automatically a new species. The world can label it a **hybrid individual**, **hybrid lineage**, or **candidate derived species** while evidence accumulates.

A derived species may be recognized when the design-defined criteria are met, such as:
- A reproducible trait profile distinguishable from both parent populations.
- A viable population or persistent lineage, not merely one individual.
- Stable inheritance of defining traits across multiple generations.
- A distinct ecological niche, behavior, reproductive schedule, anatomy, or other meaningful identity.
- A repeatable reproductive pathway within the derived lineage, or another explicit mechanism that maintains the lineage.
- Defined compatibility boundaries with parent species and other hybrids.
- A documented origin, population history, and species identifier.

The exact generation count and population thresholds should be data-driven and tunable by planet and species, not hardcoded as a universal biological law. Rare one-off hybrids remain valid discoveries without forcing the game to create a permanent species entry for every birth.

A derived species can remain geographically limited, fail to establish, merge back through gene flow where compatible, or become extinct. A new species can also be successful but ecologically disruptive; "new" does not mean "better."

## 6. Inheritance, trade-offs, and constraints

Every cross-compatible trait must specify:
- Stable trait/module ID, source lineage, inheritance mode, allowed recipients, expression range, and confidence/evidence state.
- Whether it is germline-inherited, acquired, symbiotic, learned, temporary, or installed.
- Compatibility conflicts and developmental dependencies.
- Environmental benefits and costs, including resource demands, movement penalties, sensory blind spots, vulnerability, or reproductive trade-offs.
- Whether the trait can persist through repeated breeding, is diluted/lost, or requires a continuing symbiont.
- Potential recessive or latent expression only when the lineage rules support it.
- Mutation bounds and anti-exploit constraints.

Examples:
- Armor from one lineage plus climbing ability from another may be viable but increase weight and energy cost.
- Heat tolerance combined with cold adaptation may produce a broad tolerance range only if physiology supports it; it may also impose a slower growth or food cost.
- A toxin-resistant hybrid may still be vulnerable to different toxins and may pay a metabolic cost.
- A hybrid may inherit a parent's sensory ability but retain the parent's blind spots.
- A host-dependent symbiont trait may disappear if the symbiont is not passed on.

No trait is copied at full strength by default. Dominance, dilution, incompatibility, expression, and trade-offs must be documented.

## 7. Ecological and population consequences

Crossbreeding changes the ecosystem, not just the creature model:
- Hybrid offspring compete for food, shelter, nesting sites, hosts, and territory.
- Hybrids may become prey, predators, pollinators, dispersers, soil engineers, restoration agents, or counter-restoration pressures.
- A hybrid can disrupt a food web, outcompete parents, fill an empty niche, or fail because no niche supports it.
- A rare hybrid lineage needs enough viable individuals, habitat, and reproduction opportunities to persist.
- Parent populations can lose rare traits through gene flow or benefit from useful variation, depending on the rules.
- Hybridization can reduce local population fitness when incompatible traits or reproductive costs accumulate.
- Cross-species breeding must respect carrying capacity, resource availability, and animal welfare/ecological logic within the game's fiction.

The ecology system should evaluate outcomes at local and regional scales. Avoid instant global spread from a single successful birth.

## 8. Player interaction and discovery

Players may be able to:
- Observe courtship, spawning, budding, grafting, or unusual offspring.
- Research compatibility through field observations, samples, behavior, or lineage records.
- Protect suitable habitat and manage breeding conditions.
- Identify hybrid individuals and trace parentage when evidence supports it.
- Track trait expression and reproductive success across generations.
- Discover a new species through sustained population evidence.
- Choose to protect, relocate, study, or avoid a derived lineage.

Do not expose all compatibility outcomes at the start. The player may know a cross is possible, suspect it, or discover it only after observing offspring. However, the system must not hide essential safety, consent, or gameplay rules in ways that create misleading player expectations.

## 9. Data model requirements

Each cross-lineage record should include:
- Stable IDs for both parent lineages and any reproductive roles.
- Compatibility class, directionality, mechanism, evidence, and discovery state.
- Required conditions, developmental gates, expected outcomes, and known failure modes.
- Allowed inherited traits/modules and prohibited combinations.
- Offspring development, viability, fertility, and reproductive mode rules.
- Parentage and generation tracking.
- Ecological role, habitat, resource demands, risks, and population limits.
- New-lineage recognition criteria and status.
- Versioning and validation rules.

Every offspring or derived population should retain a lineage record. Do not rely on display names alone, and do not silently overwrite a parent species with a hybrid.

## 10. Multiplayer, performance, and exploit prevention

- Server-authoritative compatibility and offspring creation prevent duplicate births or client disagreement.
- Use stable lineage and parentage IDs.
- Bound mutation and recombination; prevent unlimited stacking of mutually exclusive traits.
- Do not let players repeatedly breed, reset, or transfer individuals to bypass costs, population caps, or discovery requirements.
- Use detailed individual simulation near active players and aggregate lineage statistics for distant populations.
- Preserve named, rare, quest-critical, or player-discovered individuals according to explicit world persistence rules.
- Cross-planet transfers must pass the landscape restoration system's compatibility and transfer-risk checks.
- Log significant lineage changes so unexpected population shifts can be investigated.

## 11. Acceptance tests before implementation is called complete

- [ ] Shared habitat alone never grants reproductive compatibility.
- [ ] A documented compatible cross can produce a viable hybrid under the correct conditions.
- [ ] An incompatible cross cannot produce ordinary hybrid offspring without a separately specified mechanism.
- [ ] Limited gene/trait transfer is distinguishable from hybrid reproduction.
- [ ] Sterile and reduced-fertility hybrids follow their declared rules.
- [ ] Offspring traits remain within allowed ranges and include documented trade-offs.
- [ ] A single hybrid individual is not automatically promoted to a new species.
- [ ] A stable derived lineage can be recognized after its configured criteria are met.
- [ ] Parentage, generation, and trait provenance remain traceable.
- [ ] Hybrid populations affect cohabitation, food webs, habitat, and carrying capacity.
- [ ] Rare or isolated hybrid populations can fail to establish or become extinct.
- [ ] Players cannot exploit breeding or transfers to create unlimited resources, traits, or populations.
- [ ] Multiplayer clients agree on offspring and lineage state.
- [ ] UI distinguishes unknown compatibility, confirmed incompatibility, viable hybrid, and established derived species.

**Evidence status:** Design-only. No cross-species breeding, hybrid generation, or species-emergence simulation is claimed implemented or tested.
