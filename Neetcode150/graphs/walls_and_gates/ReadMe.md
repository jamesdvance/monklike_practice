# Walls and Gates

## Summary

Given a 2D grid where -1 is a wall, 0 is a gate, and INF (2^31 - 1) is an empty room, fill each empty room with the distance to its nearest gate. If no gate is reachable, leave it as INF.

### Key Points
- Multi-source BFS from all gates simultaneously
- Each BFS level represents distance +1 from gates
- More efficient than BFS from each empty room

### Optimal Approach
Use multi-source BFS starting from all gates.

```python
from collections import deque

def wallsAndGates(rooms: list[list[int]]) -> None:
    if not rooms:
        return

    INF = 2147483647
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    # Add all gates to the queue
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))
```

### Complexity
- Time: O(m * n)
- Space: O(m * n) for the queue

---

## Detailed Explanation

### Problem Analysis

This is a classic multi-source BFS problem. By starting from all gates simultaneously, each room is visited when the shortest path from any gate first reaches it. This is more efficient than running BFS from each room.

### Why Multi-Source BFS?

Starting from rooms and searching for gates: O(m * n) rooms * O(m * n) BFS = O((mn)^2)

Starting from gates (multi-source): O(m * n) total - each cell visited once.

### How It Works

1. All gates (distance 0) are added to the queue
2. BFS expands outward, each level is distance +1
3. When we reach an empty room, we've found its shortest distance
4. Rooms are only visited once (first visit = shortest path)

### Step-by-Step Example

```
INF  -1   0  INF          3   -1   0   1
INF INF INF  -1     ->    2    2   1  -1
INF  -1 INF  -1           1   -1   2  -1
  0  -1 INF INF           0   -1   3   4

Gates at (0,2) and (3,0) start the BFS.
Level 1: distance 1 from gates
Level 2: distance 2 from gates
...
```

### DFS Alternative (Less Efficient)

```python
def wallsAndGates(rooms: list[list[int]]) -> None:
    if not rooms:
        return

    rows, cols = len(rooms), len(rooms[0])

    def dfs(r, c, dist):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if rooms[r][c] < dist:  # Wall, gate, or already found shorter
            return

        rooms[r][c] = dist
        dfs(r + 1, c, dist + 1)
        dfs(r - 1, c, dist + 1)
        dfs(r, c + 1, dist + 1)
        dfs(r, c - 1, dist + 1)

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                dfs(r, c, 0)
```

DFS may revisit cells if a shorter path is found later, making it less efficient.

### Edge Cases
- No gates: all INF rooms remain INF
- No empty rooms: nothing to update
- Room surrounded by walls: stays INF
- All connected: all rooms get a distance value

### Related Problems
- Rotting Oranges: similar multi-source BFS
- 01 Matrix: distance to nearest 0
- Shortest Path in Binary Matrix: BFS for shortest path
