# Set Matrix Zeroes

## Summary

Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

### Key Points
- Use first row and column as markers
- Track if first row/column originally had zeros
- Process markers in reverse to avoid overwriting

### Optimal Approach
Use first row and column as flags.

```python
def setZeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])

    # Check if first row/column have zeros
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Mark zeros in first row/column
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out cells based on marks
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Handle first row
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Handle first column
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
```

### Complexity
- Time: O(m * n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The challenge is doing this in-place. We use the first row and column as markers:
- matrix[0][j] = 0 means column j should be zeroed
- matrix[i][0] = 0 means row i should be zeroed

But we need to remember if the first row/column themselves should be zeroed.

### Why Process Interior First?

If we zero the first row/column first, we lose the marker information. So:
1. Check if first row/column need zeroing
2. Use first row/column to mark other rows/columns
3. Zero the interior based on marks
4. Finally zero first row/column if needed

### Step-by-Step Example

```
Initial:
[[1,1,1],
 [1,0,1],
 [1,1,1]]

first_row_zero = False
first_col_zero = False

Mark zeros:
matrix[1][0] = 0 (row 1)
matrix[0][1] = 0 (column 1)

[[1,0,1],
 [0,0,1],
 [1,1,1]]

Zero based on marks:
[[1,0,1],
 [0,0,0],
 [1,0,1]]

First row/col unchanged.

Final:
[[1,0,1],
 [0,0,0],
 [1,0,1]]
```

### O(m + n) Space Approach

```python
def setZeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
```

### Using Single Variable for First Row/Col

```python
def setZeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    col_zero = False

    for i in range(m):
        if matrix[i][0] == 0:
            col_zero = True

        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Process in reverse
    for i in range(m - 1, -1, -1):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

        if col_zero:
            matrix[i][0] = 0
```

Processing in reverse ensures we don't overwrite markers before using them.

### Edge Cases
- Single row or column: straightforward
- All zeros: entire matrix becomes zero
- No zeros: matrix unchanged
- Zero in corner: affects first row and column

### Related Problems
- Game of Life: similar in-place state tracking
- Shortest Bridge: modifying matrix during traversal
- Surrounded Regions: marking regions
