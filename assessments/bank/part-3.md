# Part III question bank

## C16.01 | expected-value | easy | apply | 16
A lottery pays €80 with probability 0.25 and €0 otherwise. What is its expected monetary value?
+ €20 | Multiply each payoff by its probability and add.
- €60 | This multiplies €80 by the probability of receiving nothing.
- €40 | This treats the two outcomes as equally likely.
- €80 | This ignores the chance of receiving nothing.
- €25 | This confuses the percentage chance with the monetary payoff.

## C16.02 | ambiguity | easy | apply | 16
One urn has a known 50–50 mix of red and blue balls. Another has an undisclosed mix. Winning and losing prizes are identical across urns. Betting on red in the second urn introduces which feature?
+ Ambiguity about the probability | The color probability is unspecified.
- A known increase in expected winnings | The unknown mix does not establish higher expected winnings.
- A known reduction in payoff variance | A strict reduction is not established: the undisclosed mix could also be 50–50.
- A change in the prize conditional on winning | Only the probability information changes.
- A sunk cost of drawing the ball | No unrecoverable expenditure is specified.

## C16.03 | certainty-equivalent | medium | apply | 16
A person's certainty equivalent for a lottery is €36, while its expected monetary value is €45. What is the risk premium?
+ €9 | The risk premium is expected value minus certainty equivalent.
- €36 | This is the certainty equivalent itself.
- €45 | This is the expected value itself.
- €81 | Adding the two quantities does not give the premium.
- −€9 | This reverses the usual EV-minus-CE definition.

## C16.04 | expected-utility | medium | apply | 16
A decision maker has utility u(w) = √w over final wealth. A lottery yields wealth 100 or 0 with equal probability. What is its expected utility?
+ 5 | Expected utility is 0.5×√100 + 0.5×√0.
- Approximately 7.07 | This is utility of expected wealth, √50, not expected utility.
- 10 | This is utility of the high outcome alone.
- 50 | This is expected wealth, not expected utility.
- 25 | This is the lottery's certainty equivalent in wealth units.

## C16.05 | multiplicative-risk | hard | analyze | 16
An investment gains 50% in one period and loses 50% in the next. There are no deposits or withdrawals. Which comparison is correct?
+ The arithmetic mean return is 0%, but wealth falls 25%. | The average is (50−50)/2; the wealth multiplier is 1.5×0.5 = 0.75.
- The arithmetic mean return and wealth change are both 0%. | Equal percentage gains and losses do not cancel multiplicatively.
- The arithmetic mean return is −25%, and wealth falls 25%. | The wealth calculation is right but the arithmetic mean is wrong.
- The arithmetic mean return is 0%, and wealth falls 50%. | The final loss applies to the increased wealth.
- The arithmetic mean return is 25%, and wealth rises 25%. | Neither the average nor the compounded result has that value.

## C17.01 | reference-dependence | easy | apply | 17
An employee receives a €600 bonus but had expected €900. Relative to that expectation, how can the bonus be coded?
+ As a €300 shortfall | Outcomes can be evaluated relative to an expected reference point.
- As a €600 shortfall | This treats the payment itself as a loss.
- As a €900 gain | This confuses the expectation with the outcome.
- As unchanged total wealth | Receiving the payment increases wealth despite the shortfall.
- As evidence that money has negative utility | A shortfall judgment does not mean money is intrinsically undesirable.

## C17.02 | loss-aversion | easy | understand | 17
Which comparison most directly expresses loss aversion around a fixed reference point?
+ Losing €40 hurts more than gaining €40 pleases. | The asymmetry compares equal-sized losses and gains.
- Gaining €40 pleases more than gaining an additional €40 later. | This could concern timing, not loss aversion.
- A €40 gamble is less attractive than a sure €40. | These outcomes differ in risk and possibly expected payoff.
- A €40 item seems cheaper next to a €100 item. | This is a contextual comparison, not a gain–loss asymmetry.
- Spending €40 from one budget feels different from another. | This concerns mental accounting.

