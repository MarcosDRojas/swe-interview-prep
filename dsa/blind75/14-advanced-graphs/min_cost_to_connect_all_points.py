"""
Problem: Min Cost to Connect All Points (LeetCode #1584)
Difficulty: Medium
Category: Advanced Graphs
LeetCode: https://leetcode.com/problems/min-cost-to-connect-all-points

Description:
You are given an array points representing integer coordinates of some points on a 2D-plane,
where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
|xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is
exactly one simple path between any two points.

Examples:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct.

Time Complexity Target: O(n^2 log n) with Prim's on the implicit complete graph
Space Complexity Target: O(n^2) for edges, or O(n) with a lazy heap
"""

from typing import List

def min_cost_to_connect_all_points(points: List[List[int]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        points: 2D integer coordinates

    Returns:
        Minimum total Manhattan-distance cost to connect all points (minimum spanning tree)
    """
    pass


# Test Cases
def test_min_cost_to_connect_all_points():
    """Test cases for min_cost_to_connect_all_points"""

    test_cases = [
        {
            "name": 'Five points',
            "input": ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],),
            "expected": 20
        },
        {
            "name": 'Three points',
            "input": ([[3, 12], [-2, 5], [-4, 1]],),
            "expected": 18
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = min_cost_to_connect_all_points(*test['input'])
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
    test_min_cost_to_connect_all_points()
