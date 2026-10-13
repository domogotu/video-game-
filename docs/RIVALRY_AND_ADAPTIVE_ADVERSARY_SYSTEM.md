# Rivalry, Nemesis, and Adaptive Adversary System

**Project:** Lethal Absorption  
**Status:** Original design specification; not implemented, play-tested, or runtime-verified.  
**Scope:** Persistent adversaries whose histories, tactics, relationships, and regional consequences emerge from encounters.

## 1. Design goal and originality boundary

Lethal Absorption needs enemies that feel like individuals with histories, not disposable health bars. A rival can survive an encounter, learn from what happened, change tactics, recover, gain or lose status, develop a compatible adaptation, return with a changed plan, or become a temporary ally or avoidable threat.

This is an original **Rivalry and Adaptive Adversary System**. It uses broad genre ideas such as persistent rivals and remembered encounters, but must not reproduce another game's specific proprietary Nemesis implementation, interface, hierarchy presentation, character-generation rules, dialogue patterns, or patented method. Use original data models, rules, names, visuals, and interaction flows; obtain legal review before release if any implementation approaches a known patent or protected expression.

The system complements Lethal Absorption's core: **Consume. Evolve. Survive.** It is not mandatory for the first cellular slice.

## 2. Core principles

1. **History creates identity.** Behavior changes because of identifiable events, not arbitrary stat inflation.
2. **Causes are learnable.** Clues connect a rival's change to observed events, biology, training, allies, or diet.
3. **Adaptation is bounded.** No rival becomes immune to every player ability or counters every build at once.
4. **Survival has consequences.** A rival who escapes may recover, recruit help, change territory, conceal a weakness, or prepare a rematch.
5. **Victory has options.** Defeat, escape, evasion, research, negotiation, disruption, containment, or alliance may resolve a rivalry where appropriate.
6. **No mandatory random wall.** Main-story progress cannot depend on one rival spawning, surviving, or dropping a rare item.
7. **World actors have agency.** Goals and relationships fit their species and intelligence.
8. **Permanent death remains meaningful and PvP-safe.** Only eligible NPC-controlled threats may permanently end the current player character. PvP outcomes are always non-permanent, regardless of rank or consent, and cannot permanently remove assets or progression.

## 3. How rivals emerge

Potential rivals come from authored story roles, valid procedural eligibility, or significant world events. Examples:
- A predator escaped after the player interrupted its hunt.
- A territorial creature was displaced by the player's growth or absorption.
- A hunter survived a fight and began preparing for the player's most-used tactic.
- A faction scout or commander had its plans disrupted.
- A creature's diet and environmental exposure produced a distinctive compatible adaptation.
- A former competitor's goals temporarily align with the player during a crisis.

Not every hostile actor becomes a rival. Creation requires a meaningful event, appropriate cognition or biology, and an available budget slot. Ordinary creatures can remember local danger briefly without becoming persistent named adversaries.

## 4. Rival record and memory

Each persistent rival stores:
- Stable identity, original name/identifier, species/body plan, and readable visual/audio identifiers.
- Stage, region, habitat needs, movement constraints, goals, and temperament.
- Consequential encounter history, with recency and confidence.
- Whether each event was directly witnessed, inferred, or learned through a valid information channel.
- Relationship state such as unknown, wary, hostile, competing, negotiating, allied, withdrawn, or resolved where applicable.
- Condition, injuries, resources, recovery needs, allies, territory, and current plan.
- Limited learned tactics/adaptations, their causes, tells, counters, and reevaluation conditions.
- Last valid location, reappearance conditions, resolution status, and saved regional consequences.

Record consequential events, not every hit or frame: repeated player tactics, escaping a trap, being interrupted while feeding, losing territory or an ally, being spared or helped, observing a new form/ability, or surviving a fight. Aggregate repeated trivial events with a cap so rapid inputs cannot manufacture unlimited rivalry progression.

A rival cannot counter an ability it never witnessed, inferred from reliable evidence, or learned through an established information channel. Memory may be incomplete, but errors must be explainable and must not create unfair unavoidable counters.

## 5. Adaptive tactics and evolution

A rival may respond through:
- **Tactical change:** keep distance from a frequently used close-range attack, use cover against projectiles, or alter approach timing.
- **Defensive preparation:** add a limited guard, resistance, escape response, or environmental advantage with a readable tell and counter.
- **Behavioral change:** alter hunting time, avoid a dangerous route, recruit help, protect a resource, or bait the player toward favorable terrain.
- **Biological adaptation:** after compatible diet, damage exposure, or habitat pressure, develop a plausible trait or clue under existing compatibility rules.
- **Status/territory change:** gain influence through established world rules, lose access after displacement, or face a challenger.
- **Technique refinement:** improve a specific move or sequence, creating a learnable rematch pattern.

