# Lethal Absorption — Veyra Native Plant and Resource Atlas

> **Status:** Design authored; not implemented or tested. Resource names and ecology are proposed canon candidates pending review.

## 1. Purpose

The Reedwater Basin food web needs named renewable resources before a simulation can make meaningful decisions about feeding, reproduction, harvest, and recovery. This atlas establishes an initial set of original Veyran plants and resource-producing organisms. It avoids treating "grass", "flowers", or "detritus" as infinite generic inventory items.

## 2. Resource record contract

Every resource used by runtime ecology must identify:
- Stable ID and display name.
- Resource class and physical location.
- Producing organism or environmental process.
- Species that consume, depend on, or harvest it.
- Stock and renewal conditions; depletion effects.
- Seasonal behavior and dispersal limits.
- Safe/unsafe handling flags where relevant.
- Evidence state: design hypothesis, mechanic specified, implemented, or tested.

No numeric stock, growth rate, harvest amount, or respawn timer is locked until it has a design rationale and is balanced in tests.

## 3. Initial plant and resource records

### VEY-RES-PLT-001 — Reedglass Reedgrass

- **Class:** Wetland emergent plant.
- **Primary habitat:** Reedwater Run, Reedglass Marsh, Siltbend Oxbows.
- **Function:** Rooted bank cover, seed resource, and potential food for small wetland grazers.
- **Dependencies:** Moist substrate, viable water level, light, and a tolerable sediment/oxygen regime.
- **Renewal:** Regrows from surviving roots and seed when water and substrate conditions are suitable.
- **Failure modes:** Prolonged dry-down, severe scour, contamination, or repeated removal before regrowth.
- **Ecology links:** Candidate food and shelter source for Reed Skipper; candidate shoreline cover for Current Dart and Reedstalker. These are not confirmed feeding edges merely because the species share habitat.

### VEY-RES-PLT-002 — Silverleaf Bankfern

- **Class:** Moisture-tolerant understory fern.
- **Primary habitat:** Mossbank Edge, Quietroot Grotto entrance, shaded woodland channels.
- **Function:** Leaf litter, small-animal cover, and a potential browse source.
- **Dependencies:** Shaded damp soil, stable rooting substrate, and seasonal moisture.
- **Renewal:** Frond replacement and local spore establishment under suitable conditions.
- **Failure modes:** Extended drought, soil disturbance, and canopy/cover loss.
- **Ecology links:** Candidate browse for Moss-Horn Browser; leaf litter contributes to detrital resources. Diet acceptance must be specified before enabling consumption.

### VEY-RES-PLT-003 — Duskbell Bloom

- **Class:** Night-opening flowering plant.
- **Primary habitat:** Longgrass Shelf margins, Mossbank Edge clearings, Elderbank Stand openings.
- **Function:** Nectar-like adult food and a potential pollination partner for Gloam Moth.
- **Dependencies:** Suitable seasonal temperature, water, viable soil, and access to a compatible pollinator or alternate reproduction route.
- **Renewal:** Seasonal flowering and seed production; seedling recruitment depends on open microsites.
- **Failure modes:** Drought during flowering, repeated flower removal, and loss of connected flowering patches.
- **Ecology links:** Potential mutualism with Gloam Moth only if pollen transfer and plant reproductive benefit are demonstrated. This atlas does not declare that test passed.

### VEY-RES-PLT-004 — Rootmilk Tuber

- **Class:** Perennial tuber-forming understory plant.
- **Primary habitat:** Longgrass Shelf margins, Mossbank Edge, and suitable soils around Elderbank Stand.
- **Function:** Energy-rich underground storage organ; candidate food for Root-Crown Forager.
- **Dependencies:** Diggable soil, seasonal water, and enough undisturbed time to replenish storage tissue.
- **Renewal:** Regrowth from retained viable plant tissue and seed recruitment where conditions permit.
- **Failure modes:** Repeated excavation, soil compaction, prolonged drought, or waterlogging outside tolerance.
- **Ecology links:** Candidate resource for Root-Crown Forager. Harvesting the whole tuber can kill the individual plant; partial harvest rules must be defined.

### VEY-RES-PLT-005 — Mossveil Groundmat