## C17.03 | fourfold-pattern | medium | apply | 17
Under the typical fourfold pattern, how do people often respond to a small probability of a large gain and a small probability of a large loss, respectively?
+ Seek the gain gamble; seek insurance against the loss. | Overweighting small probabilities can support both lottery play and insurance.
- Avoid the gain gamble; seek the loss gamble. | This reverses the low-probability pattern.
- Prefer certainty in both gain and loss comparisons. | The low-probability gain often attracts risk seeking.
- Prefer risk in both gain and loss comparisons. | The low-probability loss often attracts risk aversion.
- Ignore both events because each is unlikely. | That is not the small-probability overweighting prediction.

## C17.04 | competing-mechanisms | medium | analyze | 17
A customer keeps a more expensive contract after a cheaper alternative appears. Which comparison best tests whether staying has a rational explanation in terms of costs?
+ Compare the future savings with the full cost of changing providers. | Switching costs can outweigh the savings from a lower price.
- Compare the old contract price with its original advertised price. | Historical prices do not measure the consequences of changing now.
- Compare the customer's attachment to the old provider with other customers' attachment. | Attachment ratings do not quantify the relevant cost comparison.
- Compare the number of favorable reviews received by the two advertisements. | Advertising reactions do not establish the customer's switching costs.
- Compare the new price's percentage discount with discounts in unrelated markets. | An unrelated discount does not determine the net benefit of this switch.

## C17.05 | value-function | hard | apply | 17
Use v(x) = x for gains and v(x) = 2x for losses relative to zero, with linear probability weights. What is the value of a 50% chance to gain €60 and a 50% chance to lose €40?
+ −10 | 0.5×60 + 0.5×(2×−40) = −10.
- 10 | This is the monetary expected value, ignoring loss aversion.
- −20 | This applies the loss multiplier but omits both 50% probability weights.
- 20 | This subtracts the loss from the gain without probability weighting.
- −50 | This counts the full loss value but only half the gain value.

## C18.01 | description-and-experience | easy | understand | 18
Which situation exemplifies a decision from experience?
+ Choosing a supplier after observing outcomes of several trial orders | The decision is informed by sampled outcomes.
- Choosing solely from a stated table of failure probabilities | This is a described distribution.
- Choosing solely from a written probability of delivery | The probability is described, not sampled through outcomes.
- Choosing from an analyst's complete theoretical payoff table | A payoff table describes the options.
- Choosing by a rule before observing any supplier outcome | The stated rule is not evidence of outcome-based experience.

## C18.02 | rare-events-in-samples | easy | apply | 18
A rare supplier failure does not appear in a buyer's first few orders. What is the most appropriate inference?
+ A small sample can miss a real failure risk. | Absence in a short sample is compatible with a positive event probability.
- The supplier's failure probability is zero. | A finite failure-free sample does not establish impossibility.
- The stated failure probability must be exaggerated. | The sample alone cannot establish that direction of error.
- Failure must occur on the next order to restore the average. | Independent events need not compensate immediately.
- The buyer has learned the full distribution of outcomes. | A short observed path need not reveal the distribution's tails.

## C18.03 | sample-missing-probability | medium | apply | 18
Each independent order has a 10% failure chance. What is the chance that all three trial orders avoid failure?
+ 72.9% | The probability is 0.9³.
- 70.0% | Subtracting three failure probabilities ignores overlap.
- 27.1% | This is the chance of at least one failure.
- 0.1% | This is the chance all three fail, 0.1³.
- 90.0% | This is the chance one order avoids failure.

## C18.04 | feedback-and-avoidance | medium | apply | 18
After one disappointing visit, a diner stops returning to a restaurant. Which learning problem can this create?
+ Later improvements may remain unobserved. | Avoidance removes opportunities to update the initial impression through experience.
- Each avoided visit adds evidence of poor service. | A visit that never occurs supplies no new service observation.
- Trying other restaurants reveals this restaurant's current quality. | Experience at other restaurants is not a direct observation of this one.
- Adding more alternatives makes the first observation representative. | A larger choice set does not improve the original sample.
- The initial observation becomes more reliable as time passes. | Elapsed time alone does not improve the evidence and conditions may change.

