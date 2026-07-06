"""
Problem: Decode Ways (LeetCode #91)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/decode-ways

Description:
You have intercepted a secret message encoded as a string of numbers. The message is decoded via
the following mapping:

"1" -> 'A'
"2" -> 'B'
...
"25" -> 'Y'
"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can
decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

 - "AAJF" with the grouping (1, 1, 10, 6)

 - "KJF" with the grouping (11, 10, 6)

 - The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire
string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

Examples:
Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).

Time Complexity Target: O(n)
Space Complexity Target: O(1) (rolling) or O(n)
"""

def decode_ways(s: str) -> int:
    """
    TODO: Implement your solution here

    Args:
        s: String of digits, possibly with leading zeros

    Returns:
        Number of ways s can be decoded to letters, or 0 if none
    """
    pass


# Test Cases
def test_decode_ways():
    """Test cases for decode_ways"""

    test_cases = [
        {
            "name": 'Two valid groupings',
            "input": ('12',),
            "expected": 2
        },
        {
            "name": 'Three valid groupings',
            "input": ('226',),
            "expected": 3
        },
        {
            "name": 'Leading zero makes it invalid',
            "input": ('06',),
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
            result = decode_ways(*test['input'])
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
    test_decode_ways()
