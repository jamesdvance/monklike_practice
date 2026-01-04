# Rotate Image

## Summary

Rotate an n x n 2D matrix by 90 degrees clockwise in-place.

### Key Points
- Transpose the matrix (swap rows and columns)
- Reverse each row
- Or: rotate layer by layer from outside in

### Optimal Approach
Transpose then reverse rows.

```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
```

### Complexity
- Time: O(n^2)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

90-degree clockwise rotation can be decomposed into:
1. Transpose: swap matrix[i][j] with matrix[j][i]
2. Reverse each row

This works because:
- Original position (i, j) -> after transpose (j, i) -> after reverse (j, n-1-i)
- This matches 90-degree rotation: (i, j) -> (j, n-1-i)

### Why This Decomposition?

After transpose: row i becomes column i (from left to right)
After row reverse: column i reads top to bottom as original row i read left to right

### Layer-by-Layer Approach

```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for layer in range(n // 2):
        first, last = layer, n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # Save top
            top = matrix[first][i]

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = top
```

### Step-by-Step Example

```
Original:      Transpose:     Reverse rows:
1 2 3          1 4 7          7 4 1
4 5 6    ->    2 5 8    ->    8 5 2
7 8 9          3 6 9          9 6 3
```

### For Counter-Clockwise (270 CW)

Transpose then reverse columns (or reverse rows then transpose):

```python
def rotate_ccw(matrix: list[list[int]]) -> None:
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each column
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
```

### 180-Degree Rotation

Reverse all rows, then reverse each row:

```python
def rotate_180(matrix: list[list[int]]) -> None:
    matrix.reverse()
    for row in matrix:
        row.reverse()
```

### Edge Cases
- 1x1 matrix: no change needed
- 2x2 matrix: single swap cycle
- Empty matrix: no change

### Related Problems
- Spiral Matrix: different traversal pattern
- Transpose Matrix: just the transpose step
- Determine Whether Matrix Can Be Obtained: rotation comparison
