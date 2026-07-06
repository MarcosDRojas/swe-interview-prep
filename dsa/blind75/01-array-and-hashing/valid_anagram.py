"""
Problem: Valid Anagram (LeetCode #242)
Difficulty: Easy
Category: Array & Hashing
LeetCode: https://leetcode.com/problems/valid-anagram

Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Examples:
Input: s = "anagram", t = "nagaram"

Output: true

Input: s = "rat", t = "car"

Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Time Complexity Target: O(n)
Space Complexity Target: O(1) (bounded alphabet)
"""

def valid_anagram(s: str, t: str) -> bool:
    """
    TODO: Implement your solution here

    Args:
        s: First string
        t: Second string

    Returns:
        True if t is an anagram of s, False otherwise
    """
    pass


# Test Cases
def test_valid_anagram():
    """Test cases for valid_anagram"""

    test_cases = [
        {
            "name": 'Valid anagram',
            "input": ('anagram', 'nagaram'),
            "expected": True
        },
        {
            "name": 'Not an anagram',
            "input": ('rat', 'car'),
            "expected": False
        },
        {
            "name": 'Different lengths',
            "input": ('ab', 'a'),
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
            result = valid_anagram(*test['input'])
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
    test_valid_anagram()
