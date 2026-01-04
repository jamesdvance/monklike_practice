# Number of Islands

## Summary

Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

### Key Points
- Classic graph traversal problem on a grid
- Use DFS or BFS to explore connected land cells
- Mark visited cells to avoid counting twice

### Optimal Approach
Use DFS to explore each island and mark cells as visited.

```python
def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return

        grid[r][c] = '0'  # Mark as visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count
```

### Complexity
- Time: O(m * n) where m is rows and n is columns
- Space: O(m * n) for recursion stack in worst case

---

## Detailed Explanation

### Problem Analysis

Each connected group of '1's forms one island. We need to:
1. Find a land cell
2. Explore all connected land cells (the entire island)
3. Mark them as visited
4. Increment island count
5. Repeat until all cells are processed

### Why Modify the Grid?

By changing '1' to '0' (or any non-'1' value), we mark cells as visited without extra space. If the grid shouldn't be modified, use a separate visited set.

### BFS Alternative

```python
from collections import deque

def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)

    return count
```

BFS avoids deep recursion but uses queue space.

### Union-Find Alternative

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1

def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                uf.count += 1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                idx = r * cols + c
                if r + 1 < rows and grid[r + 1][c] == '1':
                    uf.union(idx, (r + 1) * cols + c)
                if c + 1 < cols and grid[r][c + 1] == '1':
                    uf.union(idx, r * cols + c + 1)

    return uf.count
```

Union-Find is useful for dynamic connectivity problems.

### Edge Cases
- Empty grid: return 0
- All water: return 0
- All land: return 1
- Single cell: return 1 if land, 0 if water

### Related Problems
- Max Area of Island: find largest island
- Surrounded Regions: identify enclosed regions
- Number of Distinct Islands: count unique shapes
