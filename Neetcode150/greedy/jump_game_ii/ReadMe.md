# Jump Game II

## Summary

Given an array where nums[i] is the maximum jump length from position i, return the minimum number of jumps to reach the last index. You can always reach the last index.

### Key Points
- BFS-like approach: each "level" is one jump
- Track the farthest position reachable with current jumps
- Increment jumps when we must extend our range

### Optimal Approach
Greedy BFS simulation.

```python
def jump(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    curr_end = 0  # Farthest we can go with current jumps
    farthest = 0  # Farthest we can go with one more jump

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])

        if i == curr_end:
            jumps += 1
            curr_end = farthest

            if curr_end >= n - 1:
                break

    return jumps
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Think of it as BFS on an implicit graph:
- Each position is a node
- Edges connect to all positions reachable in one jump
- Find shortest path from 0 to n-1

### The Greedy Insight

We don't need actual BFS. For each "level" (jump count), track:
- curr_end: farthest position reachable with current number of jumps
- farthest: farthest position reachable with one more jump

When we've explored all positions up to curr_end, we must take another jump.

### Why This Works

By tracking farthest within each "level," we ensure we always make the optimal choice - jumping to the position that maximizes our next range.

### Step-by-Step Example

```
nums = [2, 3, 1, 1, 4]

Initial: jumps=0, curr_end=0, farthest=0

i=0: farthest = max(0, 0+2) = 2
     i == curr_end, so jumps=1, curr_end=2

i=1: farthest = max(2, 1+3) = 4
     1 != 2, continue

i=2: farthest = max(4, 2+1) = 4
     i == curr_end, so jumps=2, curr_end=4
     curr_end >= 4 (n-1), break

Answer: 2
```

Jumps: 0 -> 1 -> 4 (indices)

### BFS Approach (Explicit)

```python
from collections import deque

def jump(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    jumps = 0

    while queue:
        jumps += 1
        for _ in range(len(queue)):
            pos = queue.popleft()
            for next_pos in range(pos + 1, min(pos + nums[pos] + 1, n)):
                if next_pos == n - 1:
                    return jumps
                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append(next_pos)

    return -1
```

This is O(n^2) in the worst case due to the inner loop.

### DP Approach (O(n^2))

```python
def jump(nums: list[int]) -> int:
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(n):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + 1)

    return dp[n - 1]
```

### Visualization

```
nums = [2, 3, 1, 1, 4]
Index: 0  1  2  3  4

Level 0: position 0
Level 1: positions 1, 2 (reachable from 0)
Level 2: positions 3, 4 (reachable from 1, 2)

Minimum jumps to position 4: 2
```

### Edge Cases
- Single element: 0 jumps needed
- Two elements: 1 jump (if first element >= 1)
- Large first element: might reach end in 1 jump

### Related Problems
- Jump Game: just check if reachable
- Jump Game III: can go backwards
- Minimum Jumps to Reach Home: more complex rules
