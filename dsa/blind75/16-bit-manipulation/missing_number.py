"""
Problem: Missing Number (LeetCode #268)
Difficulty: Easy
Category: Bit Manipulation
LeetCode: https://leetcode.com/problems/missing-number

Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in
the range that is missing from the array.

Examples:
Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def missing_number(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: n distinct numbers from the range [0, n], one missing

    Returns:
        The one number in [0, n] missing from nums
    """
    pass


# Test Cases
def test_missing_number():
    """Test cases for missing_number"""

    test_cases = [
        {
            "name": 'Missing from the middle',
            "input": ([3, 0, 1],),
            "expected": 2
        },
        {
            "name": 'Missing the largest value',
            "input": ([0, 1],),
            "expected": 2
        },
        {
            "name": 'Larger array',
            "input": ([9, 6, 4, 2, 3, 5, 7, 0, 1],),
            "expected": 8
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = missing_number(*test['input'])
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
    test_missing_number()
