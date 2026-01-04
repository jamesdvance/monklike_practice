# Best Time to Buy and Sell Stock

## Summary

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit from one buy and one sell transaction. You must buy before you sell.

### Key Points
- Track the minimum price seen so far
- At each position, calculate potential profit if selling today
- Single pass solution tracking running minimum

### Optimal Approach
Iterate through prices, tracking the minimum price seen. At each price, calculate the profit if we sold today and update the maximum.

```python
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
```

### Complexity
- Time: O(n) - single pass through prices
- Space: O(1) - only tracking two variables

---

## Detailed Explanation

### Problem Analysis

This problem asks for the maximum difference between a later element and an earlier element. The key insight is that for any selling day, the optimal buying day is the day with the minimum price before it.

### Why Track Minimum

For each day `i`, the best profit from selling on day `i` is:
```
profit[i] = prices[i] - min(prices[0], prices[1], ..., prices[i-1])
```

By tracking the running minimum, we compute this in O(1) per day.

### Alternative: Two-Pointer View

This can be viewed as a sliding window where:
- Left pointer marks the buy day (minimum so far)
- Right pointer marks the current sell day
- We only move left when we find a lower price

```python
def maxProfit(prices: list[int]) -> int:
    left = 0  # Buy day
    max_profit = 0

    for right in range(1, len(prices)):
        if prices[right] < prices[left]:
            left = right  # Found a better buy day
        else:
            max_profit = max(max_profit, prices[right] - prices[left])

    return max_profit
```

### Kadane's Algorithm Connection

This problem is related to maximum subarray sum (Kadane's algorithm). If we compute daily price changes, the maximum profit equals the maximum subarray sum of changes:

```python
def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    current_profit = 0

    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]
        current_profit = max(0, current_profit + change)
        max_profit = max(max_profit, current_profit)

    return max_profit
```

### Step-by-Step Example

For `prices = [7, 1, 5, 3, 6, 4]`:

```
Day 0: price=7, min=7, profit=0, max_profit=0
Day 1: price=1, min=1, profit=0, max_profit=0
Day 2: price=5, min=1, profit=4, max_profit=4
Day 3: price=3, min=1, profit=2, max_profit=4
Day 4: price=6, min=1, profit=5, max_profit=5
Day 5: price=4, min=1, profit=3, max_profit=5
```

Maximum profit: 5 (buy at 1, sell at 6)

### Edge Cases
- Decreasing prices: no profit possible, return 0
- Single price: cannot complete transaction, return 0
- All same prices: profit is 0
- Two prices: simple comparison

### Common Mistakes
- Returning negative profit (should return 0)
- Not handling the constraint that buy must come before sell
- Trying to find both min and max without considering order

### Variants of This Problem
- Best Time to Buy and Sell Stock II: unlimited transactions
- Best Time to Buy and Sell Stock III: at most 2 transactions
- Best Time to Buy and Sell Stock IV: at most k transactions
- Best Time to Buy and Sell Stock with Cooldown: cooldown after selling

Each variant requires different techniques (greedy, DP, state machines).

### Related Problems
- Maximum Subarray: related via daily changes
- Best Time to Buy and Sell Stock II: greedy variant
