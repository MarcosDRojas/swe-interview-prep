"""
Problem: Merge Intervals (LeetCode #56)
Difficulty: Medium
Category: Intervals
LeetCode: https://leetcode.com/problems/merge-intervals

Description:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the intervals in
the input.

Examples:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

Time Complexity Target: O(n log n)
Space Complexity Target: O(n)
"""

from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        intervals: Array of [start, end] intervals, not necessarily sorted

    Returns:
        Non-overlapping intervals covering all input intervals
    """
    pass


# Test Cases
def test_merge_intervals():
    """Test cases for merge_intervals"""

    test_cases = [
        {
            "name": 'One pair merges',
            "input": ([[1, 3], [2, 6], [8, 10], [15, 18]],),
            "expected": [[1, 6], [8, 10], [15, 18]]
        },
        {
            "name": 'Touching endpoints merge',
            "input": ([[1, 4], [4, 5]],),
            "expected": [[1, 5]]
        },
        {
            "name": 'Input not pre-sorted',
            "input": ([[4, 7], [1, 4]],),
            "expected": [[1, 7]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = merge_intervals(*test['input'])
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
    test_merge_intervals()
