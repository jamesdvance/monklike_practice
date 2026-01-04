# Palindrome Partitioning

## Summary

Given a string `s`, partition it such that every substring is a palindrome. Return all possible palindrome partitionings.

### Key Points
- Try all possible first cuts, check if prefix is palindrome
- Recursively partition the remainder
- Each partition is a valid sequence of palindromic substrings

### Optimal Approach
Backtracking with palindrome checking at each cut.

```python
def partition(s: str) -> list[list[str]]:
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return

        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                current.append(prefix)
                backtrack(end, current)
                current.pop()

    backtrack(0, [])
    return result
```

### Complexity
- Time: O(n * 2^n) - 2^n possible partitions, each palindrome check is O(n)
- Space: O(n) for recursion depth

---

## Detailed Explanation

### Problem Analysis

We need to partition the string into substrings where each is a palindrome. At each position, we try all possible "cuts" - if the prefix from current position to cut is a palindrome, we recurse on the remainder.

### Decision Tree

For s = "aab":

```
                    "aab"
                   /     \
              "a"|"ab"  "aa"|"b"
               /          |
          "a"|"b"      ["aa","b"]
            |
        ["a","a","b"]
```

Only valid paths lead to results: ["a","a","b"] and ["aa","b"]

### Optimization: Precompute Palindromes

Use dynamic programming to precompute which substrings are palindromes:

```python
def partition(s: str) -> list[list[str]]:
    n = len(s)

    # dp[i][j] = True if s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True

    result = []

    def backtrack(start, current):
        if start == n:
            result.append(current[:])
            return

        for end in range(start, n):
            if dp[start][end]:
                current.append(s[start:end + 1])
                backtrack(end + 1, current)
                current.pop()

    backtrack(0, [])
    return result
```

This makes palindrome checking O(1) instead of O(n).

### Step-by-Step Example

s = "aab"

```
backtrack(0, [])
  end=0: "a" is palindrome
    backtrack(1, ["a"])
      end=1: "a" is palindrome
        backtrack(2, ["a","a"])
          end=2: "b" is palindrome
            backtrack(3, ["a","a","b"])
              start=3=len(s), add ["a","a","b"]
      end=2: "ab" not palindrome, skip
  end=1: "aa" is palindrome
    backtrack(2, ["aa"])
      end=2: "b" is palindrome
        backtrack(3, ["aa","b"])
          start=3=len(s), add ["aa","b"]
  end=2: "aab" not palindrome, skip

Result: [["a","a","b"], ["aa","b"]]
```

### Why Every String Has at Least One Partition?

Every single character is a palindrome. So the partition where each character is its own substring is always valid.

### Edge Cases
- Single character: return [["c"]]
- Already a palindrome: includes the whole string as one option
- No multi-character palindromes: return single-char partition only

### Related Problems
- Palindrome Partitioning II: minimum cuts needed
- Longest Palindromic Substring: find single longest
- Palindromic Substrings: count all palindromic substrings
