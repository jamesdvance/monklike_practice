# Coin Change II

## Summary

Given coin denominations and an amount, return the number of combinations to make that amount. Each coin can be used unlimited times.

### Key Points
- Unlike Coin Change (min coins), this counts combinations
- Order doesn't matter: [1,2] and [2,1] are the same combination
- Iterate coins first, then amounts

### Optimal Approach
Bottom-up DP iterating coins first.

```python
def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make amount 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
```

### Complexity
- Time: O(amount * n) where n is number of coins
- Space: O(amount)

---

## Detailed Explanation

### Problem Analysis

We want combinations, not permutations. The key is to process one coin at a time:
- With coin c, for each amount, add ways to make (amount - c)
- Since we process coins in order, we only count each combination once

### Why Coins First?

**Coins first (combinations)**:
```
dp = [1, 0, 0, 0, 0]

Coin 1: dp = [1, 1, 1, 1, 1]  # Only using 1s
Coin 2: dp = [1, 1, 2, 2, 3]  # Adding combinations with 2
```

For amount 4: [1,1,1,1], [1,1,2], [2,2] = 3 combinations

**Amount first (permutations)**:
```
For each amount, try all coins -> counts [1,2] and [2,1] separately
```

### State Definition

dp[i] = number of combinations to make amount i

### Recurrence

For each coin c:
  dp[i] += dp[i - c] for i from c to amount

### Full 2D DP

```python
def change(amount: int, coins: list[int]) -> int:
    n = len(coins)
    # dp[i][j] = ways to make amount j using first i coins
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1  # One way to make 0

    for i in range(1, n + 1):
        for j in range(amount + 1):
            # Don't use coin i
            dp[i][j] = dp[i-1][j]
            # Use coin i (can use multiple times)
            if j >= coins[i-1]:
                dp[i][j] += dp[i][j - coins[i-1]]

    return dp[n][amount]
```

### Step-by-Step Example

```
amount = 5, coins = [1, 2, 5]

dp = [1, 0, 0, 0, 0, 0]

Coin 1:
  i=1: dp[1] = 0 + dp[0] = 1
  i=2: dp[2] = 0 + dp[1] = 1
  i=3: dp[3] = 0 + dp[2] = 1
  i=4: dp[4] = 0 + dp[3] = 1
  i=5: dp[5] = 0 + dp[4] = 1
  dp = [1, 1, 1, 1, 1, 1]

Coin 2:
  i=2: dp[2] = 1 + dp[0] = 2
  i=3: dp[3] = 1 + dp[1] = 2
  i=4: dp[4] = 1 + dp[2] = 3
  i=5: dp[5] = 1 + dp[3] = 3
  dp = [1, 1, 2, 2, 3, 3]

Coin 5:
  i=5: dp[5] = 3 + dp[0] = 4
  dp = [1, 1, 2, 2, 3, 4]

Answer: 4
```

Combinations: [1,1,1,1,1], [1,1,1,2], [1,2,2], [5]

### Top-Down with Memoization

```python
def change(amount: int, coins: list[int]) -> int:
    memo = {}

    def dp(i, remaining):
        if remaining == 0:
            return 1
        if remaining < 0 or i >= len(coins):
            return 0
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        # Skip coin i OR use coin i (stay at i for unlimited use)
        result = dp(i + 1, remaining) + dp(i, remaining - coins[i])
        memo[(i, remaining)] = result
        return result

    return dp(0, amount)
```

### Difference from Coin Change

| Aspect | Coin Change | Coin Change II |
|--------|-------------|----------------|
| Goal | Minimum coins | Count combinations |
| dp[i] means | Min coins for i | Ways to make i |
| Iteration | Any order | Coins first |
| Initial | dp[0]=0, rest=inf | dp[0]=1, rest=0 |

### Edge Cases
- amount = 0: return 1 (empty combination)
- No coins: return 0 if amount > 0
- Single coin: return 1 if divisible, else 0

### Related Problems
- Coin Change: find minimum coins
- Combination Sum IV: count permutations (order matters)
- Perfect Squares: coins are perfect squares
