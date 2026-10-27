# Lethal Absorption — Resource Dossier: Reedlace Hostleaf

> **Stable ID:** VEY-RES-PLT-006  
> **Planet:** Veyra  
> **Status:** Design hypothesis; not implemented or tested  
> **Primary region:** Reedwater Basin wetland margins

## 1. Identity and ecological role

**Class:** Narrow-leaf marsh-edge perennial.  
**Primary role:** Larval host plant candidate for the Gloam Moth; secondary bank cover and small detrital input.

Reedlace Hostleaf grows in loose clusters along damp but not permanently submerged margins. Its long, flexible leaves bend with floodwater and form protected undersides where Gloam Moth eggs can be placed. The plant is deliberately distinct from Duskbell Bloom: Duskbell is a proposed adult food and pollination partner, while Reedlace Hostleaf supplies the larval feeding surface.

## 2. Habitat and life cycle

- **Habitat anchors:** Reedglass Marsh margins, sheltered Reedwater Run banks, and seasonally wet Southwash Fan where soil remains moist after water recedes.
- **Required conditions:** Moist rooted substrate, light, viable soil chemistry, and periodic oxygen access around the roots.
- **Poor conditions:** Prolonged deep submersion, severe dry-down, repeated trampling, contaminated runoff, and removal of the entire root crown.
- **Seasonal behavior:** Produces fresh leaves during suitable warm, wet periods; growth slows during cold or dry intervals.
- **Renewal:** Surviving root crowns and seed can restore a patch when moisture, light, and undisturbed growth time are available.
- **Failure states:** Repeated larval feeding can reduce leaf area; full patch removal eliminates local host availability until recolonization or regrowth occurs.

No growth rate, leaf stock, or regeneration timer is locked before resource simulation and balance testing.

## 3. Gloam Moth relationship

**Proposed interaction:** Gloam Moth lays eggs on suitable Reedlace Hostleaf; larvae consume limited leaf tissue.

The interaction must use separate states for eggs, larvae, damaged leaves, plant recovery, and adult emergence. Eggs do not guarantee successful larvae: weather, predation, host condition, and seasonal timing can cause failure.

Larval feeding should normally remove finite leaf biomass rather than instantly kill the whole plant. Severe repeated feeding may suppress growth or kill a weakened individual, but the patch must not support unlimited larvae. Gloam Moth reproduction is limited by viable host-leaf stock and suitable pupation cover.

Duskbell Bloom remains the adult feeding / potential pollination partner candidate. Reedlace Hostleaf is not automatically a pollination partner, and larval-host status does not prove that adult moths visit or pollinate it.

## 4. Player discovery and interaction

- **Clues:** Small scalloped leaf edges, silk-like attachment traces only if later supported by the species biology, eggs on protected leaf undersides, and larvae feeding at dusk or in sheltered periods.
- **Nonlethal study:** Observe damaged leaves, record patch condition, and compare feeding with plant recovery.
- **Harvest:** No harvest item or guaranteed drop is defined. Gathering leaves reduces the same local stock larvae need.
- **Absorption:** The plant is a resource/ecology record, not a creature absorption target. Any plant-derived trait must be separately designed and justified.

## 5. Food-web and simulation contract

- Reedlace Hostleaf → Gloam Moth larva: **Consumes**, conditional on leaf availability and life stage.
- Reedlace Hostleaf → wetland cover: **Habitat function**, conditional on patch density.
- Gloam Moth adult ↔ Duskbell Bloom: **Potential mutualism**, still unvalidated; pollen transfer and plant reproductive benefit must be tested separately.

Validation must cover host depletion, plant recovery, egg/larva failure, seasonal absence, and no-infinite-resource behavior. If Reedlace Hostleaf is absent or leaf stock is exhausted, local Gloam Moth reproduction must fall or fail rather than silently switching to an unspecified host.

**Evidence status:** Design hypothesis documented; not implemented or tested.
