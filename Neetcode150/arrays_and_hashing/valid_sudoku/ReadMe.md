# Valid Sudoku

## Summary

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the rules: each row, column, and 3x3 sub-box must contain digits 1-9 without repetition.

### Key Points
- Do not need to solve the Sudoku, just validate current state
- Check three constraints: rows, columns, and 3x3 boxes
- Use hash sets to track seen digits in each region

### Optimal Approach
Use sets to track digits seen in each row, column, and box. Iterate through the board once.

```python
def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue

            box_idx = (r // 3) * 3 + (c // 3)

            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False

            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)

    return True
```

### Complexity
- Time: O(1) - always 81 cells to check (9x9 board)
- Space: O(1) - fixed size sets (at most 9 elements each)

---

## Detailed Explanation

### Problem Analysis

Valid Sudoku is a constraint satisfaction checking problem. The key insight is that we can check all three constraints (rows, columns, boxes) in a single pass through the board by maintaining separate tracking sets for each constraint type.

### Understanding Box Index Calculation

The 3x3 boxes are numbered 0-8:
```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

For any cell at (row, col):
- Box row = row // 3 (integer division gives 0, 1, or 2)
- Box col = col // 3
- Box index = (row // 3) * 3 + (col // 3)

Example: cell (5, 7)
- Box row = 5 // 3 = 1
- Box col = 7 // 3 = 2
- Box index = 1 * 3 + 2 = 5

### Alternative: Single Dictionary Approach

Use a single set with encoded keys:

```python
def isValidSudoku(board: list[list[str]]) -> bool:
    seen = set()

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue

            row_key = (r, val)
            col_key = (val, c)
            box_key = (r // 3, c // 3, val)

            if row_key in seen or col_key in seen or box_key in seen:
                return False

            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)

    return True
```

This uses tuple keys to encode which constraint is being tracked.

### Three Pass Approach

A more straightforward but less efficient approach:

```python
def isValidSudoku(board: list[list[str]]) -> bool:
    # Check rows
    for row in board:
        if not isValidUnit([c for c in row if c != '.']):
            return False

    # Check columns
    for c in range(9):
        col = [board[r][c] for r in range(9) if board[r][c] != '.']
        if not isValidUnit(col):
            return False

    # Check boxes
    for box_r in range(3):
        for box_c in range(3):
            box = []
            for r in range(box_r * 3, box_r * 3 + 3):
                for c in range(box_c * 3, box_c * 3 + 3):
                    if board[r][c] != '.':
                        box.append(board[r][c])
            if not isValidUnit(box):
                return False

    return True

def isValidUnit(unit: list[str]) -> bool:
    return len(unit) == len(set(unit))
```

### Edge Cases
- Empty board (all dots): valid
- Single filled cell: valid
- Board with letters or invalid characters: depends on problem constraints
- Duplicate in same cell position: not possible with valid input

### Connection to Sudoku Solver

This validation function is a building block for Sudoku solving algorithms. When implementing a backtracking Sudoku solver, you need to validate the board state after each placement. A more efficient approach for solving is to check only the affected row, column, and box rather than the entire board.

### Related Problems
- Sudoku Solver: backtracking to fill the entire board
- N-Queens: another constraint satisfaction problem
- Valid Tic-Tac-Toe State: simpler validation problem
