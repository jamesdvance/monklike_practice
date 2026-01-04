# Coin Change

## Summary

Given an array of coin denominations and an amount, return the minimum number of coins needed to make that amount. Return -1 if impossible.

### Key Points
- Classic unbounded knapsack problem
- dp[i] = minimum coins for amount i
- For each coin, check if using it improves the solution

### Optimal Approach
Bottom-up DP iterating through amounts.

```python
def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

### Complexity
- Time: O(amount * n) where n is number of coin types
- Space: O(amount)

---

## Detailed Explanation

### Problem Analysis

For each amount, we try using each coin and take the minimum:
- If we use coin c, we need 1 + (coins for amount - c)
- We want the minimum across all valid coin choices

### State Definition

dp[i] = minimum number of coins to make amount i

### Recurrence

dp[i] = min(dp[i - coin] + 1) for each coin where coin <= i

### Alternative: Iterate Coins First

```python
def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

This iterates through coins first, then amounts.

### Top-Down with Memoization

```python
def coinChange(coins: list[int], amount: int) -> int:
    memo = {}

    def dp(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        if remaining in memo:
            return memo[remaining]

        result = float('inf')
        for coin in coins:
            result = min(result, dp(remaining - coin) + 1)

        memo[remaining] = result
        return result

    ans = dp(amount)
    return ans if ans != float('inf') else -1
```

### Step-by-Step Example

```
coins = [1, 2, 5], amount = 11

dp[0] = 0
dp[1] = min(dp[0]+1) = 1  (use coin 1)
dp[2] = min(dp[1]+1, dp[0]+1) = 1  (use coin 2)
dp[3] = min(dp[2]+1, dp[1]+1) = 2  (1+2 or 1+1+1)
dp[4] = min(dp[3]+1, dp[2]+1) = 2  (2+2)
dp[5] = min(dp[4]+1, dp[3]+1, dp[0]+1) = 1  (use coin 5)
dp[6] = min(dp[5]+1, dp[4]+1, dp[1]+1) = 2  (5+1)
dp[7] = min(dp[6]+1, dp[5]+1, dp[2]+1) = 2  (5+2)
...
dp[11] = 3  (5+5+1)

Answer: 3
```

### BFS Approach

Think of it as shortest path where each "step" uses one coin:

```python
from collections import deque

def coinChange(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    visited = {0}
    queue = deque([0])
    steps = 0

    while queue:
        steps += 1
        for _ in range(len(queue)):
            curr = queue.popleft()
            for coin in coins:
                new_amount = curr + coin
                if new_amount == amount:
                    return steps
                if new_amount < amount and new_amount not in visited:
                    visited.add(new_amount)
                    queue.append(new_amount)

    return -1
```

### Greedy Doesn't Work

For coins [1, 3, 4] and amount 6:
- Greedy: 4 + 1 + 1 = 3 coins
- Optimal: 3 + 3 = 2 coins

Greedy fails because larger coins aren't always better.

### Edge Cases
- amount = 0: return 0
- No valid combination: return -1
- Single coin equal to amount: return 1

### Related Problems
- Coin Change II: count number of combinations
- Perfect Squares: coins are perfect squares
- Minimum Cost For Tickets: similar DP with constraints
