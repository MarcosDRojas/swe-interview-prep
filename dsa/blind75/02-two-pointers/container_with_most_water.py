"""
Problem: Container With Most Water (LeetCode #11)
Difficulty: Medium
Category: Two Pointers
LeetCode: https://leetcode.com/problems/container-with-most-water

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the i^th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains
the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def container_with_most_water(height: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        height: Heights of the vertical lines

    Returns:
        Maximum amount of water a container can store
    """
    pass


# Test Cases
def test_container_with_most_water():
    """Test cases for container_with_most_water"""

    test_cases = [
        {
            "name": 'Basic example',
            "input": ([1, 8, 6, 2, 5, 4, 8, 3, 7],),
            "expected": 49
        },
        {
            "name": 'Two lines only',
            "input": ([1, 1],),
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
            result = container_with_most_water(*test['input'])
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
    test_container_with_most_water()
