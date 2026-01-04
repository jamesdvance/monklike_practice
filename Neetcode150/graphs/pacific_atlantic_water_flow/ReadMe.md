# Pacific Atlantic Water Flow

## Summary

Given an m x n matrix of heights, find all cells from which water can flow to both the Pacific Ocean (top/left edges) and Atlantic Ocean (bottom/right edges). Water flows from a cell to adjacent cells with equal or lower height.

### Key Points
- Think in reverse: start from oceans and flow upward
- A cell reaching both oceans must be in the intersection
- Use DFS/BFS from ocean edges, moving to higher or equal cells

### Optimal Approach
Run DFS from each ocean's edges, then find the intersection.

```python
def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited):
        visited.add((r, c))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and
                heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, visited)

    # Start from Pacific edges (top and left)
    for c in range(cols):
        dfs(0, c, pacific)
    for r in range(rows):
        dfs(r, 0, pacific)

    # Start from Atlantic edges (bottom and right)
    for c in range(cols):
        dfs(rows - 1, c, atlantic)
    for r in range(rows):
        dfs(r, cols - 1, atlantic)

    return list(pacific & atlantic)
```

### Complexity
- Time: O(m * n) - each cell visited at most twice
- Space: O(m * n) for the visited sets

---

## Detailed Explanation

### Problem Analysis

Forward approach (from each cell, check if it reaches both oceans) would be O((mn)^2). The key insight is to reverse the problem:

1. Start from ocean edges
2. Flow "upward" to cells with equal or greater height
3. Mark cells reachable from each ocean
4. Answer is the intersection

### Why Reverse the Flow?

```
Forward: For each cell, trace path to ocean (expensive)
Reverse: From ocean, find all cells that can reach it (efficient)
```

Reverse approach processes each cell at most twice (once per ocean).

### BFS Alternative

```python
from collections import deque

def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []

    rows, cols = len(heights), len(heights[0])

    def bfs(starts):
        visited = set(starts)
        queue = deque(starts)

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return visited

    pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)]
    atlantic_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows-1)]

    pacific = bfs(pacific_starts)
    atlantic = bfs(atlantic_starts)

    return list(pacific & atlantic)
```

### Step-by-Step Example

```
heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]

Pacific reachable (top-left edges):
Start from top row and left column, move to higher/equal cells.

Atlantic reachable (bottom-right edges):
Start from bottom row and right column, move to higher/equal cells.

Intersection: cells that can flow to both.
```

### Edge Cases
- Single cell: can reach both oceans
- 1 x n or m x 1: all cells on edges reach both
- Flat grid (all same height): all cells reach both

### Related Problems
- Number of Islands: basic grid DFS
- Surrounded Regions: similar edge-based thinking
- Longest Increasing Path in a Matrix: DFS on grid with constraints
