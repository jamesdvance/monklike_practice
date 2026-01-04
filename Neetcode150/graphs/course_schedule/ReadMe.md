# Course Schedule

## Summary

Given numCourses and prerequisites where prerequisites[i] = [a, b] means you must take course b before course a, determine if you can finish all courses. This is essentially cycle detection in a directed graph.

### Key Points
- Model as a directed graph: prerequisite -> course
- If there's a cycle, impossible to complete all courses
- Use topological sort (BFS with indegree) or DFS cycle detection

### Optimal Approach (BFS - Kahn's Algorithm)
Use topological sort with indegree tracking.

```python
from collections import defaultdict, deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    # Start with courses that have no prerequisites
    queue = deque(i for i in range(numCourses) if indegree[i] == 0)
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return completed == numCourses
```

### Complexity
- Time: O(V + E) where V is numCourses and E is len(prerequisites)
- Space: O(V + E) for the graph

---

## Detailed Explanation

### Problem Analysis

This is a classic cycle detection problem in a directed graph:
- Nodes = courses
- Edges = prerequisites (prereq -> course)
- Cycle = impossible to complete (circular dependency)

### Kahn's Algorithm (BFS Topological Sort)

1. Calculate indegree (number of prerequisites) for each course
2. Start with courses having indegree 0 (no prerequisites)
3. "Complete" a course, reduce indegree of dependent courses
4. Add newly available courses (indegree = 0) to queue
5. If all courses completed, no cycle exists

### DFS Cycle Detection

```python
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0 = unvisited, 1 = visiting (in current path), 2 = visited
    state = [0] * numCourses

    def has_cycle(course):
        if state[course] == 1:  # Back edge - cycle!
            return True
        if state[course] == 2:  # Already fully processed
            return False

        state[course] = 1  # Mark as visiting

        for next_course in graph[course]:
            if has_cycle(next_course):
                return True

        state[course] = 2  # Mark as visited
        return False

    for course in range(numCourses):
        if has_cycle(course):
            return False

    return True
```

### Why Three States in DFS?

- **Unvisited (0)**: Not yet explored
- **Visiting (1)**: Currently in the DFS stack (part of current path)
- **Visited (2)**: Fully explored, safe

A back edge to a "visiting" node indicates a cycle in the current path.

### Step-by-Step Example

```
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]

Graph:
0 -> 1, 2
1 -> 3
2 -> 3

Indegrees: [0, 1, 1, 2]

BFS:
Queue: [0] (indegree 0)
Pop 0, complete. Reduce indegree of 1, 2.
Indegrees: [0, 0, 0, 2]
Queue: [1, 2]

Pop 1, complete. Reduce indegree of 3.
Indegrees: [0, 0, 0, 1]

Pop 2, complete. Reduce indegree of 3.
Indegrees: [0, 0, 0, 0]
Queue: [3]

Pop 3, complete.

Completed: 4 = numCourses. Return True.
```

### Edge Cases
- No prerequisites: return True (all independent)
- Self-loop [0, 0]: return False (cycle)
- Disconnected graph: handle all components

### Related Problems
- Course Schedule II: return valid ordering
- Alien Dictionary: topological sort of characters
- Parallel Courses: minimum time with parallel execution
