# Regular Expression Matching

## Summary

Implement regular expression matching with '.' (matches any single character) and '*' (matches zero or more of the preceding element).

### Key Points
- '.' matches any single character
- '*' modifies the previous character (zero or more occurrences)
- dp[i][j] = does s[0:i] match p[0:j]?

### Optimal Approach
2D DP handling the '*' cases carefully.

```python
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c* that can match empty string
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # Zero occurrences of preceding element
                dp[i][j] = dp[i][j - 2]

                # One or more occurrences
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                # Direct match or '.'
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]
```

### Complexity
- Time: O(m * n)
- Space: O(m * n)

---

## Detailed Explanation

### Problem Analysis

The '*' is the tricky part. It means:
- Zero occurrences: ignore the preceding character and '*'
- One or more: match one character and stay at '*' (greedy)

### State Definition

dp[i][j] = True if s[0:i] matches p[0:j]

### Cases for Transition

1. **p[j-1] is a normal character or '.'**:
   - Match if characters equal (or '.') and dp[i-1][j-1] is True

2. **p[j-1] is '*'**:
   - Zero occurrences: dp[i][j-2] (skip x* entirely)
   - One+ occurrences: dp[i-1][j] if x matches s[i-1]

### Why dp[i-1][j] for One+ Occurrences?

If x* can match s[i-1]:
- We've "used" one x from x*
- But x* can still match more, so we stay at column j
- This is like saying: "x* matched s[i-1], can it match s[0:i-1] too?"

### Step-by-Step Example

```
s = "aab", p = "c*a*b"

       ""  c   *   a   *   b
   ""   T  F   T   F   T   F
   a    F  F   F   T   T   F
   a    F  F   F   F   T   F
   b    F  F   F   F   F   T

dp[0][2]: p="c*" can match "" (zero c's) -> T
dp[0][4]: p="c*a*" can match "" -> T
dp[1][3]: p="c*a" vs s="a" -> c* matches "", a matches a -> T
dp[1][4]: p="c*a*" vs s="a" -> c*a* matches a -> T
dp[2][4]: p="c*a*" vs s="aa" -> c* is "", a* matches "aa" -> T
dp[3][5]: p="c*a*b" vs s="aab" -> T

Answer: True
```

### Top-Down with Memoization

```python
def isMatch(s: str, p: str) -> bool:
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == len(p):
            return i == len(s)

        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

        if j + 1 < len(p) and p[j + 1] == '*':
            # Zero occurrences OR one+ occurrences
            result = dp(i, j + 2) or (first_match and dp(i + 1, j))
        else:
            result = first_match and dp(i + 1, j + 1)

        memo[(i, j)] = result
        return result

    return dp(0, 0)
```

### Edge Cases Handled

1. **Empty pattern**: matches only empty string
2. **Pattern ".*"**: matches any string (including empty)
3. **Pattern "a*"**: matches "", "a", "aa", etc.
4. **Pattern "ab*"**: matches "a", "ab", "abb", etc.
5. **Pattern ".*.*"**: redundant but valid

### Common Mistakes

1. Forgetting that '*' applies to PRECEDING element
2. Not handling "x*" at the start matching empty string
3. Confusing when to use dp[i-1][j] vs dp[i][j-2]

### Space Optimization

```python
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    prev = [False] * (n + 1)
    prev[0] = True

    for j in range(2, n + 1):
        if p[j - 1] == '*':
            prev[j] = prev[j - 2]

    for i in range(1, m + 1):
        curr = [False] * (n + 1)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                curr[j] = curr[j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    curr[j] = curr[j] or prev[j]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                curr[j] = prev[j - 1]
        prev = curr

    return prev[n]
```

### Related Problems
- Wildcard Matching: '*' matches any sequence directly
- Edit Distance: string transformation
- Distinct Subsequences: counting matches
