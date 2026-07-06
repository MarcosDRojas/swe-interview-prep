"""
Problem: Unique Paths (LeetCode #62)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/unique-paths

Description:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e.,
grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The
robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can
take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Examples:
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
- 1 <= m, n <= 100

Time Complexity Target: O(m * n)
Space Complexity Target: O(n) (rolling row) or O(m * n)
"""

def unique_paths(m: int, n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        m: Number of rows
        n: Number of columns

    Returns:
        Number of unique paths from top-left to bottom-right moving only down or right
    """
    pass


# Test Cases
def test_unique_paths():
    """Test cases for unique_paths"""

    test_cases = [
        {
            "name": '3x7 grid',
            "input": (3, 7),
            "expected": 28
        },
        {
            "name": '3x2 grid',
            "input": (3, 2),
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
            result = unique_paths(*test['input'])
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
    test_unique_paths()