- **Class:** Low-growing moss-like ground cover.
- **Primary habitat:** First Drip Hollow, damp stones near Quietroot Grotto, and shaded wet banks.
- **Function:** Moisture-retaining cover and a substrate for microbial films.
- **Dependencies:** Persistent surface moisture, suitable attachment surface, and tolerable chemistry.
- **Renewal:** Slow edge growth and spore establishment; bare patches remain bare when conditions are unsuitable.
- **Failure modes:** Drying, scraping, contamination, and repeated trampling.
- **Ecology links:** Habitat support for Glassfilm Microbe is plausible but not automatic; compatibility must be recorded per surface type.

### VEY-RES-FNG-001 — Glasscap Fungal Film

- **Class:** Fungal growth on damp deadwood and protected bark.
- **Primary habitat:** Elderbank Stand and shaded Mossbank Edge.
- **Function:** Candidate food for Bark Lantern and contributor to deadwood decomposition.
- **Dependencies:** Suitable wood, moisture, temperature, and colonization source.
- **Renewal:** Slow colonization and growth; harvested or removed patches need time and viable source material to return.
- **Failure modes:** Deadwood removal, desiccation, toxic contamination, and disturbance.
- **Ecology links:** Candidate feeding resource for Bark Lantern. This is distinct from Glassfilm Microbe; names do not imply taxonomy or direct interaction.

### VEY-RES-AQU-001 — Driftplankton Cloud

- **Class:** Aggregated drifting microscopic food resource, not one named animal species.
- **Primary habitat:** Oxygenated flowing channels and connected oxbow water.
- **Function:** Candidate food for Current Dart.
- **Dependencies:** Water chemistry, nutrient availability, oxygen, temperature, and flow.
- **Renewal:** Reproduction and transport from viable source water; local stock falls when consumed or flushed away.
- **Failure modes:** Anoxia, contamination, extreme temperature, or loss of source connectivity.
- **Ecology links:** Current Dart may filter or pick up the cloud only after its feeding animation and intake mechanics are specified. It is not assumed to be Glassfilm Microbe.

### VEY-RES-DET-001 — Basin Detritus Pool

- **Class:** Finite local pool of decomposing organic matter.
- **Primary habitat:** Sediment, leaf litter, and low-flow deposition zones.
- **Function:** Resource pool for detritivores and sediment-associated organisms.
- **Dependencies:** Organic inputs and decomposition under suitable moisture/oxygen conditions.
- **Renewal:** Material enters through plant litter, waste, and remains; conversion and consumption must conserve quantities.
- **Failure modes:** Exhaustion, oxygen collapse, contamination, or export by high flow.
- **Ecology links:** Candidate resource for Silt Burrower and Root-Crown Forager. Detritus must not generate itself without an input source.

## 4. Named host plant requirement for Gloam Moth

**Initial host candidate:** Duskbell Bloom is the adult food/potential pollination partner, but it is not automatically the larval host.

The larval host remains **unassigned** until a separate plant life-stage record confirms that Gloam Moth larvae can consume a named plant part without immediately killing the host population. Do not enable larval feeding against Duskbell Bloom just because adults visit its flowers.

Recommended next plant record: **VEY-RES-PLT-006 — Reedlace Hostleaf**, a narrow-leaf marsh-edge plant proposed as a Gloam Moth larval host. It should remain a hypothesis until a dossier defines larval feeding tolerance, plant recovery, seasonal availability, and whether feeding is destructive or sustainable.

## 5. Harvest and renewal invariants

1. Harvest cannot reduce a resource below zero.
2. Consumption, harvesting, decomposition, and transport must be explicit transfers or losses, not hidden creation.
3. A resource only renews if its prerequisites are met.
4. A plant's survival and regeneration must be separate from harvestable stock.
5. Removing habitat structures such as deadwood can remove multiple dependent resource patches.
6. A resource that is absent from a local patch cannot be harvested there merely because the species exists elsewhere on Veyra.
7. The game must show meaningful depletion cues before irreversible ecological collapse when player action is the cause.
8. Resource renewal should be testable with fixed starting stocks and reproducible environmental conditions.

## 6. Validation checklist

- [ ] Plant and resource IDs are unique and referenced consistently.
- [ ] Reed Skipper, Moss-Horn Browser, Root-Crown Forager, Bark Lantern, Current Dart, and Silt Burrower have named resource links.
- [ ] Gloam Moth larval host is selected and documented before its feeding edge is enabled.
- [ ] Each resource has stock, renewal conditions, and depletion effects defined before simulation.
- [ ] No harvest/renewal loop creates unlimited matter or energy.
- [ ] Flood, dry spell, and overharvest scenarios produce explainable changes.

**Evidence status:** Design authored; no resource simulation or biological interaction has been implemented or tested.
