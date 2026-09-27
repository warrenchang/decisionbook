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
Customers keep a contract after a better one becomes available, but switching requires several hours of paperwork. What should be checked before attributing the pattern to loss aversion?
+ Whether switching costs explain the retained contract. | A forward-looking cost can rationalize staying without a gain–loss asymmetry.
- Whether the old contract was ever advertised. | Prior advertising alone does not isolate the stated alternative mechanism.
- Whether retained contracts can be called reference points. | Renaming the option does not distinguish mechanisms.
- Whether all customers receive the same monthly statement. | Statement delivery does not measure switching costs.
- Whether the new provider has a shorter company name. | Name length is not the concrete alternative raised by the case.

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
After one poor restaurant visit, a diner never returns and never receives information about later improvements. What keeps the initial belief from being corrected?
+ Avoidance cuts off new outcome feedback. | Choices shape the experiences available for updating.
- Returning is known to have a lower expected value. | The stem supplies no current outcome comparison.
- The first visit becomes a representative random sample of all future visits. | One visit need not represent a changing service.
- The diner's dislike changes the restaurant's objective quality. | No such effect is specified.
- The restaurant's improvements erase the original experience. | New quality does not erase memory or automatically reach the diner.

## C18.05 | sampling-design | hard | analyze | 18
A buyer samples suppliers but stops testing each one as soon as it delivers successfully once. She compares the success share in each short record. Which improvement best addresses this sampling rule?
+ Set a common testing horizon in advance and retain all outcomes. | Outcome-dependent stopping distorts what is compared; a common horizon improves comparability.
- Discard failures that occurred before each supplier's first success. | This removes precisely the unfavorable evidence.
- Compare only the final delivery from each supplier. | By design, every final delivery is a success.
- Stop each test after its first failure instead. | This introduces a different outcome-dependent stopping rule.
- Extend testing only for suppliers that already look best. | Selective extension preserves unequal sampling tied to outcomes.

## C19.01 | fungibility | easy | apply | 19
Ignoring tax and contractual restrictions, €100 from a refund buys the same goods as €100 from wages. Which benchmark does this illustrate?
+ Fungibility | The source label does not change money's purchasing power.
- Loss aversion | No equal gain–loss comparison is specified.
- Exponential discounting | Timing is held out of the comparison.
- Probability weighting | No risky outcomes are involved.
- An endowment effect | Ownership status does not differ between the amounts.

## C19.02 | account-labels | easy | apply | 19
A household spends a €200 bonus on a luxury while saving an otherwise identical €200 salary payment. What most directly distinguishes the two choices?
+ The mental label attached to the money | Source labels place economically substitutable money in different accounts.
- The amount of money available | The amounts are identical.
- The nominal purchasing power of the payments | No purchasing-power difference is stipulated.
- The expected return on the same saving account | The comparison specifies no return change.
- The market price of the luxury | The item need not change price for labeling to affect spending.

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
On Monday, Priya chooses 12 tokens this Friday over 10 this Thursday. When that Thursday arrives, with all other conditions unchanged, she chooses 10 now over 12 tomorrow. Which pattern is illustrated?
+ A preference reversal when the earlier reward becomes immediate | Present bias can make immediacy change the relative ranking.
- Stable exponential discounting with unchanged preferences | Shifting both rewards equally toward the present preserves that model's ranking.
- A change in the objective number of tokens | The amounts stay fixed.
- A sunk-cost effect from Monday's decision | No irrecoverable expenditure is specified.
- A change in the lottery's stated probabilities | No lottery or probability change appears.

## C20.02 | commitment | easy | apply | 20
Before an anticipated temptation, a person voluntarily blocks access to a distracting app for the next study session. What is this arrangement?
+ A commitment device | An earlier choice restricts a later tempting action.
- A descriptive norm | It does not report what others do.
- A probability forecast | It does not assign probabilities to outcomes.
- A decoy option | No dominated comparison option is added.
- A retrospective justification | The restriction is arranged before the later choice.

## C20.03 | liquidity-and-delay | medium | analyze | 20
A worker chooses €100 today over €110 next month because an essential bill is due tomorrow and borrowing is unavailable. What must be considered before inferring strong time discounting?
+ The liquidity constraint changes the usefulness of today's money. | Immediate funds solve a need that delayed funds cannot meet.
- The worker must misunderstand the difference between 100 and 110. | The choice can be coherent with the stated constraint.
- The choice reveals a stable discount rate for every context. | Liquidity and circumstances confound that inference.
- Delayed money has no purchasing power by definition. | Its later usefulness is distinct from the urgent current need.
- The worker is treating a gain as an owned loss. | No ownership-based reference point is specified.

