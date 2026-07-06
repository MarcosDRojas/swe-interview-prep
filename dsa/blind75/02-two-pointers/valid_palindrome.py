"""
Problem: Valid Palindrome (LeetCode #125)
Difficulty: Easy
Category: Two Pointers
LeetCode: https://leetcode.com/problems/valid-palindrome

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Examples:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

def valid_palindrome(s: str) -> bool:
    """
    TODO: Implement your solution here

    Args:
        s: Input string

    Returns:
        True if s is a palindrome ignoring case and non-alphanumeric characters
    """
    pass


# Test Cases
def test_valid_palindrome():
    """Test cases for valid_palindrome"""

    test_cases = [
        {
            "name": 'Palindrome with punctuation/case',
            "input": ('A man, a plan, a canal: Panama',),
            "expected": True
        },
        {
            "name": 'Not a palindrome',
            "input": ('race a car',),
            "expected": False
        },
        {
            "name": 'Empty after stripping',
            "input": (' ',),
            "expected": True
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = valid_palindrome(*test['input'])
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
    test_valid_palindrome()
