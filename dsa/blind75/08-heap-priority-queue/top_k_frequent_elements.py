"""
Problem: Top K Frequent Elements (LeetCode #347)
Difficulty: Medium
Category: Heap / Priority Queue
LeetCode: https://leetcode.com/problems/top-k-frequent-elements

Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may
return the answer in any order.

Examples:
Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Input: nums = [1], k = 1

Output: [1]

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Time Complexity Target: O(n log k) with a heap, O(n) with bucket sort
Space Complexity Target: O(n)
"""

from typing import List

def top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of integers
        k: Number of most frequent elements to return

    Returns:
        The k most frequent elements (order doesn't matter)
    """
    pass


# Test Cases
def test_top_k_frequent_elements():
    """Test cases for top_k_frequent_elements"""

    test_cases = [
        {
            "name": 'Two most frequent',
            "input": ([1, 1, 1, 2, 2, 3], 2),
            "expected": [1, 2]
        },
        {
            "name": 'Single element',
            "input": ([1], 1),
            "expected": [1]
        },
        {
            "name": 'Tie broken by frequency only',
            "input": ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2),
            "expected": [1, 2]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = top_k_frequent_elements(*test['input'])
            ok = result is not None and sorted(result) == sorted(test['expected'])

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
    test_top_k_frequent_elements()