## C20.04 | temptation-bundling | medium | apply | 20
A student reserves a favorite audiobook for time spent exercising. Which mechanism does this arrangement use?
+ Pairing an immediately enjoyable activity with a beneficial one | The bundle gives a delayed-benefit activity a current reward.
- Removing all immediate pleasure from exercise | The arrangement adds pleasure rather than removes it.
- Replacing exercise with imagined future fitness | Exercise remains part of the chosen bundle.
- Making the future reward arrive financially sooner | The mechanism does not alter the payment date of a future reward.
- Reclassifying past exercise as a sunk cost | The arrangement concerns future behavior.

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
A learner expects a reward of 6 points and receives 2. Using received reward minus expected reward, what is the prediction error?
+ −4 points | The outcome falls four points short of expectation.
- +4 points | This reverses the subtraction.
- +2 points | This ignores the expected reward.
- −6 points | This ignores the two points actually received.
- +8 points | Adding expected and received rewards does not measure their discrepancy.

## C21.04 | replacement-response | medium | apply | 21
A writer opens social media whenever a paragraph becomes difficult. Which plan specifies a replacement response to that cue?
+ When a paragraph stalls, write one rough sentence before opening another tab. | The plan links an observable cue to a specific alternative action.
- Become more disciplined about writing in general. | This supplies neither a concrete cue nor a response.
- Feel guilty after every unproductive session. | Self-blame does not specify what to do at the cue.
- Wait until the urge to browse disappears completely. | This makes action depend on eliminating the urge.
- Count the total number of open tabs at bedtime. | Later measurement does not supply the immediate replacement.

## C21.05 | near-miss | hard | analyze | 21
Participants are randomly shown a near-miss or clear-loss display. Next-play odds are identical by design. The study detects greater reported urge after near misses, but does not measure enjoyment or later plays. Which conclusion follows?
+ The display changed reported urge, with next-play odds held fixed. | Randomized display differences identify the reported motivational response, not a change in objective odds.
- The display increased enjoyment despite the financial loss. | Enjoyment was not measured.
- The display increased subsequent playing time through the urge. | Later play and mediation were not tested.
- The display helped participants learn a more successful playing strategy. | No improved strategy or success probability was demonstrated.
- The display effect establishes the response of all experienced gamblers. | That population-wide generalization was not tested.

## C22.01 | experienced-and-remembered | easy | understand | 22
A person records pleasant moments throughout a trip but later judges the whole trip poorly because of a stressful ending. Which distinction is illustrated?
+ Experienced well-being versus remembered evaluation | Momentary records and retrospective summaries can diverge.
- Expected value versus expected utility | The example concerns temporal assessments of experience, not lottery evaluation.
- Descriptive norms versus injunctive norms | No social norm information is supplied.
- Nominal income versus real income | No price-level adjustment is involved.
- Risk versus ambiguity | The key contrast is not known versus unknown probabilities.

## C22.02 | anticipatory-utility | easy | apply | 22
A traveler enjoys looking forward to a holiday several weeks before departure. What is the immediate source of this enjoyment?
+ Anticipation of the future experience | Pleasure can occur before the event itself.
- Recollection of this completed holiday | The holiday has not yet occurred.
- A realized financial return from the holiday | No financial payoff is specified.
- The opportunity cost of staying home | A forgone alternative is not the stated enjoyment.
- Adaptation after repeated holiday experiences | The example describes anticipation, not a declining response over time.

## C22.03 | focusing-illusion | medium | apply | 22
While considering a move, someone imagines sunshine and neglects commuting, friendships, and work. Which revision best addresses the focusing illusion?
+ Compare ordinary days across all the important life domains. | A broader time-use picture restores omitted consequences.
- Collect more photographs of sunny days. | More salient sunshine deepens the narrow focus.
- Treat weather as irrelevant to every person's well-being. | The problem is disproportionate weight, not necessary irrelevance.
- Rank destinations only by average temperature. | This preserves the one-feature evaluation.
- Ask for a single happiness score before discussing daily life. | An unstructured global score may retain the same focal bias.

## C22.04 | connection-measures | medium | apply | 22
Someone meets many people each week but feels that nobody would help in a crisis. Which distinction is most directly relevant?
+ Social contact frequency versus perceived support | Many contacts do not imply a sense that help is available.
- Life evaluation versus monetary wealth | Those quantities are not the specific contrast.
- Risk preference versus time preference | No risky or delayed reward choice is described.
- Anticipation versus recollection | The example compares two dimensions of current relationships.
- Objective income versus relative income | No income comparison is provided.

## C22.05 | well-being-audit | hard | analyze | 22
A policy raises mean life satisfaction, lowers it in a vulnerable subgroup, and restricts opting out. Which review most fully addresses the chapter's well-being audit?
+ Examine subgroup consequences, affected rights, and the ability to revise. | The review needs distributional outcomes and agency as well as the mean.
- Check the overall mean and median using a second survey. | Aggregate replication leaves subgroup rights and exit unresolved.
- Compare subgroup scores while holding the no-exit rule outside the review. | Distribution alone does not assess agency.
- Confirm that opting out is legally possible without testing practical access. | Formal availability need not mean feasible exit, and outcomes remain relevant.
- Validate the questionnaire without examining who gains or loses. | Measurement quality is necessary but does not settle the decision.

