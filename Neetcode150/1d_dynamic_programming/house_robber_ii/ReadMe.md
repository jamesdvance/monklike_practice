# House Robber II

## Summary

Same as House Robber, but houses are arranged in a circle. The first and last houses are adjacent.

### Key Points
- Circular arrangement adds constraint: can't rob both first and last
- Solve two subproblems: exclude first OR exclude last
- Take maximum of both

### Optimal Approach
Run House Robber on two ranges: [0, n-2] and [1, n-1].

```python
def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses):
        prev2, prev1 = 0, 0
        for num in houses:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return prev1

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

### Complexity
- Time: O(n)
- Space: O(1) (or O(n) for slicing)

---

## Detailed Explanation

### Problem Analysis

In a circle, if we rob house 0, we cannot rob house n-1 (and vice versa).

The key insight: we can never rob both first and last house simultaneously.

So the answer is the max of:
1. Best solution excluding the last house
2. Best solution excluding the first house

### Why This Works

Either we rob house 0 or we don't:
- If we rob house 0: we can't rob house n-1, so we only consider [0, n-2]
- If we don't rob house 0: we can consider [1, n-1]

The maximum of these two covers all valid scenarios.

### Space-Optimized Version

```python
def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    def rob_range(start, end):
        prev2, prev1 = 0, 0
        for i in range(start, end):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr
        return prev1

    return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))
```

Avoids creating new arrays.

### Step-by-Step Example

```
nums = [2, 3, 2]

Case 1: Exclude last house [2, 3]
  prev2=0, prev1=0
  num=2: curr = max(0, 0+2) = 2, prev2=0, prev1=2
  num=3: curr = max(2, 0+3) = 3, prev2=2, prev1=3
  Result: 3

Case 2: Exclude first house [3, 2]
  prev2=0, prev1=0
  num=3: curr = max(0, 0+3) = 3, prev2=0, prev1=3
  num=2: curr = max(3, 0+2) = 3, prev2=3, prev1=3
  Result: 3

Answer: max(3, 3) = 3
```

### Another Example

```
nums = [1, 2, 3, 1]

Case 1: [1, 2, 3] -> rob houses 0, 2 = 1+3 = 4
Case 2: [2, 3, 1] -> rob house 1 = 3

Answer: max(4, 3) = 4
```

### Edge Cases
- Single house: return nums[0]
- Two houses: return max(nums)
- Three houses: return max of any one house

### Related Problems
- House Robber: linear version
- House Robber III: binary tree
- Pizza With 3n Slices: similar circular DP
