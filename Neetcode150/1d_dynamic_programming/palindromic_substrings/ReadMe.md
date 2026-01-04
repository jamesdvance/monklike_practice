# Palindromic Substrings

## Summary

Given a string s, return the number of palindromic substrings in it. A substring is a contiguous sequence of characters.

### Key Points
- Same approach as Longest Palindromic Substring
- Expand around center for each position
- Count palindromes instead of tracking longest

### Optimal Approach
Expand around each center, counting palindromes found.

```python
def countSubstrings(s: str) -> int:
    count = 0

    def expand(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)      # Odd length
        expand(i, i + 1)  # Even length

    return count
```

### Complexity
- Time: O(n^2)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Every palindrome has a center. For each center, we can expand outward and count how many palindromes we find before hitting a mismatch.

### Why Count During Expansion?

Each valid expansion is a new palindrome:
- Start: "a" (length 1)
- Expand: "bab" (length 3)
- Expand: "cbabc" (length 5)

Each step is a distinct palindrome.

### DP Approach

```python
def countSubstrings(s: str) -> int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    # Single characters
    for i in range(n):
        dp[i][i] = True
        count += 1

    # Two characters
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1

    # Length 3 and above
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1

    return count
```

Time: O(n^2), Space: O(n^2)

### Manacher's Algorithm (O(n))

```python
def countSubstrings(s: str) -> int:
    # Transform
    t = '^#' + '#'.join(s) + '#$'
    n = len(t)
    p = [0] * n

    center = right = 0
    for i in range(1, n - 1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])

        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    # Count: each p[i] represents (p[i] + 1) // 2 palindromes in original string
    return sum((radius + 1) // 2 for radius in p)
```

### Step-by-Step Example

```
s = "abc"

Center at 0 ('a'):
  Odd: "a" -> count = 1
  Even: "ab" -> mismatch

Center at 1 ('b'):
  Odd: "b" -> count = 2
  Even: "bc" -> mismatch

Center at 2 ('c'):
  Odd: "c" -> count = 3
  Even: out of bounds

Answer: 3 (palindromes: "a", "b", "c")
```

### Example with Multiple Palindromes

```
s = "aaa"

Center at 0:
  Odd: "a" -> count = 1
  Even: "aa" -> count = 2

Center at 1:
  Odd: "a" -> "aaa" -> count = 4
  Even: "aa" -> count = 5

Center at 2:
  Odd: "a" -> count = 6
  Even: out of bounds

Answer: 6 (palindromes: "a", "a", "a", "aa", "aa", "aaa")
```

### Edge Cases
- Single character: return 1
- All same characters: n*(n+1)/2 palindromes
- No repeated characters: n palindromes

### Related Problems
- Longest Palindromic Substring: find longest instead of count
- Longest Palindromic Subsequence: not contiguous
- Palindrome Partitioning: partition into palindromes
