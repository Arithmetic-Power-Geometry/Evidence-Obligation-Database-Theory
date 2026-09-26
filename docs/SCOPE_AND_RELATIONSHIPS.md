# Scope and Relationships to Established Work

EOD is deliberately positioned against strong neighboring literature.

## Incomplete databases and possible worlds

Incomplete database theory already represents sets of possible complete worlds and studies possible and certain answers. Therefore EOD does **not** claim possible-world semantics as new.

Classical reference:
- Abiteboul, Kanellakis, Grahne (1991), *On the Representation and Querying of Sets of Possible Worlds*.

## Complete and certain query answers

Work on query completeness and incomplete databases already asks when available information suffices for complete answers. EOD does **not** claim query-relative sufficiency itself as new.

Representative reference:
- Levy (VLDB 1996), *Obtaining Complete Answers from Incomplete Databases*.

## Provenance and why-not provenance

Provenance explains how existing inputs produce outputs. Why-not provenance explains missing outputs.

EOD's proposed object is prospective: future evidence sufficient to eliminate target-query disagreement.

Representative reference:
- Green, Karvounarakis, Tannen (PODS 2007), semiring provenance.

## Acquisitional query processing

Sensor database systems such as TinyDB actively control data acquisition and optimize when and where readings are taken. Therefore EOD does **not** claim that databases have never acquired data.

Representative reference:
- Madden, Franklin, Hellerstein, Hong (TODS 2005), *TinyDB: an acquisitional query processing system for sensor networks*.

## Experimental design and diagnostic testing

Minimum-cost tests, test-selection trees, active learning, and hypothesis discrimination are close mathematical neighbors of EOD's finite obligation problem. Their optimization ideas are not claimed as inventions here.

## Falsifiable novelty hypothesis

The current research hypothesis is narrower:

> Evidence-generating capability can be made part of logical database state, with unresolved queries natively denoting resolution obligations or impossibility certificates.

This repository treats that as a proposition to test, not as a settled historical claim.
