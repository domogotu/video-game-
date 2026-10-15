# Lethal Absorption — Ultimate and Secret Skill Framework

> **Status:** Approved design direction / design-only. This is a shared design standard, not evidence that skills, unlock logic, combat behavior, or UI have been implemented or tested.

## Purpose

Ultimate and secret skills should feel earned, personal, and consequential. **Absolute Nullification** is the reference standard for the level of mechanical specificity expected of major signature abilities: a clear fantasy, explicit activation conditions, defined effects, prerequisite branches, resource rules, counters or boundaries, readable presentation, and acceptance tests.

This standard applies across the roster—not just to the slime. It does not mean every character receives immunity or copies the slime's damage-conversion system. Each character's ultimate must express that character's biology, training, discoveries, combat identity, and world history.

## Core principles

1. **Earned, not handed out:** Level alone rarely grants a secret or signature ultimate. Qualifying actions, discoveries, research, training, environmental survival, unusual encounters, or mastery should establish eligibility.
2. **Discovery before full disclosure:** Hidden routes are not advertised as complete powers at character creation. Clues should make the route discoverable; after discovery, the Codex and Atlas explain confirmed requirements and progress.
3. **Separate progression states:** Track discovery, eligibility, unlock/acquisition, evolution or upgrade, mastery, loadout/equipping, and activation as distinct states.
4. **Conditions matter:** Activation may require a compatible form/anatomy, a resource threshold, stable traits, a target or environment, a charge state, a deliberate input, or a tactical condition. Show unmet conditions clearly.
5. **Power changes play, not only numbers:** An ultimate may change movement, defense, perception, command, resource conversion, body plan, battlefield control, or available combo routes—not merely multiply damage.
6. **Defined operating window:** State startup, duration or completion condition, upkeep, cooldown/recovery, interruption rules, and cancellation behavior. A passive trait can persist, but an activated ultimate must have explicit activation semantics.
7. **Specific strengths and honest boundaries:** Define what the skill affects, what it does not affect, and how it interacts with mixed/unknown effects. Do not claim universal immunity, guaranteed prediction, unlimited summons, infinite resources, or automatic victory unless the fiction and complete counterplay rules deliberately support a bounded exception.
8. **Readable and fair:** Telegraph major activations and high-impact effects through animation, sound, VFX, UI, and accessible alternatives. Opponents need credible responses where the skill's fantasy permits them.
9. **Player history shapes outcomes:** Different routes may satisfy a broad achievement in different ways. Preserve meaningful alternatives such as combat, exploration, research, crafting, diplomacy, stealth, and survival when thematically appropriate.
10. **World consequences are real:** NPCs and ecosystems react only to evidence they could know. Major powers may alter reputation, habitats, factions, structures, or future encounters.
11. **Shared rules, distinct identities:** Player and NPC/boss versions use consistent underlying classification and timing rules. Boss tuning can differ transparently, but cannot rely on hidden omniscience.
12. **Permanent-death and PvP safeguards remain absolute:** No ultimate, clone, echo, anchor, soul, transformation, or stored imprint can resurrect a permanently dead player character. PvP never permanently kills a player or steals their assets/progression.

## Required record for every ultimate or secret skill

Every record in the Power & Ability Catalogue must document:

- **Identity:** original name, character/route, ability category, and gameplay fantasy.
- **Discovery clues:** what the player can observe, test, or infer; what remains hidden before discovery.
- **Unlock conditions:** explicit actions, evidence, prerequisites, research, environment, mastery, and any alternate qualifying routes.
- **Evolution path:** base ability, branches, upgrades, mastery effects, and capstone relationships.
- **Activation contract:** required form/anatomy, input, startup, resource threshold, charge, target/environment requirements, and reasons activation can fail.
- **Effect contract:** targets, range/area, damage or non-damage effects, conversion or control behavior, duration, and resolution.
- **Costs and limits:** upfront cost, upkeep, resource caps, overflow, cooldown, recovery, strain, instability, or opportunity cost.
- **Boundaries and counterplay:** excluded effects, resistance/interrupt rules, counters, failure states, escape/response windows, and PvP-specific safeguards.
- **Combinations:** compatible and conflicting skills, anatomy, traits, forms, and environment interactions.
- **World response:** NPC knowledge, ecological/faction effects, persistent damage or recovery, and story consequences.
- **Presentation and accessibility:** animation, VFX, audio, UI, telegraphs, feedback for blocked activation, and configurable controls.
- **Acceptance tests:** deterministic unlock, activation, effect, edge-case, exploit, save/load, multiplayer authority, accessibility, and regression criteria.
- **Status:** proposed, design-specified, in progress, implemented, or verified—with actual evidence required for implementation/verification claims.

## Secret unlock pattern

A secret route should generally follow this chain, with flexibility when the fantasy needs it:

