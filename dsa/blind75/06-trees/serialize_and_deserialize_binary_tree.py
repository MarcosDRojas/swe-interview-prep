"""
Problem: Serialize and Deserialize Binary Tree (LeetCode #297)
Difficulty: Hard
Category: Trees
LeetCode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree

Description:
Serialization is the process of converting a data structure or object into a sequence of bits so
that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how
your serialization/deserialization algorithm should work. You just need to ensure that a binary
tree can be serialized to a string and this string can be deserialized to the original tree
structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You
do not necessarily need to follow this format, so please be creative and come up with different
approaches yourself.

Examples:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

Time Complexity Target: O(n) for both serialize and deserialize
Space Complexity Target: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a binary tree from a LeetCode-style level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def tree_to_list(root):
    """Convert a binary tree back to a LeetCode-style level-order list for comparison."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """
        TODO: Implement your solution here — encode the tree as a single string.
        """
        pass

    def deserialize(self, data: str) -> TreeNode:
        """
        TODO: Implement your solution here — decode the string back into a tree.
        """
        pass

# Test Cases
def test_serialize_and_deserialize_binary_tree():
    """Test cases for serialize_and_deserialize_binary_tree"""

    test_cases = [
        {"name": "Mixed tree", "input": [1, 2, 3, None, None, 4, 5], "expected": [1, 2, 3, None, None, 4, 5]},
        {"name": "Empty tree", "input": [], "expected": []},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            root = build_tree(test['input'])
            codec = Codec()
            result = tree_to_list(codec.deserialize(codec.serialize(root)))
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
    test_serialize_and_deserialize_binary_tree()