## C18.05 | sampling-design | hard | analyze | 18
A buyer samples suppliers but stops testing each one as soon as it delivers successfully once. She compares the success share in each short record. Which improvement best addresses this sampling rule?
+ Set a common testing horizon in advance and retain all outcomes. | Outcome-dependent stopping distorts what is compared; a common horizon improves comparability.
- Discard failures that occurred before each supplier's first success. | This removes precisely the unfavorable evidence.
- Compare only the final delivery from each supplier. | By design, every final delivery is a success.
- Stop each test after its first failure instead. | This introduces a different outcome-dependent stopping rule.
- Extend testing only for suppliers that already look best. | Selective extension preserves unequal sampling tied to outcomes.

## C19.01 | fungibility | easy | apply | 19
€100 from a refund buys the same goods as €100 from wages. Which benchmark does this illustrate?
+ Fungibility | The source label does not change money's purchasing power.
- Loss aversion | No equal gain–loss comparison is specified.
- Exponential discounting | Timing is held out of the comparison.
- Probability weighting | No risky outcomes are involved.
- An endowment effect | Ownership status does not differ between the amounts.

## C19.02 | account-labels | easy | apply | 19
A household spends a €200 bonus more readily than €200 of salary. If mental accounting drives the difference, which change should most directly reduce it?
+ Present both payments as additions to one available balance. | Combining the funds weakens the separation into source-based spending accounts.
- Describe each payment's source more vividly before spending. | Making the labels more salient can reinforce the separation.
- Display each payment in a separately named budget category. | Separate categories maintain the source-based distinction.
- Increase both payments by the same percentage. | Equal increases retain the account distinction rather than directly addressing it.
- Change both payments from bank transfers to cash. | A common payment format does not itself remove their different mental labels.

## C19.03 | account-closing | medium | apply | 19
An investor resists selling a losing asset because selling would “make the loss real.” Which operation is most directly implicated?
+ Closing the mental account | Realization makes the loss explicit in a completed account.
- Updating a discount rate from market evidence | No discount-rate evidence is mentioned.
- Insuring a rare external loss | The investor is not buying insurance.
- Diversifying across independent assets | No portfolio diversification is described.
- Estimating a Bayesian posterior | The stated concern is realization, not a probability update.

## C19.04 | narrow-bracketing | medium | apply | 19
A household evaluates each small subscription separately and finds each affordable, yet the combined monthly bill exceeds its budget. What would directly address the problem?
+ Evaluate the subscriptions jointly against the monthly budget. | Broadening the bracket makes their combined cost visible.
- Divide every subscription into smaller daily amounts. | This may further obscure the aggregate burden.
- Put each subscription in a different labeled account. | More separation can preserve the hidden total.
- Review only the least expensive subscription. | One item cannot reveal the whole bill.
- Ignore recurring payments once the first month is paid. | That omits future avoidable costs.

## C19.05 | continuation-value | hard | analyze | 19
A project has spent €90,000 irrecoverably. Stopping now returns €10,000 in salvage. Continuing costs €30,000 more and yields €45,000 at completion, with no salvage afterward. All amounts are certain. What should an expected-money maximizer do?
+ Continue; its future net payoff exceeds stopping by €5,000. | Continue gives 45−30 = 15 thousand; stop gives 10 thousand.
- Stop; total spending would exceed the completion revenue. | That comparison counts the sunk €90,000.
- Continue; it exceeds stopping by €15,000. | This omits the salvage opportunity cost.
- Be indifferent; completion revenue offsets all future costs. | The two future net payoffs are not equal.
- Stop; salvage exceeds the completion payoff by €5,000. | This reverses the correct comparison.

