"""
Problem: Word Search (LeetCode #79)
Difficulty: Medium
Category: Backtracking
LeetCode: https://leetcode.com/problems/word-search

Description:
Given an m x n grid of characters board and a string word, return true if word exists in the
grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Examples:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

Time Complexity Target: O(rows * cols * 4^L), L = word length
Space Complexity Target: O(L) recursion depth
"""

from typing import List

def word_search(board: List[List[str]], word: str) -> bool:
    """
    TODO: Implement your solution here

    Args:
        board: Grid of characters
        word: Word to search for

    Returns:
        True if word can be constructed from sequentially adjacent cells
    """
    pass


# Test Cases
def test_word_search():
    """Test cases for word_search"""

    test_cases = [
        {
            "name": 'Word found via a bending path',
            "input": ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'),
            "expected": True
        },
        {
            "name": 'Word found in a straight line',
            "input": ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'),
            "expected": True
        },
        {
            "name": 'Word not on the board',
            "input": ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'),
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
            result = word_search(*test['input'])
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
    test_word_search()
