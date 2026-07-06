"""
Problem: Set Matrix Zeroes (LeetCode #73)
Difficulty: Medium
Category: Geometry & Math
LeetCode: https://leetcode.com/problems/set-matrix-zeroes

Description:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Examples:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

Time Complexity Target: O(rows * cols)
Space Complexity Target: O(1) extra (reuse first row/column as markers)
"""

from typing import List


def set_matrix_zeroes(matrix: List[List[int]]) -> None:
    """
    TODO: Implement your solution here (modify the matrix in place, return nothing)

    Args:
        matrix: Grid where any zero must zero out its entire row and column, in place
    """
    pass


# Test Cases
def test_set_matrix_zeroes():
    """Test cases for set_matrix_zeroes (modifies the matrix in place, returns nothing)"""

    test_cases = [
        {"name": "Zero in the middle", "input": [[1, 1, 1], [1, 0, 1], [1, 1, 1]], "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]},
        {"name": "Zero in a corner", "input": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: matrix = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            matrix = [row[:] for row in test['input']]
            set_matrix_zeroes(matrix)
            ok = matrix == test['expected']

            if ok:
                print(f"  [PASS]: {matrix}")
                passed += 1
            else:
                print(f"  [FAIL]: Got {matrix}")
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
    test_set_matrix_zeroes()
