# Sliding Window Maximum

## Summary

Given an array `nums` and a window size `k`, return the maximum value in each sliding window as it moves from left to right.

### Key Points
- Naive approach checking max in each window is O(n*k)
- Use a monotonic deque to track potential maximums
- Deque maintains indices of elements in decreasing order

### Optimal Approach
Use a monotonic decreasing deque. Elements are removed if they are smaller than the incoming element (they can never be the maximum) or if they fall outside the window.

```python
from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    result = []
    dq = deque()  # Store indices

    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of smaller elements (they will never be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Window is complete, record maximum
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

### Complexity
- Time: O(n) - each element added and removed from deque at most once
- Space: O(k) - deque holds at most k elements

---

## Detailed Explanation

### Problem Analysis

For each window position, we need the maximum element. The naive approach of scanning each window is O(n*k). The key insight is that we can maintain candidates for maximum more efficiently using a monotonic deque.

### Why Monotonic Decreasing Deque

The deque maintains elements (by index) in decreasing order of value. This gives us:
1. Maximum is always at the front
2. When a new element arrives, smaller elements in the deque are useless (the new element is newer and larger, so it will always be preferred)

### The Two Key Operations

**Remove from front (outside window)**
```python
while dq and dq[0] < i - k + 1:
    dq.popleft()
```
Indices that have fallen out of the current window are removed.

**Remove from back (smaller elements)**
```python
while dq and nums[dq[-1]] < nums[i]:
    dq.pop()
```
Elements smaller than the incoming element are removed because:
- They cannot be the maximum in the current window (current element is larger)
- They cannot be the maximum in any future window (current element is larger and will exit the window later or at the same time)

### Step-by-Step Example

For `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`:

```
i=0: dq=[], add 0, dq=[0]
i=1: nums[0]=1 < nums[1]=3, pop, dq=[], add 1, dq=[1]
i=2: nums[1]=3 > nums[2]=-1, add 2, dq=[1,2], output nums[1]=3
i=3: dq[0]=1 >= 3-3+1=1, keep, nums[2]=-1 > nums[3]=-3, add 3, dq=[1,2,3], output nums[1]=3
i=4: dq[0]=1 < 4-3+1=2, popleft, dq=[2,3]
     nums[3]=-3 < nums[4]=5, pop, nums[2]=-1 < 5, pop, dq=[], add 4, dq=[4], output nums[4]=5
i=5: nums[4]=5 > nums[5]=3, add 5, dq=[4,5], output nums[4]=5
i=6: dq[0]=4 >= 4, keep, nums[5]=3 < nums[6]=6, pop, nums[4]=5 < 6, pop, dq=[], add 6, dq=[6], output nums[6]=6
i=7: dq[0]=6 >= 5, keep, nums[6]=6 < nums[7]=7, pop, dq=[], add 7, dq=[7], output nums[7]=7
```

Result: [3, 3, 5, 5, 6, 7]

### Alternative: Heap-Based Approach

Use a max-heap, removing elements outside the window lazily:

```python
import heapq

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    result = []
    heap = []  # max-heap using negative values

    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))

        if i >= k - 1:
            # Remove elements outside window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            result.append(-heap[0][0])

    return result
```

- Time: O(n log n) - heap operations
- Space: O(n) - heap can grow to size n

This is simpler but less efficient than the deque approach.

### Why Store Indices?

We store indices rather than values because we need to check if an element is still within the window. An element's position tells us when it will leave the window.

### Edge Cases
- k = 1: each element is its own maximum
- k = len(nums): single window covering entire array
- All same elements: all maximums are that element
- Strictly decreasing: deque always has one element after the first window

### Common Mistakes
- Storing values instead of indices
- Forgetting to remove elements outside the window
- Off-by-one when checking window boundaries

### Related Problems
- Min Stack: similar idea of tracking extremes
- Daily Temperatures: monotonic stack variant
- Largest Rectangle in Histogram: monotonic stack
