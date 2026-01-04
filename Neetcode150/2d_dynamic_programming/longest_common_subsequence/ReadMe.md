# Longest Common Subsequence

## Summary

Given two strings, return the length of their longest common subsequence. A subsequence is derived by deleting some or no elements without changing order.

### Key Points
- If characters match, extend LCS by 1
- If not, take max of excluding either character
- Classic 2D DP on two strings

### Optimal Approach
2D DP with space optimization.

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # Ensure text2 is shorter for space optimization
    if m < n:
        text1, text2 = text2, text1
        m, n = n, m

    prev = [0] * (n + 1)

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr

    return prev[n]
```

### Complexity
- Time: O(m * n)
- Space: O(min(m, n))

---

## Detailed Explanation

### Problem Analysis

For strings text1[0:i] and text2[0:j]:
- If text1[i-1] == text2[j-1]: LCS includes this character
- Otherwise: LCS is max of excluding either last character

### State Definition

dp[i][j] = length of LCS of text1[0:i] and text2[0:j]

### Recurrence

```
if text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

### Full 2D DP

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
```

### Step-by-Step Example

```
text1 = "abcde", text2 = "ace"

    ""  a  c  e
""   0  0  0  0
a    0  1  1  1
b    0  1  1  1
c    0  1  2  2
d    0  1  2  2
e    0  1  2  3

Answer: 3 (LCS = "ace")
```

### Top-Down with Memoization

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    memo = {}

    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        if text1[i - 1] == text2[j - 1]:
            result = dp(i - 1, j - 1) + 1
        else:
            result = max(dp(i - 1, j), dp(i, j - 1))

        memo[(i, j)] = result
        return result

    return dp(len(text1), len(text2))
```

### Reconstructing the LCS

```python
def longestCommonSubsequence(text1: str, text2: str) -> str:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find actual LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))
```

### Edge Cases
- One string empty: LCS = 0
- Identical strings: LCS = length of string
- No common characters: LCS = 0

### Related Problems
- Edit Distance: minimum operations to transform
- Shortest Common Supersequence: combine both strings
- Longest Palindromic Subsequence: LCS of string and its reverse
