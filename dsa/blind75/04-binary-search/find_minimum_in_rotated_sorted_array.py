"""
Problem: Find Minimum in Rotated Sorted Array (LeetCode #153)
Difficulty: Medium
Category: Binary Search
LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For
example, the array nums = [0,1,2,4,5,6,7] might become:

 - [4,5,6,7,0,1,2] if it was rotated 4 times.

 - [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this
array.

You must write an algorithm that runs in O(log n) time.

Examples:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.

Time Complexity Target: O(log n)
Space Complexity Target: O(1)
"""

from typing import List

def find_minimum_in_rotated_sorted_array(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Rotated ascending array of unique elements

    Returns:
        The minimum element in the array
    """
    pass


# Test Cases
def test_find_minimum_in_rotated_sorted_array():
    """Test cases for find_minimum_in_rotated_sorted_array"""

    test_cases = [
        {
            "name": 'Rotated 3 times',
            "input": ([3, 4, 5, 1, 2],),
            "expected": 1
        },
        {
            "name": 'Rotated 4 times',
            "input": ([4, 5, 6, 7, 0, 1, 2],),
            "expected": 0
        },
        {
            "name": 'Rotated full length (no visible rotation)',
            "input": ([11, 13, 15, 17],),
            "expected": 11
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = find_minimum_in_rotated_sorted_array(*test['input'])
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
    test_find_minimum_in_rotated_sorted_array()
