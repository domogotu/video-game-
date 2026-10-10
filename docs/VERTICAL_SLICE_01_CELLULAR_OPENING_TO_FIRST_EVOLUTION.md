# Vertical Slice 01: Cellular Opening to First Evolution

**Project:** Lethal Absorption  
**Status:** Bounded gameplay design specification; not implemented or play-tested.  
**Purpose:** Freeze the smallest representative slice that proves the simple opening, basic controls, staged menu onboarding, earned evolution cinematic, and transition into animal-scale exploration.

## 1. Slice Objective

Prove that a player can learn the basics in a simple colorful cellular environment, grow through understandable actions, make at least one meaningful evolutionary choice, and transition into a distinct animal-scale survival region without being overwhelmed by systems.

This slice is not the full first stage, the full animal stage, or a complete game. It is the minimum representative sequence used to judge whether the central premise works.

## 2. Scope Boundary

### Included
- One compact, colorful, futuristic cellular environment.
- One player cell with readable movement and absorption feedback.
- A small set of nutrient types and a limited number of hazards/predators.
- Basic movement, absorb/gather, dodge, and a simple attack once taught.
- A clear growth meter and short-term milestones.
- Contextual introductions to the basic HUD, inventory/resource view, discovery log, and evolution/skill tree.
- One early trait choice that has a visible gameplay effect.
- A threshold-based evolution cinematic reflecting the player's recorded trait choice and absorption history.
- One bounded animal-scale environment loaded after the cinematic.
- A new body plan and a short safe introduction to animal movement, gathering, evasion, and basic combat.
- A clear first objective after transition.
- A saved progression summary that records the player's choices and explains which prior capabilities carry forward.

### Excluded from this slice
- Multiplayer networking and PvP.
- Full open world or planet-scale streaming.
- Space travel and Living Ship Form.
- Full 100-species catalogue or complete Evolution Atlas.
- Large-scale destruction, cosmic abilities, raids, and endgame bosses.
- Full crafting economy, settlements, faction simulation, or procedural story.
- Every possible cell-to-animal evolutionary route.
- Production-quality cinematics and final visual assets; use representative storyboard/animatic requirements during design review.

Excluded features remain backlog items; they are not deleted from the overall vision.

## 3. Opening Sequence and Teaching Order

### Beat 1 — Enter the micro-world
Show the player in a clean, vibrant micro-environment with a small number of visible nutrients, currents or terrain cues, and one non-lethal environmental hazard. Keep the screen uncluttered. The player can immediately move.

**Teach:** movement only.  
**Exit:** player can steer, stop, and reach a nearby safe nutrient cluster.

### Beat 2 — Gather and absorb
Highlight a nearby safe nutrient with a subtle visual cue. On approach, teach the absorb input and show the growth meter increase. The cue fades once the player understands the action.

**Teach:** gathering/absorption.  
**Exit:** player successfully absorbs enough nutrients to see a clear growth response.

### Beat 3 — Read danger and dodge
Introduce one readable predator or moving hazard with an unmistakable approach cue and a safe escape route. Teach dodge after the player has experienced the danger cue, not before.

**Teach:** danger recognition and dodge.  
**Exit:** player avoids one threat using movement or dodge and understands why the attempt succeeded.

### Beat 4 — Learn a simple attack
Only after the first survival actions are understood, introduce a small hostile target or practice opportunity that can be handled with a simple attack. Do not force the player to attack every creature; evasion remains valid where the space permits it.

**Teach:** attack and target feedback.  
**Exit:** player successfully uses the attack or safely disengages and understands the basic combat option.

### Beat 5 — Introduce the first menu when it has a purpose
After the player earns the first meaningful growth milestone, reveal the resource/inventory view and one simple discovery record. Later, reveal the evolution/skill tree at the first trait decision. Do not expose every menu in the opening minute.

**Teach:** only the menu relevant to the current decision.  
**Exit:** player can find their current resource, see a discovered fact, and understand the available evolution choice.

