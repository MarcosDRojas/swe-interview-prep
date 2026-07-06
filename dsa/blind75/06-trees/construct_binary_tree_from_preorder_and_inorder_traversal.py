"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal (LeetCode #105)
Difficulty: Medium
Category: Trees
LeetCode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a
binary tree and inorder is the inorder traversal of the same tree, construct and return the
binary tree.

Examples:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

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


def construct_binary_tree_from_preorder_and_inorder_traversal(preorder: "List[int]", inorder: "List[int]") -> TreeNode:
    """
    TODO: Implement your solution here

    Args:
        preorder: Preorder traversal of the tree
        inorder: Inorder traversal of the same tree

    Returns:
        The root of the reconstructed tree
    """
    pass

# Test Cases
def test_construct_binary_tree_from_preorder_and_inorder_traversal():
    """Test cases for construct_binary_tree_from_preorder_and_inorder_traversal"""

    test_cases = [
        {"name": "Several nodes", "input": ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), "expected": [3, 9, 20, None, None, 15, 7]},
        {"name": "Single node", "input": ([-1], [-1]), "expected": [-1]},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: preorder = {test['input'][0]}, inorder = {test['input'][1]}")
        print(f"  Expected: {test['expected']}")

        try:
            preorder, inorder = test['input']
            result = tree_to_list(construct_binary_tree_from_preorder_and_inorder_traversal(preorder, inorder))
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
    test_construct_binary_tree_from_preorder_and_inorder_traversal()
