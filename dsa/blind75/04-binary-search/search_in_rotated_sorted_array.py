"""
Problem: Search in Rotated Sorted Array (LeetCode #33)
Difficulty: Medium
Category: Binary Search
LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array

Description:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1
<= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left
rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of
target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4

Time Complexity Target: O(log n)
Space Complexity Target: O(1)
"""

from typing import List

def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Rotated ascending array of unique elements
        target: Value to search for

    Returns:
        Index of target in nums, or -1 if not present
    """
    pass


# Test Cases
def test_search_in_rotated_sorted_array():
    """Test cases for search_in_rotated_sorted_array"""

    test_cases = [
        {
            "name": 'Target present in rotated part',
            "input": ([4, 5, 6, 7, 0, 1, 2], 0),
            "expected": 4
        },
        {
            "name": 'Target absent',
            "input": ([4, 5, 6, 7, 0, 1, 2], 3),
            "expected": -1
        },
        {
            "name": 'Single element, not found',
            "input": ([1], 0),
            "expected": -1
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = search_in_rotated_sorted_array(*test['input'])
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
    test_search_in_rotated_sorted_array()
