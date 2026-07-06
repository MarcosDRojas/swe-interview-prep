# Advanced Graphs

## Core idea

This folder covers graphs with **weighted edges**, where "shortest/cheapest" replaces plain reachability — plus one classic Eulerian-path problem. The tools are specific named algorithms (Dijkstra, Prim's/Kruskal's for minimum spanning tree, Hierholzer's for Eulerian paths) rather than a single general template, so recognizing *which* named algorithm applies is most of the battle.

**Recognition signal:** edges have weights/costs (not just "connected or not"), and the question asks for a minimum cost path, minimum cost to connect everything, or a route that uses every edge exactly once.

## Key structures & idioms

- **Dijkstra's algorithm (Network Delay Time)** — shortest path from a single source in a graph with **non-negative** weights. Use a min-heap keyed by distance; always expand the currently-closest unvisited node next, relaxing its neighbors' distances.
  ```python
  import heapq
  dist = {node: float('inf') for node in nodes}
  dist[source] = 0
  heap = [(0, source)]
  while heap:
      d, node = heapq.heappop(heap)
      if d > dist[node]:
          continue  # stale entry, already found a better path
      for neighbor, weight in graph[node]:
          nd = d + weight
          if nd < dist[neighbor]:
              dist[neighbor] = nd
              heapq.heappush(heap, (nd, neighbor))
  ```
  This is the same min-heap "always take the smallest next" instinct as [08. Heap / Priority Queue](../08-heap-priority-queue/README.md), applied to path costs instead of raw values.

- **Minimum Spanning Tree (Min Cost to Connect All Points)** — connect all nodes with the minimum total edge weight, no cycles. Two standard approaches:
  - *Prim's*: like Dijkstra, but the priority is "cheapest edge to add a new node to the growing tree," not "shortest path from the source." Min-heap of `(edge_weight, node)`, greedily grow the tree.
  - *Kruskal's*: sort all edges by weight, add each edge via Union-Find (see [13. Graphs](../13-graphs/README.md)) as long as it doesn't connect two nodes already in the same component (i.e. doesn't create a cycle).
  For "all points on a plane" style problems, the graph is implicit and complete (every pair of points is a potential edge, weighted by distance) — you generate edges rather than being handed them.

- **Eulerian path (Reconstruct Itinerary)** — a path that uses every edge exactly once. Build an adjacency list (sorted, since you usually need lexicographically smallest results), then run **Hierholzer's algorithm**: DFS, but only add a node to the final path *after* you've exhausted all of its outgoing edges — post-order, not pre-order. This ensures dead-ends get "used up" before their parent edge is finalized, so no edge is left stranded.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Dijkstra (heap-based) | O((V + E) log V) | O(V + E) | Single-source shortest path, non-negative weights |
| Prim's (heap-based) | O(E log V) | O(V + E) | Minimum spanning tree, dense-ish graphs |
| Kruskal's (sort + union-find) | O(E log E) | O(V) | Minimum spanning tree, sparse graphs or edge list already given |
| Hierholzer's (Eulerian path) | O(E log E) with sorted adjacency, O(E) traversal | O(E) | Must use every edge exactly once |

## Common pitfalls

- Using Dijkstra on a graph with **negative** edge weights — it assumes non-negative weights and will silently give wrong answers; that requires Bellman-Ford instead (not in this folder, but worth knowing the boundary).
- Not skipping "stale" heap entries in Dijkstra (a node can be pushed multiple times at different distances before being finalized) — check `if d > dist[node]: continue`.
- In MST problems over points on a plane, forgetting the graph is complete (O(n²) possible edges) — for small n this is fine, but say the complexity out loud.
- In Reconstruct Itinerary, building the path pre-order (adding a node when you *arrive*) instead of post-order (adding when you're *done* with it) — this is the one detail that makes or breaks Hierholzer's.
- Forgetting to reverse the final path at the end when building it post-order (Hierholzer's naturally produces the path backwards).

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Reconstruct Itinerary](reconstruct_itinerary.py) | Hierholzer's algorithm, post-order DFS on edges |
| [Min Cost to Connect All Points](min_cost_to_connect_all_points.py) | minimum spanning tree (Prim's or Kruskal's) on an implicit complete graph |
| [Network Delay Time](network_delay_time.py) | Dijkstra's shortest path from a single source |
