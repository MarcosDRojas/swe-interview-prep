"""
Problem: Reorder List (LeetCode #143)
Difficulty: Medium
Category: Linked List
LeetCode: https://leetcode.com/problems/reorder-list

Description:
You are given the head of a singly linked-list. The list can be represented as:

L0 -> L1 -> ... -> Ln - 1 -> Ln

Reorder the list to be on the following form:

L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Examples:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000

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


def reorder_list(head: ListNode) -> None:
    """
    TODO: Implement your solution here (modify the list in place, return nothing)

    Args:
        head: Head of a singly linked list
    """
    pass


# Test Cases
def test_reorder_list():
    """Test cases for reorder_list"""

    test_cases = [
        {"name": "Even number of nodes", "input": [1, 2, 3, 4], "expected": [1, 4, 2, 3]},
        {"name": "Odd number of nodes", "input": [1, 2, 3, 4, 5], "expected": [1, 5, 2, 4, 3]},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: head = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            head = build_linked_list(test['input'])
            reorder_list(head)
            result = linked_list_to_list(head)
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
    test_reorder_list()