## C20.01 | present-bias | easy | apply | 20
On Monday, Priya prefers 12 tokens on Friday to 10 on Thursday. On Thursday, with other conditions unchanged, she prefers 10 now to 12 tomorrow. Which model can explain this reversal?
+ Present-biased discounting | Making the earlier reward immediate can change its relative weight.
- Exponential discounting with a constant discount rate | Moving both rewards equally toward the present preserves their ranking in this model.
- Probability weighting | The scenario concerns certain dated rewards rather than changes in probabilities.
- Sunk-cost reasoning | No irrecoverable prior expenditure explains the change.
- Ambiguity aversion | Uncertainty about the reward probabilities is not part of the comparison.

## C20.02 | commitment | easy | apply | 20
Before an anticipated temptation, a person voluntarily blocks access to a distracting app for the next study session. What is this arrangement?
+ A commitment device | An earlier choice restricts a later tempting action.
- A descriptive norm | It does not report what others do.
- A probability forecast | It does not assign probabilities to outcomes.
- A decoy option | No dominated comparison option is added.
- A retrospective justification | The restriction is arranged before the later choice.

## C20.03 | liquidity-and-delay | medium | analyze | 20
A worker chooses €100 today over €110 next month. Which additional fact most weakens the interpretation that this reveals strong impatience?
+ An essential bill is due tomorrow and borrowing is unavailable. | A liquidity constraint can make the earlier payment valuable without strong impatience.
- Both payments are guaranteed by the same institution. | This removes a payment-risk explanation rather than adding a liquidity explanation.
- The choice is made privately without a response deadline. | This reduces pressure but does not explain the value of earlier resources.
- The worker can state both payment amounts accurately. | Comprehension does not rule out patience or liquidity as explanations.
- Prices are expected to remain unchanged over the month. | Stable prices remove an inflation explanation without identifying time preference.

## C20.04 | temptation-bundling | medium | apply | 20
A student reserves a favorite audiobook for time spent exercising. Which intervention is this?
+ Temptation bundling | An immediately enjoyable activity is paired with a beneficial activity.
- A commitment through financial forfeiture | No money is lost for failing to exercise.
- Episodic future thinking | The student is not simulating a future episode.
- A descriptive-norm message | The arrangement supplies no information about other people's behavior.
- Goal-gradient feedback | It provides no signal of distance to a goal.

## C20.05 | discounting | hard | apply | 20
A person values money linearly and uses exponential discounting with a constant annual factor δ = 0.8. Payments are certain and liquidity is irrelevant. Which option has the greatest present value?
+ €130 in one year | Its present value is 0.8×130 = €104.
- €100 today | Its present value is €100, below €104.
- €120 in one year | Its present value is €96.
- €150 in two years | Its present value is 0.8²×150 = €96.
- €190 in three years | Its present value is 0.8³×190 = €97.28.

## C21.01 | habit-versus-frequency | easy | understand | 21
What evidence most directly distinguishes a habit from an action that is merely frequent?
+ A familiar cue elicits the response with little deliberation. | Habit concerns learned automaticity in a context, not frequency alone.
- The action occurred several times last month. | Repetition alone does not establish automatic control.
- The action is judged beneficial by the person. | Desirability is separate from habitual execution.
- The action required a fresh written plan each time. | Repeated planning points toward deliberative control.
- The action has a large financial reward. | Reward size does not identify automaticity.

## C21.02 | wanting-and-liking | easy | apply | 21
A person feels a strong urge to check an app but gets little enjoyment from doing so. Which distinction describes this experience?
+ Strong wanting with weak liking | Motivational pull and experienced pleasure can diverge.
- Weak wanting with strong liking | This reverses the stated urge and enjoyment.
- Strong liking with no learned cues | The stem states little enjoyment and supplies no cue history.
- Low frequency with high satisfaction | Neither frequency nor satisfaction matches the key distinction.
- Habituation with increased sensory pleasure | The stem does not describe a diminished sensory response.

## C21.03 | reward-prediction-error | medium | apply | 21
A learner expects a reward of 6 points and receives 2. What is the reward prediction error?
+ −4 points | Received reward minus expected reward is 2 minus 6.
- +4 points | This reverses the direction of the discrepancy.
- +2 points | This ignores the expected reward.
- −6 points | This ignores the two points received.
- +8 points | Adding expected and received rewards does not measure prediction error.

