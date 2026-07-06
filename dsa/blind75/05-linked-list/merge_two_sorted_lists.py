"""
Problem: Merge Two Sorted Lists (LeetCode #21)
Difficulty: Easy
Category: Linked List
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists

Description:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes
of the first two lists.

Return the head of the merged linked list.

Examples:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

Time Complexity Target: O(n + m)
Space Complexity Target: O(1) extra (reuses input nodes)
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


def merge_two_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    TODO: Implement your solution here

    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list

    Returns:
        Head of the merged sorted linked list
    """
    pass


# Test Cases
def test_merge_two_sorted_lists():
    """Test cases for merge_two_sorted_lists"""

    test_cases = [
        {"name": "Two non-empty lists", "input": ([1, 2, 4], [1, 3, 4]), "expected": [1, 1, 2, 3, 4, 4]},
        {"name": "Both empty", "input": ([], []), "expected": []},
        {"name": "One empty", "input": ([], [0]), "expected": [0]},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        l1, l2 = test['input']
        print(f"\n{test['name']}")
        print(f"  Input: list1 = {l1}, list2 = {l2}")
        print(f"  Expected: {test['expected']}")

        try:
            head1 = build_linked_list(l1)
            head2 = build_linked_list(l2)
            result_head = merge_two_sorted_lists(head1, head2)
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
    test_merge_two_sorted_lists()
