"""
Problem: Number of Islands (LeetCode #200)
Difficulty: Medium
Category: Graphs
LeetCode: https://leetcode.com/problems/number-of-islands

Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

Examples:
Input: grid = [
 ["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
 ["1","1","0","0","0"],
 ["1","1","0","0","0"],
 ["0","0","1","0","0"],
 ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

Time Complexity Target: O(rows * cols)
Space Complexity Target: O(rows * cols) worst case (recursion stack or visited set)
"""

from typing import List

def number_of_islands(grid: List[List[str]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        grid: 2D grid of '1' (land) and '0' (water)

    Returns:
        Number of islands (connected groups of land cells)
    """
    pass


# Test Cases
def test_number_of_islands():
    """Test cases for number_of_islands"""

    test_cases = [
        {
            "name": 'One connected island',
            "input": ([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']],),
            "expected": 1
        },
        {
            "name": 'Three separate islands',
            "input": ([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']],),
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = number_of_islands(*test['input'])
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
    test_number_of_islands()
