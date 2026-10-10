# Luck, Randomness, and Fortunate Discovery System

**Project:** Lethal Absorption  
**Status:** Design specification — proposed, not implemented or tested  
**Purpose:** Make luck a real progression factor so players can occasionally unlock rare discoveries earlier than expected, while preserving fairness, agency, compatibility, and long-term progression.

## 1. Core rule

Luck can create an opportunity, reveal a clue, or produce an unusually favorable outcome. It must not silently bypass every requirement for owning, safely using, or mastering a powerful ability.

**Design principle: luck opens doors; player decisions and play develop what is found.**

Players following the same route may have different discovery histories. Neither player should be guaranteed the same rare result at the same moment.

## 2. Where randomness may apply

- **Absorption outcomes:** biomass, ordinary resources, research clues, partial trait information, compatible trait fragments, or—rarely—a new discovery.
- **Mutation events:** beneficial, neutral, mixed, or challenging outcomes, limited by biology, current form, environment, and established world rules.
- **Exploration:** rare organisms, resource clusters, unusual environmental conditions, hidden locations, and temporary opportunities.
- **Research and experimentation:** unexpected observations, clues, and new candidate recipes or ability interactions.
- **Ability weaving:** an experiment can reveal an unrecorded interaction when its components and conditions plausibly support one.
- **Combat and encounters:** a rare opening, environmental advantage, or discoverable weakness; randomness must not decide every critical hit or boss outcome.
- **Evolution:** an unusual compatible path can be revealed earlier than normal through a rare event, but the player must still meet any necessary stabilization, body-plan, resource, or mastery requirements.

Randomness must never override established compatibility, sapient-species protections, protected story states, or critical mission rules.

## 3. Separate luck from other progression factors

Track these as distinct concepts:

1. **Chance:** the random component of an eligible event.
2. **Luck modifiers:** earned, equipped, environmental, or temporary effects that can influence eligible outcomes.
3. **Discovery:** learning that an option or interaction exists.
4. **Eligibility:** whether the character, form, environment, and prerequisites permit the result.
5. **Ownership:** whether the character has actually acquired the trait or ability.
6. **Stabilization:** making a volatile or newly acquired trait reliably usable.
7. **Mastery:** improving control through practice and deliberate use.

A lucky discovery may reveal an ability without granting full ownership. A lucky acquisition may grant ownership but require stabilization. A lucky player can find a rare path early without automatically mastering it.

## 4. Fairness and anti-frustration rules

- **No impossible lottery gates:** the main story, basic controls, and essential progression cannot require a rare random drop.
- **Pity / bad-luck protection:** repeated eligible attempts without a meaningful discovery may gradually improve the chance of a relevant result or provide a guaranteed clue/alternative route after a defined threshold.
- **No duplicate waste:** repeated discoveries should provide a useful alternative such as research progress, synthesis material, mastery insight, or a conversion resource.
- **No forced reload fishing:** random outcomes should be saved consistently enough to discourage trivial save/reload exploitation, while preserving reasonable recovery from bugs or failures.
- **No hidden punishment:** luck must not secretly lower success odds elsewhere to offset a fortunate result.
- **No mandatory grind:** a lucky route may be faster; a non-lucky route must remain viable through research, exploration, combat, crafting, or other deliberate play.
- **Transparent uncertainty:** where useful, the UI communicates broad likelihood or rarity. It need not expose every internal probability, but must not falsely promise certainty.
- **Respect player settings:** provide accessibility options for reducing random variation in suitable noncompetitive modes where feasible. Competitive modes, if added, require separately defined rules.

## 5. Luck modifiers and trade-offs

Potential sources include temporary environmental conditions, equipment or biological traits, research insights, consumables, and choices that deliberately favor exploration over predictable performance.

Modifiers must be bounded and legible. A high-luck build should not guarantee rare abilities, bypass eligibility, or become mandatory. Any trade-off—such as lower immediate combat strength or resource efficiency—must be stated before the player commits.

Luck modifiers should affect only designated eligible rolls, not every game system. Stacking must have a cap or diminishing returns, to be balanced during implementation.

## 6. Rarity and probability policy

Use rarity bands for design and communication: **Common, Uncommon, Rare, Very Rare, and Exceptional**. These bands are descriptive until playtesting establishes actual numeric probabilities.

Do not hard-code final percentages in this design phase. Numeric rates require implementation tests across many simulated attempts, checks for exploitability, and playtests for perceived fairness. Rates may vary by source, eligibility, region, research, and modifier—but must be documented and testable.

Randomness should use reproducible seeded outcomes where appropriate for debugging and save integrity. Avoid uncontrolled random behavior that makes bugs impossible to reproduce.

## 7. Example outcomes

**Example A — lucky early mutation:** A cell absorbs a compatible organism and unexpectedly reveals a rare membrane trait. The player gets a discovery entry and a visible explanation of the unusual result. If stabilization is required, that remains a next step.

**Example B — ordinary route:** Another player gets nutrients and a research clue from the same kind of organism. They can still discover the membrane trait later by studying related organisms or conducting experiments.

**Example C — lucky synthesis clue:** During a valid Fire + Wind experiment, the player discovers an uncommon pressure-spread interaction. This reveals a recipe; it does not grant unrelated abilities or unlimited damage.

**Example D — bad-luck protection:** After many eligible attempts without a new trait, the game guarantees a meaningful clue or alternate research lead rather than forcing endless repetition.

**Example E — luck cannot override eligibility:** A creature that cannot biologically support underwater breathing does not randomly gain a complete aquatic adaptation from an incompatible absorption result. It may receive a clue toward a compatible route instead.

## 8. User experience requirements

When a significant random outcome occurs:
- Show what happened and why it is notable.
- Record the result in the discovery history.
- Distinguish a clue, a candidate recipe, an acquired trait, and a mastered ability.
- Explain any remaining prerequisites.
- Allow the player to inspect the result later; do not require them to read a long explanation during combat.

Minor resource variance should stay unobtrusive. Rare or build-defining outcomes deserve clear feedback.

## 9. Required verification when implemented

- Same seed and same eligible state can reproduce the result for debugging.
- Random outcomes never bypass eligibility or required story progression.
- Main progression remains completable without rare drops.
- Bad-luck protection activates at its defined threshold.
- Duplicate outcomes always have a useful, documented result.
- Luck stacking respects caps/diminishing returns.
- Rare outcomes are logged accurately and persist through save/load.
- Save/reload does not provide a trivial exploit for unlimited rerolls.
- Simulation runs confirm observed rates are within agreed tolerance.
- Playtests compare lucky and unlucky progression paths for viability and frustration.
- Accessibility and competitive-mode rules are tested separately if those modes exist.

## 10. Scope boundary

This specification establishes the design rules, not final probability values or implemented code. Exact rates, pity thresholds, stacking caps, save behavior, and UI details remain to be balanced and verified during implementation.

**Current state:** Specified at design level. Not implemented, playtested, or verified in a playable build.
