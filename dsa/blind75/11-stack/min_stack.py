"""
Problem: Min Stack (LeetCode #155)
Difficulty: Medium
Category: Stack
LeetCode: https://leetcode.com/problems/min-stack

Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant
time.

Implement the MinStack class:

 - MinStack() initializes the stack object.

 - void push(int value) pushes the element value onto the stack.

 - void pop() removes the element on the top of the stack.

 - int top() gets the top element of the stack.

 - int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Examples:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top(); // return 0
minStack.getMin(); // return -2

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Time Complexity Target: O(1) for every operation
Space Complexity Target: O(n)
"""

class MinStack:
    def __init__(self):
        """
        TODO: Implement your solution here (e.g. an auxiliary stack tracking the
        running minimum at each depth alongside the main stack)
        """
        pass

    def push(self, val: int) -> None:
        """
        TODO: Implement your solution here
        """
        pass

    def pop(self) -> None:
        """
        TODO: Implement your solution here
        """
        pass

    def top(self) -> int:
        """
        TODO: Implement your solution here
        """
        pass

    def getMin(self) -> int:
        """
        TODO: Implement your solution here
        """
        pass


# Test Cases
def test_min_stack():
    """Test cases for MinStack, driven by (method, args, expected) operation sequences."""

    scenarios = [
        {
            "name": "Push/pop with running minimum",
            "ops": ["push", "push", "push", "getMin", "pop", "top", "getMin"],
            "args": [[-2], [0], [-3], [], [], [], []],
            "expected": [None, None, None, -3, None, 0, -2],
        },
    ]

    passed = 0
    failed = 0
    total = 0

    for scenario in scenarios:
        print(f"\n{scenario['name']}")
        stack = MinStack()
        for op, args, expected in zip(scenario["ops"], scenario["args"], scenario["expected"]):
            total += 1
            try:
                result = getattr(stack, op)(*args)
                ok = (expected is None) or (result == expected)
                print(f"  stack.{op}({', '.join(map(repr, args))}) -> {result}  (expected {expected})")
                if ok:
                    passed += 1
                else:
                    print(f"  [FAIL]: Got {result}, expected {expected}")
                    failed += 1
            except Exception as e:
                print(f"  [FAIL]: {type(e).__name__}: {e}")
                failed += 1

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {total} calls")

    if failed == 0:
        print("All test cases passed!")
    else:
        print("Some test cases failed. Please review the implementation.")


if __name__ == "__main__":
    test_min_stack()
