# Heap / Priority Queue

## Core idea

When you repeatedly need "the smallest/largest remaining item" rather than a full sort, a heap gives you that in O(log n) per operation instead of re-sorting (O(n log n)) every time something changes. It's the right structure whenever the problem is inherently incremental (streaming data, k-way merge, top-k) rather than a one-shot static sort.

**Recognition signal:** the phrase "kth largest/smallest," "top k," "merge k sorted ___," or "running median" — anything where you need ongoing access to an extreme value as data arrives or as you consume from multiple sources at once.

## Key structures & idioms

- **Python's `heapq` is a min-heap only.** For a max-heap, negate values going in and out:
  ```python
  import heapq
  heap = []
  heapq.heappush(heap, -x)
  largest = -heapq.heappop(heap)
  ```
- **Top K Frequent Elements**: count frequencies (hash map), then either (a) push all `(freq, val)` onto a heap and pop the top k, O(n log n), or (b) use a fixed-size heap of size k, O(n log k) — or note that **bucket sort by frequency** achieves O(n) since frequency is bounded by array length, which is worth mentioning as the optimal approach even if the heap solution is the one you code first.
- **Merge k Sorted Lists**: push the head of each of the k lists onto a min-heap keyed by value; repeatedly pop the smallest, push its `.next` if it exists. This generalizes the two-list merge from [05. Linked List](../05-linked-list/README.md) — same idea, just with k candidates instead of 2, so you need a structure that gives you the min of k things cheaply instead of a single comparison.
- **Find Median from Data Stream**: maintain **two heaps** — a max-heap for the lower half of numbers seen so far, a min-heap for the upper half, kept balanced in size (differ by at most 1). The median is then either the top of the larger heap, or the average of both tops. This is the signature "two-heap" pattern — recognize it whenever you need a running median or a running split-point.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Sort everything upfront | O(n log n) once | O(n) | Static data, one-time query |
| Heap of size n | O(n log n) build, O(log n) per pop | O(n) | Need repeated extremes, don't know k in advance |
| Fixed-size heap of size k | O(n log k) | O(k) | Explicitly need top/bottom k, k known and small |
| Two-heap (running median) | O(log n) per insert, O(1) per query | O(n) | Streaming median / balance point |
| k-way merge via heap | O(n log k), n = total elements, k = number of lists | O(k) | Merging k sorted sources |

## Common pitfalls

- Forgetting `heapq` is min-only and getting max-heap logic backwards (sign errors on push/pop).
- Rebuilding the heap from scratch on every new element instead of incrementally pushing/popping — defeats the point.
- In the two-heap median pattern, forgetting to rebalance sizes after every insert, or breaking the tie rule for which heap gets the "extra" element when the total count is odd.
- Using a heap when a bucket-sort/counting approach is actually O(n) and simpler to reason about (Top K Frequent) — always mention the better bound even if you implement the heap version first.
- In k-way merge, pushing raw list nodes onto the heap when the language's heap needs comparable tuples — pair the value with a tiebreaker (like source-list index) if node objects aren't directly comparable.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Find Median from Data Stream](find_median_from_data_stream.py) | two heaps (max-heap low half, min-heap high half), rebalanced on insert |
| [Top K Frequent Elements](top_k_frequent_elements.py) | frequency count + fixed-size heap (or bucket sort for O(n)) |
| [Merge k Sorted Lists](merge_k_sorted_lists.py) | min-heap of k list heads, pop-and-replace |
