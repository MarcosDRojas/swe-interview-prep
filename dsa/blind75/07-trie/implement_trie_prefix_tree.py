"""
Problem: Implement Trie (Prefix Tree) (LeetCode #208)
Difficulty: Medium
Category: Trie
LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree

Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
and retrieve keys in a dataset of strings. There are various applications of this data
structure, such as autocomplete and spellchecker.

Implement the Trie class:

 - Trie() Initializes the trie object.

 - void insert(String word) Inserts the string word into the trie.

 - boolean search(String word) Returns true if the string word is in the trie (i.e., was
inserted before), and false otherwise.

 - boolean startsWith(String prefix) Returns true if there is a previously inserted string word
that has the prefix prefix, and false otherwise.

Examples:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple"); // return True
trie.search("app"); // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app"); // return True

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Time Complexity Target: O(L) per insert/search/startsWith, L = key length
Space Complexity Target: O(total characters across inserted words)
"""

class Trie:
    def __init__(self):
        """
        TODO: Implement your solution here
        """
        pass

    def insert(self, word: str) -> None:
        """
        TODO: Implement your solution here
        """
        pass

    def search(self, word: str) -> bool:
        """
        TODO: Implement your solution here
        """
        pass

    def startsWith(self, prefix: str) -> bool:
        """
        TODO: Implement your solution here
        """
        pass


# Test Cases
def test_trie():
    """Test cases for Trie, driven by (method, args, expected) operation sequences —
    the same style LeetCode itself uses for design problems."""

    scenarios = [
        {
            "name": "Insert/search/startsWith sequence",
            "ops": ["insert", "search", "search", "startsWith", "insert", "search"],
            "args": [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            "expected": [None, True, False, True, None, True],
        },
    ]

    passed = 0
    failed = 0
    total = 0

    for scenario in scenarios:
        print(f"\n{scenario['name']}")
        trie = Trie()
        for op, args, expected in zip(scenario["ops"], scenario["args"], scenario["expected"]):
            total += 1
            try:
                result = getattr(trie, op)(*args)
                ok = (expected is None) or (result == expected)
                print(f"  trie.{op}({', '.join(map(repr, args))}) -> {result}  (expected {expected})")
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
    test_trie()