1. **Signal:** an unusual encounter, environmental anomaly, witness account, residue, item, or body reaction provides a clue.
2. **Investigation:** the player gathers evidence and separates a hypothesis from a confirmed rule.
3. **Experiment:** a deliberate action tests the hypothesis and exposes a real risk or trade-off.
4. **Qualification:** the player proves the required behavior or achievement under defined conditions.
5. **Unlock:** the Atlas reveals the ability and explains what was earned without granting unrelated mastery.
6. **Stabilization:** training, resource investment, or a follow-up challenge makes the ability reliably usable.
7. **Mastery:** meaningful execution unlocks variants, more efficient use, combinations, or deeper effects.
8. **Consequence:** the world, NPCs, or future encounters respond when there is credible evidence of the new power.

Not every secret must use all eight steps, but skipping a step should be a deliberate design decision. Avoid opaque random drops as the only route to a defining power.

## Reference implementation-by-design: Absolute Nullification

**Absolute Nullification** is the slime's actual player-activated ultimate. When fully unlocked, correctly configured, and deliberately activated while all stated conditions hold, it nullifies the defined incoming hostile damage classes and routes them into eligible reserves such as health/repair, energy, stamina, biomass, analysis/stability, or offensive charge.

Its governing boundaries remain explicit:
- It is conditional and time/resource-bounded, not an always-on passive.
- Conversion requires the relevant branches; unknown and mixed damage are covered only at the specified final rank.
- Resource caps and overflow prevent infinite-generation loops.
- Non-damage control, forced movement, imprisonment, arena removal, or objective effects are not automatically nullified unless a separate defined effect covers them.
- It does not change other characters' base damage rules.
- It does not bypass permanent-death rules or enable permanent PvP theft.
- Its exact costs, durations, thresholds, and cooldown remain open for balancing and prototype validation.

The slime's connected defensive and offensive branches are prerequisites and upgrades; **Absolute Nullification** is the name of the skill the player activates. Any later mastery label or form name must not obscure that distinction.

## Cross-route examples to develop to this standard

These are working candidates, not finalized abilities or implementation claims. Each must receive a complete record before it is approved for implementation.

| Route / identity | Ultimate or secret-skill candidate | Earned condition and gameplay identity |
|---|---|---|
| Hidden slime | **Absolute Nullification** | Master connected membrane, impact, recovery, energy conversion, analysis, stability, and absorption branches; survive and analyze qualifying mixed/exotic attacks. Nullifies defined damage during a bounded active window and routes it into capped reserves. |
| Shadow-command sovereign | **Eclipse Dominion** | Demonstrate disciplined command across a multi-stage encounter, preserve qualifying echo traces, and master command bandwidth. Creates a limited tactical domain for repositioning and coordinated echoes; upkeep, range, counter-signatures, and command disruption remain relevant. |
| Limit-breaker martial ascendant | **Limit Convergence** | Prove technique, energy control, recovery discipline, and adaptation against a worthy rival or trial. Temporarily synchronizes movement, defense, and energy release for precise high-commitment combos; strain and a vulnerable recovery window follow. |
| Adaptive goblin reclaimer | **Apex Reconfiguration** | Stabilize several compatible traits, demonstrate selective consumption, and solve a dangerous encounter using preparation and adaptation. Reconfigures a limited set of traits for the current threat; incompatible traits, mass/slot limits, and stabilization costs prevent perfect instant counters. |
| Mythic staff ascendant | **Heaven-Thread Reversal** | Master staff timing, feints, deflection, aerial recovery, and a mythic traversal/combat trial. Redirects eligible momentum into a chained counter-route; poor timing, grabs, ranged pressure, or missed deflections can interrupt it. |
| Undead spell sovereign | **Sovereign Grand Rite** | Research and stabilize several spell families, defend a contested ritual, and prove command restraint. Establishes a temporary prepared domain with layered wards and bounded servants; components, concentration, dispel, anchor disruption, and upkeep remain relevant. |

The names above are original working names and may be revised. They are design candidates, not promises of a fixed franchise character or copied moveset. Character-specific powers must preserve originality and any rights/licensing boundaries documented elsewhere.

## Implementation acceptance gates

1. Every approved ultimate has a complete, uniquely identified catalogue record and a traceable Atlas prerequisite graph.
2. Hidden clues and unlocks are deterministic enough to validate, with hypothesis/confirmed status correctly represented.
3. Activation conditions, resource consumption, duration, interruption, cooldown, and effect boundaries agree across UI, server rules, player behavior, and NPC/boss behavior.
4. Mixed, unknown, repeated, overlapping, and edge-case effects cannot bypass defined protections or create infinite resource loops.
5. Save/load, respec, form switching, disconnect/reconnect, and multiplayer authority cannot duplicate, retain, or activate unearned powers.
6. Telegraphed effects have readable counters or explicitly defined non-counterable windows, with no hidden instant-win outcomes.
7. PvP never permanently kills a player or steals assets/progression; no ability restores a permanently dead character.
8. Tests are run against actual implementation and results are recorded before any feature is labeled implemented or verified.

**Implementation status:** This framework and its candidate examples are design-only. No skill logic, UI, animation, balance, or acceptance test is claimed implemented or verified.
