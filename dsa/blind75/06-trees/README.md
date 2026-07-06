# Trees

## Core idea

Almost everything here is **recursion that trusts its own base case** — define what a function returns for a node in terms of what it returns for that node's children, and let the recursion handle the rest. The hard part is rarely the recursion itself; it's correctly identifying what information needs to flow *down* (as parameters) versus *up* (as return values).

**Recognition signal:** the problem is defined on a `TreeNode` with `.left`/`.right`, and the property you care about (depth, balance, sum, validity) is naturally defined in terms of the same property on subtrees.

## Key structures & idioms

- **DFS (recursive), the default tool:**
  ```python
  def dfs(node):
      if not node:
          return <base case>
      left = dfs(node.left)
      right = dfs(node.right)
      return <combine left, right, node.val>
  ```
  Covers invert, max depth, same tree, subtree, max path sum, in various "combine" flavors.

- **BFS / level order** — use a queue (`collections.deque`), process one full level at a time by snapshotting the queue's current length before looping:
  ```python
  queue = deque([root])
  while queue:
      level = []
      for _ in range(len(queue)):
          node = queue.popleft()
          level.append(node.val)
          if node.left: queue.append(node.left)
          if node.right: queue.append(node.right)
  ```

- **BST invariant propagation** — validating a BST isn't just "left < node < right" checked locally; the bound has to carry all the way down. Pass `(low, high)` bounds through the recursion and narrow them at each step, rather than only comparing immediate children.

- **In-order traversal = sorted order for a BST** — the single most useful BST fact. Kth smallest becomes "in-order traversal, stop at the k-th visit" instead of a special algorithm.

- **LCA via BST property** — at each node, if both target values are less than the current node, go left; if both greater, go right; otherwise (split or match) the current node is the LCA. No need for a general-tree LCA algorithm when you know it's a BST.

- **Encode structure explicitly for serialize/deserialize** — preorder traversal with an explicit sentinel for `None` (e.g. `"#"`) is enough to reconstruct the exact tree, because preorder + null markers removes all structural ambiguity.

- **Passing extra state through recursion for "global" answers** (max path sum) — use a mutable closure variable (or a small class/list) to track a running best across the whole recursion, while the return value itself carries only "best path *usable by my parent*" (which must be a single downward path, not a fork).

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| DFS (recursive) | O(n) — visits every node once | O(h) call stack, h = height (O(log n) balanced, O(n) worst case skewed) | Most tree problems |
| BFS (level order) | O(n) | O(w) queue, w = max width (up to O(n)) | Level-by-level problems |
| Construct from traversals | O(n) (with a hashmap index lookup) or O(n²) naive | O(n) | Rebuilding a tree from preorder/inorder |

## Common pitfalls

- Confusing what should be a **parameter** (info flowing down, like BST bounds) with what should be a **return value** (info flowing up, like subtree height) — draw the recursion on paper if unsure.
- Off-by-one between "max path sum through a node" (can use both children, but can't be returned upward as-is) vs. "best downward path from a node" (must pick at most one child) — these are two different quantities computed in the same function.
- Forgetting that "subtree" means an exact match from some node downward, not just "these values appear somewhere" — same-tree check is a helper, not the whole answer.
- Naive `preorder.index(val)` lookups when reconstructing a tree from traversals — O(n) per call makes the whole thing O(n²); precompute a value→index map first.
- Not handling `None` root as a valid, immediate base case before touching `.left`/`.right`.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Invert Binary Tree](invert_binary_tree.py) | DFS, swap children at every node |
| [Maximum Depth of Binary Tree](maximum_depth_of_binary_tree.py) | DFS, `1 + max(left, right)` |
| [Same Tree](same_tree.py) | DFS, compare structure and values in lockstep |
| [Subtree of Another Tree](subtree_of_another_tree.py) | DFS + same-tree check at every node |
| [Lowest Common Ancestor of a Binary Search Tree](lowest_common_ancestor_of_a_binary_search_tree.py) | use BST ordering to choose a direction, no full traversal needed |
| [Binary Tree Level Order Traversal](binary_tree_level_order_traversal.py) | BFS with per-level queue snapshot |
| [Validate Binary Search Tree](validate_binary_search_tree.py) | DFS with propagated (low, high) bounds |
| [Kth Smallest Element in a BST](kth_smallest_element_in_a_bst.py) | in-order traversal = sorted order |
| [Construct Binary Tree from Preorder and Inorder Traversal](construct_binary_tree_from_preorder_and_inorder_traversal.py) | preorder gives roots, inorder splits left/right subtree ranges |
| [Binary Tree Maximum Path Sum](binary_tree_maximum_path_sum.py) | DFS returning "best downward path," tracking global best separately |
| [Serialize and Deserialize Binary Tree](serialize_and_deserialize_binary_tree.py) | preorder + explicit null markers |
