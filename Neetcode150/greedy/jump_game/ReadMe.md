# Jump Game

## Summary

Given an array where nums[i] is the maximum jump length from position i, determine if you can reach the last index starting from index 0.

### Key Points
- Track the farthest position reachable
- At each step, update max reach if current position is reachable
- Return True if max reach >= last index

### Optimal Approach
Greedy - track maximum reachable position.

```python
def canJump(nums: list[int]) -> bool:
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
        if max_reach >= len(nums) - 1:
            return True

    return True
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

At each position i, if we can reach i (i <= max_reach), we can potentially reach up to i + nums[i]. We update max_reach and continue.

If at any point i > max_reach, we're stuck and can't proceed.

### The Greedy Insight

We don't care about the exact path - just whether the end is reachable. By always tracking the farthest we can go, we ensure we're considering all possibilities.

### Alternative: Work Backwards

```python
def canJump(nums: list[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0
```

Start from the end, move the goal closer when we find a position that can reach it.

### DP Approach (Less Efficient)

```python
def canJump(nums: list[int]) -> bool:
    n = len(nums)
    dp = [False] * n
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = True
                if i + j >= n - 1:
                    return True

    return dp[n - 1]
```

Time: O(n * max_jump), less efficient.

### Step-by-Step Example

```
nums = [2, 3, 1, 1, 4]

i=0: max_reach = max(0, 0+2) = 2
i=1: 1 <= 2, max_reach = max(2, 1+3) = 4
i=2: 2 <= 4, max_reach = max(4, 2+1) = 4
i=3: 3 <= 4, max_reach = max(4, 3+1) = 4
i=4: 4 <= 4, max_reach >= 4 (last index)

Answer: True
```

### Example: Cannot Reach

```
nums = [3, 2, 1, 0, 4]

i=0: max_reach = 3
i=1: max_reach = max(3, 1+2) = 3
i=2: max_reach = max(3, 2+1) = 3
i=3: max_reach = max(3, 3+0) = 3
i=4: 4 > 3 -> stuck!

Answer: False
```

### Edge Cases
- Single element: always True
- First element is 0 (and n > 1): False
- All zeros except first: depends on first value

### Related Problems
- Jump Game II: minimum jumps to reach end
- Jump Game III: can jump +/- nums[i]
- Frog Jump: variable jump sizes
