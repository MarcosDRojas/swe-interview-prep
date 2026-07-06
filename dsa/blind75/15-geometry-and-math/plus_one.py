"""
Problem: Plus One (LeetCode #66)
Difficulty: Easy
Category: Geometry & Math
LeetCode: https://leetcode.com/problems/plus-one

Description:
You are given a large integer represented as an integer array digits, where each digits[i] is
the i^th digit of the integer. The digits are ordered from most significant to least significant
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Examples:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.

Time Complexity Target: O(n)
Space Complexity Target: O(1) extra (O(n) if a new digit must be added)
"""

from typing import List

def plus_one(digits: List[int]) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        digits: Digits of a large integer, most significant first

    Returns:
        Digits of the integer after adding one
    """
    pass


# Test Cases
def test_plus_one():
    """Test cases for plus_one"""

    test_cases = [
        {
            "name": 'No carry needed',
            "input": ([1, 2, 3],),
            "expected": [1, 2, 4]
        },
        {
            "name": 'Carry within the number',
            "input": ([4, 3, 2, 1],),
            "expected": [4, 3, 2, 2]
        },
        {
            "name": 'All nines grows the array',
            "input": ([9],),
            "expected": [1, 0]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = plus_one(*test['input'])
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
    test_plus_one()
