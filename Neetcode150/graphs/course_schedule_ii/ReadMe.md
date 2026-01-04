# Course Schedule II

## Summary

Given numCourses and prerequisites, return the ordering of courses to finish all courses. If impossible (cycle exists), return an empty array. This is topological sort.

### Key Points
- Same as Course Schedule but return the order
- Use BFS (Kahn's) or DFS topological sort
- Track visited nodes to detect cycles

### Optimal Approach (BFS - Kahn's Algorithm)
Topological sort with order tracking.

```python
from collections import defaultdict, deque

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(numCourses) if indegree[i] == 0)
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == numCourses else []
```

### Complexity
- Time: O(V + E)
- Space: O(V + E)

---

## Detailed Explanation

### Problem Analysis

This extends Course Schedule by returning a valid topological ordering. The order in which courses are "completed" in Kahn's algorithm gives us the answer.

### DFS Topological Sort

```python
from collections import defaultdict

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * numCourses
    order = []

    def dfs(course):
        if state[course] == 1:  # Cycle
            return False
        if state[course] == 2:  # Already processed
            return True

        state[course] = 1

        for next_course in graph[course]:
            if not dfs(next_course):
                return False

        state[course] = 2
        order.append(course)  # Add after all dependencies
        return True

    for course in range(numCourses):
        if not dfs(course):
            return []

    return order[::-1]  # Reverse for correct order
```

### Why Reverse in DFS?

In DFS, we add a course to the result after processing all its dependents. This gives us reverse topological order (dependencies come after). We reverse to get the correct order.

In BFS, we process courses as they become available (prerequisites satisfied), giving us correct order directly.

### Step-by-Step Example

```
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]

Graph:
0 -> 1, 2
1 -> 3
2 -> 3

BFS Order:
Start: [0] (indegree 0)
Complete 0 -> order = [0]
Add 1, 2 to queue (indegree now 0)
Complete 1 -> order = [0, 1]
Complete 2 -> order = [0, 1, 2]
Add 3 to queue
Complete 3 -> order = [0, 1, 2, 3]

Valid orderings: [0,1,2,3] or [0,2,1,3]
```

### Multiple Valid Orders

There can be multiple valid topological orderings. Both BFS and DFS will produce one valid order, but they may differ:

- BFS: processes by "layers" of available courses
- DFS: explores depth-first, may produce different valid order

### Cycle Detection

Both approaches detect cycles:
- BFS: fewer than numCourses completed means cycle
- DFS: back edge to "visiting" node means cycle

### Edge Cases
- No prerequisites: return [0, 1, 2, ..., n-1] (any order)
- Single course: return [0]
- Cycle exists: return []

### Related Problems
- Course Schedule: just detect if possible
- Alien Dictionary: topological sort of characters
- Sequence Reconstruction: verify unique topological order
