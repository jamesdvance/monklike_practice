# Unique Paths

## Summary

A robot is at the top-left corner of an m x n grid and can only move right or down. Count the number of unique paths to reach the bottom-right corner.

### Key Points
- Classic 2D DP problem
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Can optimize to O(n) space

### Optimal Approach
Use 1D DP with rolling row.

```python
def uniquePaths(m: int, n: int) -> int:
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[n - 1]
```

### Complexity
- Time: O(m * n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

To reach cell (i, j), the robot must come from either:
- Cell (i-1, j) - above
- Cell (i, j-1) - left

Total paths = paths from above + paths from left.

### State Definition

dp[i][j] = number of unique paths to reach cell (i, j)

### Recurrence

dp[i][j] = dp[i-1][j] + dp[i][j-1]

### Base Cases

- First row: dp[0][j] = 1 (only way is moving right)
- First column: dp[i][0] = 1 (only way is moving down)

### Full 2D DP

```python
def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
```

### Why 1D Works

When filling dp[j], we need:
- dp[j] from previous row (still in dp[j] before update)
- dp[j-1] from current row (already updated)

So we can reuse the same array.

### Step-by-Step Example

```
m = 3, n = 7

Initial: dp = [1, 1, 1, 1, 1, 1, 1]

Row 1:
  j=1: dp[1] = 1 + 1 = 2
  j=2: dp[2] = 1 + 2 = 3
  j=3: dp[3] = 1 + 3 = 4
  ...
  dp = [1, 2, 3, 4, 5, 6, 7]

Row 2:
  j=1: dp[1] = 2 + 1 = 3
  j=2: dp[2] = 3 + 3 = 6
  j=3: dp[3] = 4 + 6 = 10
  ...
  dp = [1, 3, 6, 10, 15, 21, 28]

Answer: 28
```

### Mathematical Solution

The answer is a combinatorial formula:
- Total moves: (m-1) down + (n-1) right = m+n-2 moves
- Choose which (m-1) are down (or which (n-1) are right)

```python
from math import comb

def uniquePaths(m: int, n: int) -> int:
    return comb(m + n - 2, m - 1)
```

Or without library:
```python
def uniquePaths(m: int, n: int) -> int:
    # C(m+n-2, m-1) = (m+n-2)! / ((m-1)! * (n-1)!)
    result = 1
    for i in range(1, m):
        result = result * (n - 1 + i) // i
    return result
```

### Top-Down with Memoization

```python
def uniquePaths(m: int, n: int) -> int:
    memo = {}

    def dp(i, j):
        if i == 0 or j == 0:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]

        memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
        return memo[(i, j)]

    return dp(m - 1, n - 1)
```

### Edge Cases
- 1 x n or m x 1: only 1 path
- 1 x 1: return 1
- Large grids: combinatorial formula is fastest

### Related Problems
- Unique Paths II: with obstacles
- Minimum Path Sum: find min cost path
- Dungeon Game: more complex constraints
