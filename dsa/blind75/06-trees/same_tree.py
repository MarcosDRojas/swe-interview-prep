"""
Problem: Same Tree (LeetCode #100)
Difficulty: Easy
Category: Trees
LeetCode: https://leetcode.com/problems/same-tree

Description:
Given the roots of two binary trees p and q, write a function to check if they are the same or
not.

Two binary trees are considered the same if they are structurally identical, and the nodes have
the same value.

Examples:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

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


def same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    TODO: Implement your solution here

    Args:
        p: Root of the first binary tree
        q: Root of the second binary tree

    Returns:
        True if the trees are structurally identical with the same values
    """
    pass

# Test Cases
def test_same_tree():
    """Test cases for same_tree"""

    test_cases = [
        {"name": "Identical trees", "input": ([1, 2, 3], [1, 2, 3]), "expected": True},
        {"name": "Different structure", "input": ([1, 2], [1, None, 2]), "expected": False},
        {"name": "Same values, different shape", "input": ([1, 2, 1], [1, 1, 2]), "expected": False},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: p = {test['input'][0]}, q = {test['input'][1]}")
        print(f"  Expected: {test['expected']}")

        try:
            p = build_tree(test['input'][0])
            q = build_tree(test['input'][1])
            result = same_tree(p, q)
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
    test_same_tree()
