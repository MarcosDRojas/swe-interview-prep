"""
Problem: Graph Valid Tree (LeetCode #261)
Difficulty: Medium (Premium)
Category: Graphs
LeetCode: https://leetcode.com/problems/graph-valid-tree

Description:
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of
edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and
bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

(This problem is LeetCode Premium-only, so the official statement page isn't public — this
description is written from the well-known problem, not fetched from LeetCode.)

Examples:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
Explanation: There is a cycle (1-2-3-1), so it cannot be a tree.

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges.

Time Complexity Target: O(V + E) with union-find (near O(E))
Space Complexity Target: O(V)
"""

from typing import List

def graph_valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        n: Number of nodes, labeled 0..n-1
        edges: Undirected edges

    Returns:
        True if the edges form a single valid tree (connected, no cycles)
    """
    pass


# Test Cases
def test_graph_valid_tree():
    """Test cases for graph_valid_tree"""

    test_cases = [
        {
            "name": 'Valid tree',
            "input": (5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
            "expected": True
        },
        {
            "name": 'Cycle present',
            "input": (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]),
            "expected": False
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = graph_valid_tree(*test['input'])
            ok = result == test['expected']

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
    test_graph_valid_tree()
