"""
Problem: Longest Increasing Subsequence (LeetCode #300)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/longest-increasing-subsequence

Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Examples:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
- Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

Time Complexity Target: O(n^2) naive, O(n log n) with patience sorting / binary search
Space Complexity Target: O(n)
"""

from typing import List

def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of integers

    Returns:
        Length of the longest strictly increasing subsequence
    """
    pass


# Test Cases
def test_longest_increasing_subsequence():
    """Test cases for longest_increasing_subsequence"""

    test_cases = [
        {
            "name": 'Mixed values',
            "input": ([10, 9, 2, 5, 3, 7, 101, 18],),
            "expected": 4
        },
        {
            "name": 'Multiple valid subsequences of same length',
            "input": ([0, 1, 0, 3, 2, 3],),
            "expected": 4
        },
        {
            "name": 'All duplicates',
            "input": ([7, 7, 7, 7, 7, 7, 7],),
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
            result = longest_increasing_subsequence(*test['input'])
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
    test_longest_increasing_subsequence()
