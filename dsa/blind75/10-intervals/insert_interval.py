"""
Problem: Insert Interval (LeetCode #57)
Difficulty: Medium
Category: Intervals
LeetCode: https://leetcode.com/problems/insert-interval

Description:
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti,
endi] represent the start and the end of the i^th interval and intervals is sorted in ascending
order by starti. You are also given an interval newInterval = [start, end] that represents the
start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by
starti and intervals still does not have any overlapping intervals (merge overlapping intervals
if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Examples:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5

Time Complexity Target: O(n)
Space Complexity Target: O(n) for the output
"""

from typing import List

def insert_interval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        intervals: Non-overlapping intervals sorted by start
        newInterval: Interval to insert

    Returns:
        Intervals after inserting and merging newInterval, still sorted and non-overlapping
    """
    pass


# Test Cases
def test_insert_interval():
    """Test cases for insert_interval"""

    test_cases = [
        {
            "name": 'Insert without overlap elsewhere',
            "input": ([[1, 3], [6, 9]], [2, 5]),
            "expected": [[1, 5], [6, 9]]
        },
        {
            "name": 'Insert overlapping several intervals',
            "input": ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            "expected": [[1, 2], [3, 10], [12, 16]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = insert_interval(*test['input'])
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
    test_insert_interval()
