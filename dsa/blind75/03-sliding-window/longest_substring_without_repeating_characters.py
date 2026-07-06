"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Difficulty: Medium
Category: Sliding Window
LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters

Description:
Given a string s, find the length of the longest substring without duplicate characters.

Examples:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Time Complexity Target: O(n)
Space Complexity Target: O(min(n, alphabet size))
"""

def longest_substring_without_repeating_characters(s: str) -> int:
    """
    TODO: Implement your solution here

    Args:
        s: Input string

    Returns:
        Length of the longest substring without duplicate characters
    """
    pass


# Test Cases
def test_longest_substring_without_repeating_characters():
    """Test cases for longest_substring_without_repeating_characters"""

    test_cases = [
        {
            "name": 'Repeats after 3 unique chars',
            "input": ('abcabcbb',),
            "expected": 3
        },
        {
            "name": 'All same character',
            "input": ('bbbbb',),
            "expected": 1
        },
        {
            "name": 'Longest substring in the middle',
            "input": ('pwwkew',),
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = longest_substring_without_repeating_characters(*test['input'])
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
    test_longest_substring_without_repeating_characters()
