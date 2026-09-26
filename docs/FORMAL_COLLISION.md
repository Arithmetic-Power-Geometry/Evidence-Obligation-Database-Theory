# Formal Collision Audit: EOD vs Closest Established Formalisms

## 1. Access-method answerability

Established access-method work asks whether a database query can be answered using restricted interfaces and, when answerable, whether an access plan can retrieve all answers under integrity constraints.

This collides directly with any broad EOD claim of being the first theory of "future answerability."

### Shared structure

Both can contain:

- a query target;
- restricted information-producing mechanisms;
- plans that invoke those mechanisms;
- a notion of successful answer recovery.

### Non-equivalence not yet proved

EOD currently adds explicit finite possible worlds, query-disagreeing obstruction pairs, evidence costs, minimum obligations, adaptive outcome branches, and an impossibility witness.

Those additions do **not** by themselves prove expressive separation. They may be encodable as annotations, planning objectives, or derived objects over an access-method formalism.

Therefore the defensible current claim is:

> EOD packages query-relative resolution, acquisition cost, admissibility, and certificates into a single database-state/query semantics.

A strict expressiveness claim remains open.

## 2. Acquisitional query processing

TinyDB/ACQP made physical acquisition part of query processing and addressed when/where/how often sensor samples should be taken.

Therefore "databases that decide what data to acquire" is prior art.

Potential EOD distinction:

- ACQP primarily optimizes execution/acquisition for obtaining query results from sensors.
- EOD's primitive target is invariance of a query across a current version space, and it may return an impossibility certificate when admissible evidence cannot force invariance.

This is a semantic distinction to test, not yet a separation theorem.

## 3. Epistemic planning with sensing

Conditional epistemic planning already represents incomplete possible worlds, sensing actions, observation-contingent plans, and knowledge goals.

Therefore adaptive evidence trees are not novel by themselves.

Potential EOD distinction:

- query-relative database semantics and algebra;
- explicit minimum evidence obligations as query outputs;
- database-level obstruction and impossibility certificates.

Again, this may be a specialization/integration rather than strict expressiveness.

## Surviving research hypothesis

After the collision audit, the strongest responsible hypothesis is narrower:

> EOD is a database-native resolution semantics that treats admissible evidence capability as part of database state and returns a typed resolution object—answer certificate, costed evidence obligation/policy, or impossibility certificate—for a database query.

Whether this constitutes a conservative extension, useful synthesis, or expressively distinct model must be established by formal translation results.

## Required next theorem

Do **not** attempt to prove that sensing plans or access plans cannot represent EOD.

Instead prove a representation theorem:

1. characterize finite deterministic EOD as a query-relative discrimination problem;
2. give an exact translation into a finite conditional sensing problem;
3. identify which EOD objects are preserved by the translation;
4. isolate the additional database-specific structure, if any.

If the translation preserves everything, position EOD as a database abstraction/integration rather than a new foundational expressiveness class.
