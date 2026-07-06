"""
Problem: Word Break (LeetCode #139)
Difficulty: Medium
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/word-break

Description:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Examples:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.

Time Complexity Target: O(n^2) with a set for O(1) dictionary lookups
Space Complexity Target: O(n)
"""

from typing import List

def word_break(s: str, wordDict: List[str]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        s: String to segment
        wordDict: Dictionary of reusable words

    Returns:
        True if s can be segmented into a sequence of dictionary words
    """
    pass


# Test Cases
def test_word_break():
    """Test cases for word_break"""

    test_cases = [
        {
            "name": 'Segments into two words',
            "input": ('leetcode', ['leet', 'code']),
            "expected": True
        },
        {
            "name": 'Reuses a word twice',
            "input": ('applepenapple', ['apple', 'pen']),
            "expected": True
        },
        {
            "name": 'Cannot be segmented',
            "input": ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
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
            result = word_break(*test['input'])
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
    test_word_break()
