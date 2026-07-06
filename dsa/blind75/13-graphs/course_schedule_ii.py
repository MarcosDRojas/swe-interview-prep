"""
Problem: Course Schedule II (LeetCode #210)
Difficulty: Medium
Category: Graphs
LeetCode: https://leetcode.com/problems/course-schedule-ii

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You
are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take
course bi first if you want to take course ai.

 - For example, the pair [0, 1], indicates that to take course 0 you have to first take course
1.

Return the ordering of courses you should take to finish all courses. If there are many valid
answers, return any of them. If it is impossible to finish all courses, return an empty array.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs [ai, bi] are distinct.

Time Complexity Target: O(V + E)
Space Complexity Target: O(V + E)
"""

from typing import List

def course_schedule_ii(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        numCourses: Total number of courses, labeled 0..numCourses-1
        prerequisites: prerequisites[i] = [a, b] means b must be taken before a

    Returns:
        A valid course order (multiple valid orders may exist), or [] if impossible
    """
    pass


# Test Cases
def test_course_schedule_ii():
    """Test cases for course_schedule_ii"""

    test_cases = [
        {
            "name": 'Single prerequisite',
            "input": (2, [[1, 0]]),
            "expected": [0, 1]
        },
        {
            "name": 'Diamond dependency',
            "input": (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
            "expected": [0, 2, 1, 3]
        },
        {
            "name": 'Cyclic — impossible',
            "input": (2, [[1, 0], [0, 1]]),
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
            result = course_schedule_ii(*test['input'])
            def _has_valid_order(n, prereqs):
                graph = {i: [] for i in range(n)}
                indeg = [0] * n
                for a, b in prereqs:
                    graph[b].append(a)
                    indeg[a] += 1
                queue = [i for i in range(n) if indeg[i] == 0]
                seen = 0
                while queue:
                    node = queue.pop()
                    seen += 1
                    for nb in graph[node]:
                        indeg[nb] -= 1
                        if indeg[nb] == 0:
                            queue.append(nb)
                return seen == n
            def _valid_order(order, n, prereqs):
                if order is None:
                    return False
                if not _has_valid_order(n, prereqs):
                    return order == []
                if sorted(order) != list(range(n)):
                    return False
                pos = {c: i for i, c in enumerate(order)}
                return all(pos[a] > pos[b] for a, b in prereqs)
            n_courses, prereqs = test['input']
            ok = _valid_order(result, n_courses, prereqs)

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
    test_course_schedule_ii()
