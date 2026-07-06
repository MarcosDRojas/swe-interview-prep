"""
Problem: Invert Binary Tree (LeetCode #226)
Difficulty: Easy
Category: Trees
LeetCode: https://leetcode.com/problems/invert-binary-tree

Description:
Given the root of a binary tree, invert the tree, and return its root.

Examples:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Time Complexity Target: O(n)
Space Complexity Target: O(h) recursion stack
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


def invert_binary_tree(root: TreeNode) -> TreeNode:
    """
    TODO: Implement your solution here

    Args:
        root: Root of a binary tree

    Returns:
        The root of the inverted tree
    """
    pass

# Test Cases
def test_invert_binary_tree():
    """Test cases for invert_binary_tree"""

    test_cases = [
        {"name": "Several levels", "input": [4, 2, 7, 1, 3, 6, 9], "expected": [4, 7, 2, 9, 6, 3, 1]},
        {"name": "Three nodes", "input": [2, 1, 3], "expected": [2, 3, 1]},
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
            result = tree_to_list(invert_binary_tree(root))
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
    test_invert_binary_tree()
