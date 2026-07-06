# Binary Search

## Core idea

Any time you can ask a yes/no question about a candidate answer and the answers to that question are **monotonic** (all "no" then all "yes", or vice versa, across the search space), you can binary search on it — not just on plain sorted arrays. Halving the search space each step gives O(log n) instead of O(n).

**Recognition signal:** the input is sorted, *or* "sorted with a twist" (rotated), *or* the problem asks you to search over a range of possible answers rather than array indices (that variant doesn't appear in this folder's problems but is worth knowing generalizes).

## Key structures & idioms

- **Classic binary search template:**
  ```python
  lo, hi = 0, len(arr) - 1
  while lo <= hi:
      mid = (lo + hi) // 2
      if arr[mid] == target:
          return mid
      elif arr[mid] < target:
          lo = mid + 1
      else:
          hi = mid - 1
  return -1
  ```

- **Rotated sorted array trick**: a rotated sorted array is still sorted on *at least one side* of any midpoint. At each step:
  1. Compare `arr[lo]` to `arr[mid]` to determine which half (`lo..mid` or `mid..hi`) is the properly sorted one.
  2. Check whether the target lies within that sorted half's range.
  3. If yes, recurse/iterate into that half; if no, go to the other half.

  This is the one nontrivial insight in this category — the rest is bookkeeping. Be able to draw a rotated array and walk through why one side is always sorted.

- **Finding the minimum (pivot point)**: same idea, but you're not looking for a target — you're looking for the one index where `arr[i] > arr[i+1]` (the rotation point). Compare `arr[mid]` to `arr[hi]`: if `arr[mid] > arr[hi]`, the minimum is to the right of mid; otherwise it's at or to the left of mid.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Linear scan | O(n) | O(1) | Baseline, or unsorted input |
| Binary search | O(log n) | O(1) iterative / O(log n) recursive (call stack) | Sorted or "sorted with a twist" input |

## Common pitfalls

- `mid = (lo + hi) // 2` can overflow in other languages (not a concern in Python, but say it out loud in an interview — shows awareness) — safer form is `lo + (hi - lo) // 2`.
- Off-by-one in the loop condition (`lo <= hi` vs `lo < hi`) and in updating `lo`/`hi` (`mid` vs `mid ± 1`) — pick a convention and be consistent, then trace a 2-element and 1-element array by hand to check for infinite loops.
- On the rotated array, comparing `arr[mid]` to `arr[lo]` incorrectly when `lo == mid` (2-element window) — handle small windows carefully.
- Assuming there are no duplicates — the classic rotated-array binary search assumes distinct values; duplicates can break the "which half is sorted" check and force a fallback to linear in the worst case.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Find Minimum in Rotated Sorted Array](find_minimum_in_rotated_sorted_array.py) | compare `arr[mid]` vs `arr[hi]` to find the rotation point |
| [Search in Rotated Sorted Array](search_in_rotated_sorted_array.py) | identify the sorted half, then check if target is in its range |
