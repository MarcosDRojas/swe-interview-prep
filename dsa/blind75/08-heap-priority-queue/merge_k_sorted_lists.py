"""
Problem: Merge k Sorted Lists (LeetCode #23)
Difficulty: Hard
Category: Heap / Priority Queue
LeetCode: https://leetcode.com/problems/merge-k-sorted-lists

Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Examples:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
 1->4->5,
 1->3->4,
 2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Input: lists = []
Output: []

Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.

Time Complexity Target: O(n log k), n = total nodes, k = number of lists
Space Complexity Target: O(k) for the heap
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


def merge_k_sorted_lists(lists: "List[ListNode]") -> ListNode:
    """
    TODO: Implement your solution here

    Args:
        lists: A list of the heads of k sorted linked lists

    Returns:
        The head of one fully merged sorted linked list
    """
    pass


# Test Cases
def test_merge_k_sorted_lists():
    """Test cases for merge_k_sorted_lists"""

    test_cases = [
        {"name": "Three sorted lists", "input": [[1, 4, 5], [1, 3, 4], [2, 6]], "expected": [1, 1, 2, 3, 4, 4, 5, 6]},
        {"name": "No lists", "input": [], "expected": []},
        {"name": "One empty list", "input": [[]], "expected": []},
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: lists = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            heads = [build_linked_list(values) for values in test['input']]
            result_head = merge_k_sorted_lists(heads)
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
    test_merge_k_sorted_lists()
