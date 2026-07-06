"""
Problem: Spiral Matrix (LeetCode #54)
Difficulty: Medium
Category: Geometry & Math
LeetCode: https://leetcode.com/problems/spiral-matrix

Description:
Given an m x n matrix, return all elements of the matrix in spiral order.

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

Time Complexity Target: O(rows * cols)
Space Complexity Target: O(1) extra (besides output)
"""

from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        matrix: m x n matrix

    Returns:
        All elements of the matrix visited in spiral order
    """
    pass


# Test Cases
def test_spiral_matrix():
    """Test cases for spiral_matrix"""

    test_cases = [
        {
            "name": '3x3 matrix',
            "input": ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5]
        },
        {
            "name": '3x4 matrix',
            "input": ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = spiral_matrix(*test['input'])
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
    test_spiral_matrix()
