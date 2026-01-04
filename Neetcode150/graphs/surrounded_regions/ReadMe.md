# Surrounded Regions

## Summary

Given an m x n board with 'X' and 'O', capture all regions surrounded by 'X'. A region is captured by flipping all 'O's to 'X's. Regions on the border or connected to the border cannot be captured.

### Key Points
- Work from the edges inward, not center outward
- Mark 'O's connected to border as safe
- Flip remaining 'O's to 'X' and restore safe ones

### Optimal Approach
Use DFS from border 'O's to mark safe cells, then flip the rest.

```python
def solve(board: list[list[str]]) -> None:
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'S'  # Mark as safe
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Mark all 'O's connected to border
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # Flip remaining 'O' to 'X', restore 'S' to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'
```

### Complexity
- Time: O(m * n)
- Space: O(m * n) for recursion stack in worst case

---

## Detailed Explanation

### Problem Analysis

A region of 'O's is surrounded if it has no connection to the border. Instead of finding surrounded regions (complex), we find regions NOT surrounded (connected to border) and flip everything else.

### Three-Phase Algorithm

1. **Mark safe**: DFS from all border 'O's, mark connected cells as 'S'
2. **Capture**: Change all remaining 'O' to 'X' (these are surrounded)
3. **Restore**: Change 'S' back to 'O' (these touch the border)

### Step-by-Step Example

```
Input:          After marking:    Final:
X X X X         X X X X           X X X X
X O O X    ->   X O O X      ->   X X X X
X X O X         X X O X           X X X X
X O X X         X S X X           X O X X

Border 'O' at (3,1) marked as 'S'.
'O's at (1,1), (1,2), (2,2) are surrounded, flipped to 'X'.
'S' at (3,1) restored to 'O'.
```

### BFS Alternative

```python
from collections import deque

def solve(board: list[list[str]]) -> None:
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def bfs(r, c):
        if board[r][c] != 'O':
            return
        queue = deque([(r, c)])
        board[r][c] = 'S'

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    queue.append((nr, nc))

    # Mark border-connected 'O's
    for r in range(rows):
        bfs(r, 0)
        bfs(r, cols - 1)
    for c in range(cols):
        bfs(0, c)
        bfs(rows - 1, c)

    # Flip and restore
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'
```

### Union-Find Alternative

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

def solve(board: list[list[str]]) -> None:
    if not board:
        return

    rows, cols = len(board), len(board[0])
    uf = UnionFind(rows * cols + 1)
    dummy = rows * cols  # Virtual node for border

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                idx = r * cols + c
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    uf.union(idx, dummy)
                if r > 0 and board[r-1][c] == 'O':
                    uf.union(idx, (r-1) * cols + c)
                if c > 0 and board[r][c-1] == 'O':
                    uf.union(idx, r * cols + c - 1)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and uf.find(r * cols + c) != uf.find(dummy):
                board[r][c] = 'X'
```

### Edge Cases
- All 'X': no changes
- All 'O': only border cells remain 'O'
- 1 x n or m x 1: nothing surrounded
- Single cell: cannot be surrounded

### Related Problems
- Number of Enclaves: count cells in surrounded regions
- Pacific Atlantic Water Flow: similar border-based thinking
- Flood Fill: basic DFS on grid