## C21.04 | replacement-response | medium | apply | 21
A writer opens social media whenever a paragraph becomes difficult. Which plan specifies a replacement response to that cue?
+ When a paragraph stalls, write one rough sentence before opening another tab. | The plan links an observable cue to a specific alternative action.
- Become more disciplined about writing in general. | This supplies neither a concrete cue nor a response.
- Feel guilty after every unproductive session. | Self-blame does not specify what to do at the cue.
- Wait until the urge to browse disappears completely. | This makes action depend on eliminating the urge.
- Count the total number of open tabs at bedtime. | Later measurement does not supply the immediate replacement.

## C21.05 | near-miss | medium | analyze | 21
A slot-machine player interprets a near miss as evidence of improving skill. Which comparison best tests that interpretation?
+ Compare subsequent win rates after near misses and clear losses under the same game rules. | The interpretation predicts an improvement in future success, not merely greater motivation.
- Compare the reported urge to continue after near misses and clear losses. | Motivation to continue does not establish greater skill or better odds.
- Compare reported enjoyment after near misses and successful spins. | Enjoyment does not test whether a near miss predicts future success.
- Compare time spent watching near-miss and clear-loss displays. | Attention to a display does not establish improved performance.
- Compare the visual similarity of near misses and successful spins. | Resemblance to success is not evidence of an increased chance of winning.

## C22.01 | experienced-and-remembered | easy | understand | 22
A person records pleasant moments throughout a trip but later judges the whole trip poorly because of a stressful ending. Which distinction is illustrated?
+ Experienced well-being versus remembered evaluation | Momentary records and retrospective summaries can diverge.
- Expected value versus expected utility | The example concerns temporal assessments of experience, not lottery evaluation.
- Descriptive norms versus injunctive norms | No social norm information is supplied.
- Nominal income versus real income | No price-level adjustment is involved.
- Risk versus ambiguity | The key contrast is not known versus unknown probabilities.

## C22.02 | anticipatory-utility | easy | apply | 22
A traveler feels happier during ordinary workdays after booking a holiday. Which concept can account for this benefit before departure?
+ Anticipatory utility | Looking forward to a future experience can provide present enjoyment.
- Remembered utility | Remembered utility concerns an evaluation of a past experience.
- Hedonic adaptation | Adaptation concerns adjustment to a changed condition over time.
- Duration neglect | Duration neglect concerns how an episode's length enters its evaluation.
- Projection bias | Projection bias concerns mispredicting future preferences from a current state.

## C22.03 | focusing-illusion | medium | apply | 22
While considering a move, someone imagines sunshine and neglects commuting, friendships, and work. Which revision best addresses the focusing illusion?
+ Compare ordinary days across all the important life domains. | A broader time-use picture restores omitted consequences.
- Collect more photographs of sunny days. | More salient sunshine deepens the narrow focus.
- Treat weather as irrelevant to every person's well-being. | The problem is disproportionate weight, not necessary irrelevance.
- Rank destinations only by average temperature. | This preserves the one-feature evaluation.
- Ask for a single happiness score before discussing daily life. | An unstructured global score may retain the same focal bias.

## C22.04 | connection-measures | medium | apply | 22
A survey records weekly social encounters and whether respondents expect help in a crisis. Why retain both measures?
+ Social integration and perceived support describe different features of relationships. | Contact and expected access to help need not coincide.
- Both measure received support, but one uses a shorter recall period. | Expecting help does not show that support has actually been received.
- Contact counts measure relationship quality more directly than expected help does. | Frequency alone does not establish the quality of relationships.
- Expected help measures social integration independently of respondents' beliefs. | This is a perception-based measure, not an objective count of contacts.
- Combining the measures eliminates differences in what relationships mean to respondents. | Multiple measures do not remove individual differences in interpretation.

