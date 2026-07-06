"""
Problem: Rotate Image (LeetCode #48)
Difficulty: Medium
Category: Geometry & Math
LeetCode: https://leetcode.com/problems/rotate-image

Description:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees
(clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix
directly. DO NOT allocate another 2D matrix and do the rotation.

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

Time Complexity Target: O(n^2)
Space Complexity Target: O(1) extra (in place)
"""

from typing import List


def rotate_image(matrix: List[List[int]]) -> None:
    """
    TODO: Implement your solution here (rotate the matrix in place, return nothing)

    Args:
        matrix: n x n matrix to rotate 90 degrees clockwise, in place
    """
    pass


# Test Cases
def test_rotate_image():
    """Test cases for rotate_image (modifies the matrix in place, returns nothing)"""

    test_cases = [
        {"name": "3x3 matrix", "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
        {"name": "4x4 matrix", "input": [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], "expected": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: matrix = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            matrix = [row[:] for row in test['input']]
            rotate_image(matrix)
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
    test_rotate_image()
