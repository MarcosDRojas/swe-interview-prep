"""
Problem: Coin Change (LeetCode #322)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/coin-change

Description:
You are given an integer array coins representing coins of different denominations and an
integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Examples:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

Time Complexity Target: O(amount * len(coins))
Space Complexity Target: O(amount)
"""

from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        coins: Available coin denominations (unlimited supply)
        amount: Target amount to make

    Returns:
        Fewest coins needed to make amount, or -1 if impossible
    """
    pass


# Test Cases
def test_coin_change():
    """Test cases for coin_change"""

    test_cases = [
        {
            "name": 'Reachable with 3 coins',
            "input": ([1, 2, 5], 11),
            "expected": 3
        },
        {
            "name": 'Unreachable amount',
            "input": ([2], 3),
            "expected": -1
        },
        {
            "name": 'Zero amount',
            "input": ([1], 0),
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
            result = coin_change(*test['input'])
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
    test_coin_change()
