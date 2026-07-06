"""
Problem: Find Median from Data Stream (LeetCode #295)
Difficulty: Hard
Category: Heap / Priority Queue
LeetCode: https://leetcode.com/problems/find-median-from-data-stream

Description:
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.

 - For example, for arr = [2,3,4], the median is 3.

 - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

 - MedianFinder() initializes the MedianFinder object.

 - void addNum(int num) adds the integer num from the data stream to the data structure.

 - double findMedian() returns the median of all elements so far. Answers within 10^-5 of the
actual answer will be accepted.

Examples:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1); // arr = [1]
medianFinder.addNum(2); // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3); // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Time Complexity Target: O(log n) per addNum, O(1) per findMedian
Space Complexity Target: O(n)
"""

class MedianFinder:
    def __init__(self):
        """
        TODO: Implement your solution here (e.g. two heaps: max-heap for the lower
        half, min-heap for the upper half, kept balanced in size)
        """
        pass

    def addNum(self, num: int) -> None:
        """
        TODO: Implement your solution here
        """
        pass

    def findMedian(self) -> float:
        """
        TODO: Implement your solution here
        """
        pass


# Test Cases
def test_median_finder():
    """Test cases for MedianFinder, driven by (method, args, expected) operation sequences."""

    scenarios = [
        {
            "name": "Running median as numbers stream in",
            "ops": ["addNum", "addNum", "findMedian", "addNum", "findMedian"],
            "args": [[1], [2], [], [3], []],
            "expected": [None, None, 1.5, None, 2.0],
        },
    ]

    passed = 0
    failed = 0
    total = 0

    for scenario in scenarios:
        print(f"\n{scenario['name']}")
        finder = MedianFinder()
        for op, args, expected in zip(scenario["ops"], scenario["args"], scenario["expected"]):
            total += 1
            try:
                result = getattr(finder, op)(*args)
                ok = (expected is None) or (result is not None and abs(result - expected) < 1e-5)
                print(f"  finder.{op}({', '.join(map(repr, args))}) -> {result}  (expected {expected})")
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
    test_median_finder()
