# Lethal Absorption — Species Dossier: Glassfilm Microbe

> **Stable ID:** LA-PLN-MIC-001  
> **Planet:** Veyra  
> **Status:** Designed — concept dossier; not implemented or tested  
> **Design scope:** First-region microbial producer and early environmental teaching species.

## 1. Identity and originality

**Working name:** Glassfilm Microbe  
**Functional role:** Photosynthetic or light-assisted microbial biofilm producer, surface stabilizer, and early nutrient source.  
**Originality note:** An original fictional microorganism inspired by broad real-world biofilm ecology. It is not intended to represent a specific real species.

This organism forms thin, translucent, slightly iridescent films on damp stone, submerged rock, shaded roots, and the margins of slow water. The “glass” quality is a visual nickname, not actual glass or a brittle mineral shell. A mature colony may appear as a faint rainbow sheen when wet and become nearly invisible when dry.

## 2. Body plan and life cycle

- **Body plan:** Microscopic single cells embedded in a hydrated extracellular matrix; visible gameplay encounters represent a colony, not a single cell.
- **Scale:** Individual cells are microscopic. Detectable patches range from a fingertip-sized sheen to connected mats spanning several stones. Exact dimensions are reserved for simulation scale.
- **Life stages:** Dispersed cell → attached microcolony → connected film → stressed dormant patch → renewed growth after suitable moisture and light return.
- **Reproduction:** Cell division and fragmentation of the film; water movement carries fragments downstream. No sexual system is established.
- **Lifespan:** Individual cells are short-lived relative to the persistent colony, which can survive cycles of stress through dormant or low-activity patches.
- **Mortality:** Prolonged drying, abrasive scouring, toxic contamination, intense heat, or burial under sediment can kill or displace a patch. Recovery is possible only if viable cells remain or new cells arrive.

## 3. Habitat and distribution

**Primary habitat anchors:** Reedwater Run, Reedglass Marsh margins, First Drip Hollow, Mossbank Edge, and the wet lip of Quietroot Grotto. These are habitat links, not final spawn coordinates.

**Preferred conditions:** Damp mineral surfaces, shallow clear water, moderate light, slow flow, and access to dissolved nutrients.  
**Avoids or weakens in:** Frequently scoured channels, thick mobile sediment, long dry spells, heavy shade, toxic runoff, and rapidly changing water chemistry.

Seasonal floods can spread fragments while also stripping exposed colonies. Dry spells reduce active coverage but may leave protected refuges. The colony is common enough to teach pattern recognition, but should not blanket every wet surface.

## 4. Senses, interaction, and player-readable clues

The colony has no centralized nervous system or intentional pursuit behavior. It responds locally to light, moisture, nutrient availability, and chemical stress.

- **Visual clue:** Subtle rainbow sheen at a low angle; a dull matte trace on stressed patches.
- **Touch clue:** Slightly slick surface; no hard collision or glass-shard hazard.
- **Slime sensory clue:** Chemical sampling may distinguish nutrient-rich active film from a depleted or contaminated patch after the relevant cue has been taught.
- **Vibration clue:** The film itself is not a meaningful long-range vibration detector. Contact can transmit local surface texture only.
- **Misleading cues:** Reflections can resemble wet mineral or insect wings; contaminated film may smell chemically “rich” without being safe.

## 5. Ecology and food-web hypotheses

**Primary contribution:** Uses light and dissolved nutrients to produce biomass and bind fine particles, creating a basal food resource and small refuges for microbes and minute grazers.

**Proposed interactions — require later simulation validation:**
- Provides a potential grazing surface for Reed Skipper juveniles and other microscopic feeders.
- May be disturbed by Silt Burrower sediment movement and by flood scouring.
- Adds organic matter when cells die, supporting decomposition.
- Can modestly reduce loose-particle movement on stable wet rock; it does not prevent major erosion or flooding.
- Competes with Ember Mat and Brine Lace only where their environmental tolerances overlap; no global microbial dominance.

These are design hypotheses, not verified food-web edges. A species or biome implementation must not treat them as proven until a simulation or explicit design review records the result.

## 6. Resources and collection

