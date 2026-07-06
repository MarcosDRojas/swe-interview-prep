"""
Problem: Reconstruct Itinerary (LeetCode #332)
Difficulty: Hard
Category: Advanced Graphs
LeetCode: https://leetcode.com/problems/reconstruct-itinerary

Description:
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure
and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with
"JFK". If there are multiple valid itineraries, you should return the itinerary that has the
smallest lexical order when read as a single string.

 - For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. You must use all the tickets once
and only once.

Examples:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
- fromi and toi consist of uppercase English letters.
- fromi != toi

Time Complexity Target: O(E log E) (sorting adjacency lists)
Space Complexity Target: O(E)
"""

from typing import List

def reconstruct_itinerary(tickets: List[List[str]]) -> List[str]:
    """
    TODO: Implement your solution here

    Args:
        tickets: tickets[i] = [from, to] airport pairs, all must be used exactly once

    Returns:
        The itinerary starting at JFK, using every ticket, smallest lexical order if multiple exist
    """
    pass


# Test Cases
def test_reconstruct_itinerary():
    """Test cases for reconstruct_itinerary"""

    test_cases = [
        {
            "name": 'Single valid route',
            "input": ([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']],),
            "expected": ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
        },
        {
            "name": 'Smallest lexical order among options',
            "input": ([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']],),
            "expected": ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = reconstruct_itinerary(*test['input'])
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
    test_reconstruct_itinerary()
