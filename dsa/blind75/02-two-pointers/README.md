# Two Pointers

## Core idea

Instead of checking every pair (O(n²)), walk two indices toward each other (or in the same direction at different speeds) across a **sorted** array or a string, eliminating a whole set of candidates with each comparison instead of one at a time.

**Recognition signal:** the problem involves a sorted array (or can be sorted without losing what you need), and asks about pairs/triples summing to something, or comparing from both ends inward.

## Key structures & idioms

- **Opposite-direction pointers** (left at start, right at end, move inward):
  ```python
  lo, hi = 0, len(arr) - 1
  while lo < hi:
      # evaluate arr[lo], arr[hi]
      # move lo forward, hi backward, or both, based on the comparison
  ```
  This is the backbone of both palindrome checks and container/area problems: at each step you can prove that one side is definitely not part of a better answer, so you discard it.

- **Fix one, two-pointer the rest** (3Sum): sort the array, fix the first element, then two-pointer the remaining subarray for the other two. Turns an O(n³) brute force into O(n²).
  ```python
  nums.sort()
  for i in range(len(nums)):
      lo, hi = i + 1, len(nums) - 1
      while lo < hi:
          s = nums[i] + nums[lo] + nums[hi]
          if s == 0: ...
          elif s < 0: lo += 1
          else: hi -= 1
  ```
  Watch for duplicate skipping so you don't emit the same triple twice.

- **Greedy elimination proof** (Container With Most Water): area is `min(height[lo], height[hi]) * (hi - lo)`. Moving the *taller* pointer can only shrink or keep the width while capping height at the same shorter wall — it can never improve. So you always move the shorter pointer. This is the key insight, not a rule to memorize blindly — be able to justify it out loud.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Brute-force all pairs/triples | O(n²) / O(n³) | O(1) | Baseline |
| Two pointers on sorted array | O(n) per fixed element, O(n²) total for 3Sum, O(n) for pair problems | O(1) extra (O(log n)–O(n) for the sort) | Sorted input, looking for pairs/triples matching a target |

## Common pitfalls

- Forgetting to sort first when the problem doesn't explicitly say the input is sorted (3Sum) — two pointers only works because sorted order lets you reason about which side to move.
- Not skipping duplicates in 3Sum, producing duplicate triples in the output.
- In palindrome checks, forgetting to skip non-alphanumeric characters and normalize case before comparing.
- In Container With Most Water, moving the wrong pointer (moving the taller one) — re-derive the proof above if you're not sure which one to move.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Valid Palindrome](valid_palindrome.py) | opposite-direction pointers, skip non-alphanumeric |
| [3Sum](three_sum.py) | sort + fix one + two-pointer the rest, skip duplicates |
| [Container With Most Water](container_with_most_water.py) | opposite-direction pointers, always move the shorter wall |
