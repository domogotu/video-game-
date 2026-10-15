# Lethal Absorption — Live Prey Capture and Stamina-Driven Absorption

> **Status:** Approved design direction; design-only, not implemented or tested.
>
> **Scope:** Universal combat and hunting mechanic for eligible playable species and abilities. This is not a Slime-only mechanic.
>
> **Core rule:** The player must create and recognize a live-capture opportunity during combat. There is no universal “press this button to absorb” prompt that replaces the encounter. The player initiates and maintains a grab/engulf attempt through the relevant held input, and stamina is the primary cost.

## 1. Intended player experience

Hunt and track a target using evidence, senses, terrain, and preparation. When combat begins, the player can weaken the target and then choose whether to continue attacking, disengage, or attempt live capture. The target must still be alive when the capture attempt begins. If its health reaches zero first, the live-prey opportunity is lost.

Capture is an active contest, not a menu action or guaranteed finisher. The target can struggle, counter, flee, call for help, exploit terrain, or receive assistance from allies. The player must decide whether they have enough stamina and a safe enough position to commit.

## 2. Encounter flow

1. **Track:** Read footprints, scent, disturbed vegetation, sound, environmental signs, and other unlocked sensory clues. Evidence is imperfect and may be stale or misleading.
2. **Locate and assess:** Identify the prey, nearby allies, escape routes, hazards, and potential reinforcements.
3. **Engage:** Use attacks, positioning, movement, and learned abilities. Ordinary damage reduces health; control effects and body mechanics can create openings.
4. **Create an opening:** The target becomes capturable only when its current condition permits it. Eligibility depends on target type, remaining health, posture/stagger or other qualifying state, relative size/strength, resistance, and relevant abilities. Do not use one universal health percentage for every creature.
5. **Commit to the hold:** The player must be in valid range and position and use the applicable held grab/engulf input. The hold is not an automatic prompt or guaranteed success.
6. **Contest:** Stamina is spent to initiate and maintain the attempt. The target reacts, struggles, counters, escapes, or signals allies. The player can be interrupted or forced to release.
7. **Resolve:** If the hold completes and the target is eligible, absorption begins according to the character's abilities and target rules. If the target escapes, the player releases, stamina is exhausted, or an interruption succeeds, the attempt fails and combat continues.
8. **Aftermath:** The world responds to visible or audible evidence: allies may investigate, prey may flee, predators may approach, and surviving groups may remember the encounter.

## 3. Resource rules: stamina first

- **Stamina is the primary cost** for physical pursuit, grappling, restraining, holding, struggling against resistance, and maintaining a live absorption attempt.
- Starting a capture attempt has a stamina commitment; maintaining the hold drains stamina over time. Powerful, larger, struggling, or highly resistant prey can increase the drain.
- Low stamina reduces the player's ability to maintain control and increases the risk of escape or interruption. The exact thresholds and drain rates require balancing.
- Movement, dodging, sprinting, heavy attacks, and other exertion may compete for the same stamina reserve. The player must choose between continuing pressure and saving enough stamina to secure the capture.
- **Energy remains separate** for designated supernatural, elemental, ranged, or otherwise energy-based abilities. Routine grabbing and holding do not default to energy costs unless a particular ability explicitly changes the rule.
- Biomass, digestion capacity, compatibility, and trait-storage limits govern what happens after successful absorption; stamina alone does not guarantee that any target can be absorbed.
- No infinite hold, infinite resource conversion, or stamina-free repeated capture loop.

## 4. No universal capture button prompt

The interface must not simply announce “Press X to absorb” whenever a health threshold is reached. The player learns the system through animation, creature behavior, sensory feedback, combat knowledge, and the character's available controls.

The applicable grab/engulf input may be held to maintain the attempt. Contextual UI can communicate stamina drain, grip stability, target resistance, and interruption risk, but it must not make the decision for the player or imply that a target is guaranteed to be capturable. Accessibility options may make state information clearer without removing the active contest.

Controls must be remappable and support controller, keyboard/mouse, and accessibility needs. Exact input mapping is a platform/control-layout decision.

## 5. Target behavior and agency

While under pressure, an enemy uses its own assessment and capabilities to select among responses such as:
- Fight back or use a counterattack.
- Break contact and flee toward cover or a known escape route.
- Call, signal, or make noise to alert nearby allies.
- Guard a vulnerable body area or resist engulfment.
- Use terrain, water, narrow passages, verticality, or environmental hazards.
- Exploit a player's low stamina, poor position, or overcommitment.
- Receive aid from allies that distract, attack, interrupt, or attempt to free it.
- Play dead, feint, or change behavior only where that species or character has a credible capability to do so.

