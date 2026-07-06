"""
Problem: Kth Smallest Element in a BST (LeetCode #230)
Difficulty: Medium
Category: Trees
LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-bst

Description:
Given the root of a binary search tree, and an integer k, return the k^th smallest value
(1-indexed) of all the values of the nodes in the tree.

Examples:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Time Complexity Target: O(h + k)
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


def kth_smallest_element_in_a_bst(root: TreeNode, k: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        root: Root of a binary search tree
        k: 1-indexed position to find (in sorted order)

    Returns:
        The k-th smallest value in the tree
    """
    pass

# Test Cases
def test_kth_smallest_element_in_a_bst():
    """Test cases for kth_smallest_element_in_a_bst"""

    test_cases = [
        {"name": "k = 1", "input": ([3, 1, 4, None, 2], 1), "expected": 1},
        {"name": "k = 3", "input": ([5, 3, 6, 2, 4, None, None, 1], 3), "expected": 3},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root = {test['input'][0]}, k = {test['input'][1]}")
        print(f"  Expected: {test['expected']}")

        try:
            tree_vals, k = test['input']
            root = build_tree(tree_vals)
            result = kth_smallest_element_in_a_bst(root, k)
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
    test_kth_smallest_element_in_a_bst()
