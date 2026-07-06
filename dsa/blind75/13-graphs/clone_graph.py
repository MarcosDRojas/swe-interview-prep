"""
Problem: Clone Graph (LeetCode #133)
Difficulty: Medium
Category: Graphs
LeetCode: https://leetcode.com/problems/clone-graph

Description:
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
 public int val;
 public List<Node> neighbors;
}



Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the
first node with val == 1, the second node with val == 2, and so on. The graph is represented in
the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list
describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given
node as a reference to the cloned graph.

Examples:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

Time Complexity Target: O(V + E)
Space Complexity Target: O(V) for the visited/clone map
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj_list):
    """Build a graph from an adjacency list (1-indexed values, like LeetCode's format)."""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj_list(node):
    """Convert a graph back to an adjacency list (sorted by node value) for comparison."""
    if not node:
        return []
    visited = {}
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur.val in visited:
            continue
        visited[cur.val] = sorted(n.val for n in cur.neighbors)
        for n in cur.neighbors:
            if n.val not in visited:
                stack.append(n)
    return [visited[val] for val in sorted(visited)]


def clone_graph(node: Node) -> Node:
    """
    TODO: Implement your solution here

    Args:
        node: Reference to a node in a connected undirected graph

    Returns:
        A deep copy (clone) of the graph, starting from the equivalent node
    """
    pass


# Test Cases
def test_clone_graph():
    """Test cases for clone_graph"""

    test_cases = [
        {"name": "Four connected nodes", "input": [[2, 4], [1, 3], [2, 4], [1, 3]], "expected": [[2, 4], [1, 3], [2, 4], [1, 3]]},
        {"name": "Single node, no neighbors", "input": [[]], "expected": [[]]},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: adjList = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            original = build_graph(test['input'])
            cloned = clone_graph(original)
            result = graph_to_adj_list(cloned)
            ok = result == test['expected'] and (cloned is None or (original is not None and cloned is not original))

            if result is None and not ok:
                print(f"  [FAIL]: Function not yet implemented (returned None)")
                failed += 1
            elif ok:
                print(f"  [PASS]: {result}")
                passed += 1
            else:
                print(f"  [FAIL]: Got {result}")
                failed += 1

        except Exception as e:
            print(f"  [FAIL]: {type(e).__name__}: {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")

    if failed == 0:
        print("All test cases passed!")
    else:
        print("Some test cases failed. Please review the implementation.")


if __name__ == "__main__":
    test_clone_graph()