Every counter needs a tell, cost, limitation, or exploitable alternative. A counter reduces a tactic's effectiveness; it does not silently disable an entire player build. Use a small, bounded number of active counters per rival; exact counts are for later tuning. Avoid endless counter escalation: reassess after major events and let outdated preparations weaken or be abandoned. Player adaptation remains meaningful through new tactics, environment use, allies, stealth, research, or alternate abilities.

A rival does not gain a player's ability merely because it was used against them. Require biological compatibility, witnessed evidence, resources/training, or another documented cause.

## 6. State transitions and outcomes

Conceptual flow: ELIGIBLE → INTRODUCED → ACTIVE → LEARNING/RECOVERING → REMATCH READY → RESOLVED. Optional states include WITHDRAWN, DISPLACED, ALLIED, CONTAINED, or DEAD. Runtime names may differ.

Every transition needs an explicit cause:
- A valid escape after combat leads to recovery, not an immediate teleporting rematch.
- Reappearance occurs only after recovery and a valid location/eligibility check.
- A rival that loses territory may relocate or contest a nearby area.
- An alliance requires supported trust and goal conditions.
- A dead rival stays dead if the world's rules establish permanent death; no unexplained resurrection of the same identity.

Possible outcomes include defeat, escape/disengagement, outmaneuvering, research, disrupting supplies or allies, negotiation/reconciliation, alliance, containment/displacement, or avoidance. Outcomes depend on the adversary's species, intelligence, and context. Rewards may include knowledge, access, regional change, encounter clues, or a compatible mutation opportunity. A unique mandatory power cannot require killing a named rival when the story/world supports another route.

Not every rival passes through every state. Some are authored story antagonists; a wild animal may only remember a threat and alter its behavior.

## 7. Territory, factions, and social consequences

For eligible intelligent factions or social species, rival outcomes may change local patrols, prey behavior, trade access, hostility, routes, resource control, or leadership. Allies can provide warnings, information, supplies, rescue attempts, or coordinated tactics, subject to their own limits.

Leadership is not a universal ladder: some species are solitary, symbiotic, migratory, or non-hierarchical. Succession after death/departure follows that group's ecology or culture and may leave a temporary vacancy. Local events do not cause global consequences unless a communication or political chain explains them. Detailed social simulation stays near active regions; distant relationships use bounded abstract updates.

## 8. Integration with existing systems

- **Creature ecology/diet:** rivals hunt, forage, and defend territory under the existing ecosystem rules. Mutations require compatible causes and eligibility.
- **Alpha/special creatures:** Alpha status and rivalry are separate labels. An Alpha may be a rival, but not every Alpha is personal; not every rival is an Alpha.
- **Absorption/discovery:** rewards follow normal eligibility: resources, verified knowledge, clues, partial traits, or compatible mutation opportunities—not automatic full power transfer. Sapient adversaries remain subject to agency, culture, and narrative rules.
- **Evolution/body plans:** tactics respect anatomy, stage, environment, and resources.
- **Ability weaving/environment:** counters use plausible cover, spacing, material interaction, disruption, or compatible defense—not blanket immunity. World damage follows existing persistence and protected-area rules.
- **Permanent death/legacy:** only eligible NPC-controlled threats can permanently end the player's current character. PvP cannot permanently remove a character, inventory, anatomy, resources, discoveries, specimens, or progression. A successor may encounter a legacy footprint after a qualifying NPC-caused defeat.

## 9. Fairness and player control

- Communicate identity and important behavior changes through cues, journal entries, dialogue, tracks, or environmental changes.
- Let players inspect known facts without revealing every hidden tactic.
- Do not adapt so quickly that players cannot understand the lesson or enjoy a chosen build.
- Difficulty/accessibility options may reduce adaptation speed, retaliation pressure, memory complexity, or pursuit persistence.
- Do not punish control remapping or basic accessibility options.
- Avoid repeatedly targeting under-levelled or recovering players, peaceful explorers, or players trying to leave.
- Rivals cannot appear inside safe tutorial areas or block required resources/objectives.
- Give fair warning for high-risk rematches and preserve disengagement routes.
- Prevent spawn-camping, unavoidable repeated ambushes, and reward-farming loops.
- Repeatedly defeating/manipulating one rival cannot generate unlimited resources, reputation, or mutation rolls.

