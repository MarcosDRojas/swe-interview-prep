"""
Problem: Reverse Bits (LeetCode #190)
Difficulty: Easy
Category: Bit Manipulation
LeetCode: https://leetcode.com/problems/reverse-bits

Description:
Reverse bits of a given 32 bits signed integer.

Examples:
Input: n = 43261596

Output: 964176192

Explanation:

 
 
 Integer
 Binary
 
 
 43261596
 00000010100101000001111010011100
 
 
 964176192
 00111001011110000010100101000000

Input: n = 2147483644

Output: 1073741822

Explanation:

 
 
 Integer
 Binary
 
 
 2147483644
 01111111111111111111111111111100
 
 
 1073741822
 00111111111111111111111111111110

Constraints:
- 0 <= n <= 2^31 - 2
- n is even.

Time Complexity Target: O(32) = O(1)
Space Complexity Target: O(1)
"""

def reverse_bits(n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: 32-bit unsigned integer

    Returns:
        The bits of n reversed, as a 32-bit unsigned integer
    """
    pass


# Test Cases
def test_reverse_bits():
    """Test cases for reverse_bits"""

    test_cases = [
        {
            "name": 'Basic example',
            "input": (43261596,),
            "expected": 964176192
        },
        {
            "name": 'High bits set',
            "input": (2147483644,),
            "expected": 1073741822
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = reverse_bits(*test['input'])
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
    test_reverse_bits()
