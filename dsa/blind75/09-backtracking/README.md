# Backtracking

## Core idea

Backtracking is DFS over a decision tree of partial choices, where you **undo** a choice after exploring it so the same state can be reused for the next branch. The pattern is always: choose → explore → un-choose. It's brute force, but organized so you prune dead branches as early as possible instead of generating everything and filtering after.

**Recognition signal:** the problem asks for "all possible ___" (subsets, combinations, arrangements, paths) rather than a single optimal answer — if it asked for just the *count* or the *best* one, DP or greedy might apply instead, so backtracking is specifically for enumerating a full solution space.

## Key structures & idioms

- **General shape:**
  ```python
  def backtrack(path, remaining_choices):
      if <path is a complete/valid solution>:
          results.append(path[:])  # copy! path is mutated in place
          return
      for choice in remaining_choices:
          path.append(choice)
          backtrack(path, <updated remaining_choices>)
          path.pop()  # undo — this is the "backtrack" step
  ```
  The `path.pop()` after the recursive call is the entire idea. Forgetting it is the single most common bug in this category.

- **Subsets**: at each element, branch into two choices — include it or don't. 2^n leaves, one per subset. Alternatively, build incrementally: at each recursive call, add the current `path` as a valid subset, then iterate forward through remaining elements adding one at a time.

- **Combination Sum**: same include/exclude branching, but since elements can be reused, the recursive call for "include" stays at the same index (not `i + 1`) while "skip" moves to `i + 1`. Prune a branch immediately once the running sum exceeds the target — don't wait to find out at the leaf.

- **Word Search (grid)**: DFS from each starting cell, marking cells visited *in place* (e.g. temporarily overwrite with a sentinel character) so you don't revisit them within the current path, then restore the original value when backtracking out. This in-place marking avoids a separate `visited` set and its bookkeeping.

## Complexity cheat sheet

| Problem shape | Time | Space | Notes |
|---|---|---|---|
| Subsets | O(n · 2^n) | O(n) recursion depth (plus O(2^n) output) | Every element is in or out |
| Combination Sum | O(2^t) worst case, t = target/min value | O(target/min value) depth | Pruned hard by the "sum exceeds target" cutoff |
| Word Search | O(rows · cols · 4^L), L = word length | O(L) recursion depth | Pruned by early mismatch and visited marking |

Backtracking complexity bounds are usually loose worst cases — the actual runtime in practice is much lower because of pruning. Say this out loud in an interview; it shows you understand *why* backtracking beats naive full enumeration even though the Big-O looks similar.

## Common pitfalls

- Appending `path` itself instead of `path[:]` (a copy) to the results list — since `path` is mutated afterward, every stored "result" ends up pointing at the same, later-emptied list.
- Forgetting the "undo" step (`path.pop()` / restoring a marked grid cell) — state leaks between branches and produces wrong or duplicate results.
- Not pruning early (e.g. checking the sum-exceeds-target condition only at the leaf instead of the moment it happens) — correctness is fine either way, but you lose the performance backtracking is supposed to provide.
- For "reuse allowed" vs. "use once" problems, mixing up whether the next recursive call should start at the same index or the next one — this is the one line that distinguishes Combination Sum from a use-once variant.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Subsets](subsets.py) | include/exclude branching over all elements |
| [Combination Sum](combination_sum.py) | include/exclude with reuse (stay at same index) + prune on sum |
| [Word Search](word_search.py) | grid DFS with in-place visited marking and restore |
