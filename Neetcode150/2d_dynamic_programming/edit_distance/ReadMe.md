# Edit Distance

## Summary

Given two strings word1 and word2, return the minimum number of operations to convert word1 to word2. Operations are: insert, delete, or replace a character.

### Key Points
- Classic string DP problem
- Three choices at each mismatch: insert, delete, replace
- dp[i][j] = min operations for word1[0:i] to word2[0:j]

### Optimal Approach
2D DP with space optimization.

```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j],      # delete
                                  curr[j - 1],   # insert
                                  prev[j - 1])   # replace
        prev = curr

    return prev[n]
```

### Complexity
- Time: O(m * n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

To transform word1[0:i] to word2[0:j]:
- If characters match: no operation needed, use previous result
- If they don't match, try all three operations:
  - Insert: transform word1[0:i] to word2[0:j-1], then insert word2[j-1]
  - Delete: transform word1[0:i-1] to word2[0:j], deleting word1[i-1]
  - Replace: transform word1[0:i-1] to word2[0:j-1], replace word1[i-1]

### State Definition

dp[i][j] = minimum operations to convert word1[0:i] to word2[0:j]

### Recurrence

```
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = 1 + min(dp[i-1][j],    # delete
                       dp[i][j-1],     # insert
                       dp[i-1][j-1])   # replace
```

### Full 2D DP

```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # delete
                                   dp[i][j - 1],       # insert
                                   dp[i - 1][j - 1])   # replace

    return dp[m][n]
```

### Step-by-Step Example

```
word1 = "horse", word2 = "ros"

       ""  r  o  s
   ""   0  1  2  3
   h    1  1  2  3
   o    2  2  1  2
   r    3  2  2  2
   s    4  3  3  2
   e    5  4  4  3

At dp[3][1] (word1="hor", word2="r"):
  word1[2]='r' == word2[0]='r'
  dp[3][1] = dp[2][0] = 2

At dp[5][3] (word1="horse", word2="ros"):
  word1[4]='e' != word2[2]='s'
  dp[5][3] = 1 + min(dp[4][3], dp[5][2], dp[4][2])
           = 1 + min(2, 4, 3) = 3

Answer: 3
```

Operations: horse -> rorse (replace h with r) -> rose (delete r) -> ros (delete e)

### Top-Down with Memoization

```python
def minDistance(word1: str, word2: str) -> int:
    memo = {}

    def dp(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if (i, j) in memo:
            return memo[(i, j)]

        if word1[i - 1] == word2[j - 1]:
            result = dp(i - 1, j - 1)
        else:
            result = 1 + min(dp(i - 1, j),      # delete
                             dp(i, j - 1),       # insert
                             dp(i - 1, j - 1))   # replace

        memo[(i, j)] = result
        return result

    return dp(len(word1), len(word2))
```

### Reconstructing the Operations

```python
def minDistanceWithPath(word1: str, word2: str):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # Backtrack
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Delete {word1[i - 1]}")
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(f"Insert {word2[j - 1]}")
            j -= 1
        else:
            operations.append(f"Replace {word1[i - 1]} with {word2[j - 1]}")
            i -= 1
            j -= 1

    return dp[m][n], operations[::-1]
```

### Edge Cases
- Empty word1: insert all of word2
- Empty word2: delete all of word1
- Identical words: 0 operations

### Related Problems
- One Edit Distance: check if exactly one edit apart
- Delete Operation for Two Strings: only deletions allowed
- Minimum ASCII Delete Sum: weighted deletions
