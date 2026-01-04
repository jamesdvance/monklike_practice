# Partition Equal Subset Sum

## Summary

Given a non-empty array of positive integers, determine if the array can be partitioned into two subsets with equal sum.

### Key Points
- Total sum must be even (otherwise impossible)
- Reduces to: can we find subset with sum = total/2?
- 0/1 Knapsack problem variant

### Optimal Approach
Use DP to track achievable sums.

```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]
```

### Complexity
- Time: O(n * target)
- Space: O(target)

---

## Detailed Explanation

### Problem Analysis

If we can split array into two equal subsets, each has sum = total/2.

So the problem becomes: can we select some elements that sum to total/2?

This is the subset sum problem (special case of 0/1 knapsack).

### Why Iterate Backwards?

We iterate j from target down to num to avoid using the same number twice.

If we went forwards, dp[j - num] might already be updated in the current iteration, effectively using num multiple times.

### Full 2D DP Approach

```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)

    # dp[i][j] = can we make sum j using first i elements?
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum 0 is always achievable
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Don't take nums[i-1]
            dp[i][j] = dp[i-1][j]

            # Take nums[i-1] if possible
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]

    return dp[n][target]
```

### Bitset Optimization

Use a bitmask where bit j is set if sum j is achievable:

```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    bits = 1  # Bit 0 is set (sum 0 is achievable)

    for num in nums:
        bits |= bits << num

    return (bits >> target) & 1 == 1
```

Very fast due to bitwise operations.

### Top-Down with Memoization

```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    memo = {}

    def dp(i, remaining):
        if remaining == 0:
            return True
        if i >= len(nums) or remaining < 0:
            return False
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        # Take or skip current number
        result = dp(i + 1, remaining - nums[i]) or dp(i + 1, remaining)
        memo[(i, remaining)] = result
        return result

    return dp(0, target)
```

### Step-by-Step Example

```
nums = [1, 5, 11, 5]
total = 22, target = 11

Initial: dp = [T, F, F, F, F, F, F, F, F, F, F, F]

num = 1:
  j=11: dp[11] = dp[11] or dp[10] = F
  ...
  j=1: dp[1] = dp[1] or dp[0] = T
  dp = [T, T, F, F, F, F, F, F, F, F, F, F]

num = 5:
  j=11: dp[11] = dp[11] or dp[6] = F
  j=6: dp[6] = dp[6] or dp[1] = T
  j=5: dp[5] = dp[5] or dp[0] = T
  dp = [T, T, F, F, F, T, T, F, F, F, F, F]

num = 11:
  j=11: dp[11] = dp[11] or dp[0] = T
  dp = [T, T, F, F, F, T, T, F, F, F, F, T]

Answer: dp[11] = True (subset [1, 5, 5] or [11])
```

### Early Termination

```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2

    if max(nums) > target:
        return False  # Single element too large

    dp = {0}
    for num in nums:
        dp = dp | {x + num for x in dp if x + num <= target}
        if target in dp:
            return True

    return target in dp
```

### Edge Cases
- Odd total: return False
- Single element: return False (can't split)
- Contains target exactly: return True
- All elements same and even count: return True

### Related Problems
- Target Sum: count ways to reach target with +/-
- Last Stone Weight II: minimize remaining weight
- Coin Change: minimum coins for target
