"""
Problem: Jump Game (LeetCode #55)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/jump-game

Description:
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Examples:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def jump_game(nums: List[int]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        nums: nums[i] is the max jump length from index i

    Returns:
        True if the last index is reachable from the first
    """
    pass


# Test Cases
def test_jump_game():
    """Test cases for jump_game"""

    test_cases = [
        {
            "name": 'Reachable',
            "input": ([2, 3, 1, 1, 4],),
            "expected": True
        },
        {
            "name": 'Stuck at a zero',
            "input": ([3, 2, 1, 0, 4],),
            "expected": False
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = jump_game(*test['input'])
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
    test_jump_game()
