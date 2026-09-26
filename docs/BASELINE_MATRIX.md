# Closest-neighbor baseline matrix

EOD must be evaluated against neighboring problems without collapsing their distinctions.

| Neighbor | Established focus | Collision with EOD | Required comparison |
|---|---|---|---|
| Incomplete DB / certain answers | answers invariant across possible completions | shared possible-world/query-invariance machinery | show what evidence capability adds beyond current certain/possible answers |
| Query answerability under access methods | whether a query can be answered through constrained interfaces | very close to future answerability | formal translation or separation is mandatory |
| Acquisitional query processing / TinyDB | where, when, how often to physically acquire sensor data; acquisition-aware optimization | very close to cost-aware evidence acquisition | distinguish sensor sampling/query execution from query-relative resolution certificates |
| Provenance / why-not | explanation of produced or missing answers | close to certificates/explanations | compare backward/missing-answer explanation with future resolving evidence |
| Active testing / information acquisition | select observations/tests to discriminate hypotheses | close algorithmically | do not claim test-selection optimization itself as novel |
| Epistemic planning with sensing | action policies that make propositions known | potentially close to adaptive EOD | compare database query semantics, state representation, and certificate objects |

## Current strongest risk

**Access-method answerability and epistemic planning are the two most important formal novelty risks.**

The next theory milestone must therefore prove an explicit relationship: an embedding, equivalence on a fragment, or a separation under clearly stated assumptions. Merely using different terminology is insufficient.
