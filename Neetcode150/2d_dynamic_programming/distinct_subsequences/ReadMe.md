# Distinct Subsequences

## Summary

Given two strings s and t, return the number of distinct subsequences of s which equal t. A subsequence is derived by deleting some or no characters.

### Key Points
- If characters match, we can use it or skip it
- If characters don't match, we must skip s's character
- dp[i][j] = ways to form t[0:j] from s[0:i]

### Optimal Approach
2D DP with space optimization.

```python
def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)

    if m < n:
        return 0

    # dp[j] = ways to form t[0:j]
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty t can always be formed

    for i in range(1, m + 1):
        # Iterate backwards to avoid using updated values
        for j in range(min(i, n), 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]

    return dp[n]
```

### Complexity
- Time: O(m * n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

For each character in s, we decide: use it to match t, or skip it.

- If s[i] == t[j]: we can use it (consume both) OR skip s[i]
- If s[i] != t[j]: we must skip s[i]

### State Definition

dp[i][j] = number of ways to form t[0:j] using s[0:i]

### Recurrence

```
if s[i-1] == t[j-1]:
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # (use s[i-1] to match) + (skip s[i-1])
else:
    dp[i][j] = dp[i-1][j]
    # skip s[i-1]
```

### Full 2D DP

```python
def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Empty t can be formed from any prefix of s
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]
```

### Step-by-Step Example

```
s = "rabbbit", t = "rabbit"

       ""  r  a  b  b  i  t
   ""   1  0  0  0  0  0  0
   r    1  1  0  0  0  0  0
   a    1  1  1  0  0  0  0
   b    1  1  1  1  0  0  0
   b    1  1  1  2  1  0  0
   b    1  1  1  3  3  0  0
   i    1  1  1  3  3  3  0
   t    1  1  1  3  3  3  3

At dp[5][4] (s="rabbb", t="rabb"):
  s[4]='b' == t[3]='b'
  dp[5][4] = dp[4][3] + dp[4][4] = 2 + 1 = 3

Answer: 3
```

### Top-Down with Memoization

```python
def numDistinct(s: str, t: str) -> int:
    memo = {}

    def dp(i, j):
        # Base cases
        if j == 0:
            return 1  # Formed t completely
        if i == 0:
            return 0  # s exhausted but t not formed

        if (i, j) in memo:
            return memo[(i, j)]

        if s[i - 1] == t[j - 1]:
            result = dp(i - 1, j - 1) + dp(i - 1, j)
        else:
            result = dp(i - 1, j)

        memo[(i, j)] = result
        return result

    return dp(len(s), len(t))
```

### Why Iterate Backwards in 1D?

In 1D optimization:
```python
for j in range(min(i, n), 0, -1):
    if s[i-1] == t[j-1]:
        dp[j] += dp[j-1]
```

If we went forward, dp[j-1] would already be updated in the current iteration, using the wrong (current, not previous) value.

### Edge Cases
- t longer than s: return 0
- s equals t: return 1
- Empty t: return 1
- Empty s (non-empty t): return 0

### Related Problems
- Edit Distance: minimum operations
- Longest Common Subsequence: different optimization
- Interleaving String: matching from two sources
