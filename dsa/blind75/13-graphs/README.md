# Graphs

## Core idea

Most graph problems are DFS or BFS with one extra piece of bookkeeping layered on: a `visited` set (don't reprocess a node), an in-degree count (topological ordering), or a union-find structure (connectivity). Get comfortable building an adjacency list from raw input first — that's usually step 0 and is easy to fumble under pressure.

**Recognition signal:** the problem involves a grid (implicit graph — each cell connects to its neighbors), an explicit list of nodes/edges, or a list of prerequisite/dependency pairs (implies a directed graph and likely topological sort).

## Key structures & idioms

- **Build the adjacency list first:**
  ```python
  from collections import defaultdict
  graph = defaultdict(list)
  for a, b in edges:
      graph[a].append(b)
      graph[b].append(a)  # only if undirected
  ```
- **DFS/BFS with visited set** — the universal template:
  ```python
  visited = set()
  def dfs(node):
      if node in visited:
          return
      visited.add(node)
      for neighbor in graph[node]:
          dfs(neighbor)
  ```
- **Grid as implicit graph (Number of Islands, Pacific Atlantic)** — neighbors are the 4 (or 8) adjacent cells; treat visited cells the same as any graph traversal (a separate `visited` set, or mutate the grid in place if allowed, e.g. flipping `'1'` to `'0'`).
- **Multi-source BFS/DFS (Pacific Atlantic Water Flow)** — instead of checking "can each cell reach both oceans" (slow, checks from every cell), start the search **from the oceans inward**: flood-fill from all Pacific-adjacent cells, separately flood-fill from all Atlantic-adjacent cells, then intersect the two reachable sets. Flipping the direction of the search is the key insight.
- **Clone Graph** — DFS/BFS while maintaining a hash map from original node → cloned node, so you never clone the same node twice and correctly handle cycles.
- **Topological sort (Course Schedule I/II)** — two equivalent approaches:
  - *Kahn's algorithm (BFS)*: compute in-degree for every node, start a queue with all in-degree-0 nodes, repeatedly pop and decrement neighbors' in-degrees, pushing any that hit 0. If you process fewer than all nodes, there's a cycle.
  - *DFS with a recursion-stack marker*: DFS each node, tracking both "fully visited" and "currently in the recursion stack" — hitting a node that's in the current stack means a cycle.
  Course Schedule I asks "is it possible" (cycle detection only); Course Schedule II asks for the actual order (same algorithm, but collect the pop/finish order).
- **Graph Valid Tree / Connected Components (Union-Find)** — a tree is exactly a connected graph with `n - 1` edges and no cycles. Union-Find (disjoint set) lets you detect a cycle in O(near-1) per union: if two nodes being connected are already in the same set, adding that edge creates a cycle.
  ```python
  parent = list(range(n))
  def find(x):
      while parent[x] != x:
          parent[x] = parent[parent[x]]  # path compression
          x = parent[x]
      return x
  def union(a, b):
      ra, rb = find(a), find(b)
      if ra == rb:
          return False  # already connected -> would create a cycle
      parent[ra] = rb
      return True
  ```
- **Alien Dictionary** — build a graph where an edge `a -> b` means character `a` comes before character `b`, derived by comparing each pair of adjacent words and finding their first differing character. Then topologically sort the character graph — same algorithm as Course Schedule, applied to letters instead of courses.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| DFS/BFS traversal | O(V + E) | O(V) visited set/recursion stack | Standard reachability/connectivity |
| Multi-source BFS/DFS | O(V + E) | O(V) | "Can reach from multiple starting points" — flip direction if that's cheaper |
| Topological sort (Kahn's or DFS) | O(V + E) | O(V) | Ordering with dependency constraints, cycle detection in a directed graph |
| Union-Find | O(E · α(V)) ≈ O(E) practically | O(V) | Connectivity / cycle detection, especially with incremental edges |

## Common pitfalls

- Forgetting to mark a node visited **before** recursing into its neighbors (or right when you enqueue it for BFS) — leads to infinite loops or duplicate work on cycles.
- For directed graphs, conflating "visited overall" with "visited in the current DFS path" — cycle detection specifically needs the latter (recursion-stack membership), not just a global visited set.
- In grid problems, forgetting boundary checks before indexing neighbors, or not handling all 4 directions consistently.
- Building an undirected adjacency list from directed input (or vice versa) — re-read the problem statement on whether edges are one-way or two-way.
- In Union-Find, skipping path compression and union by rank — without them, `find` degrades toward O(n) per call on adversarial inputs.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Number of Islands](number_of_islands.py) | grid DFS/BFS, mark visited cells |
| [Clone Graph](clone_graph.py) | DFS/BFS + hashmap of original → clone |
| [Pacific Atlantic Water Flow](pacific_atlantic_water_flow.py) | multi-source BFS/DFS from both oceans inward, intersect results |
| [Course Schedule](course_schedule.py) | topological sort / cycle detection in a directed graph |
| [Course Schedule II](course_schedule_ii.py) | topological sort, return the actual order |
| [Graph Valid Tree](graph_valid_tree.py) | union-find, n-1 edges and no cycle |
| [Number of Connected Components in an Undirected Graph](number_of_connected_components_in_an_undirected_graph.py) | union-find, count distinct roots |
| [Alien Dictionary](alien_dictionary.py) | derive edges from adjacent word pairs, then topological sort |
