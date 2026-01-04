# Maximum Subarray

## Summary

Given an integer array, find the contiguous subarray with the largest sum and return the sum.

### Key Points
- Kadane's algorithm: track running sum, reset when negative
- Current sum = max(current element, current sum + element)
- Classic greedy problem

### Optimal Approach (Kadane's Algorithm)
Track the best ending at each position.

```python
def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

At each position, we decide:
1. Extend the previous subarray by including current element
2. Start a new subarray from current element

We start fresh when the previous subarray sum is negative (it would only decrease our total).

### The Key Insight

If curr_sum < 0, adding nums[i] gives us less than just nums[i] alone. So we start fresh with nums[i].

### Alternative Formulation

```python
def maxSubArray(nums: list[int]) -> int:
    max_sum = float('-inf')
    curr_sum = 0

    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum
```

### DP Perspective

```python
def maxSubArray(nums: list[int]) -> int:
    n = len(nums)
    # dp[i] = max sum of subarray ending at index i
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])

    return max(dp)
```

### Divide and Conquer (O(n log n))

```python
def maxSubArray(nums: list[int]) -> int:
    def helper(left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        # Max crossing the middle
        left_max = float('-inf')
        curr = 0
        for i in range(mid, left - 1, -1):
            curr += nums[i]
            left_max = max(left_max, curr)

        right_max = float('-inf')
        curr = 0
        for i in range(mid + 1, right + 1):
            curr += nums[i]
            right_max = max(right_max, curr)

        cross_max = left_max + right_max

        return max(helper(left, mid), helper(mid + 1, right), cross_max)

    return helper(0, len(nums) - 1)
```

### Step-by-Step Example

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i=0: curr_sum = -2, max_sum = -2
i=1: curr_sum = max(1, -2+1) = 1, max_sum = 1
i=2: curr_sum = max(-3, 1-3) = -2, max_sum = 1
i=3: curr_sum = max(4, -2+4) = 4, max_sum = 4
i=4: curr_sum = max(-1, 4-1) = 3, max_sum = 4
i=5: curr_sum = max(2, 3+2) = 5, max_sum = 5
i=6: curr_sum = max(1, 5+1) = 6, max_sum = 6
i=7: curr_sum = max(-5, 6-5) = 1, max_sum = 6
i=8: curr_sum = max(4, 1+4) = 5, max_sum = 6

Answer: 6 (subarray [4, -1, 2, 1])
```

### Finding the Actual Subarray

```python
def maxSubArray(nums: list[int]) -> tuple[int, int, int]:
    max_sum = float('-inf')
    curr_sum = 0
    start = end = temp_start = 0

    for i, num in enumerate(nums):
        curr_sum += num

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

        if curr_sum < 0:
            curr_sum = 0
            temp_start = i + 1

    return max_sum, start, end
```

### Edge Cases
- All negative: return the largest (least negative)
- Single element: return that element
- All positive: return sum of entire array

### Related Problems
- Maximum Product Subarray: product instead of sum
- Maximum Sum Circular Subarray: circular array
- Best Time to Buy and Sell Stock: max profit
