# Target Sum

## Summary

Given an array of integers and a target, assign + or - to each integer and count ways to achieve the target sum.

### Key Points
- Equivalent to subset sum problem
- Split array into two groups: positive and negative
- Transform to: count subsets with sum = (total + target) / 2

### Optimal Approach
Convert to subset sum and use DP.

```python
def findTargetSumWays(nums: list[int], target: int) -> int:
    total = sum(nums)

    # Check if solution is possible
    if (total + target) % 2 != 0 or abs(target) > total:
        return 0

    subset_sum = (total + target) // 2

    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for num in nums:
        for j in range(subset_sum, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[subset_sum]
```

### Complexity
- Time: O(n * subset_sum)
- Space: O(subset_sum)

---

## Detailed Explanation

### Problem Analysis

Let P = sum of positive group, N = sum of negative group.
- P + N = total (sum of all nums)
- P - N = target

Solving: P = (total + target) / 2

So we need to count subsets with sum P.

### Why the Math Works

P - N = target
P + N = total
Adding: 2P = total + target
So: P = (total + target) / 2

If (total + target) is odd, no solution exists.

### Direct DP Approach

Track all possible sums and their counts.

```python
def findTargetSumWays(nums: list[int], target: int) -> int:
    dp = {0: 1}

    for num in nums:
        next_dp = {}
        for s, count in dp.items():
            next_dp[s + num] = next_dp.get(s + num, 0) + count
            next_dp[s - num] = next_dp.get(s - num, 0) + count
        dp = next_dp

    return dp.get(target, 0)
```

This tracks all reachable sums, using a dictionary.

### 2D DP with Offset

```python
def findTargetSumWays(nums: list[int], target: int) -> int:
    total = sum(nums)
    if abs(target) > total:
        return 0

    n = len(nums)
    # dp[i][j] = ways using first i nums to reach sum j
    # j is offset by total (so -total to +total maps to 0 to 2*total)
    dp = [[0] * (2 * total + 1) for _ in range(n + 1)]
    dp[0][total] = 1  # Sum 0 is at index total

    for i in range(n):
        for j in range(2 * total + 1):
            if dp[i][j] > 0:
                dp[i + 1][j + nums[i]] += dp[i][j]
                dp[i + 1][j - nums[i]] += dp[i][j]

    return dp[n][total + target]
```

### Top-Down with Memoization

```python
def findTargetSumWays(nums: list[int], target: int) -> int:
    memo = {}

    def dp(i, curr_sum):
        if i == len(nums):
            return 1 if curr_sum == target else 0
        if (i, curr_sum) in memo:
            return memo[(i, curr_sum)]

        result = dp(i + 1, curr_sum + nums[i]) + dp(i + 1, curr_sum - nums[i])
        memo[(i, curr_sum)] = result
        return result

    return dp(0, 0)
```

### Step-by-Step Example

```
nums = [1, 1, 1, 1, 1], target = 3

total = 5
subset_sum = (5 + 3) / 2 = 4

Find subsets summing to 4:
dp = [1, 0, 0, 0, 0]

num=1: dp = [1, 1, 0, 0, 0]
num=1: dp = [1, 2, 1, 0, 0]
num=1: dp = [1, 3, 3, 1, 0]
num=1: dp = [1, 4, 6, 4, 1]
num=1: dp = [1, 5, 10, 10, 5]

Answer: dp[4] = 5
```

Ways: +1+1+1+1-1, +1+1+1-1+1, +1+1-1+1+1, +1-1+1+1+1, -1+1+1+1+1

### Handling Zeros

Zeros can be either + or -, so each zero doubles the count:

```python
def findTargetSumWays(nums: list[int], target: int) -> int:
    zeros = nums.count(0)
    nums = [n for n in nums if n != 0]

    # ... rest of algorithm ...

    return result * (2 ** zeros)
```

### Edge Cases
- target > sum(nums): return 0
- target < -sum(nums): return 0
- (total + target) is odd: return 0
- All zeros: 2^n if target == 0

### Related Problems
- Partition Equal Subset Sum: can we split into two equal halves
- Last Stone Weight II: minimize remaining weight
- Coin Change II: count combinations
