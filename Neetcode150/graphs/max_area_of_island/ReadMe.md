# Max Area of Island

## Summary

Given a 2D grid of 0s and 1s, find the maximum area of an island. An island is a group of 1s connected horizontally or vertically. Area is the number of cells in the island.

### Key Points
- Similar to Number of Islands but track area during traversal
- Use DFS or BFS to explore each island
- Return the count of cells in the largest island

### Optimal Approach
Use DFS to explore each island and count its area.

```python
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0

        grid[r][c] = 0  # Mark as visited
        area = 1
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    return max_area
```

### Complexity
- Time: O(m * n) where m is rows and n is columns
- Space: O(m * n) for recursion stack in worst case

---

## Detailed Explanation

### Problem Analysis

This extends Number of Islands by returning area instead of count. The DFS function now returns the size of the connected component it explored.

### Concise DFS Version

```python
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    def dfs(r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
            grid[r][c] = 0
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        return 0

    return max(dfs(r, c) for r in range(len(grid)) for c in range(len(grid[0])))
```

### BFS Alternative

```python
from collections import deque

def maxAreaOfIsland(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = 0
        area = 0

        while queue:
            row, col = queue.popleft()
            area += 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc))

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, bfs(r, c))

    return max_area
```

### Iterative DFS with Stack

```python
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = 0
                stack = [(r, c)]
                grid[r][c] = 0

                while stack:
                    row, col = stack.pop()
                    area += 1

                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                max_area = max(max_area, area)

    return max_area
```

### Edge Cases
- Empty grid: return 0
- All water (0s): return 0
- All land (1s): return m * n
- Multiple islands of same max size: return that size

### Related Problems
- Number of Islands: count islands instead of area
- Island Perimeter: calculate perimeter of single island
- Count Sub Islands: compare islands in two grids
