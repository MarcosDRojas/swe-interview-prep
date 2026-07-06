"""
Problem: House Robber II (LeetCode #213)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/house-robber-ii

Description:
You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed. All houses at this place are arranged in a circle. That means the first
house is the neighbor of the last one. Meanwhile, adjacent houses have a security system
connected, and it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

Examples:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [1,2,3]
Output: 3

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def house_robber_ii(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Money stashed in each house, arranged in a circle

    Returns:
        Maximum money robbable without robbing two adjacent houses (first and last are adjacent)
    """
    pass


# Test Cases
def test_house_robber_ii():
    """Test cases for house_robber_ii"""

    test_cases = [
        {
            "name": 'Circular adjacency blocks both ends',
            "input": ([2, 3, 2],),
            "expected": 3
        },
        {
            "name": 'Skip the middle house',
            "input": ([1, 2, 3, 1],),
            "expected": 4
        },
        {
            "name": 'Three houses in a circle',
            "input": ([1, 2, 3],),
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = house_robber_ii(*test['input'])
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
    test_house_robber_ii()
