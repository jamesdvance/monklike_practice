# Burst Balloons

## Summary

Given n balloons with numbers, bursting balloon i gives coins nums[i-1] * nums[i] * nums[i+1]. Find the maximum coins by bursting all balloons.

### Key Points
- Think of which balloon to burst LAST in a range
- dp[i][j] = max coins for bursting all balloons between i and j
- Add virtual balloons with value 1 at boundaries

### Optimal Approach
Interval DP - think in terms of last balloon burst.

```python
def maxCoins(nums: list[int]) -> int:
    # Add boundary balloons
    nums = [1] + nums + [1]
    n = len(nums)

    dp = [[0] * n for _ in range(n)]

    # Length of interval (excluding boundaries)
    for length in range(1, n - 1):
        for left in range(0, n - length - 1):
            right = left + length + 1

            # Try each balloon as the last to burst
            for k in range(left + 1, right):
                coins = nums[left] * nums[k] * nums[right]
                coins += dp[left][k] + dp[k][right]
                dp[left][right] = max(dp[left][right], coins)

    return dp[0][n - 1]
```

### Complexity
- Time: O(n^3)
- Space: O(n^2)

---

## Detailed Explanation

### Problem Analysis

The key insight is to think backwards: instead of "which balloon to burst first," think "which balloon to burst LAST" in a given range.

If balloon k is the last to burst in range (i, j):
- All other balloons in (i, j) are already burst
- So balloon k is adjacent to boundaries i and j
- Coins = nums[i] * nums[k] * nums[j] + (coins from left) + (coins from right)

### Why Think Backwards?

Forward thinking is hard because:
- Bursting balloon i changes the neighbors
- The subproblems overlap in complex ways

Backward thinking (last burst) works because:
- When k is the last, its neighbors are i and j (boundaries)
- Subproblems (i, k) and (k, j) are independent

### State Definition

dp[i][j] = maximum coins from bursting all balloons STRICTLY between indices i and j

### Recurrence

For each k in range (i+1, j-1) as the last balloon:
```
dp[i][j] = max(dp[i][j],
               nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
```

### Step-by-Step Example

```
nums = [3, 1, 5, 8]
Modified: [1, 3, 1, 5, 8, 1]
Indices:   0  1  2  3  4  5

Length 1 (single balloon between boundaries):
dp[0][2]: burst 1 last -> 1*3*1 = 3
dp[1][3]: burst 2 last -> 3*1*5 = 15
dp[2][4]: burst 3 last -> 1*5*8 = 40
dp[3][5]: burst 4 last -> 5*8*1 = 40

Length 2:
dp[0][3]:
  k=1: 1*3*5 + dp[0][1] + dp[1][3] = 15 + 0 + 15 = 30
  k=2: 1*1*5 + dp[0][2] + dp[2][3] = 5 + 3 + 0 = 8
  dp[0][3] = 30

dp[1][4]:
  k=2: 3*1*8 + dp[1][2] + dp[2][4] = 24 + 0 + 40 = 64
  k=3: 3*5*8 + dp[1][3] + dp[3][4] = 120 + 15 + 0 = 135
  dp[1][4] = 135

dp[2][5]:
  k=3: 1*5*1 + dp[2][3] + dp[3][5] = 5 + 0 + 40 = 45
  k=4: 1*8*1 + dp[2][4] + dp[4][5] = 8 + 40 + 0 = 48
  dp[2][5] = 48

Length 3:
dp[0][4]:
  k=1: 1*3*8 + 0 + 135 = 159
  k=2: 1*1*8 + 3 + 135 = 146
  k=3: 1*5*8 + 30 + 0 = 70
  dp[0][4] = 159

Continue to dp[0][5] = 167
```

### Top-Down with Memoization

```python
def maxCoins(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    memo = {}

    def dp(left, right):
        if left + 1 >= right:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]

        result = 0
        for k in range(left + 1, right):
            coins = nums[left] * nums[k] * nums[right]
            coins += dp(left, k) + dp(k, right)
            result = max(result, coins)

        memo[(left, right)] = result
        return result

    return dp(0, n - 1)
```

### Why Add Boundary 1s?

When we burst a balloon at the edge, its neighbor becomes the boundary. By adding virtual balloons with value 1, we handle this uniformly.

### Edge Cases
- Single balloon: just burst it, coins = 1 * nums[0] * 1 = nums[0]
- Two balloons: try both orders
- All 1s: order doesn't matter

### Related Problems
- Minimum Cost to Merge Stones: similar interval DP
- Palindrome Partitioning II: interval DP for strings
- Strange Printer: interval DP with printing
