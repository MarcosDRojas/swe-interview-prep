"""
Problem: Course Schedule (LeetCode #207)
Difficulty: Medium
Category: Graphs
LeetCode: https://leetcode.com/problems/course-schedule

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You
are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take
course bi first if you want to take course ai.

 - For example, the pair [0, 1], indicates that to take course 0 you have to first take course
1.

Return true if you can finish all courses. Otherwise, return false.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

Time Complexity Target: O(V + E)
Space Complexity Target: O(V + E)
"""

from typing import List

def course_schedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        numCourses: Total number of courses, labeled 0..numCourses-1
        prerequisites: prerequisites[i] = [a, b] means b must be taken before a

    Returns:
        True if all courses can be finished (no cyclic dependency)
    """
    pass


# Test Cases
def test_course_schedule():
    """Test cases for course_schedule"""

    test_cases = [
        {
            "name": 'No cycle',
            "input": (2, [[1, 0]]),
            "expected": True
        },
        {
            "name": 'Cyclic dependency',
            "input": (2, [[1, 0], [0, 1]]),
            "expected": False
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = course_schedule(*test['input'])
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
    test_course_schedule()
