# N-Queens

## Summary

Place n queens on an n x n chessboard such that no two queens attack each other. Return all distinct solutions.

### Key Points
- Queens attack horizontally, vertically, and diagonally
- Place one queen per row, track columns and diagonals
- Use sets to track attacked columns and diagonals
- Iterates over rows rather than row, col

### Optimal Approach
Backtracking with sets to track conflicts.

```python
def solveNQueens(n: int) -> list[list[str]]:
    result = []
    board = [['.'] * n for _ in range(n)]

    cols = set()
    pos_diag = set()  # row + col
    neg_diag = set()  # row - col

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            backtrack(row + 1)

            # Remove queen
            board[row][col] = '.'
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)
    return result
```

### Complexity
- Time: O(n!) - upper bound on valid placements
- Space: O(n) for recursion and tracking sets

---

## Detailed Explanation

### Problem Analysis

The N-Queens problem is a classic constraint satisfaction problem. We place queens row by row, ensuring no two queens share a column, row, or diagonal.

### Diagonal Tracking

For an n x n board:
- **Positive diagonals** (going �): cells with same (row + col) value
- **Negative diagonals** (going �): cells with same (row - col) value

```
Positive diagonals (row + col):
0  1  2  3
1  2  3  4
2  3  4  5
3  4  5  6

Negative diagonals (row - col):
 0  -1  -2  -3
 1   0  -1  -2
 2   1   0  -1
 3   2   1   0
```

### Why Row-by-Row?

Since each row must have exactly one queen, we iterate through rows and decide which column to place the queen. This automatically ensures no two queens share a row.

### Step-by-Step Example (n=4)

```
Row 0: Try col 0
  Place Q at (0,0)
  cols={0}, pos_diag={0}, neg_diag={0}

  Row 1: Try col 0 - blocked (cols)
         Try col 1 - blocked (neg_diag: 1-1=0)
         Try col 2
    Place Q at (1,2)
    cols={0,2}, pos_diag={0,3}, neg_diag={0,-1}

    Row 2: Try col 0 - blocked
           Try col 1 - blocked (neg_diag: 2-1=1? no)
                       blocked (pos_diag: 2+1=3? yes)
           Try col 2 - blocked
           Try col 3 - blocked (pos_diag: 2+3=5? no)
                       blocked (neg_diag: 2-3=-1? yes)
    All blocked, backtrack

  Row 1: Try col 3
    Place Q at (1,3)
    ... continue ...
```

Eventually finds solutions like:
```
. Q . .
. . . Q
Q . . .
. . Q .
```

### Return Count Only

For just counting solutions:

```python
def totalNQueens(n: int) -> int:
    count = 0
    cols = set()
    pos_diag = set()
    neg_diag = set()

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            backtrack(row + 1)

            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)
    return count
```

### Number of Solutions

| n | Solutions |
|---|-----------|
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 7 | 40 |
| 8 | 92 |

### Edge Cases
- n = 1: single cell with queen
- n = 2 or 3: no solution possible
- Large n: exponential solutions

### Related Problems
- N-Queens II: count solutions only
- Sudoku Solver: similar constraint satisfaction
- Valid Sudoku: checking constraints