- **Nonlethal study:** Inspect the sheen, compare wet and stressed patches, and revisit after a water-level change.
- **Possible resource:** Trace biomass or a low-tier membrane/nutrient-processing research sample, available only after a suitable collection ability is learned.
- **Collection rule:** Taking a small sample should have negligible local impact; scraping a large fraction reduces cover and the microhabitat it provides.
- **Renewal:** Regrowth depends on moisture, light, nutrient access, and surviving cells. A scraped dry or polluted site must not instantly replenish.
- **No free power:** The film does not grant a finished ability merely by being touched or consumed.

## 7. Absorption and evolution compatibility

**Player absorption:** The Glassfilm Microbe is not a creature-sized live-prey target. Early Slime interaction is limited to safe trace sampling or low-volume biomass uptake once the relevant capability is available.

**Potential learning outcomes:** Basic nutrient processing, recognition of biofilm-like surfaces, and improved interpretation of some dissolved-nutrient traces. These are candidate progression outcomes, not automatic unlocks.

**Risks and limits:** Contaminated film may carry toxins or irritants; excessive intake can burden a primitive digestive system. Biomass is low-value and cannot substitute for the full progression loop of observing, analyzing, adapting, and mastering.

**Compatibility conflicts:** No direct combat trait, eye branch, or large-body anatomy should be inferred from this microbe. Any biochemical adaptation requires later evidence and a defined cost.

## 8. Abilities, training, and mastery

This organism is not a trainer and has no intentional abilities. Environmental study may contribute to these Slime learning records:

| Candidate record | Learning evidence | Limitation |
|---|---|---|
| Nutrient Trace Reading | Compare active, depleted, and contaminated films | Chemistry varies by location and weather |
| Surface Biofilm Processing | Safely process a small sample after a compatible digestive adaptation | Not a combat ability; low biomass yield |
| Flood-Spread Ecology | Observe film distribution before and after a flood | Requires repeated visits; not an instant skill |

All entries remain candidate design hooks until connected to the skill atlas and implemented.

## 9. AI and simulation contract

The colony requires only local environmental state, not creature-style pathfinding.

- State variables: moisture, light exposure, dissolved nutrient availability, contamination, sediment cover, and recent scouring.
- State transitions: dormant/stressed ↔ active growth ↔ fragmented/displaced ↔ depleted/dead patch.
- Spatial behavior: expand slowly across suitable connected surfaces; spread fragments only through plausible water flow.
- Conservation rule: biomass cannot appear instantly; growth must consume environmental resources and respect suitable conditions.
- Debug evidence: patch coverage, state transitions, nutrient consumption, flood displacement, and regrowth should be inspectable in simulation logs.

No numerical growth rates, nutrient yields, or global population totals are established in this design.

## 10. Regional variants and discovery

- **Run sheen:** Better exposed to moving water; more frequently fragmented.
- **Marsh-edge film:** More tolerant of variable water chemistry; more often sediment-covered.
- **Grotto film:** Slow-growing and shade-adapted; less visually obvious.
  
These are proposed ecological forms, not separate species or finalized stat variants. Discovery should teach the player that a similar-looking sheen can have different condition and safety states.

## 11. Accessibility, counterplay, and unresolved decisions

- Do not require color discrimination alone: pair sheen with shape, surface context, and sensory cues.
- Do not make the organism a mandatory grind gate. Alternative early nutrient sources must remain available.
- Environmental hazards should be telegraphed through observable changes before the colony becomes lethal or unusable.
- Confirm later: exact metabolism, light dependence, safe sample size, and whether microbial knowledge unlocks any player-facing skill.
- Confirm later: precise links to Reed Skipper and Silt Burrower through ecology review and simulation.
- Confirm later: final visual palette and biome-specific density.

## 12. Completion audit

- [x] Stable ID, role, body plan, life stages, habitats, cues, ecology hypotheses, resource rules, absorption limits, and simulation contract documented.
- [ ] Cross-linked into runtime species data and biome population tables.
- [ ] Food-web hypotheses reviewed and validated.
- [ ] Skill atlas links finalized.
- [ ] Balance, accessibility, and simulation tests passed.

**Evidence status:** Design authored in repository; no implementation or test evidence yet.
