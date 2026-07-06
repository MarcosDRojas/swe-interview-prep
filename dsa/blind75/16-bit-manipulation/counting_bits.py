"""
Problem: Counting Bits (LeetCode #338)
Difficulty: Easy
Category: Bit Manipulation
LeetCode: https://leetcode.com/problems/counting-bits

Description:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Examples:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
- 0 <= n <= 10^5

Time Complexity Target: O(n)
Space Complexity Target: O(n) for the output
"""

from typing import List

def counting_bits(n: int) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        n: Upper bound (inclusive)

    Returns:
        ans[i] = number of set bits in i, for every i from 0 to n
    """
    pass


# Test Cases
def test_counting_bits():
    """Test cases for counting_bits"""

    test_cases = [
        {
            "name": 'n = 2',
            "input": (2,),
            "expected": [0, 1, 1]
        },
        {
            "name": 'n = 5',
            "input": (5,),
            "expected": [0, 1, 1, 2, 1, 2]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = counting_bits(*test['input'])
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
    test_counting_bits()
