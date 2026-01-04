# House Robber

## Summary

Given an array representing money in each house, find the maximum amount you can rob without robbing two adjacent houses.

### Key Points
- Cannot rob adjacent houses
- dp[i] = max(dp[i-1], dp[i-2] + nums[i])
- Either skip current house or rob it with previous-previous

### Optimal Approach
Bottom-up DP with constant space.

```python
def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, 0

    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr

    return prev1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

At each house, we have two choices:
1. Skip it: keep the maximum from previous houses
2. Rob it: add current value to maximum excluding adjacent house

### State Definition

dp[i] = maximum money robbed considering houses 0 to i

### Recurrence

dp[i] = max(dp[i-1], dp[i-2] + nums[i])

- dp[i-1]: don't rob house i
- dp[i-2] + nums[i]: rob house i (can't use i-1)

### Full DP Array Approach

```python
def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[n-1]
```

### Top-Down with Memoization

```python
def rob(nums: list[int]) -> int:
    memo = {}

    def dp(i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]

        memo[i] = max(dp(i-1), dp(i-2) + nums[i])
        return memo[i]

    return dp(len(nums) - 1)
```

### Step-by-Step Example

```
nums = [2, 7, 9, 3, 1]

dp[0] = 2 (rob house 0)
dp[1] = max(2, 7) = 7 (rob house 1)
dp[2] = max(7, 2+9) = 11 (rob houses 0, 2)
dp[3] = max(11, 7+3) = 11 (still best: houses 0, 2)
dp[4] = max(11, 11+1) = 12 (rob houses 0, 2, 4)

Answer: 12
```

### Alternative Formulation

Think of it as: include/exclude at each step.

```python
def rob(nums: list[int]) -> int:
    include, exclude = 0, 0

    for num in nums:
        new_include = exclude + num
        new_exclude = max(include, exclude)
        include, exclude = new_include, new_exclude

    return max(include, exclude)
```

- include: max if we rob current house
- exclude: max if we skip current house

### Edge Cases
- Single house: return nums[0]
- Two houses: return max(nums[0], nums[1])
- All same values: alternating houses

### Related Problems
- House Robber II: circular arrangement
- House Robber III: tree structure
- Delete and Earn: similar DP pattern
