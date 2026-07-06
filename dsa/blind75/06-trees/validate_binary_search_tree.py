"""
Problem: Validate Binary Search Tree (LeetCode #98)
Difficulty: Medium
Category: Trees
LeetCode: https://leetcode.com/problems/validate-binary-search-tree

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

 - The left subtree of a node contains only nodes with keys strictly less than the node's key.

 - The right subtree of a node contains only nodes with keys strictly greater than the node's
key.

 - Both the left and right subtrees must also be binary search trees.

Examples:
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

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


def validate_binary_search_tree(root: TreeNode) -> bool:
    """
    TODO: Implement your solution here

    Args:
        root: Root of a binary tree

    Returns:
        True if the tree is a valid binary search tree
    """
    pass

# Test Cases
def test_validate_binary_search_tree():
    """Test cases for validate_binary_search_tree"""

    test_cases = [
        {"name": "Valid small BST", "input": [2, 1, 3], "expected": True},
        {"name": "Right child violates BST property", "input": [5, 1, 4, None, None, 3, 6], "expected": False},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            root = build_tree(test['input'])
            result = validate_binary_search_tree(root)
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
    test_validate_binary_search_tree()
