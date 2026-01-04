# Longest Increasing Subsequence

## Summary

Given an integer array, return the length of the longest strictly increasing subsequence.

### Key Points
- Subsequence doesn't need to be contiguous
- O(n^2) DP: for each element, check all previous
- O(n log n): binary search with patience sorting

### Optimal Approach (Binary Search)
Use a list to track smallest endings for each length.

```python
import bisect

def lengthOfLIS(nums: list[int]) -> int:
    tails = []

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)
```

### Complexity
- Time: O(n log n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

We want the longest strictly increasing subsequence. For [10, 9, 2, 5, 3, 7, 101, 18], the answer is 4: [2, 3, 7, 101] or [2, 5, 7, 101].

### O(n^2) DP Approach

```python
def lengthOfLIS(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n  # dp[i] = LIS ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

dp[i] = length of longest increasing subsequence ending at index i

### Binary Search Insight

The tails array maintains the smallest ending value for each subsequence length:
- tails[0] = smallest ending of LIS of length 1
- tails[1] = smallest ending of LIS of length 2
- etc.

When we see a new number:
- If it's larger than all tails, extend the longest subsequence
- Otherwise, replace the first tail that's >= num (to keep smaller endings)

### Step-by-Step Example

```
nums = [10, 9, 2, 5, 3, 7, 101, 18]

num=10: tails=[] -> [10]
num=9:  bisect_left([10], 9)=0 -> [9]
num=2:  bisect_left([9], 2)=0 -> [2]
num=5:  bisect_left([2], 5)=1 -> [2, 5]
num=3:  bisect_left([2,5], 3)=1 -> [2, 3]
num=7:  bisect_left([2,3], 7)=2 -> [2, 3, 7]
num=101: bisect_left([2,3,7], 101)=3 -> [2, 3, 7, 101]
num=18: bisect_left([2,3,7,101], 18)=3 -> [2, 3, 7, 18]

Answer: len(tails) = 4
```

Note: tails is NOT the actual LIS, just tracks smallest endings.

### Reconstructing the LIS

```python
def lengthOfLIS_with_sequence(nums: list[int]) -> list[int]:
    n = len(nums)
    if n == 0:
        return []

    # dp[i] = length of LIS ending at i
    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find index of maximum
    max_len = max(dp)
    max_idx = dp.index(max_len)

    # Reconstruct
    result = []
    idx = max_idx
    while idx != -1:
        result.append(nums[idx])
        idx = parent[idx]

    return result[::-1]
```

### Patience Sorting Explanation

The binary search approach is equivalent to "patience sorting":
1. Each pile has cards in decreasing order (top to bottom)
2. A new card goes on the leftmost pile whose top is >= card
3. If no such pile, start a new pile
4. Number of piles = LIS length

### Non-Decreasing Variant

For longest non-decreasing (allowing equal values):

```python
def lengthOfLIS(nums: list[int]) -> int:
    tails = []
    for num in nums:
        pos = bisect.bisect_right(tails, num)  # Use bisect_right
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

### Edge Cases
- Single element: return 1
- Already sorted ascending: return n
- Already sorted descending: return 1
- All same elements: return 1 (strictly increasing)

### Related Problems
- Number of Longest Increasing Subsequence: count how many LIS exist
- Longest Increasing Subsequence II: with constraint on difference
- Russian Doll Envelopes: 2D LIS
