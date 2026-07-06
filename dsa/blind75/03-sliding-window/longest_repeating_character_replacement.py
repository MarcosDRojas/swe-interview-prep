"""
Problem: Longest Repeating Character Replacement (LeetCode #424)
Difficulty: Medium
Category: Sliding Window
LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement

Description:
You are given a string s and an integer k. You can choose any character of the string and change
it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.

Examples:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length

Time Complexity Target: O(n)
Space Complexity Target: O(1) (bounded alphabet)
"""

def longest_repeating_character_replacement(s: str, k: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        s: Input string of uppercase letters
        k: Max number of characters that may be replaced

    Returns:
        Length of the longest substring of a single repeated letter achievable
    """
    pass


# Test Cases
def test_longest_repeating_character_replacement():
    """Test cases for longest_repeating_character_replacement"""

    test_cases = [
        {
            "name": 'Replace two to match',
            "input": ('ABAB', 2),
            "expected": 4
        },
        {
            "name": 'Replace one in the middle',
            "input": ('AABABBA', 1),
            "expected": 4
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = longest_repeating_character_replacement(*test['input'])
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
    test_longest_repeating_character_replacement()
