"""
Problem: Two Sum (LeetCode #1)
Difficulty: Easy
Category: Array & Hashing
LeetCode: https://leetcode.com/problems/two-sum

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same
element twice.

You can return the answer in any order.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
- Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List

# How to think about it:
#   0. Brute force checks every pair with a nested loop (O(n^2) time,
#      O(1) space). The pattern here is trading space for time: a hash
#      map turns "have I seen this value before?" into an O(1) average
#      lookup, dropping the second loop entirely -> O(n) time, O(n) space.
#   1. Work backwards from the return type: we return indices, so anything
#      we look up in the dict must give us back an index.
#   2. Cache what you've directly observed (nums[i] -> i) — don't cache a
#      derived/computed value like the complement, since there's nothing
#      meaningful to map it to yet.
#   3. Compute the thing you're searching for (target - x) fresh at lookup
#      time, and check it against what's already cached.
def two_sum(nums: List[int], target: int) -> List[int]:
    memory = {}
    
    for i, x in enumerate(nums):
        bin = target - x
        if bin in memory:
            return [memory[bin], i]
        memory[x] = i


# Test Cases
def test_two_sum():
    """Test cases for two_sum"""

    test_cases = [
        {
            "name": 'Basic example',
            "input": ([2, 7, 11, 15], 9),
            "expected": [0, 1]
        },
        {
            "name": 'Target at end',
            "input": ([3, 2, 4], 6),
            "expected": [1, 2]
        },
        {
            "name": 'Same number used twice',
            "input": ([3, 3], 6),
            "expected": [0, 1]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = two_sum(*test['input'])
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
    test_two_sum()
