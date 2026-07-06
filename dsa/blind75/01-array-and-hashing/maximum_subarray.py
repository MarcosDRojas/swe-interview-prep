"""
Problem: Maximum Subarray (LeetCode #53)
Difficulty: Medium
Category: Array & Hashing
LeetCode: https://leetcode.com/problems/maximum-subarray

Description:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Examples:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def maximum_subarray(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of integers

    Returns:
        Largest sum of any contiguous subarray
    """
    pass


# Test Cases
def test_maximum_subarray():
    """Test cases for maximum_subarray"""

    test_cases = [
        {
            "name": 'Mixed positive/negative',
            "input": ([-2, 1, -3, 4, -1, 2, 1, -5, 4],),
            "expected": 6
        },
        {
            "name": 'Single element',
            "input": ([1],),
            "expected": 1
        },
        {
            "name": 'All positive',
            "input": ([5, 4, -1, 7, 8],),
            "expected": 23
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = maximum_subarray(*test['input'])
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
    test_maximum_subarray()
