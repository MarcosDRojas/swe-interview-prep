"""
Problem: Climbing Stairs (LeetCode #70)
Difficulty: Easy
Category: Dynamic Programming
LeetCode: https://leetcode.com/problems/climbing-stairs

Description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Examples:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

def climbing_stairs(n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: Number of steps to the top

    Returns:
        Number of distinct ways to climb to the top taking 1 or 2 steps at a time
    """
    pass


# Test Cases
def test_climbing_stairs():
    """Test cases for climbing_stairs"""

    test_cases = [
        {
            "name": 'Two steps',
            "input": (2,),
            "expected": 2
        },
        {
            "name": 'Three steps',
            "input": (3,),
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = climbing_stairs(*test['input'])
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
    test_climbing_stairs()
