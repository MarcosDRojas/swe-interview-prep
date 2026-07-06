"""
Problem: Non-overlapping Intervals (LeetCode #435)
Difficulty: Medium
Category: Intervals
LeetCode: https://leetcode.com/problems/non-overlapping-intervals

Description:
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum
number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2,
3] are non-overlapping.

Examples:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

Time Complexity Target: O(n log n)
Space Complexity Target: O(1) extra
"""

from typing import List

def non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        intervals: Array of [start, end] intervals

    Returns:
        Minimum number of intervals to remove so the rest don't overlap
    """
    pass


# Test Cases
def test_non_overlapping_intervals():
    """Test cases for non_overlapping_intervals"""

    test_cases = [
        {
            "name": 'One removal needed',
            "input": ([[1, 2], [2, 3], [3, 4], [1, 3]],),
            "expected": 1
        },
        {
            "name": 'Two removals needed',
            "input": ([[1, 2], [1, 2], [1, 2]],),
            "expected": 2
        },
        {
            "name": 'Already non-overlapping',
            "input": ([[1, 2], [2, 3]],),
            "expected": 0
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = non_overlapping_intervals(*test['input'])
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
    test_non_overlapping_intervals()
