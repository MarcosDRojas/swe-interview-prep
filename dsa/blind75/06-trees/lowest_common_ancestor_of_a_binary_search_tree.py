"""
Problem: Lowest Common Ancestor of a Binary Search Tree (LeetCode #235)
Difficulty: Medium
Category: Trees
LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes
in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a
node to be a descendant of itself)."

Examples:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

Time Complexity Target: O(h)
Space Complexity Target: O(1) iterative / O(h) recursive
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

def find_node(root, val):
    """Test helper: locate the node with the given value."""
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def lowest_common_ancestor_of_a_binary_search_tree(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    TODO: Implement your solution here

    Args:
        root: Root of a binary search tree
        p: First node
        q: Second node

    Returns:
        The lowest common ancestor node of p and q
    """
    pass

# Test Cases
def test_lowest_common_ancestor_of_a_binary_search_tree():
    """Test cases for lowest_common_ancestor_of_a_binary_search_tree"""

    test_cases = [
        {"name": "LCA is an ancestor of both", "input": ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8), "expected": 6},
        {"name": "LCA is one of the nodes itself", "input": ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4), "expected": 2},
        {"name": "Two-node tree", "input": ([2, 1], 2, 1), "expected": 2},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root = {test['input'][0]}, p = {test['input'][1]}, q = {test['input'][2]}")
        print(f"  Expected: {test['expected']}")

        try:
            tree_vals, p_val, q_val = test['input']
            root = build_tree(tree_vals)
            p = find_node(root, p_val)
            q = find_node(root, q_val)
            result = lowest_common_ancestor_of_a_binary_search_tree(root, p, q)
            ok = result is not None and result.val == test['expected']

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
    test_lowest_common_ancestor_of_a_binary_search_tree()
