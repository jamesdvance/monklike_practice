# Best Time to Buy and Sell Stock with Cooldown

## Summary

Given stock prices, find maximum profit with unlimited transactions. After selling, you must wait one day before buying again (cooldown).

### Key Points
- Three states: holding stock, just sold (cooldown), ready to buy
- Track profit for each state
- Transitions between states based on action

### Optimal Approach
State machine DP.

```python
def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0

    hold = -prices[0]  # Holding a stock
    sold = 0           # Just sold, in cooldown
    rest = 0           # Not holding, ready to buy

    for i in range(1, len(prices)):
        prev_hold = hold
        hold = max(hold, rest - prices[i])  # Keep holding or buy
        rest = max(rest, sold)               # Keep resting or finish cooldown
        sold = prev_hold + prices[i]         # Sell today

    return max(sold, rest)
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The cooldown constraint means we can't buy immediately after selling. We need to track three states:

1. **hold**: We are holding a stock
2. **sold**: We just sold (entering cooldown)
3. **rest**: We're not holding and not in cooldown (can buy)

### State Transitions

```
hold -> hold (do nothing)
hold -> sold (sell stock)

sold -> rest (cooldown over)

rest -> rest (do nothing)
rest -> hold (buy stock)
```

### Recurrence

```
hold[i] = max(hold[i-1], rest[i-1] - prices[i])
sold[i] = hold[i-1] + prices[i]
rest[i] = max(rest[i-1], sold[i-1])
```

### Full DP Array Approach

```python
def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0

    hold = [0] * n
    sold = [0] * n
    rest = [0] * n

    hold[0] = -prices[0]

    for i in range(1, n):
        hold[i] = max(hold[i-1], rest[i-1] - prices[i])
        sold[i] = hold[i-1] + prices[i]
        rest[i] = max(rest[i-1], sold[i-1])

    return max(sold[n-1], rest[n-1])
```

### Alternative: Two States

```python
def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0

    buy = -prices[0]  # Max profit when we need to buy/are holding
    sell = 0          # Max profit when we need to sell/just sold
    prev_sell = 0     # sell from 2 days ago (for cooldown)

    for i in range(1, len(prices)):
        temp = sell
        sell = max(sell, buy + prices[i])
        buy = max(buy, prev_sell - prices[i])
        prev_sell = temp

    return sell
```

### Step-by-Step Example

```
prices = [1, 2, 3, 0, 2]

Day 0 (price=1):
  hold = -1 (buy)
  sold = 0
  rest = 0

Day 1 (price=2):
  hold = max(-1, 0-2) = -1 (keep holding)
  sold = -1 + 2 = 1 (sell)
  rest = max(0, 0) = 0

Day 2 (price=3):
  hold = max(-1, 0-3) = -1
  sold = -1 + 3 = 2
  rest = max(0, 1) = 1 (cooldown from yesterday)

Day 3 (price=0):
  hold = max(-1, 1-0) = 1 (buy at price 0!)
  sold = -1 + 0 = -1
  rest = max(1, 2) = 2

Day 4 (price=2):
  hold = max(1, 2-2) = 1
  sold = 1 + 2 = 3 (sell at price 2)
  rest = max(2, -1) = 2

Answer: max(3, 2) = 3
```

Path: Buy at 1, sell at 2, cooldown, buy at 0, sell at 2. Profit = 1 + 2 = 3.

### Top-Down with Memoization

```python
def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    memo = {}

    def dp(i, holding):
        if i >= n:
            return 0
        if (i, holding) in memo:
            return memo[(i, holding)]

        # Do nothing
        result = dp(i + 1, holding)

        if holding:
            # Sell (next day is cooldown, skip to i+2)
            result = max(result, prices[i] + dp(i + 2, False))
        else:
            # Buy
            result = max(result, -prices[i] + dp(i + 1, True))

        memo[(i, holding)] = result
        return result

    return dp(0, False)
```

### Edge Cases
- Single price: return 0
- Decreasing prices: don't buy at all, return 0
- Two prices: can make one transaction

### Related Problems
- Best Time to Buy and Sell Stock: single transaction
- Best Time to Buy and Sell Stock II: no cooldown
- Best Time to Buy and Sell Stock III: max 2 transactions
- Best Time to Buy and Sell Stock IV: max k transactions
