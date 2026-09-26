# Experimental plan toward a publication-grade EOD evaluation

## Phase A — exhaustive finite audit

Enumerate small explicit evidence systems and compare:

- exact fixed obligation cost;
- exact adaptive worst-case cost;
- greedy fixed cost;
- resolvability/impossibility rate;
- obstruction size.

Purpose: validate implementation and discover structural conjectures.

## Phase B — controlled synthetic scaling

Generate larger world/evidence systems with controlled:

- number of worlds;
- number of evidence operations;
- outcome alphabet size;
- evidence cost distribution;
- redundancy;
- query-answer classes;
- fraction of inadmissible operations.

Measure runtime, memory, obligation cost, approximation ratio, certificate size, and adaptive gap.

## Phase C — database baselines

Compare semantic outputs against:

1. relational representation;
2. possible-world / certain-answer evaluation;
3. provenance-style explanation;
4. acquisitional/sensor-query framing where applicable.

The comparison must distinguish semantic capability from implementation speed.

## Phase D — application workloads

Candidate domains should have naturally meaningful future evidence operations, such as:

- data-quality repair/verification;
- entity-resolution verification;
- sensor acquisition;
- diagnostic decision support using public benchmark data;
- fraud investigation with staged evidence.

No application should be selected merely because it makes EOD look favorable.

## Phase E — ablation

Remove one EOD component at a time:

- costs;
- admissibility;
- adaptive branching;
- impossibility certification;
- query-relative obstruction.

Measure what explanatory or optimization capability is lost.

## Paper-freeze criterion

Do not freeze the manuscript until theory, algorithms, baselines, scaling experiments, and at least one convincing application workload are complete and reproducible.
