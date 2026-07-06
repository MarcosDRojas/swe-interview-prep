# Data Structures Review

A standalone refresher on the data structures interviews expect you to know cold — what each one is, its core operations with Big-O, when to reach for it, and the gotchas that trip people up under pressure. This is structure-level knowledge, independent of any specific Blind75 problem; see [blind75/](blind75/README.md) for pattern-level practice built on top of these.

## Quick-reference: operation complexity

| Structure | Access | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| Array (static) | O(1) | O(n) | — | — | O(n) |
| Dynamic array (Python list) | O(1) | O(n) | O(1) amortized end / O(n) middle | O(n) | O(n) |
| Singly linked list | O(n) | O(n) | O(1) at known node | O(1) at known node | O(n) |
| Doubly linked list | O(n) | O(n) | O(1) at known node | O(1) at known node | O(n) |
| Stack | O(n) | O(n) | O(1) top | O(1) top | O(n) |
| Queue / Deque | O(n) | O(n) | O(1) ends | O(1) ends | O(n) |
| Hash table | — | O(1) avg / O(n) worst | O(1) avg / O(n) worst | O(1) avg / O(n) worst | O(n) |
| Binary search tree (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Binary search tree (unbalanced) | O(n) | O(n) | O(n) | O(n) | O(n) |
| Binary heap | O(1) min/max | O(n) | O(log n) | O(log n) | O(n) |
| Trie | — | O(L), L = key length | O(L) | O(L) | O(total chars, shared prefixes) |
| Graph (adjacency list) | — | O(V + E) traversal | O(1) edge | O(degree) edge | O(V + E) |
| Union-Find | — | O(α(n)) find | O(α(n)) union | — | O(V) |

`α(n)` (inverse Ackermann) is effectively constant for any input size that fits in memory — treat Union-Find operations as O(1) in an interview.

---

## Arrays

Contiguous memory, so index access is O(1) — the trade-off is that insert/delete in the middle requires shifting every element after it, O(n).

- **Python lists are dynamic arrays**: `append` is O(1) amortized (occasional O(n) resize, spread out over many appends), but `insert(0, x)` or `pop(0)` are O(n) since everything shifts.
- **Static vs. dynamic**: a plain array (fixed size, e.g. in C) can't grow; a dynamic array (Python `list`, Java `ArrayList`) doubles its backing capacity when full, which is what makes amortized append O(1).
- **When to use**: default choice when you need order, index access, and don't need frequent insert/delete away from the end.
- **Gotcha**: slicing (`arr[a:b]`) creates a new O(n) copy in Python — be aware of this if you're reasoning about complexity in a loop that slices repeatedly.

## Linked Lists

A chain of nodes, each holding a value and a pointer to the next (and, for doubly linked, the previous). No index access — reaching the k-th node costs O(k).

- **Singly linked**: `.next` only. Cheap to build, but can't walk backward, and deleting a node requires a reference to its *predecessor*.
- **Doubly linked**: `.next` and `.prev`. Costs more memory per node but allows O(1) deletion given just the node itself, and O(1) traversal in either direction — this is why an LRU cache is typically a doubly linked list + hash map.
- **When to use**: frequent insertion/deletion at arbitrary positions once you already have a reference to the location, or when you need O(1) operations at both ends without the resize behavior of a dynamic array (see Deque below).
- **Gotcha**: always consider a dummy/sentinel head node to avoid special-casing "the list is empty" or "we're modifying the head."

## Stacks

LIFO (last in, first out). Push and pop from the same end — O(1) for both if backed by a dynamic array or a linked list with a head pointer.

- **Backing structure**: a Python `list` used with `append`/`pop` (from the end) is already an efficient stack — no need for a separate class.
- **When to use**: anything with nested/matching structure (parentheses, function call frames, undo history), or where you need "the most recent thing that hasn't been resolved yet" (see [11. Stack](blind75/11-stack/README.md) for monotonic-stack techniques built on top of this).
- **Gotcha**: don't use `list.pop(0)` or `list.insert(0, x)` to simulate a stack from the "wrong" end — that's O(n) per operation; always operate on the end of the list.

## Queues & Deques

FIFO (first in, first out) for a plain queue; a deque (double-ended queue) allows O(1) push/pop from **both** ends.

- **Backing structure**: use `collections.deque` in Python — a Python `list` is a bad queue because `pop(0)` is O(n) (it has to shift every remaining element).
- **When to use**: BFS traversal (graphs, trees, grids), sliding-window problems that need O(1) access to both the oldest and newest element, task scheduling.
- **Gotcha**: reaching for `list` instead of `deque` for a queue is one of the most common "silently O(n) instead of O(1)" mistakes in Python interview code.

## Hash Tables (Hash Maps / Hash Sets)

Maps keys to values (or just stores keys, for a set) via a hash function that converts a key into a bucket index, giving O(1) average-case lookup/insert/delete.

- **Why O(1) average, O(n) worst case**: worst case only shows up with pathological hash collisions (many keys hashing to the same bucket) — in practice and in almost all interview contexts, treat it as O(1).
- **Requirements**: keys must be hashable (immutable in Python — no `list` or `dict` as a key; use `tuple` instead).
- **When to use**: anything needing "have I seen this before," frequency counting, or O(1) lookup by key instead of scanning — this is the single highest-leverage structure in interview prep; see [01. Array & Hashing](blind75/01-array-and-hashing/README.md).
- **Gotcha**: iteration order in Python `dict` is insertion order (guaranteed since 3.7), but don't rely on hash-based ordering assumptions from other languages.

## Trees (Binary Trees & Binary Search Trees)

A binary tree is a node with up to two children. A **binary search tree (BST)** additionally guarantees: everything in the left subtree is smaller, everything in the right subtree is larger — which is what makes O(log n) search possible *if the tree is balanced*.

- **Balanced vs. unbalanced**: a BST built by inserting already-sorted data degenerates into a linked list (O(n) operations) unless it's self-balancing (AVL, Red-Black tree). Interview problems usually assume or construct a reasonably balanced tree, but know the failure mode.
- **Traversal orders**: pre-order (node, left, right), in-order (left, node, right — produces sorted output for a BST), post-order (left, right, node). Know which one you need before writing the recursion.
- **When to use**: hierarchical data, or when you need ordered data with faster-than-array insert/delete (at the cost of losing O(1) index access) — see [06. Trees](blind75/06-trees/README.md).
- **Gotcha**: recursive tree functions are bounded by O(h) stack depth (h = height) — O(log n) for balanced, but O(n) worst case for a degenerate tree, which can hit Python's recursion limit on large inputs.

## Heaps (Priority Queues)

A binary tree stored in an array, satisfying the heap property (parent is always ≤ both children for a min-heap, or ≥ for a max-heap) — not a BST; siblings have no ordering relationship, only the parent/child relationship is guaranteed.

- **Why it's not sorted**: a heap only guarantees the *root* is the min/max, not that the whole structure is ordered — that's exactly why extracting the min/max is O(log n) (fix up the tree) rather than O(1) traversal + resort.
- **Array representation**: for a node at index `i`, children are at `2i+1` and `2i+2`, parent is at `(i-1)//2` — no explicit pointers needed.
- **Python's `heapq`**: min-heap only; negate values for a max-heap (see [08. Heap / Priority Queue](blind75/08-heap-priority-queue/README.md)).
- **When to use**: repeated access to the current min/max as the data set changes (streaming), k-way merges, "top k" problems, scheduling by priority.
- **Gotcha**: building a heap from an existing list via `heapify` is O(n), not O(n log n) — cheaper than pushing elements one at a time if you already have all the data upfront.

## Tries (Prefix Trees)

A tree where each path from the root spells out a prefix, and shared prefixes across different words share the same path — see [07. Trie](blind75/07-trie/README.md) for full detail.

- **When to use**: prefix search, autocomplete, word-dictionary lookups where many words share prefixes.
- **Gotcha**: don't confuse "word exists in trie" with "prefix exists in trie" — needs an explicit end-of-word marker per node.

## Graphs

A set of nodes (vertices) and connections (edges), which may be directed or undirected, weighted or unweighted — see [13. Graphs](blind75/13-graphs/README.md) and [14. Advanced Graphs](blind75/14-advanced-graphs/README.md) for traversal and algorithm detail.

- **Adjacency list** (`dict[node] -> list of neighbors`): O(V + E) space, efficient for sparse graphs (most interview graphs) — the default choice.
- **Adjacency matrix** (`V x V` grid, `matrix[i][j] = weight or 1/0`): O(V²) space, but O(1) edge-existence check — worth it only for dense graphs or when you need frequent "are these two nodes connected" queries.
- **When to use**: relationships/networks, dependency graphs, grids (implicitly a graph where each cell connects to its neighbors).
- **Gotcha**: always clarify directed vs. undirected before building the adjacency list — it changes whether you add the edge in one direction or both.

## Union-Find (Disjoint Set)

Tracks a partition of elements into disjoint groups, supporting near-O(1) "are these two elements in the same group" and "merge these two groups" — see [13. Graphs](blind75/13-graphs/README.md#key-structures--idioms) for the implementation.

- **Path compression** (flatten the tree toward the root during `find`) and **union by rank/size** (attach the smaller tree under the bigger one) are both required to get the near-constant-time bound — without them it degrades toward O(n) per operation on adversarial input.
- **When to use**: connectivity queries, cycle detection in undirected graphs, Kruskal's minimum spanning tree.

---

## What interviewers are actually listening for

Naming the structure is table stakes. What separates a strong answer:
1. **State the Big-O and justify it** ("hash map gives O(1) average because...") rather than just asserting it.
2. **Know the failure mode** (hash collisions, unbalanced trees, adversarial Union-Find input) even if you don't need to handle it for this problem.
3. **Justify the trade-off against the next-best alternative** ("I could sort instead, but that's O(n log n) and I only need O(1) lookups, so a hash set is better here").
