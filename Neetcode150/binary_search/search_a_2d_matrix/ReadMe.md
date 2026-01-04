# Search a 2D Matrix

## Summary

Given an m x n matrix where each row is sorted left-to-right and the first element of each row is greater than the last element of the previous row, determine if a target value exists in the matrix.

### Key Points
- Matrix can be treated as a single sorted array
- Use binary search on this virtual 1D array
- Convert 1D index to 2D coordinates: row = idx // n, col = idx % n

### Optimal Approach
Treat the matrix as a sorted array of m*n elements and perform binary search.

```python
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        row, col = mid // n, mid % n
        val = matrix[row][col]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

### Complexity
- Time: O(log(m*n)) = O(log m + log n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The matrix properties guarantee that if we flatten it to a 1D array, it would be fully sorted. We can leverage this without actually flattening by computing the row and column from a 1D index.

### Index Conversion

For a matrix with n columns:
- 1D index `idx` maps to row `idx // n`, column `idx % n`
- For example, in a 3x4 matrix, index 7 maps to row 7//4=1, col 7%4=3

### Alternative: Two Binary Searches

First find the row, then search within that row:

```python
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])

    # Binary search for the correct row
    top, bottom = 0, m - 1
    while top <= bottom:
        mid = (top + bottom) // 2
        if matrix[mid][0] > target:
            bottom = mid - 1
        elif matrix[mid][n - 1] < target:
            top = mid + 1
        else:
            # Target could be in this row
            break
    else:
        return False  # No valid row found

    row = (top + bottom) // 2

    # Binary search within the row
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

This is O(log m + log n), same asymptotic complexity.

### Alternative: Staircase Search (O(m + n))

Start from top-right or bottom-left corner:

```python
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # Start from top-right

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False
```

This is O(m + n), worse than binary search but works even if the matrix is only row-sorted and column-sorted (Search a 2D Matrix II).

### Edge Cases
- Empty matrix: return False
- Single element: check if it equals target
- Target smaller than all elements: binary search goes to left = 0, returns False
- Target larger than all elements: binary search exceeds right, returns False

### Related Problems
- Search a 2D Matrix II: matrix where each row and column is sorted (staircase search)
- Kth Smallest Element in a Sorted Matrix: different property, requires heap/binary search on value
