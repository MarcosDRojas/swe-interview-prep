# Sliding Window

## Core idea

When you need to examine every contiguous subarray/substring, a brute force is O(n²) or worse. A sliding window keeps a running range `[left, right]` and expands/shrinks it incrementally, reusing work from the previous position instead of recomputing from scratch — turning it into O(n).

**Recognition signal:** the problem talks about a contiguous subarray/substring satisfying some condition (longest, shortest, contains-at-most-k, no repeats), and the condition can be checked/updated incrementally as the window changes by one element.

## Key structures & idioms

- **Variable-size window (expand right, shrink left on violation):**
  ```python
  left = 0
  window = {}  # or a running count/sum
  best = 0
  for right, ch in enumerate(s):
      # add ch to window
      while <window invalid>:
          # remove s[left] from window
          left += 1
      best = max(best, right - left + 1)
  ```
  This is the shape behind "longest substring without repeating characters" and "longest repeating character replacement."

- **Two-hashmap window (minimum window substring style)**: one map for "what I need" (fixed, built from the target string), one for "what I currently have" in the window, plus a counter of how many required characters are currently satisfied. Shrink from the left greedily whenever the window is still valid, to find the *minimum* valid window rather than the maximum.

- **Fixed-size window**: when the window size is given directly (not part of what you're solving for), you don't need the while-loop shrink — just add the new right element and drop the leftmost element as you slide, both O(1) amortized.

- **Single-pass running extrema (Best Time to Buy and Sell Stock)**: technically a window-of-one-side problem — track the minimum price seen so far and the best profit so far in one pass, rather than checking all pairs.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Brute-force all substrings/subarrays | O(n²) or O(n³) | varies | Baseline |
| Sliding window | O(n) (each pointer moves right at most n times, so O(2n) total) | O(k) where k = alphabet/window content size | Contiguous range with incrementally checkable condition |

## Common pitfalls

- Shrinking the window with an `if` instead of a `while` — if the invalidity can persist after removing just one element, a single `if` leaves the window still invalid.
- Off-by-one on window length — it's `right - left + 1`, not `right - left`.
- In minimum window substring, forgetting to handle characters with repeated required counts (e.g. target needs two `'a'`s) — a single boolean "have I seen this char" isn't enough, you need counts.
- Recomputing the window's validity from scratch on every step instead of updating incrementally — that silently turns your O(n) solution back into O(n²).

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Longest Substring Without Repeating Characters](longest_substring_without_repeating_characters.py) | variable window, shrink while duplicate present |
| [Longest Repeating Character Replacement](longest_repeating_character_replacement.py) | variable window, shrink while `window_size - max_count > k` |
| [Minimum Window Substring](minimum_window_substring.py) | two-hashmap window, shrink to find minimum valid |
| [Best Time to Buy and Sell Stock](best_time_to_buy_and_sell_stock.py) | single pass, track running min price and best profit |