### Beat 6 — Make one meaningful trait choice
Offer two clearly different, balanced starter adaptations, for example:
- **Current-Sensitive Membrane:** improves movement/control in currents or reveals current direction.
- **Impact-Resistant Membrane:** reduces the effect of one defined environmental collision or minor attack.

These are example candidates, not final names or locked balance. The final pair must be mutually understandable, show trade-offs, and support different approaches without making one a mandatory best choice.

**Teach:** evolution choice and consequence.  
**Exit:** player selects a trait, sees it recorded, and experiences its effect in the remaining cellular play.

### Beat 7 — Earn the transition
The player must meet the defined growth threshold and complete the essential learning beats. A clear progress indicator communicates the remaining requirement. Do not require hidden actions or repetitive grinding after the required condition is met.

When ready, offer a clear evolution moment. Save the current evolution history, then play the transition cinematic.

**Exit:** transition conditions are visible and met; the player understands why evolution is happening.

### Beat 8 — Cinematic and animal-scale arrival
Show the cell's growth into an organism whose anatomy reflects the selected trait and acquired biological history. The scene should show continuity without pretending every microscopic detail must directly determine the final body. The new environment is larger, but bounded and designed for performance.

After arrival, teach the new movement/camera model and the immediate survival objective in context. Avoid repeating the entire first tutorial.

**Exit:** player can move, gather, and avoid a threat as the new organism, and can explain the immediate goal.

## 4. First Transition Contract

The transition from cell to animal is the proof of the game's multi-game structure. It must meet all of these requirements:
1. The trigger is based on visible growth and completed essential actions, not a hidden timer.
2. The player’s chosen starter trait affects at least one visible feature or behavior of the evolved organism.
3. The cinematic can be skipped or replayed through a recap without losing progression.
4. The transition saves the character’s trait and absorption history before changing stage.
5. The new stage has a distinct camera/movement feel and a different scale of navigation.
6. The new stage starts with a clear safe-area objective and one manageable danger.
7. The new stage introduces only the controls and menus needed now.
8. The player is not forced to repeat the cellular tutorial.
9. The new environment is bounded, navigable, and has a planned active-entity budget.
10. No unexplained loss of an ability, resource, or trait occurs during transition.

## 5. Animal-Scale Arrival Area

Use one bounded habitat that can demonstrate a few different interactions without requiring a huge world. A candidate layout includes:
- **Arrival clearing:** safe onboarding and a visible landmark.
- **Gathering patch:** food or biomass with at least two resource choices.
- **Cover route:** vegetation, rocks, or terrain to hide or break line of sight.
- **Water edge or shallow pool:** introduces water as a readable environmental option only if the starting body can safely interact with it.
- **Threat zone:** one predator or hostile creature with readable detection and pursuit behavior.
- **Shelter/den landmark:** a memorable location that can later serve as a return point or objective.

Do not require all these features if the slice becomes too large. The minimum must have a safe arrival, a resource location, a usable route/cover option, and one readable threat.

The animal-stage region should feel spacious through composition, sightlines, landmarks, and route choices—not through empty acreage. Limit simultaneous active creatures and effects. Distant ecosystem state may be summarized rather than fully simulated.

## 6. Basic Interaction Rules

- **Movement:** immediately responsive and suited to the current body plan.
- **Absorption:** requires a valid target/resource, range, and a short clear interaction; no silent auto-grant of every trait.
- **Dodge:** has a defined cost or recovery window and cannot be repeated indefinitely without consequence.
- **Attack:** communicates range, hit, miss, and target response. Avoid a long combat tutorial before the player understands survival.
- **Growth:** every gain is visible and the threshold is explainable.
- **Discovery:** the game distinguishes observed information from confirmed unlocks.
- **Evolution:** previews the selected trait's effect and any meaningful trade-off.
- **Persistence:** the selected trait and essential stage-transition state survive leaving and re-entering the slice.

Exact numbers, control bindings, animation timings, and final art are intentionally not frozen until a playable prototype or controlled usability test can inform them.

## 7. First-Slice Acceptance Checklist

Mark the slice design ready for implementation handoff only when all mandatory items below are satisfied:

