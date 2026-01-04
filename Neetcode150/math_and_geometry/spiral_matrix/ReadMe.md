# Spiral Matrix

## Summary

Given an m x n matrix, return all elements in spiral order (clockwise from outside in).

### Key Points
- Track boundaries: top, bottom, left, right
- Move right, down, left, up, then shrink boundaries
- Stop when boundaries cross

### Optimal Approach
Boundary tracking with direction cycling.

```python
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Move right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Move down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Move left (if still valid)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Move up (if still valid)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

### Complexity
- Time: O(m * n)
- Space: O(1) extra space (output not counted)

---

## Detailed Explanation

### Problem Analysis

We traverse the matrix in a spiral: right along top row, down the right column, left along bottom row, up the left column, then move inward and repeat.

### Why Check Boundaries?

After moving right and down, the remaining matrix might be:
- Just one row (no need to move left)
- Just one column (no need to move up)

The boundary checks prevent double-counting.

### Step-by-Step Example

```
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

Initial: top=0, bottom=2, left=0, right=2

Round 1:
  Right: 1,2,3 -> top=1
  Down: 6,9 -> right=1
  Left: 8,7 -> bottom=1
  Up: 4 -> left=1

Round 2:
  Right: 5 -> top=2
  top > bottom, done

Result: [1,2,3,6,9,8,7,4,5]
```

### Direction-Based Approach

```python
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []
    seen = [[False] * cols for _ in range(rows)]

    # Directions: right, down, left, up
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = c = di = 0

    for _ in range(rows * cols):
        result.append(matrix[r][c])
        seen[r][c] = True

        nr, nc = r + dr[di], c + dc[di]

        if 0 <= nr < rows and 0 <= nc < cols and not seen[nr][nc]:
            r, c = nr, nc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]

    return result
```

### Recursive Layer Approach

```python
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    def spiral_layer(top, bottom, left, right):
        if top > bottom or left > right:
            return []

        result = []

        # Top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])

        # Right column (excluding top)
        for row in range(top + 1, bottom + 1):
            result.append(matrix[row][right])

        if top < bottom:
            # Bottom row (excluding right)
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][col])

        if left < right:
            # Left column (excluding top and bottom)
            for row in range(bottom - 1, top, -1):
                result.append(matrix[row][left])

        return result + spiral_layer(top + 1, bottom - 1, left + 1, right - 1)

    return spiral_layer(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
```

### Edge Cases
- 1 x n matrix: just the row
- m x 1 matrix: just the column
- 1 x 1 matrix: single element
- Empty matrix: empty list

### Related Problems
- Spiral Matrix II: generate matrix in spiral order
- Rotate Image: different matrix transformation
- Diagonal Traverse: different traversal pattern