## C22.05 | well-being-audit | medium | analyze | 22
A policy raises mean life satisfaction. Which additional finding most strongly challenges using that average alone to justify adoption?
+ A vulnerable subgroup loses access to an essential service and has no workable appeal. | Distributional harm and loss of agency remain relevant despite an improved mean.
- Respondents differ in the importance they attach to income, health, and relationships. | Different priorities are expected and do not by themselves overturn the result.
- The improvement is larger on a satisfaction scale than on a positive-affect scale. | Different dimensions of well-being can move by different amounts.
- A second survey uses a different numerical range but finds a similar standardized effect. | A replicated effect across compatible scales strengthens rather than undermines the mean result.
- The policy improves satisfaction without changing participants' reported material aspirations. | Well-being can improve without changing that particular aspiration measure.

## P03.01 | insurance-and-tail-exposure | easy | apply | 16,18
A small firm has never suffered a fire, but credible evidence gives a 1% annual risk of a €200,000 loss that would bankrupt it. Insurance costs more than the €2,000 expected loss. What should guide the decision?
+ Evaluate the premium alongside the firm's capacity to bear the uninsured loss. | A favorable average and a failure-free history do not remove an unaffordable tail exposure.
- Reject insurance solely because the premium exceeds expected loss. | Expected money alone omits the firm's capacity to survive the loss.
- Treat the failure-free history as a zero-risk estimate. | Rare events can be absent from limited experience.
- Buy insurance at any premium because the loss is large. | Price and alternatives still matter.
- Assume a fire is due because none has occurred recently. | Absence of recent events does not create a balancing requirement.

## P03.02 | future-self-and-measures | easy | analyze | 20,22
An age-progressed self-image increases hypothetical retirement allocations. Which follow-up most directly tests whether the effect extends to saving behavior?
+ Randomly assign the image intervention and compare subsequent account contributions. | This tests the intervention against an actual saving outcome.
- Repeat the hypothetical allocation with a different windfall amount. | Another hypothetical allocation does not establish behavioral transfer.
- Compare balances of people who volunteer to view the image with those who decline. | Self-selection prevents isolating the image's effect on saving.
- Ask whether viewing the image makes retirement saving seem more important. | A changed attitude is not an observed contribution.
- Compare recognition accuracy for current and age-progressed photographs. | Recognition does not measure saving behavior.

## P03.03 | insurance-and-reference-points | medium | analyze | 16,17
A person rejects a fair gamble over final wealth but has made no explicit gain–loss comparison. Which evidence would most specifically help distinguish reference-dependent valuation from stable concave utility over final wealth?
+ Vary the reference point while holding final-wealth lotteries fixed. | Stable utility over final wealth predicts invariance; reference dependence can change rankings. This test alone does not identify loss aversion.
- Record the person's dislike of this one gamble again. | One risky choice is compatible with several mechanisms.
- Assume any aversion to risk is a measure of loss aversion. | Risk aversion and loss aversion are distinct.
- Measure only whether the gamble has positive expected value. | Expected value alone does not identify the value function.
- Ask whether the person has ever bought insurance. | Insurance can reflect several motives and constraints.

## P03.04 | delayed-payment-and-trust | medium | analyze | 18,20
A buyer chooses a smaller immediate rebate over a larger delayed one. Which comparison best separates impatience from concerns about receiving payment?
+ Offer both payment dates with the same credible payment guarantee. | Equalizing payment reliability reduces its confounding with the delay.
- Increase the delayed amount while leaving its reliability unchanged. | This changes the reward trade-off while retaining the reliability difference.
- Ask the buyer to imagine spending the delayed payment. | Imagery changes how the future is represented without controlling payment risk.
- Present the immediate rebate after describing the delayed rebate. | Presentation order does not equalize payment reliability.
- Compare the choice with another buyer's choice at a different seller. | Changing buyers and sellers introduces additional differences.

## P03.05 | budgeting-and-present-bias | medium | apply | 19,20
A saver chooses an account earmarked for saving that also delays withdrawals. Which pair of mechanisms could support the saving goal?
+ Mental accounting and commitment | The label separates the money mentally; the delay restricts immediate access.
- Loss aversion and numerical anchoring | The design specifies neither a framed loss nor a starting numerical estimate.
- Exponential discounting and diversification | A labeled access restriction does not specify either a discount function or a portfolio mix.
- Probability weighting and insurance | No probability transformation or transfer of risk is described.
- Habituation and social proof | The account does not rely on repeated exposure or evidence of others' choices.

