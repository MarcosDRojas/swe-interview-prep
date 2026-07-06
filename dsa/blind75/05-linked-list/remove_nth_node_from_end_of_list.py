"""
Problem: Remove Nth Node From End of List (LeetCode #19)
Difficulty: Medium
Category: Linked List
LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list

Description:
Given the head of a linked list, remove the n^th node from the end of the list and return its
head.

Examples:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    """Build a linked list from a Python list, return the head (or None)."""
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def linked_list_to_list(head):
    """Convert a linked list back to a Python list for easy comparison."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def remove_nth_node_from_end_of_list(head: ListNode, n: int) -> ListNode:
    """
    TODO: Implement your solution here

    Args:
        head: Head of a singly linked list
        n: Position from the end of the list to remove (1 = last node)

    Returns:
        Head of the list after removing the n-th node from the end
    """
    pass


# Test Cases
def test_remove_nth_node_from_end_of_list():
    """Test cases for remove_nth_node_from_end_of_list"""

    test_cases = [
        {"name": "Remove from middle", "input": ([1, 2, 3, 4, 5], 2), "expected": [1, 2, 3, 5]},
        {"name": "Remove the only node", "input": ([1], 1), "expected": []},
        {"name": "Remove the head", "input": ([1, 2], 1), "expected": [1]},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        values, n = test['input']
        print(f"\n{test['name']}")
        print(f"  Input: head = {values}, n = {n}")
        print(f"  Expected: {test['expected']}")

        try:
            head = build_linked_list(values)
            result_head = remove_nth_node_from_end_of_list(head, n)
            result = linked_list_to_list(result_head)
            ok = result == test['expected']

            if ok:
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
    test_remove_nth_node_from_end_of_list()
