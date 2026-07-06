"""
Problem: Best Time to Buy and Sell Stock (LeetCode #121)
Difficulty: Easy
Category: Sliding Window
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

Description:
You are given an array prices where prices[i] is the price of a given stock on the i^th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List

def best_time_to_buy_and_sell_stock(prices: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        prices: prices[i] is the stock price on day i

    Returns:
        Maximum achievable profit from one buy and one later sell, or 0
    """
    pass


# Test Cases
def test_best_time_to_buy_and_sell_stock():
    """Test cases for best_time_to_buy_and_sell_stock"""

    test_cases = [
        {
            "name": 'Profitable trade exists',
            "input": ([7, 1, 5, 3, 6, 4],),
            "expected": 5
        },
        {
            "name": 'Prices only decrease',
            "input": ([7, 6, 4, 3, 1],),
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
            result = best_time_to_buy_and_sell_stock(*test['input'])
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
    test_best_time_to_buy_and_sell_stock()