## 10. Randomness, persistence, and performance

- Rival eligibility may include chance, but story-critical progression cannot depend on a specific random rival.
- Persist named identity, committed injuries/status, encounter history, learned tactics, resolution, and regional consequences.
- Generate random outcomes at valid event boundaries and save them; loading cannot reroll for a better result.
- Deduplicate events to prevent repeated rewards, adaptation stacks, or reputation changes.
- Missing/corrupt optional rival data must not erase valid player progression.
- Bound persistent rivals by region, stage, narrative role, and performance budget.
- Use simulation tiers: detailed active encounter, reduced-rate nearby region, abstract distant updates, and archived inactive records.
- Define which records are active, archived, resolved, or eligible for reuse. Never silently delete a story-critical rival.
- Exact odds, memory decay, adaptation timing, active-rival limits, and archive strategy remain open until a prototype is profiled and play-tested.

If performance is exceeded, simplify distant simulation and nonessential social interactions before sacrificing active encounter readability or save integrity.

## 11. Stage rollout

- **Cellular opening:** no full rival system; only short-lived threat memory.
- **Animal-scale exploration:** later milestone may introduce one territorial creature that remembers a meaningful encounter, with clear tells and noncombat options.
- **Apex creature stage:** introduce persistent predator rivals, limited adaptation, territory shifts, and diet-related history.
- **Main-form adventure:** support named faction adversaries, recurring rivals, allies, and regional consequences.
- **Living Ship/cosmic stage:** use scale-appropriate rivalries with colossal organisms, civilizations, or cosmic entities.

The first vertical slice does not implement this full system. It remains a later milestone after the core creature loop is stable.

## 12. Future prototype acceptance criteria

- [ ] A rival persists across at least two separated encounters if it validly survives.
- [ ] Behavior changes are traceable to observed or reliably learned events.
- [ ] Rivals do not counter information they could not plausibly know.
- [ ] Each active counter has a readable tell, limitation, cost, or alternative approach.
- [ ] Recovery, withdrawal, and reappearance follow valid state transitions.
- [ ] Supported resolutions create distinct, persistent consequences.
- [ ] Noncombat resolutions exist where appropriate; not every creature is forced into a humanoid hierarchy.
- [ ] Rival and Alpha identities remain distinct even when one creature qualifies for both.
- [ ] Diet and absorption rules govern all rival mutations and rewards.
- [ ] Mandatory progression does not require a random rival or rare reward.
- [ ] Save/load preserves history and does not duplicate rewards or reroll outcomes.
- [ ] Rivalry does not bypass permanent player-character death.\n- [ ] PvP cannot permanently end a player character or remove their assets/progression.\n- [ ] NPC attribution cannot be used to bypass protection for player-caused or uncertain outcomes.
- [ ] Difficulty/accessibility options preserve fair warning and agency.
- [ ] Performance caps and archive policies prevent unbounded persistent-actor growth.
- [ ] Originality and legal review occur before public release.

## 13. Open decisions

Resolve at a later prototype gate: active rivals per region; first introduction stage; memory retention and information sharing; adaptation slot count/cooldowns; faction simulation depth; difficulty tuning; authored/procedural balance; save/archive strategy; and implementation-specific legal review.

**Current state:** Design specified and ready for review. No playable implementation or runtime test evidence is established.

## 14. Perception-driven hunting and investigation

Persistent rivals and ordinary enemies use the dedicated [Perception, Investigation, and Adaptive Hunter AI](PERCEPTION_INVESTIGATION_AND_ADAPTIVE_HUNTER_AI.md) specification. They must react to evidence rather than receive omniscient player coordinates.

The shared behavior model covers justified senses, stimulus detection, suspicion, investigation, last-known-position searching, pursuit, lost contact, reassessment, and recovery. Rival learning is based on plausible witnessed or inferred events with confidence and recency. Tactical adaptation remains bounded, telegraphed, and counterable; one rival's knowledge is not automatically shared with every creature or faction.

A bounded encounter director may manage tension and pacing only after individual perception and search behavior are fair. It cannot teleport enemies, bypass safe zones or tutorial protection, force unavoidable spawns, or override the rule that PvP can never permanently kill a character. Simulation tiers and bounded memory prevent the system from becoming too expensive or retaining stale omniscient knowledge.

**Status:** Integrated design requirement; implementation and runtime tests outstanding.
