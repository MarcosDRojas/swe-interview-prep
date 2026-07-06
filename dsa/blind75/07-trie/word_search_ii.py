"""
Problem: Word Search II (LeetCode #212)
Difficulty: Hard
Category: Trie
LeetCode: https://leetcode.com/problems/word-search-ii

Description:
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once
in a word.

Examples:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.

Time Complexity Target: O(rows * cols * 4^L) worst case, pruned heavily by the trie
Space Complexity Target: O(total characters in the word list)
"""

from typing import List

def word_search_ii(board: List[List[str]], words: List[str]) -> List[str]:
    """
    TODO: Implement your solution here

    Args:
        board: Grid of lowercase letters
        words: Candidate words to find on the board

    Returns:
        All words from the word list that can be built on the board (order doesn't matter)
    """
    pass


# Test Cases
def test_word_search_ii():
    """Test cases for word_search_ii"""

    test_cases = [
        {
            "name": 'Two words found',
            "input": ([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']),
            "expected": ['eat', 'oath']
        },
        {
            "name": 'No words found',
            "input": ([['a', 'b'], ['c', 'd']], ['abcb']),
            "expected": []
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = word_search_ii(*test['input'])
            ok = result is not None and sorted(result) == sorted(test['expected'])

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
    test_word_search_ii()
