"""
Problem: Contains Duplicate (LeetCode #217)
Difficulty: Easy
Category: Array & Hashing
LeetCode: https://leetcode.com/problems/contains-duplicate

Description:
Given an integer array nums, return true if any value appears at least twice in the array, and
return false if every element is distinct.

Examples:
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of integers

    Returns:
        True if any value appears at least twice, False if all distinct
    """
    pass


# Test Cases
def test_contains_duplicate():
    """Test cases for contains_duplicate"""

    test_cases = [
        {
            "name": 'Has duplicate',
            "input": ([1, 2, 3, 1],),
            "expected": True
        },
        {
            "name": 'All distinct',
            "input": ([1, 2, 3, 4],),
            "expected": False
        },
        {
            "name": 'Multiple duplicates',
            "input": ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],),
            "expected": True
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = contains_duplicate(*test['input'])
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
    test_contains_duplicate()
