"""
Problem: Maximum Product Subarray (LeetCode #152)
Difficulty: Medium
Category: Array & Hashing
LeetCode: https://leetcode.com/problems/maximum-product-subarray

Description:
Given an integer array nums, find a subarray that has the largest product, and return the
product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

Examples:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def maximum_product_subarray(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of integers

    Returns:
        Largest product of any contiguous subarray
    """
    pass


# Test Cases
def test_maximum_product_subarray():
    """Test cases for maximum_product_subarray"""

    test_cases = [
        {
            "name": 'Basic example',
            "input": ([2, 3, -2, 4],),
            "expected": 6
        },
        {
            "name": 'Zero splits the array',
            "input": ([-2, 0, -1],),
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
            result = maximum_product_subarray(*test['input'])
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
    test_maximum_product_subarray()