## P03.06 | forecasts-of-well-being | medium | analyze | 20,22
A traveler selects a holiday for its spectacular highlights but dislikes most days of the trip. Which forecasting method best addresses that mismatch next time?
+ Imagine a typical day in each itinerary, including travel and waiting. | This brings ordinary experienced time into a comparison dominated by highlights.
- Estimate how impressive each itinerary would sound in a story afterward. | This emphasizes anticipated memory and social presentation rather than daily experience.
- Compare the single most enjoyable activity available at each destination. | Focusing on the peak repeats the original omission.
- Predict the final overall rating without considering the itinerary's daily schedule. | A global forecast can leave the same neglected periods unexamined.
- Rank destinations by the intensity of excitement when viewing their advertisements. | Immediate excitement need not predict enjoyment throughout the trip.

## P03.07 | habit-versus-sunk-cost | medium | analyze | 19,21
Maya automatically opens a service when she sees its icon. Leo consciously keeps using it because he paid a nonrefundable annual fee, despite a better free alternative and no switching costs. Which diagnosis fits each stated reason?
+ Cue-linked habit for Maya; sunk-cost reasoning for Leo | Their behavior looks similar but the described mechanisms differ.
- Sunk-cost reasoning for Maya; cue-linked habit for Leo | This reverses the mechanisms supplied in the stem.
- Present bias for both | No immediate-versus-delayed reward comparison is specified.
- Rational updating from service quality for both | The stated reasons are cues and past payment, not new quality evidence.
- Ambiguity aversion for both | Unknown probabilities are not central to either account.

## P03.08 | experience-and-memory | medium | analyze | 18,22
A person judges a service from one vivid final failure, despite records of many ordinary successful uses. Which review would best distinguish recent memory from the service's overall performance?
+ Compare the full dated outcome record with the retrospective rating. | This makes the sampled history and later summary separately observable.
- Delete the final failure because it is unpleasant. | A full review should retain relevant failures.
- Use the final failure as the only representative observation. | This preserves the possible recency distortion.
- Ask for the same global rating several more times. | Repeated summaries do not recover the outcome distribution.
- Count how often the failure story is retold. | Retelling measures salience, not the whole performance record.

## P03.09 | risk-and-discounting | hard | apply | 16,20
With linear utility and an annual discount factor of 0.9, compare a certain €70 today with an 80% chance of €100 in one year and €0 otherwise. Ignore liquidity and payment risks beyond those stated. Which is preferred?
+ The delayed lottery; its discounted expected value is €72. | 0.9×(0.8×100) = 72, above 70.
- The certain payment; the lottery is worth €64 today. | This applies the 0.8 probability twice and omits discounting.
- The delayed lottery; its discounted expected value is €90. | This ignores the 20% chance of no payment.
- The certain payment; the lottery is worth €8 today. | This uses the 10% discount rate as the weight instead of the 0.9 discount factor.
- The options tie; discounting cancels the probability. | Probability and discounting both enter multiplicatively.

## P03.10 | positive-mean-and-experience | hard | analyze | 16,18
An investment multiplies wealth by 1.5 or 0.6 with equal probability each period. A sample contains one of each outcome. Which statement correctly compares expected one-period return with the realized two-period path?
+ Expected one-period return is +5%; the sampled path loses 10%. | The expected multiplier is 1.05; the sampled product is 1.5×0.6 = 0.9.
- Expected one-period return is +10%; the sampled path gains 10%. | Both calculations confuse arithmetic and multiplicative changes.
- Expected one-period return is −10%; the sampled path loses 10%. | The path loss is correct, but the expected one-period return is positive.
- Expected one-period return is +5%; the sampled path gains 5%. | The realized path is determined by multiplication, not the one-period expectation.
- Expected one-period return is 0%; the sampled path breaks even. | The gains and losses are neither equal nor multiplicatively offsetting.
