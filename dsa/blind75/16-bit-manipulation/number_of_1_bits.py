"""
Problem: Number of 1 Bits (LeetCode #191)
Difficulty: Easy
Category: Bit Manipulation
LeetCode: https://leetcode.com/problems/number-of-1-bits

Description:
Given a positive integer n, write a function that returns the number of set bits in its binary
representation (also known as the Hamming weight).

Examples:
Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
- 1 <= n <= 2^31 - 1
- Follow up: If this function is called many times, how would you optimize it?

Time Complexity Target: O(number of set bits)
Space Complexity Target: O(1)
"""

def number_of_1_bits(n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: Positive integer

    Returns:
        Number of set bits (1s) in the binary representation of n
    """
    pass


# Test Cases
def test_number_of_1_bits():
    """Test cases for number_of_1_bits"""

    test_cases = [
        {
            "name": 'Three set bits',
            "input": (11,),
            "expected": 3
        },
        {
            "name": 'Single set bit',
            "input": (128,),
            "expected": 1
        },
        {
            "name": 'Many set bits',
            "input": (2147483645,),
            "expected": 30
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = number_of_1_bits(*test['input'])
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
    test_number_of_1_bits()
