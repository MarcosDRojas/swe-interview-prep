"""
Problem: 3Sum (LeetCode #15)
Difficulty: Medium
Category: Two Pointers
LeetCode: https://leetcode.com/problems/3sum

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i !=
j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Examples:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Time Complexity Target: O(n^2)
Space Complexity Target: O(n) (sort) or O(1) extra besides output
"""

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of integers

    Returns:
        All unique triplets that sum to zero (order of triplets/output doesn't matter)
    """
    pass


# Test Cases
def test_three_sum():
    """Test cases for three_sum"""

    test_cases = [
        {
            "name": 'Two valid triplets',
            "input": ([-1, 0, 1, 2, -1, -4],),
            "expected": [[-1, -1, 2], [-1, 0, 1]]
        },
        {
            "name": 'No valid triplet',
            "input": ([0, 1, 1],),
            "expected": []
        },
        {
            "name": 'All zeros',
            "input": ([0, 0, 0],),
            "expected": [[0, 0, 0]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = three_sum(*test['input'])
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
    test_three_sum()
