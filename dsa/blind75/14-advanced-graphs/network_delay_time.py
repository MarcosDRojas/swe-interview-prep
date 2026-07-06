"""
Problem: Network Delay Time (LeetCode #743)
Difficulty: Medium
Category: Advanced Graphs
LeetCode: https://leetcode.com/problems/network-delay-time

Description:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of
travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the
target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes
to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Examples:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Time Complexity Target: O((V + E) log V)
Space Complexity Target: O(V + E)
"""

from typing import List

def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        times: times[i] = [u, v, w]: directed edge u->v taking w time
        n: Number of nodes, labeled 1..n
        k: Source node the signal starts from

    Returns:
        Minimum time for all n nodes to receive the signal, or -1 if impossible
    """
    pass


# Test Cases
def test_network_delay_time():
    """Test cases for network_delay_time"""

    test_cases = [
        {
            "name": 'All nodes reachable',
            "input": ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),
            "expected": 2
        },
        {
            "name": 'Single edge, correct source',
            "input": ([[1, 2, 1]], 2, 1),
            "expected": 1
        },
        {
            "name": 'Single edge, wrong source',
            "input": ([[1, 2, 1]], 2, 2),
            "expected": -1
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = network_delay_time(*test['input'])
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
    test_network_delay_time()
