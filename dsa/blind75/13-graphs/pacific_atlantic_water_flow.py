"""
Problem: Pacific Atlantic Water Flow (LeetCode #417)
Difficulty: Medium
Category: Graphs
LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow

Description:
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The
Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r,
c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
north, south, east, and west if the neighboring cell's height is less than or equal to the
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Examples:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
 [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
 [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
 [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
 [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
 [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
 [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
 [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

Time Complexity Target: O(rows * cols)
Space Complexity Target: O(rows * cols)
"""

from typing import List

def pacific_atlantic_water_flow(heights: List[List[int]]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        heights: Grid of heights above sea level

    Returns:
        Coordinates [r, c] where water can flow to both the Pacific and Atlantic (order doesn't matter)
    """
    pass


# Test Cases
def test_pacific_atlantic_water_flow():
    """Test cases for pacific_atlantic_water_flow"""

    test_cases = [
        {
            "name": 'Mixed heights grid',
            "input": ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],),
            "expected": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        },
        {
            "name": 'Single cell',
            "input": ([[1]],),
            "expected": [[0, 0]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = pacific_atlantic_water_flow(*test['input'])
            ok = result is not None and sorted(sorted(x) for x in result) == sorted(sorted(x) for x in test['expected'])

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
    test_pacific_atlantic_water_flow()
