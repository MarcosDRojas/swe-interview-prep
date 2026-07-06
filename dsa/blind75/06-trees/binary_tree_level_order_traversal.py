"""
Problem: Binary Tree Level Order Traversal (LeetCode #102)
Difficulty: Medium
Category: Trees
LeetCode: https://leetcode.com/problems/binary-tree-level-order-traversal

Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e.,
from left to right, level by level).

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

Time Complexity Target: O(n)
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


def binary_tree_level_order_traversal(root: TreeNode) -> "List[List[int]]":
    """
    TODO: Implement your solution here

    Args:
        root: Root of a binary tree

    Returns:
        A list of levels, each a list of node values left to right
    """
    pass

# Test Cases
def test_binary_tree_level_order_traversal():
    """Test cases for binary_tree_level_order_traversal"""

    test_cases = [
        {"name": "Three levels", "input": [3, 9, 20, None, None, 15, 7], "expected": [[3], [9, 20], [15, 7]]},
        {"name": "Single node", "input": [1], "expected": [[1]]},
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
            result = binary_tree_level_order_traversal(root)
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
    test_binary_tree_level_order_traversal()
