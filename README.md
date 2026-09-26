# Evidence-Obligation Database Theory (EOD)

> A proposed database model in which a database state is defined not only by what it currently knows, but also by what it can still learn.

**Author:** Mohammad Amir Khusru Akhtar  
**Copyright © 2026 Mohammad Amir Khusru Akhtar**  
**License:** Apache License 2.0

## Core idea

Conventional database queries primarily map a stored database state to an answer. In incomplete or uncertain settings they may instead expose certain answers, possible answers, nulls, confidence, provenance, or missing-answer explanations.

EOD introduces a different native query result:

```text
QUERY
  -> ANSWER CERTIFICATE
  -> EVIDENCE OBLIGATION
  -> IMPOSSIBILITY CERTIFICATE
```

The central proposal is that **future evidence-generating capability is part of database state**.

Two systems can therefore contain the same current facts yet be different EOD databases if they have different abilities to acquire evidence that resolves future queries.

## Status

Version 0.1 — theory and finite reference engine under construction.

## License

Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
