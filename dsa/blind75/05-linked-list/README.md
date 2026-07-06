# Linked List

## Core idea

No random access (no `arr[i]`), so the whole game is pointer manipulation: rewiring `.next`, and using **multiple pointers moving at different speeds or offsets** to simulate things arrays get for free (like "the middle" or "n-th from the end").

**Recognition signal:** the problem is phrased in terms of node links rather than indices, or explicitly gives you a `ListNode` with `.val`/`.next`.

## Key structures & idioms

- **Dummy head node** — sidesteps having to special-case "what if the answer starts with a new first node" (merging lists, removing a node). Always create `dummy = ListNode(0, head)` and return `dummy.next`.

- **Iterative reversal** (three pointers: prev, curr, next):
  ```python
  prev = None
  curr = head
  while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt
  return prev
  ```

- **Fast & slow pointers (Floyd's cycle detection)** — slow moves 1 step, fast moves 2. If there's a cycle, they *will* meet inside it (fast gains on slow by 1 each step, so it can't skip over it). Used for cycle detection, finding the middle, and (with a second phase) finding the cycle's start.

- **Two-pointer with a gap (n-th from end)** — advance one pointer `n` steps first, then move both together; when the lead pointer hits the end, the trailing one is exactly `n` from the end. Avoids a separate length-counting pass.

- **Merge via dummy + two pointers**: walk both lists, always attach the smaller current node, advance that list's pointer — classic merge-step from merge sort, just applied to already-sorted lists.

- **Reorder / split-and-interleave**: find the middle (fast/slow), reverse the second half (iterative reversal above), then merge the two halves by alternating nodes. Notice this problem is really three earlier idioms composed together — that composability is the main lesson of this category.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Convert to array first | O(n) time, O(n) extra space | Simple to reason about, but loses the "why linked list" point of the exercise — avoid in an interview unless you say why |
| Pointer manipulation in place | O(n) time, O(1) extra space | The expected approach for nearly everything in this folder |
| Merge k Sorted Lists via heap | O(n log k) | O(k) | See [08. Heap / Priority Queue](../08-heap-priority-queue/README.md) — cross-listed here since it's still fundamentally a linked-list merge |

## Common pitfalls

- Losing the reference to `curr.next` before reassigning `curr.next = prev` during reversal — always save `nxt` first.
- Forgetting the dummy head, then writing awkward special-case branches for "is this the first node."
- Off-by-one in the fast/slow gap technique — decide whether "n-th from the end" is 0-indexed or 1-indexed and walk through a 2-3 node example by hand.
- Not handling `head is None` or a single-node list as a base case before applying multi-pointer logic.
- Mutating `.next` pointers while still relying on the *old* structure elsewhere in the same iteration (order of operations matters more here than almost any other category).

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Reverse Linked List](reverse_linked_list.py) | iterative prev/curr/next reversal |
| [Linked List Cycle](linked_list_cycle.py) | fast & slow pointers (Floyd's) |
| [Merge Two Sorted Lists](merge_two_sorted_lists.py) | dummy head + two-pointer merge |
| Merge k Sorted Lists | see [08. Heap / Priority Queue](../08-heap-priority-queue/README.md) |
| [Remove Nth Node From End of List](remove_nth_node_from_end_of_list.py) | two pointers with an n-node gap |
| [Reorder List](reorder_list.py) | find middle + reverse half + merge/interleave |
