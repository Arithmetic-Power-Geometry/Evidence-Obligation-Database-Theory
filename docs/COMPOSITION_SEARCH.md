# Automated search for compositionality limits

The repository now includes an exhaustive finite search over small binary evidence systems.

The search deliberately uses a **coarse local resolution signature**:

\[
(\text{status},\text{possible answers},\text{minimum cost},\text{obstruction count}).
\]

It asks whether two systems can have identical local signatures for Boolean queries \(q\) and \(r\) but different signatures for \(q\land r\).

A found collision would prove only that this particular coarse summary is insufficient for composition. It would **not** prove that no richer EOD annotation can compose.

Run:

```bash
python experiments/search_composition_counterexample.py
```

This search-first methodology prevents a hand-designed example from being mistaken for a general theorem.