## P03.01 | insurance-and-tail-exposure | easy | apply | 16,18
A small firm has never suffered a fire, but credible evidence gives a 1% annual risk of a €200,000 loss that would bankrupt it. Insurance costs more than the €2,000 expected loss. What should guide the decision?
+ Evaluate the premium alongside the firm's capacity to bear the uninsured loss. | A favorable average and a failure-free history do not remove an unaffordable tail exposure.
- Reject insurance solely because the premium exceeds expected loss. | Expected money alone omits the firm's capacity to survive the loss.
- Treat the failure-free history as a zero-risk estimate. | Rare events can be absent from limited experience.
- Buy insurance at any premium because the loss is large. | Price and alternatives still matter.
- Assume a fire is due because none has occurred recently. | Absence of recent events does not create a balancing requirement.

## P03.02 | future-self-and-measures | easy | analyze | 20,22
An experiment finds that viewing an age-progressed self-image raises hypothetical retirement allocations. Which outcome has been demonstrated?
+ A change in stated allocation in that experimental task | Future-self vividness affected the measured hypothetical choice.
- A rise in actual retirement deposits | Hypothetical allocation is not an observed deposit.
- A permanent improvement in experienced well-being | That outcome and horizon were not measured.
- Equal financial gains for every participant | Neither realized gains nor equal effects were shown.
- A change in the market return on retirement assets | The experiment changes a decision setting, not asset returns.

## P03.03 | insurance-and-reference-points | medium | analyze | 16,17
A person rejects a fair gamble over final wealth but has made no explicit gain–loss comparison. Which evidence would most specifically help distinguish reference-dependent valuation from stable concave utility over final wealth?
+ Vary the reference point while holding final-wealth lotteries fixed. | Stable utility over final wealth predicts invariance; reference dependence can change rankings. This test alone does not identify loss aversion.
- Record the person's dislike of this one gamble again. | One risky choice is compatible with several mechanisms.
- Assume any aversion to risk is a measure of loss aversion. | Risk aversion and loss aversion are distinct.
- Measure only whether the gamble has positive expected value. | Expected value alone does not identify the value function.
- Ask whether the person has ever bought insurance. | Insurance can reflect several motives and constraints.

## P03.04 | delayed-payment-and-trust | medium | analyze | 18,20
A buyer refuses a larger delayed rebate because the seller has repeatedly failed to pay rebates. What is the most relevant alternative to an impatience explanation?
+ Experience has reduced trust in receiving the delayed payment. | Timing and payment risk are confounded in the choice.
- The larger amount necessarily has lower nominal value. | The nominal amount is explicitly larger.
- A delayed payment cannot enter expected utility. | Uncertain delayed payments can be modeled.
- The buyer is responding to a cost already irrecoverably paid. | The choice concerns future receipt.
- The buyer must prefer smaller sums at every date. | The concern may be reliability rather than amount.

## P03.05 | budgeting-and-present-bias | medium | apply | 19,20
A saver moves money into a voluntarily chosen account earmarked for saving, with a withdrawal delay. Which pair of mechanisms could support the saving goal?
+ A saving label plus a restriction on immediate access | Mental accounting and commitment can work together.
- A lower future balance plus a higher spending limit | These changes would not describe the arrangement.
- Repetition of a slogan plus a numerical anchor | Neither is specified by the account design.
- A sunk expenditure plus a guaranteed investment return | The funds are not necessarily spent, and no return is guaranteed.
- A change in prices plus elimination of opportunity cost | The account does neither.

## P03.06 | forecasts-of-well-being | medium | analyze | 20,22
Someone chooses a demanding holiday for its anticipated highlights but later dislikes most days of it. What should a future holiday comparison add?
+ Predictions of ordinary daily experience as well as memorable highlights. | Decision utility and anticipated memory can omit much of experienced time.
- Only the anticipated final photograph. | This narrows the forecast further.
- Only the cheapest ticket among all destinations. | Price alone does not capture the relevant experiences.
- The assumption that remembered and experienced utility coincide. | Their divergence is precisely the issue.
- A rule that the most intense holiday is best. | Intensity need not mean more desirable daily experience.

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
An investment independently multiplies wealth by 1.5 or 0.6 with equal probability each period. A sample contains one of each outcome. Which statement correctly compares expected one-period return with the realized two-period path?
+ Expected one-period return is +5%; the sampled path loses 10%. | The expected multiplier is 1.05; the sampled product is 1.5×0.6 = 0.9.
- Expected one-period return is +10%; the sampled path gains 10%. | Both calculations confuse arithmetic and multiplicative changes.
- Expected one-period return is −10%; the sampled path loses 10%. | The path loss is correct, but the expected one-period return is positive.
- Expected one-period return is +5%; the sampled path gains 5%. | The realized path is determined by multiplication, not the one-period expectation.
- Expected one-period return is 0%; the sampled path breaks even. | The gains and losses are neither equal nor multiplicatively offsetting.
