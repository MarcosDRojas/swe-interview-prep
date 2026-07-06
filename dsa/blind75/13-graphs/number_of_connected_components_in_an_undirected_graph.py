"""
Problem: Number of Connected Components in an Undirected Graph (LeetCode #323)
Difficulty: Medium (Premium)
Category: Graphs
LeetCode: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

Description:
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai,
bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

(This problem is LeetCode Premium-only, so the official statement page isn't public — this
description is written from the well-known problem, not fetched from LeetCode.)

Examples:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.

Time Complexity Target: O(V + E) with union-find (near O(E))
Space Complexity Target: O(V)
"""

from typing import List

def number_of_connected_components_in_an_undirected_graph(n: int, edges: List[List[int]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: Number of nodes, labeled 0..n-1
        edges: Undirected edges

    Returns:
        Number of connected components in the graph
    """
    pass


# Test Cases
def test_number_of_connected_components_in_an_undirected_graph():
    """Test cases for number_of_connected_components_in_an_undirected_graph"""

    test_cases = [
        {
            "name": 'Two components',
            "input": (5, [[0, 1], [1, 2], [3, 4]]),
            "expected": 2
        },
        {
            "name": 'One component',
            "input": (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
            "expected": 1
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = number_of_connected_components_in_an_undirected_graph(*test['input'])
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
    test_number_of_connected_components_in_an_undirected_graph()
