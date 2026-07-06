"""
Problem: Pow(x, n) (LeetCode #50)
Difficulty: Medium
Category: Geometry & Math
LeetCode: https://leetcode.com/problems/powx-n

Description:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Examples:
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- n is an integer.
- Either x is not zero or n > 0.
- -10^4 <= x^n <= 10^4

Time Complexity Target: O(log n)
Space Complexity Target: O(log n) recursive, O(1) iterative
"""

def pow_x_n(x: float, n: int) -> float:
    """
    TODO: Implement your solution here

    Args:
        x: Base
        n: Exponent (may be negative)

    Returns:
        x raised to the power n
    """
    pass


# Test Cases
def test_pow_x_n():
    """Test cases for pow_x_n"""

    test_cases = [
        {
            "name": 'Positive exponent',
            "input": (2.0, 10),
            "expected": 1024.0
        },
        {
            "name": 'Non-integer base',
            "input": (2.1, 3),
            "expected": 9.261
        },
        {
            "name": 'Negative exponent',
            "input": (2.0, -2),
            "expected": 0.25
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = pow_x_n(*test['input'])
            ok = result is not None and abs(result - test['expected']) < 1e-5

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
    test_pow_x_n()
