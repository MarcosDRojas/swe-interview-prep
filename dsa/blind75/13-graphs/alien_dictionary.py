"""
Problem: Alien Dictionary (LeetCode #269)
Difficulty: Hard (Premium)
Category: Graphs
LeetCode: https://leetcode.com/problems/alien-dictionary

Description:
There is a new alien language that uses the English alphabet. However, the order among the
letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in
words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically
increasing order by the new language's rules. If there is no solution, return "". If there are
multiple solutions, return any of them.

(This problem is LeetCode Premium-only, so the official statement page isn't public — this
description is written from the well-known problem, not fetched from LeetCode.)

Examples:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Input: words = ["z","x"]
Output: "zx"

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.

Time Complexity Target: O(total characters in words)
Space Complexity Target: O(alphabet size)
"""

from typing import List

def alien_dictionary(words: List[str]) -> str:
    """
    TODO: Implement your solution here

    Args:
        words: Words sorted lexicographically by the alien language's rules

    Returns:
        The alphabet's letter order (any valid ordering), or '' if the input is contradictory
    """
    pass


# Test Cases
def test_alien_dictionary():
    """Test cases for alien_dictionary"""

    test_cases = [
        {
            "name": 'Derivable order',
            "input": (['wrt', 'wrf', 'er', 'ett', 'rftt'],),
            "expected": 'wertf'
        },
        {
            "name": 'Two letters',
            "input": (['z', 'x'],),
            "expected": 'zx'
        },
        {
            "name": 'Contradictory order',
            "input": (['z', 'x', 'z'],),
            "expected": ''
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = alien_dictionary(*test['input'])
            def _valid_alien_order(order, words):
                if order is None:
                    return False
                letters = set(''.join(words))
                if order == '':
                    return False
                if set(order) != letters or len(order) != len(letters):
                    return False
                pos = {c: i for i, c in enumerate(order)}
                for a, b in zip(words, words[1:]):
                    min_len = min(len(a), len(b))
                    j = 0
                    while j < min_len and a[j] == b[j]:
                        j += 1
                    if j == min_len:
                        if len(a) > len(b):
                            return False
                    elif pos[a[j]] > pos[b[j]]:
                        return False
                return True
            words_in = test['input'][0]
            if test['expected'] == '':
                ok = result == ''
            else:
                ok = _valid_alien_order(result, words_in)

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
    test_alien_dictionary()
