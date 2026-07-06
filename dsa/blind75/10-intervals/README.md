# Intervals

## Core idea

Almost every interval problem becomes trivial once the intervals are **sorted by start time** — overlap questions turn into a simple linear scan comparing each interval only to the *last one you kept*, instead of comparing every pair.

**Recognition signal:** input is a list of `[start, end]` pairs, and the question involves merging, inserting, or counting overlaps.

## Key structures & idioms

- **Sort by start, then scan and compare to the last merged interval:**
  ```python
  intervals.sort(key=lambda x: x[0])
  merged = [intervals[0]]
  for start, end in intervals[1:]:
      if start <= merged[-1][1]:      # overlaps last kept interval
          merged[-1][1] = max(merged[-1][1], end)
      else:
          merged.append([start, end])
  ```
- **Overlap test**: two intervals `[a, b]` and `[c, d]` overlap iff `a <= d and c <= b`. Internalize this one comparison — it's reused in every problem in this category.
- **Insert Interval**: rather than inserting then re-sorting/merging everything (O(n log n)), walk the already-sorted list once in three phases — intervals entirely before the new one (copy as-is), intervals overlapping the new one (merge into it, expanding its bounds), intervals entirely after (copy as-is). One O(n) pass, no sort needed since the input is already sorted.
- **Non-overlapping Intervals (minimum removals)**: this is really an **interval scheduling / greedy** problem — sort by **end** time (not start), and greedily keep an interval whenever it starts at or after the end of the last interval you kept. Sorting by end time maximizes the number of non-overlapping intervals you can keep, which minimizes the number you must remove.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Compare all pairs | O(n²) | O(1) | Baseline |
| Sort + single scan | O(n log n) (dominated by the sort) | O(n) for output | Merge / insert / count-overlaps |
| Greedy by end time | O(n log n) | O(1) extra | Maximize kept / minimize removed intervals |

## Common pitfalls

- Sorting by the wrong key — merge/insert problems sort by **start**, but the "minimum removals to eliminate overlaps" problem needs to sort by **end** — mixing these up gives a plausible-looking but wrong greedy.
- Off-by-one on the overlap test — deciding whether touching endpoints (`a == d`) count as overlapping depends on the problem statement; check whether intervals are inclusive.
- In Insert Interval, forgetting that the new interval can overlap **multiple** existing intervals in a row — the merge phase needs a `while`/loop, not a single `if`.
- Mutating the input list while iterating over it, causing skipped or repeated elements.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Insert Interval](insert_interval.py) | three-phase single pass (before / overlapping-merge / after), no full re-sort needed |
| [Merge Intervals](merge_intervals.py) | sort by start, scan and merge into last kept interval |
| [Non-overlapping Intervals](non_overlapping_intervals.py) | greedy, sort by end time, keep if start >= last kept end |