AI must be evidence-driven, not omniscient. It reacts to what it senses or can plausibly infer; it does not teleport to allies or instantly know hidden player state.

## 6. Multiple enemies and special prey

Capture attempts create vulnerability. While the player is holding one target, other enemies can attack, flank, call reinforcements, or attempt to interrupt. The player may need to separate the target from its group, exhaust nearby threats, use terrain, or accept the risk of being interrupted.

Special, elite, Alpha, boss, or unusually large prey may require additional prerequisites or a unique contest. Some targets may be impossible to absorb directly, may resist beyond the player's current capabilities, or may require a special ability or story-defined resolution. Their rules must be communicated through clues and encounter behavior rather than a generic prompt.

A target's capture eligibility should be contextual, not just “health below X.” Health is one factor among vulnerability, size, anatomy, resistance, current state, and the player's abilities.

## 7. Successful absorption is not automatic mastery

A successful live absorption can open a later process of digestion, safety checks, analysis, trait eligibility, adaptation, and mastery. It must not automatically grant every skill or ability of the target. Incompatible material can be rejected, require stabilization, or cause a bounded drawback.

Sapient beings retain agency and are not interchangeable loot containers. Any absorption involving sapient characters needs explicit world, narrative, and gameplay rules and must not silently turn people into ordinary ingredients. Existing protections against permanent PvP character death and theft of progression/assets remain absolute.

## 8. Failure states and counterplay

Capture can fail if:
- The target is already dead or becomes dead before the live hold begins.
- The player is out of range, badly positioned, or lacks the required body capability.
- Stamina is insufficient to initiate or maintain the attempt.
- The target breaks free, counters, or forces a release.
- An ally or environmental event interrupts the hold.
- The target's anatomy, size, armor, traits, or special status makes it ineligible for that attempt.
- The player's own control, stability, or absorption capacity is insufficient under the specific rules.

Failure should have readable causes and meaningful consequences, not arbitrary hidden rolls. The target may escape, reposition, call for help, or resume fighting. The player should retain control and be able to respond.

## 9. Tuning and fairness

Exact stamina costs, capture windows, hold duration, struggle strength, health eligibility, and resistance scaling are intentionally not hard-coded in this design document. They should be data-driven and tuned per target family, player form, ability rank, and difficulty.

Avoid a single dominant strategy. Fast damage, stamina preservation, tracking, ambush, crowd control, and team coordination should all matter. Do not let a low-health target become an automatic free capture. Do not let every enemy escape without counterplay either.

PvP cannot permanently kill the player or permanently remove owned assets/progression. If live capture is permitted in PvP, it must obey those protections and have explicit release, rescue, duration, and counter rules.

## 10. HUD and feedback requirements

During a hold, show enough information to support decisions:
- Player stamina remaining and current drain.
- Grip/hold stability or contest progress, where appropriate.
- Target resistance or struggle state, conveyed through clear visual/audio cues.
- Nearby interruption danger when the player has evidence of it.
- Clear feedback for successful completion, forced release, voluntary release, and failure.

Avoid a universal “absorb now” marker. The encounter state, target animation, prior knowledge, and the player's deliberate held input should communicate the opportunity.

## 11. Acceptance criteria before implementation is considered complete

1. The mechanic works across eligible species and body plans, not only Slime.
2. A dead target cannot be live-captured; the player must begin before health reaches zero.
3. The player must actively initiate and maintain the hold; no universal prompt performs absorption automatically.
4. Stamina is the primary resource for physical grab/hold/struggle actions; energy is only used where a defined ability requires it.
5. Target behavior can include struggle, escape, counterattack, alarm/call for help, and ally intervention when plausible.
6. Multiple enemies can create meaningful interruption risk.
7. Eligibility reflects more than a single universal health percentage and is data-driven.
8. Success/failure feedback is clear and supports accessibility without removing player agency.
9. Absorption results obey digestion, compatibility, mastery, and sapient-agency rules.
10. PvP protections and multiplayer-authoritative validation cannot be bypassed.
11. Save/load, multiplayer synchronization, resource accounting, and edge cases are tested against actual implementation before claiming completion.

**Implementation status:** Design-only. This document does not claim the combat, stamina, capture, AI response, absorption, UI, or tests are implemented.
