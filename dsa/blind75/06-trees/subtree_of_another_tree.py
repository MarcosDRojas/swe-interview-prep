"""
Problem: Subtree of Another Tree (LeetCode #572)
Difficulty: Easy
Category: Trees
LeetCode: https://leetcode.com/problems/subtree-of-another-tree

Description:
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's
descendants. The tree tree could also be considered as a subtree of itself.

Examples:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4

Time Complexity Target: O(n * m)
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


def subtree_of_another_tree(root: TreeNode, subRoot: TreeNode) -> bool:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the main binary tree
        subRoot: Root of the candidate subtree

    Returns:
        True if subRoot is a subtree of root
    """
    pass

# Test Cases
def test_subtree_of_another_tree():
    """Test cases for subtree_of_another_tree"""

    test_cases = [
        {"name": "Is a subtree", "input": ([3, 4, 5, 1, 2], [4, 1, 2]), "expected": True},
        {"name": "Extra node breaks the match", "input": ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]), "expected": False},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root = {test['input'][0]}, subRoot = {test['input'][1]}")
        print(f"  Expected: {test['expected']}")

        try:
            root = build_tree(test['input'][0])
            subRoot = build_tree(test['input'][1])
            result = subtree_of_another_tree(root, subRoot)
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
    test_subtree_of_another_tree()
