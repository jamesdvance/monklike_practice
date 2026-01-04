# Interleaving String

## Summary

Given strings s1, s2, and s3, determine if s3 is formed by interleaving s1 and s2 while preserving their relative character order.

### Key Points
- Characters from s1 and s2 must appear in order in s3
- dp[i][j] = can we form s3[0:i+j] using s1[0:i] and s2[0:j]?
- At each position, s3's character must come from s1 or s2

### Optimal Approach
2D DP with space optimization.

```python
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)

    if m + n != len(s3):
        return False

    dp = [False] * (n + 1)
    dp[0] = True

    # Initialize first row (using only s2)
    for j in range(1, n + 1):
        dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[n]
```

### Complexity
- Time: O(m * n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

We need to check if s3 can be formed by picking characters alternately from s1 and s2 while maintaining their order.

At position (i, j), we've used i characters from s1 and j from s2, so we're at position i+j in s3.

### State Definition

dp[i][j] = True if s3[0:i+j] can be formed by interleaving s1[0:i] and s2[0:j]

### Recurrence

dp[i][j] is True if:
- dp[i-1][j] and s1[i-1] == s3[i+j-1] (take from s1), OR
- dp[i][j-1] and s2[j-1] == s3[i+j-1] (take from s2)

### Full 2D DP

```python
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # First column (using only s1)
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    # First row (using only s2)
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    # Fill rest
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                       (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[m][n]
```

### Step-by-Step Example

```
s1 = "aab", s2 = "axy", s3 = "aaxaby"

       ""   a    x    y
   ""   T   F    F    F
   a    T   T    F    F
   a    T   T    T    F
   b    F   T    T    T

Check dp[3][3]:
- dp[2][3] and s1[2]='b' == s3[5]='y'? F and F = F
- dp[3][2] and s2[2]='y' == s3[5]='y'? T and T = T

Answer: True
```

### Top-Down with Memoization

```python
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    memo = {}

    def dp(i, j):
        if i == m and j == n:
            return True
        if (i, j) in memo:
            return memo[(i, j)]

        result = False
        k = i + j

        if i < m and s1[i] == s3[k]:
            result = dp(i + 1, j)
        if not result and j < n and s2[j] == s3[k]:
            result = dp(i, j + 1)

        memo[(i, j)] = result
        return result

    return dp(0, 0)
```

### BFS Approach

```python
from collections import deque

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    queue = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
        i, j = queue.popleft()

        if i == m and j == n:
            return True

        k = i + j

        if i < m and s1[i] == s3[k] and (i + 1, j) not in visited:
            visited.add((i + 1, j))
            queue.append((i + 1, j))

        if j < n and s2[j] == s3[k] and (i, j + 1) not in visited:
            visited.add((i, j + 1))
            queue.append((i, j + 1))

    return False
```

### Edge Cases
- One string empty: s3 must equal the other
- Both strings empty: s3 must be empty
- Length mismatch: return False immediately

### Related Problems
- Edit Distance: operations on strings
- Distinct Subsequences: count interleaving patterns
- Scramble String: more complex interleaving
