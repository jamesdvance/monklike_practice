# Decode Ways

## Summary

A message containing letters A-Z is encoded as numbers 1-26. Given a string of digits, return the number of ways to decode it.

### Key Points
- Single digit (1-9) is valid
- Two digits (10-26) is valid
- Leading zeros are invalid
- dp[i] depends on dp[i-1] and dp[i-2]

### Optimal Approach
Bottom-up DP with constant space.

```python
def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    prev2, prev1 = 1, 1  # dp[i-2], dp[i-1]

    for i in range(1, len(s)):
        curr = 0

        # Single digit decode
        if s[i] != '0':
            curr += prev1

        # Two digit decode
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2

        prev2, prev1 = prev1, curr

    return prev1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

At each position, we can decode:
1. Current digit as a single letter (if not '0')
2. Previous digit + current digit as one letter (if 10-26)

### State Definition

dp[i] = number of ways to decode s[0:i+1]

### Recurrence

```
dp[i] = 0
if s[i] != '0':
    dp[i] += dp[i-1]  # Decode current digit alone
if 10 <= int(s[i-1:i+1]) <= 26:
    dp[i] += dp[i-2]  # Decode two digits together
```

### Full DP Array Approach

```python
def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has one way
    dp[1] = 1  # First character (non-zero)

    for i in range(2, n + 1):
        # Single digit
        if s[i-1] != '0':
            dp[i] += dp[i-1]

        # Two digits
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]

    return dp[n]
```

### Step-by-Step Example

```
s = "226"

dp[0] = 1 (base case)
dp[1] = 1 (s[0]='2' is valid)

i = 2 (s[1] = '2'):
  Single: '2' != '0', dp[2] += dp[1] = 1
  Two: '22' = 22, valid, dp[2] += dp[0] = 2

i = 3 (s[2] = '6'):
  Single: '6' != '0', dp[3] += dp[2] = 2
  Two: '26' = 26, valid, dp[3] += dp[1] = 3

Answer: 3

Decodings: "BZ" (2,26), "VF" (22,6), "BBF" (2,2,6)
```

### Handling Zeros

'0' cannot be decoded alone, only as part of "10" or "20".

```
s = "10"
dp[1] = 1 ('1')
dp[2]:
  Single: '0' is invalid, no addition
  Two: '10' = 10, valid, dp[2] = dp[0] = 1

Answer: 1 (only "J")
```

### Invalid Cases

```
s = "06" -> starts with 0, return 0
s = "100" -> no valid decoding for last 0
s = "30" -> 30 > 26, and 0 alone is invalid
```

### Top-Down with Memoization

```python
def numDecodings(s: str) -> int:
    memo = {}

    def dp(i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i in memo:
            return memo[i]

        result = dp(i + 1)

        if i + 1 < len(s) and int(s[i:i+2]) <= 26:
            result += dp(i + 2)

        memo[i] = result
        return result

    return dp(0)
```

### Edge Cases
- Empty string: return 0
- Starts with '0': return 0
- Contains "00": return 0
- Single digit: return 1 (if not '0')

### Related Problems
- Decode Ways II: includes '*' wildcard
- Climbing Stairs: similar structure
- Number of Ways to Separate Numbers: harder variant