- [ ] Opening objective is understandable without a wall of text.
- [ ] Movement is the first mechanic taught.
- [ ] Absorption/gathering is taught before advanced menus.
- [ ] Dodge is taught in response to a readable threat.
- [ ] Attack is taught only after basic survival actions.
- [ ] Menus appear contextually and in the right order.
- [ ] At least two starter trait choices produce meaningfully different effects.
- [ ] Growth and transition requirements are visible.
- [ ] The transition cinematic reflects the chosen path.
- [ ] The animal-scale area has explicit boundaries and a limited entity budget.
- [ ] The first animal-stage objective and immediate danger are clear.
- [ ] The character's history and chosen trait carry through the transition.
- [ ] Skipping the cinematic does not skip required information or break continuity.
- [ ] Failure and recovery are defined for each essential interaction.
- [ ] All out-of-scope features are recorded rather than quietly pulled into the slice.

## 8. Exit Decisions — Resolved Design Baseline

The five required design decisions are resolved provisionally by the working defaults in Section 9. They are sufficient to freeze the **design scope** for implementation planning; exact numeric tuning remains subject to prototype evidence.

- Starter traits: Current-Sensitive Membrane and Impact-Resistant Membrane.
- Evolution trigger: visible growth threshold plus demonstration of movement, absorption, dodge, and attack once; killing is not required.
- Animal-stage layout: compact habitat with arrival clearing, nearby resource patch, cover route, and one readable threat.
- Camera: first-person-forward as the baseline, with an optional third-person setting if feasible; camera must not change combat rules.
- Simulation budget: one active threat in the immediate onboarding path, a small handful of neutral/resource creatures nearby, and no off-screen high-cost simulation.

The consistency review must preserve these decisions and verify that the predator-prey/diet demonstration remains small enough for the slice. New ideas go to the backlog unless they block an acceptance criterion. Do not expand the full species catalogue, cosmic endgame, or planetary systems within this slice.


## 9. Working Defaults to Prevent Design Stalling

Use these defaults to move the slice forward. They are provisional design decisions for the first prototype, not final balance values. Change them only if review or playtesting reveals a concrete problem.

1. **Starter traits:** Keep the two proposed options: Current-Sensitive Membrane and Impact-Resistant Membrane. Each must provide one immediately observable advantage; neither grants a universally superior build.
2. **Evolution trigger:** Require the growth meter to reach its threshold and the player to demonstrate movement, absorption, dodge, and attack at least once. A safe evasion or disengagement counts as successful survival; do not require killing a creature. Display the requirements and progress clearly.
3. **Animal-stage camera:** Use an immersive first-person-forward presentation to support the animal-exploration fantasy. Preserve body/ability readability through contextual animation, shadow/reflection when appropriate, sensory cues, and an optional third-person camera setting if feasible. Camera choice must not change combat rules.
4. **Arrival layout:** Use one compact habitat with an arrival clearing, a nearby resource patch, a cover route, and one readable threat. Treat water as optional for this first slice unless safe swimming/breath rules are included in scope.
5. **Simulation budget:** Begin with one active threat at a time in the immediate onboarding path, a small handful of neutral/resource creatures nearby, and no off-screen high-cost simulation. Exact counts are implementation targets to validate, not promises about final capacity.
6. **Minimal living-ecosystem proof:** Include one predator and one prey species with readable hunt/escape behavior, plus a bounded diet-driven growth or condition change and one possible adaptation clue. This is a small observable demonstration—not a full food-web simulation, a required rare mutation, or a complex Alpha encounter. Keep it outside the first control-teaching beats so the opening remains simple.

### Step status clarification

The vertical-slice design baseline is **SCOPE FROZEN FOR IMPLEMENTATION HANDOFF**, subject to the single consistency review and correction pass recorded in the project audit. The predator-prey/diet proof in item 6 is included as a tightly bounded ecosystem requirement. Exact numeric counts and rates remain prototype tuning items. This is design closure only; do not label the slice implemented, play-tested, or fully verified.
