"""
Problem: Linked List Cycle (LeetCode #141)
Difficulty: Easy
Category: Linked List
LeetCode: https://leetcode.com/problems/linked-list-cycle

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Examples:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list_with_cycle(values, pos):
    """Build a linked list from values; if pos >= 0, tail.next points back to that index."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def linked_list_cycle(head: ListNode) -> bool:
    """
    TODO: Implement your solution here

    Args:
        head: Head of a singly linked list (may contain a cycle)

    Returns:
        True if the linked list has a cycle, False otherwise
    """
    pass


# Test Cases
def test_linked_list_cycle():
    """Test cases for linked_list_cycle"""

    test_cases = [
        {"name": "Cycle back to 2nd node", "input": ([3, 2, 0, -4], 1), "expected": True},
        {"name": "Cycle back to head", "input": ([1, 2], 0), "expected": True},
        {"name": "No cycle", "input": ([1], -1), "expected": False},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        values, pos = test['input']
        print(f"\n{test['name']}")
        print(f"  Input: head = {values}, pos = {pos}")
        print(f"  Expected: {test['expected']}")

        try:
            head = build_linked_list_with_cycle(values, pos)
            result = linked_list_cycle(head)
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
    test_linked_list_cycle()
