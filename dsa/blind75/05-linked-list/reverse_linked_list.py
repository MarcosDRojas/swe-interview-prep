"""
Problem: Reverse Linked List (LeetCode #206)
Difficulty: Easy
Category: Linked List
LeetCode: https://leetcode.com/problems/reverse-linked-list

Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Examples:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

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


def reverse_linked_list(head: ListNode) -> ListNode:
    """
    TODO: Implement your solution here

    Args:
        head: Head of a singly linked list

    Returns:
        The head of the reversed linked list
    """
    pass


# Test Cases
def test_reverse_linked_list():
    """Test cases for reverse_linked_list"""

    test_cases = [
        {"name": "Several nodes", "input": [1, 2, 3, 4, 5], "expected": [5, 4, 3, 2, 1]},
        {"name": "Two nodes", "input": [1, 2], "expected": [2, 1]},
        {"name": "Empty list", "input": [], "expected": []},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            head = build_linked_list(test['input'])
            result_head = reverse_linked_list(head)
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
    test_reverse_linked_list()
