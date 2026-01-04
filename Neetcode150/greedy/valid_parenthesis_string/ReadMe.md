# Valid Parenthesis String

## Summary

Given a string with '(', ')', and '*', where '*' can be '(', ')', or empty, determine if the string is valid (properly matched parentheses).

### Key Points
- '*' provides flexibility - track range of possible open counts
- Track minimum and maximum possible open parentheses
- Valid if we can reach 0 open at the end

### Optimal Approach
Track range of possible open counts.

```python
def checkValidString(s: str) -> bool:
    low = 0   # Minimum possible open count
    high = 0  # Maximum possible open count

    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            low = max(0, low - 1)
            high -= 1
        else:  # c == '*'
            low = max(0, low - 1)  # '*' as ')'
            high += 1              # '*' as '('

        if high < 0:
            return False

    return low == 0
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Without '*', we just count: +1 for '(', -1 for ')'. Valid if count ends at 0 and never goes negative.

With '*', we have choices. We track the range [low, high] of possible open counts.

### The Range Intuition

- low: minimum opens if we use '*' greedily as ')' or empty
- high: maximum opens if we use '*' greedily as '('

As long as 0 is within [low, high] at the end, we're valid.

### Why low = max(0, low - 1)?

We could treat '*' as empty (no change) or ')' (decrease). But we can't go below 0 opens (negative means too many ')' with no fix).

### Step-by-Step Example

```
s = "(*))"

i=0 '(': low=1, high=1
i=1 '*': low=max(0,0)=0, high=2
i=2 ')': low=max(0,-1)=0, high=1
i=3 ')': low=max(0,-1)=0, high=0

low == 0, high >= 0 -> True
```

Possible interpretations:
- "(()" -> invalid, but with * as ')': "()" + "))" -> "(())" valid!

### DP Approach

```python
def checkValidString(s: str) -> bool:
    n = len(s)
    # dp[i][j] = can we reach j open parens after processing s[0:i]?
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(n + 1):
            if not dp[i][j]:
                continue

            if s[i] == '(':
                if j + 1 <= n:
                    dp[i + 1][j + 1] = True
            elif s[i] == ')':
                if j > 0:
                    dp[i + 1][j - 1] = True
            else:  # '*'
                dp[i + 1][j] = True          # empty
                if j + 1 <= n:
                    dp[i + 1][j + 1] = True  # as '('
                if j > 0:
                    dp[i + 1][j - 1] = True  # as ')'

    return dp[n][0]
```

Time: O(n^2), Space: O(n^2)

### Two-Pass Approach

```python
def checkValidString(s: str) -> bool:
    # Left to right: treat '*' as '('
    open_count = 0
    for c in s:
        if c == '(' or c == '*':
            open_count += 1
        else:
            open_count -= 1
        if open_count < 0:
            return False

    # Right to left: treat '*' as ')'
    close_count = 0
    for c in reversed(s):
        if c == ')' or c == '*':
            close_count += 1
        else:
            close_count -= 1
        if close_count < 0:
            return False

    return True
```

First pass: ensure we never have too many ')' (by being generous with '(').
Second pass: ensure we never have too many '(' (by being generous with ')').

### Example Analysis

```
s = "(*)"

Forward pass: ( -> 1, * (as () -> 2, ) -> 1. OK
Backward pass: ) -> 1, * (as )) -> 2, ( -> 1. OK

Answer: True

Interpretations: "()" (empty *), "(())" (as '('), "())" invalid, but "()" valid!
```

### Edge Cases
- Empty string: True
- All '*': True (all empty)
- "(((": False (no way to close)
- ")))": False (unmatched close)

### Related Problems
- Valid Parentheses: without '*'
- Longest Valid Parentheses: find longest valid substring
- Remove Invalid Parentheses: minimum removals
