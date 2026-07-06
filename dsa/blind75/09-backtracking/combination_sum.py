"""
Problem: Combination Sum (LeetCode #39)
Difficulty: Medium
Category: Backtracking
LeetCode: https://leetcode.com/problems/combination-sum

Description:
Given an array of distinct integers candidates and a target integer target, return a list of all
unique combinations of candidates where the chosen numbers sum to target. You may return the
combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are
unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.

Examples:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []

Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

Time Complexity Target: O(2^target) worst case, pruned by the running-sum cutoff
Space Complexity Target: O(target / min(candidates)) recursion depth
"""

from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        candidates: Array of distinct positive integers (reusable)
        target: Target sum

    Returns:
        All unique combinations that sum to target; order doesn't matter
    """
    pass


# Test Cases
def test_combination_sum():
    """Test cases for combination_sum"""

    test_cases = [
        {
            "name": 'Two combinations',
            "input": ([2, 3, 6, 7], 7),
            "expected": [[2, 2, 3], [7]]
        },
        {
            "name": 'Three combinations',
            "input": ([2, 3, 5], 8),
            "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        },
        {
            "name": 'No combination possible',
            "input": ([2], 1),
            "expected": []
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = combination_sum(*test['input'])
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
    test_combination_sum()
