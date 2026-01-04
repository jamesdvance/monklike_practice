# Longest Increasing Path in a Matrix

## Summary

Given an m x n matrix, return the length of the longest increasing path. You can move in four directions (up, down, left, right) and each step must go to a strictly larger value.

### Key Points
- DFS with memoization (not regular DP order)
- No need to track visited - strictly increasing prevents cycles
- Each cell computes its longest increasing path starting from it

### Optimal Approach
DFS with memoization.

```python
def longestIncreasingPath(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    memo = {}

    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]

        max_length = 1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                max_length = max(max_length, 1 + dfs(nr, nc))

        memo[(r, c)] = max_length
        return max_length

    return max(dfs(r, c) for r in range(m) for c in range(n))
```

### Complexity
- Time: O(m * n) - each cell computed once
- Space: O(m * n) for memoization

---

## Detailed Explanation

### Problem Analysis

Unlike typical grid DP, we can't fill cells in a simple order because paths can go any direction. However, memoization works because:
1. The "strictly increasing" constraint prevents cycles
2. Each cell's answer only depends on cells with larger values

### Why No Visited Set?

Since we only move to strictly larger values, we can never return to a previously visited cell in the same path. The increasing constraint acts as our visited check.

### Topological Sort Approach

Sort cells by value and process smallest first:

```python
def longestIncreasingPath(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    # Sort cells by value
    cells = [(matrix[r][c], r, c) for r in range(m) for c in range(n)]
    cells.sort()

    dp = [[1] * n for _ in range(m)]

    for val, r, c in cells:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] < matrix[r][c]:
                dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)

    return max(max(row) for row in dp)
```

Processing smallest values first ensures dependencies are computed first.

### BFS with Indegree (Peeling Onion)

Think of it as topological sort on the DAG of increasing edges:

```python
from collections import deque

def longestIncreasingPath(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    indegree = [[0] * n for _ in range(m)]

    # Count indegrees (how many neighbors are smaller)
    for r in range(m):
        for c in range(n):
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] < matrix[r][c]:
                    indegree[r][c] += 1

    # Start with cells that have no smaller neighbors (indegree 0)
    queue = deque()
    for r in range(m):
        for c in range(n):
            if indegree[r][c] == 0:
                queue.append((r, c))

    length = 0
    while queue:
        length += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        queue.append((nr, nc))

    return length
```

### Step-by-Step Example

```
matrix = [[9,9,4],
          [6,6,8],
          [2,1,1]]

From cell (2,1) value=1:
  Can go to (2,0)=2, (1,1)=6
  dfs(2,0): can go to (1,0)=6 -> dfs(1,0): can go to (0,0)=9 -> 1
            path: 1->2->6->9, length 4
  dfs(1,1): can go to (0,1)=9, (1,2)=8
            dfs(1,2): can go to (0,2)=4... nope, 4 < 8
            path: 1->6->8, length 3

Best from (2,1): 4
```

### Memoization Key Insight

Once we know the longest path from cell (r, c), we never need to recompute it. This is because:
- The path only depends on reachable larger values
- Those values don't change during our exploration

### Edge Cases
- Single cell: return 1
- All same values: return 1 (no increasing path)
- Strictly sorted matrix: diagonal path

### Related Problems
- Number of Increasing Paths in a Grid: count all paths
- Pacific Atlantic Water Flow: similar grid exploration
- Longest Increasing Subsequence: 1D version
