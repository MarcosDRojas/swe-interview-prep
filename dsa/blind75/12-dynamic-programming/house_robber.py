"""
Problem: House Robber (LeetCode #198)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/house-robber

Description:
You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

Examples:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def house_robber(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Money stashed in each house, in a row

    Returns:
        Maximum money robbable without robbing two adjacent houses
    """
    pass


# Test Cases
def test_house_robber():
    """Test cases for house_robber"""

    test_cases = [
        {
            "name": 'Skip the middle house',
            "input": ([1, 2, 3, 1],),
            "expected": 4
        },
        {
            "name": 'Rob every other house',
            "input": ([2, 7, 9, 3, 1],),
            "expected": 12
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = house_robber(*test['input'])
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
    test_house_robber()
