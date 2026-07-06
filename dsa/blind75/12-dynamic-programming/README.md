# Dynamic Programming

## Core idea

DP applies when a problem has **overlapping subproblems** (the same smaller question gets asked repeatedly) and **optimal substructure** (the best answer to the whole problem is built from the best answers to its subproblems). The entire skill is: define what `dp[i]` (or `dp[i][j]`) *means* in one sentence, find the recurrence that computes it from smaller states, then decide whether to implement it top-down (recursion + memo) or bottom-up (iterative table).

**Recognition signal:** the problem asks for a count, a min/max, or a yes/no over an optimum ("longest," "minimum number of," "number of ways," "can you reach/form"), and brute force would recompute the same smaller subproblem many times (usually visible as exponential-looking recursion with repeated arguments).

## Key structures & idioms

- **1D DP (sequence problems)** — `dp[i]` depends on a small, fixed window of earlier `dp` values:
  - Climbing Stairs / House Robber: `dp[i] = dp[i-1] + dp[i-2]` (or `max(...)` for robber) — literally Fibonacci-shaped. Note both can be reduced to O(1) space since only the last two values matter.
  - House Robber II (circular): run the linear House Robber twice — once excluding the last house, once excluding the first — because "circular" just means "the first and last can't both be taken," which two linear subcases fully cover.
  - Coin Change: `dp[amount] = min(dp[amount - coin] + 1 for coin in coins if amount >= coin)` — a min over choices, bottom-up from `dp[0] = 0`.
  - Longest Increasing Subsequence: `dp[i]` = length of the longest increasing subsequence *ending at i* = `1 + max(dp[j] for j < i if nums[j] < nums[i])`, O(n²) naive (O(n log n) possible with binary search on a patience-sorting pile, worth mentioning as a follow-up optimization).
  - Word Break / Combination Sum IV / Decode Ways / Jump Game: all "can I reach position i" or "how many ways to reach position i" — `dp[i]` built from some set of valid predecessors `dp[j]`.

- **2D DP (two-sequence or grid problems)**:
  - Longest Common Subsequence: `dp[i][j]` = LCS length of `text1[:i]` and `text2[:j]`. If characters match, `dp[i][j] = 1 + dp[i-1][j-1]`; otherwise `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.
  - Unique Paths: `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (ways to reach a cell = sum of ways to reach the cell above and the cell to the left).

- **Top-down vs. bottom-up**: top-down (recursion + `@lru_cache` or a manual memo dict) mirrors your brute-force thinking most directly — write the brute force first, then add memoization. Bottom-up (iterative, filling a table from the base case up) avoids recursion-depth limits and is usually what you convert to once the recurrence is confirmed correct.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Brute-force recursion (no memo) | exponential, e.g. O(2^n) | O(n) call stack | Baseline — always state it and show why it recomputes work |
| Top-down with memoization | O(number of distinct states) | O(states) memo + O(depth) call stack | Once you've confirmed the recurrence |
| Bottom-up table | O(number of distinct states) | O(states), often reducible to O(1) or O(n) with rolling variables | Preferred final form — no recursion overhead |

## Common pitfalls

- Jumping straight to the recurrence without stating what `dp[i]` *means* in a sentence — if you can't say it in one sentence, the recurrence will have bugs.
- Off-by-one on base cases (`dp[0]`, empty string/subsequence cases) — these anchor everything built on top, verify them first by hand on a tiny example.
- For counting problems, confusing "at least one way" (boolean OR, like Word Break) with "number of ways" (sum, like Combination Sum IV / Decode Ways) — same recursion shape, different combination operator.
- In 2D DP, mixing up row/column indices or off-by-one between "string index" and "dp array index" (many solutions use `dp` sized `(n+1)` to cleanly represent the empty-prefix base case).
- Not recognizing when O(n²) can be reduced to O(1) or O(n) extra space because only a fixed window of previous states is ever used (House Robber, Climbing Stairs, LCS row-by-row).

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Climbing Stairs](climbing_stairs.py) | `dp[i] = dp[i-1] + dp[i-2]` |
| [Coin Change](coin_change.py) | min-over-choices, bottom-up from `dp[0] = 0` |
| [Longest Increasing Subsequence](longest_increasing_subsequence.py) | `dp[i]` = best subsequence ending at i |
| [Longest Common Subsequence](longest_common_subsequence.py) | 2D DP, match vs. no-match branches |
| [Word Break](word_break.py) | `dp[i]` = can prefix of length i be segmented |
| [Combination Sum IV](combination_sum_iv.py) | count-the-ways variant, sum not min |
| [House Robber](house_robber.py) | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` |
| [House Robber II](house_robber_ii.py) | circular — run House Robber twice on two linear subarrays |
| [Decode Ways](decode_ways.py) | count-the-ways over valid 1- and 2-digit decodings |
| [Unique Paths](unique_paths.py) | 2D grid DP, sum of above and left |
| [Jump Game](jump_game.py) | reachability DP (often reducible to a greedy furthest-reach scan) |
