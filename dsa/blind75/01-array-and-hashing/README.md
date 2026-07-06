# Array & Hashing

## Core idea

Arrays give O(1) index access but O(n) search. A hash map/set trades space for turning that O(n) search into O(1) average lookup. Most problems in this category are really asking: *"can you avoid the nested loop by remembering what you've already seen?"*

**Recognition signal:** if your first instinct is a nested loop to compare every pair, or to check "have I seen this value/complement before," reach for a hash map or hash set first.

## Key structures & idioms

- **Hash set** — membership/duplicate checks in O(1) avg. `seen = set()`.
- **Hash map (value → index/count)** — the "have I seen the complement" pattern:
  ```python
  seen = {}
  for i, x in enumerate(nums):
      complement = target - x
      if complement in seen:
          return [seen[complement], i]
      seen[x] = i
  ```
- **Frequency counting** — `Counter(s)` or a manual dict, used for anagrams, top-k, character constraints.
- **Prefix / suffix products or sums** — precompute running products/sums from the left and right so you can answer "everything except index i" in O(1) per index without division.
- **Kadane's algorithm** (max subarray) — a single running "best sum ending here" instead of recomputing all subarrays:
  ```python
  best = cur = nums[0]
  for x in nums[1:]:
      cur = max(x, cur + x)
      best = max(best, cur)
  ```
- **Modified binary search on rotated arrays** — a sorted array rotated at a pivot is still "half sorted" at every split; the trick is figuring out *which* half is sorted and whether the target lies in it. (Full binary search treatment lives in [04. Binary Search](../04-binary-search/README.md) — these two problems are cross-listed here because they're also fundamentally array problems.)

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Brute-force nested loop | O(n²) | O(1) | Baseline — always state it, then improve |
| Hash map single pass | O(n) | O(n) | Lookup/complement/duplicate problems |
| Sort first | O(n log n) | O(1)–O(n) | When order doesn't matter and you don't need original indices |
| Prefix/suffix arrays | O(n) | O(n) (or O(1) extra if output array doesn't count) | "Except self" style problems |
| Kadane's | O(n) | O(1) | Running max/min subarray |

## Common pitfalls

- Using a hash map when you don't actually need indices — a `set` is lighter and clearer if you only need membership.
- Forgetting that **division isn't allowed** in "product except self" (breaks on zeros) — that's why prefix/suffix products exist.
- Off-by-one on prefix arrays — decide up front whether `prefix[i]` includes index `i` or stops just before it, and be consistent.
- For max product subarray: unlike sum, a negative number can flip a very negative running product into the new max — you need to track running **min** as well as running max.
- Assuming rotated-array binary search degenerates to a normal search — the "which half is sorted" check must run every iteration, not just once.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Two Sum](two_sum.py) | complement lookup → hash map |
| [Contains Duplicate](contains_duplicate.py) | membership check → hash set |
| [Valid Anagram](valid_anagram.py) | frequency counting or sort-and-compare |
| [Product of Array Except Self](product_of_array_except_self.py) | prefix × suffix product, no division |
| [Maximum Subarray](maximum_subarray.py) | Kadane's algorithm |
| [Maximum Product Subarray](maximum_product_subarray.py) | Kadane's variant tracking running min *and* max |
| Find Minimum in Rotated Sorted Array | see [04. Binary Search](../04-binary-search/README.md) |
| Search in Rotated Sorted Array | see [04. Binary Search](../04-binary-search/README.md) |
| 3Sum | see [02. Two Pointers](../02-two-pointers/README.md) |
| Container With Most Water | see [02. Two Pointers](../02-two-pointers/README.md) |
