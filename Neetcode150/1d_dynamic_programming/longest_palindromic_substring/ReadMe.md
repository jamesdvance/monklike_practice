# Longest Palindromic Substring

## Summary

Given a string s, return the longest palindromic substring in s.

### Key Points
- Expand around center for each position
- Two cases: odd length (single center) and even length (two centers)
- Track start and length of longest found

### Optimal Approach
Expand around each center.

```python
def longestPalindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0

    for i in range(len(s)):
        # Odd length palindrome
        l1, r1 = expand(i, i)
        if r1 - l1 > end - start:
            start, end = l1, r1

        # Even length palindrome
        l2, r2 = expand(i, i + 1)
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]
```

### Complexity
- Time: O(n^2)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

A palindrome reads the same forwards and backwards. Every palindrome has a center:
- Odd length: single character center (e.g., "aba" centers on 'b')
- Even length: between two characters (e.g., "abba" centers between 'b's)

### Expand Around Center

For each potential center:
1. Start with the center character(s)
2. Expand outward while characters match
3. Record if longer than previous best

### DP Approach

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    # dp[i][j] = True if s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]

    start, max_len = 0, 1

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

            if dp[i][j] and length > max_len:
                start = i
                max_len = length

    return s[start:start + max_len]
```

Time: O(n^2), Space: O(n^2)

### Manacher's Algorithm (O(n))

Advanced algorithm using symmetry properties:

```python
def longestPalindrome(s: str) -> str:
    # Transform: "abc" -> "^#a#b#c#$"
    t = '^#' + '#'.join(s) + '#$'
    n = len(t)
    p = [0] * n  # p[i] = radius of palindrome centered at i

    center = right = 0

    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])

        # Expand
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Update center and right boundary
        if i + p[i] > right:
            center, right = i, i + p[i]

    # Find maximum
    max_len, center_idx = max((p[i], i) for i in range(1, n - 1))
    start = (center_idx - max_len) // 2

    return s[start:start + max_len]
```

### Step-by-Step Example

```
s = "babad"

Expand from index 0 ('b'):
  Odd: "b" -> no expansion
  Even: "ba" -> not palindrome

Expand from index 1 ('a'):
  Odd: "a" -> expand to "bab" -> stop
  Length 3, update result

Expand from index 2 ('b'):
  Odd: "b" -> expand to "aba" -> stop
  Length 3, same as before

Expand from index 3 ('a'):
  Odd: "a" -> no expansion
  Even: "ad" -> not palindrome

Expand from index 4 ('d'):
  Odd: "d" -> no expansion

Answer: "bab" (or "aba")
```

### Edge Cases
- Single character: return that character
- All same characters: return entire string
- No palindrome longer than 1: return first character

### Related Problems
- Palindromic Substrings: count all palindromes
- Longest Palindromic Subsequence: subsequence, not substring
- Shortest Palindrome: add characters to front
