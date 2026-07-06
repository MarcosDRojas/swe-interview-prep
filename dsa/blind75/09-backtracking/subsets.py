"""
Problem: Subsets (LeetCode #78)
Difficulty: Medium
Category: Backtracking
LeetCode: https://leetcode.com/problems/subsets

Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

Time Complexity Target: O(n * 2^n)
Space Complexity Target: O(n) recursion depth (plus O(2^n) output)
"""

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of unique integers

    Returns:
        All possible subsets (the power set); order doesn't matter
    """
    pass


# Test Cases
def test_subsets():
    """Test cases for subsets"""

    test_cases = [
        {
            "name": 'Three elements',
            "input": ([1, 2, 3],),
            "expected": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        },
        {
            "name": 'Single element',
            "input": ([0],),
            "expected": [[], [0]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = subsets(*test['input'])
            ok = result is not None and sorted(sorted(x) for x in result) == sorted(sorted(x) for x in test['expected'])

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
    test_subsets()
