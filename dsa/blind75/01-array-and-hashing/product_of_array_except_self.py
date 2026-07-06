"""
Problem: Product of Array Except Self (LeetCode #238)
Difficulty: Medium
Category: Array & Hashing
LeetCode: https://leetcode.com/problems/product-of-array-except-self

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Examples:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Time Complexity Target: O(n)
Space Complexity Target: O(1) extra (output array doesn't count)
"""

from typing import List

def product_of_array_except_self(nums: List[int]) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of integers

    Returns:
        Array where answer[i] is the product of all elements except nums[i]
    """
    pass


# Test Cases
def test_product_of_array_except_self():
    """Test cases for product_of_array_except_self"""

    test_cases = [
        {
            "name": 'Basic example',
            "input": ([1, 2, 3, 4],),
            "expected": [24, 12, 8, 6]
        },
        {
            "name": 'Contains a zero',
            "input": ([-1, 1, 0, -3, 3],),
            "expected": [0, 0, 9, 0, 0]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = product_of_array_except_self(*test['input'])
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
    test_product_of_array_except_self()
