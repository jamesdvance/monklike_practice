# Rotting Oranges

## Summary

In a grid, each cell can be empty (0), have a fresh orange (1), or have a rotten orange (2). Every minute, fresh oranges adjacent to rotten ones become rotten. Return the minimum minutes until no fresh oranges remain, or -1 if impossible.

### Key Points
- Multi-source BFS: start from all rotten oranges simultaneously
- Track minutes as BFS levels
- After BFS, check if any fresh oranges remain

### Optimal Approach
Use BFS starting from all initially rotten oranges at once.

```python
from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    while queue:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

    return minutes - 1 if fresh == 0 else -1
```

### Complexity
- Time: O(m * n)
- Space: O(m * n) for the queue

---

## Detailed Explanation

### Problem Analysis

This is a multi-source BFS problem where all rotten oranges spread simultaneously. Each BFS level represents one minute. We need the time for the "rot wave" to reach all fresh oranges.

### Why Multi-Source BFS?

Single-source BFS would require running from each rotten orange and taking the maximum. Multi-source BFS adds all sources to the queue initially, simulating simultaneous spreading.

### Why minutes - 1?

The loop increments minutes before processing, so after the last level with fresh oranges, minutes is incremented one extra time. Alternatively:

```python
minutes = -1
while queue:
    minutes += 1
    # ... process level
return minutes if fresh == 0 else -1
```

### Step-by-Step Example

```
Initial:     Minute 1:    Minute 2:    Minute 3:    Minute 4:
2 1 1        2 2 1        2 2 2        2 2 2        2 2 2
1 1 0   ->   2 1 0   ->   2 2 0   ->   2 2 0   ->   2 2 0
0 1 1        0 1 1        0 2 1        0 2 2        0 2 2

Answer: 4 minutes
```

### Alternative: Track Time in Queue

```python
from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh += 1

    max_time = 0
    while queue:
        r, c, time = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                max_time = time + 1
                queue.append((nr, nc, time + 1))

    return max_time if fresh == 0 else -1
```

### Edge Cases
- No fresh oranges: return 0
- No rotten oranges but fresh exist: return -1
- Fresh orange isolated (no path to rotten): return -1
- All rotten: return 0

### Related Problems
- Walls and Gates: similar multi-source BFS
- Shortest Path in Binary Matrix: BFS for shortest path
- 01 Matrix: distance to nearest zero
