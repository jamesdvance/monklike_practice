# Min Cost Climbing Stairs

## Summary

Given an array cost where cost[i] is the cost to step on stair i, find the minimum cost to reach the top. You can start at index 0 or 1, and can climb 1 or 2 steps at a time.

### Key Points
- Similar to Climbing Stairs but with costs
- dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
- Can start from step 0 or step 1

### Optimal Approach
Bottom-up DP with constant space.

```python
def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)

    prev2, prev1 = cost[0], cost[1]

    for i in range(2, n):
        curr = min(prev1, prev2) + cost[i]
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

To reach step i, you pay cost[i] plus the minimum cost to reach either step i-1 or step i-2.

The "top" is beyond the last step, so the answer is the minimum of reaching the last step or second-to-last step.

### State Definition

dp[i] = minimum cost to reach step i (and pay for stepping on it)

### Recurrence

dp[i] = cost[i] + min(dp[i-1], dp[i-2])

### Full DP Array Approach

```python
def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])
```

### In-Place Modification

```python
def minCostClimbingStairs(cost: list[int]) -> int:
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])

    return min(cost[-1], cost[-2])
```

Modifies input but uses O(1) extra space.

### Top-Down with Memoization

```python
def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    memo = {}

    def dp(i):
        if i < 0:
            return 0
        if i <= 1:
            return cost[i]
        if i in memo:
            return memo[i]

        memo[i] = cost[i] + min(dp(i-1), dp(i-2))
        return memo[i]

    return min(dp(n-1), dp(n-2))
```

### Step-by-Step Example

```
cost = [10, 15, 20]

dp[0] = 10 (cost to reach and pay step 0)
dp[1] = 15 (cost to reach and pay step 1)
dp[2] = 20 + min(15, 10) = 20 + 10 = 30

To reach top (beyond step 2):
- From step 1: 15
- From step 2: 30

Answer: min(15, 30) = 15
```

Path: Start at step 1 (pay 15), jump to top.

### Another Example

```
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

Optimal path: 0 -> 2 -> 3 -> 4 -> 6 -> 7 -> 9 -> top
Cost: 1 + 1 + 1 + 1 + 1 + 1 + 1 = 6
```

### Edge Cases
- Two steps: return min(cost[0], cost[1])
- All same costs: any path works
- Alternating high/low: take low costs

### Related Problems
- Climbing Stairs: count paths without costs
- House Robber: non-adjacent elements
- Jump Game II: minimum jumps
