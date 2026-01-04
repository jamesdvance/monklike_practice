# Swim in Rising Water

## Summary

Given an n x n grid where grid[i][j] represents elevation, find the minimum time t such that you can swim from top-left to bottom-right. At time t, you can swim through any cell with elevation <= t.

### Key Points
- This is a shortest path problem with a twist
- The "cost" is the maximum elevation along the path
- Use modified Dijkstra or binary search with BFS

### Optimal Approach (Modified Dijkstra)
Use a min-heap to always expand the cell with minimum elevation.

```python
import heapq

def swimInWater(grid: list[list[int]]) -> int:
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]  # (max_elevation, row, col)
    visited[0][0] = True

    while heap:
        max_elev, r, c = heapq.heappop(heap)

        if r == n - 1 and c == n - 1:
            return max_elev

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                new_elev = max(max_elev, grid[nr][nc])
                heapq.heappush(heap, (new_elev, nr, nc))

    return -1
```

### Complexity
- Time: O(n^2 log n)
- Space: O(n^2)

---

## Detailed Explanation

### Problem Analysis

We need to find a path from (0,0) to (n-1,n-1) that minimizes the maximum elevation along the path. This is the "minimax path" problem.

Think of it as: what's the minimum water level needed so we can swim through?

### Why Modified Dijkstra?

Regular Dijkstra minimizes sum of edge weights. Here, we minimize the maximum weight (elevation) along the path.

By using a min-heap ordered by max elevation so far, we always explore the path with the smallest "bottleneck" first.

### Step-by-Step Example

```
grid = [[0,2],
        [1,3]]

Start at (0,0), elevation 0.
Heap: [(0, 0, 0)]

Pop (0, 0, 0):
  Neighbors: (0,1) elev 2, (1,0) elev 1
  Push: [(1, 1, 0), (2, 0, 1)]

Pop (1, 1, 0):
  Neighbors: (1,1) elev 3
  max_elev = max(1, 3) = 3
  Push: [(2, 0, 1), (3, 1, 1)]

Pop (2, 0, 1):
  Neighbors: (1,1) already visited

Pop (3, 1, 1):
  This is destination!
  Return 3
```

### Binary Search + BFS Alternative

Binary search on the answer, check if path exists.

```python
from collections import deque

def swimInWater(grid: list[list[int]]) -> int:
    n = len(grid)

    def can_reach(t):
        if grid[0][0] > t:
            return False

        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            if r == n - 1 and c == n - 1:
                return True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and
                    not visited[nr][nc] and grid[nr][nc] <= t):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return False

    left, right = max(grid[0][0], grid[n-1][n-1]), n * n - 1

    while left < right:
        mid = (left + right) // 2
        if can_reach(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

Time: O(n^2 log(n^2)) = O(n^2 log n)

### Union-Find Alternative

Process cells by elevation, union adjacent cells.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def swimInWater(grid: list[list[int]]) -> int:
    n = len(grid)
    uf = UnionFind(n * n)

    # Sort cells by elevation
    cells = [(grid[r][c], r, c) for r in range(n) for c in range(n)]
    cells.sort()

    visited = [[False] * n for _ in range(n)]

    for elev, r, c in cells:
        visited[r][c] = True

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc]:
                uf.union(r * n + c, nr * n + nc)

        if uf.connected(0, n * n - 1):
            return elev

    return -1
```

### Comparison of Approaches

| Approach | Time | Space | Idea |
|----------|------|-------|------|
| Dijkstra | O(n^2 log n) | O(n^2) | Greedy expansion by max elevation |
| Binary Search | O(n^2 log n) | O(n^2) | Check if path exists at time t |
| Union-Find | O(n^2 log n) | O(n^2) | Connect cells by elevation order |

### Edge Cases
- 1x1 grid: return grid[0][0]
- Grid with 0 at start and end: answer is max elevation on some path
- All same values: return that value

### Related Problems
- Path With Minimum Effort: similar minimax path
- Shortest Path in Binary Matrix: standard BFS
- Cheapest Flights Within K Stops: constrained shortest path
