"""
Problem: Longest Common Subsequence (LeetCode #1143)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/longest-common-subsequence

Description:
Given two strings text1 and text2, return the length of their longest common subsequence. If
there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining
characters.

 - For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Examples:
Input: text1 = "abcde", text2 = "ace" 
Output: 3 
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Time Complexity Target: O(n * m)
Space Complexity Target: O(n * m) (reducible to O(min(n, m)))
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    TODO: Implement your solution here

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of the longest common subsequence, or 0 if none
    """
    pass


# Test Cases
def test_longest_common_subsequence():
    """Test cases for longest_common_subsequence"""

    test_cases = [
        {
            "name": 'Partial overlap',
            "input": ('abcde', 'ace'),
            "expected": 3
        },
        {
            "name": 'Identical strings',
            "input": ('abc', 'abc'),
            "expected": 3
        },
        {
            "name": 'No common subsequence',
            "input": ('abc', 'def'),
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
            result = longest_common_subsequence(*test['input'])
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
    test_longest_common_subsequence()
