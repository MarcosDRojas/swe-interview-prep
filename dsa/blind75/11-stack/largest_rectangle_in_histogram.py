"""
Problem: Largest Rectangle in Histogram (LeetCode #84)
Difficulty: Hard
Category: Stack
LeetCode: https://leetcode.com/problems/largest-rectangle-in-histogram

Description:
Given an array of integers heights representing the histogram's bar height where the width of
each bar is 1, return the area of the largest rectangle in the histogram.

Examples:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List

def largest_rectangle_in_histogram(heights: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        heights: Bar heights, each bar has width 1

    Returns:
        Area of the largest rectangle that fits in the histogram
    """
    pass


# Test Cases
def test_largest_rectangle_in_histogram():
    """Test cases for largest_rectangle_in_histogram"""

    test_cases = [
        {
            "name": 'Mixed heights',
            "input": ([2, 1, 5, 6, 2, 3],),
            "expected": 10
        },
        {
            "name": 'Two bars',
            "input": ([2, 4],),
            "expected": 4
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = largest_rectangle_in_histogram(*test['input'])
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
    test_largest_rectangle_in_histogram()
