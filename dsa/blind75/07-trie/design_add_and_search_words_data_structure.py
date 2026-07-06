"""
Problem: Design Add and Search Words Data Structure (LeetCode #211)
Difficulty: Medium
Category: Trie
LeetCode: https://leetcode.com/problems/design-add-and-search-words-data-structure

Description:
Design a data structure that supports adding new words and finding if a string matches any
previously added string.

Implement the WordDictionary class:

 - WordDictionary() Initializes the object.

 - void addWord(word) Adds word to the data structure, it can be matched later.

 - bool search(word) Returns true if there is any string in the data structure that matches word
or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Examples:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.

Time Complexity Target: O(L) for addWord; O(L) best case / O(26^L) worst case for search with wildcards
Space Complexity Target: O(total characters across added words)
"""

class WordDictionary:
    def __init__(self):
        """
        TODO: Implement your solution here
        """
        pass

    def addWord(self, word: str) -> None:
        """
        TODO: Implement your solution here
        """
        pass

    def search(self, word: str) -> bool:
        """
        TODO: Implement your solution here (word may contain '.' wildcards)
        """
        pass


# Test Cases
def test_word_dictionary():
    """Test cases for WordDictionary, driven by (method, args, expected) operation sequences."""

    scenarios = [
        {
            "name": "addWord then search with wildcards",
            "ops": ["addWord", "addWord", "addWord", "search", "search", "search", "search"],
            "args": [["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            "expected": [None, None, None, False, True, True, True],
        },
    ]

    passed = 0
    failed = 0
    total = 0

    for scenario in scenarios:
        print(f"\n{scenario['name']}")
        wd = WordDictionary()
        for op, args, expected in zip(scenario["ops"], scenario["args"], scenario["expected"]):
            total += 1
            try:
                result = getattr(wd, op)(*args)
                ok = (expected is None) or (result == expected)
                print(f"  wd.{op}({', '.join(map(repr, args))}) -> {result}  (expected {expected})")
                if ok:
                    passed += 1
                else:
                    print(f"  [FAIL]: Got {result}, expected {expected}")
                    failed += 1
            except Exception as e:
                print(f"  [FAIL]: {type(e).__name__}: {e}")
                failed += 1

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {total} calls")

    if failed == 0:
        print("All test cases passed!")
    else:
        print("Some test cases failed. Please review the implementation.")


if __name__ == "__main__":
    test_word_dictionary()
