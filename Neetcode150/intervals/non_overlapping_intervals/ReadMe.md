# Non-overlapping Intervals

## Summary

Given an array of intervals, return the minimum number of intervals to remove to make the rest non-overlapping.

### Key Points
- Sort by end time (greedy choice)
- Keep intervals that end earliest
- Count overlaps that must be removed

### Optimal Approach
Sort by end time, greedily keep non-overlapping.

```python
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            # No overlap, keep this interval
            prev_end = end
        else:
            # Overlap, remove this interval
            count += 1

    return count
```

### Complexity
- Time: O(n log n) for sorting
- Space: O(1) extra space

---

## Detailed Explanation

### Problem Analysis

This is equivalent to finding the maximum number of non-overlapping intervals (interval scheduling maximization). Remove = n - max_non_overlapping.

### Why Sort by End Time?

Ending earlier leaves more room for future intervals. By always choosing the interval that ends earliest among non-overlapping options, we maximize the number of intervals we can keep.

### Greedy Proof

If we choose an interval that ends later when an earlier-ending option exists, we might block a future interval. The earlier-ending interval never blocks more than the later-ending one.

### Step-by-Step Example

```
intervals = [[1,2],[2,3],[3,4],[1,3]]

Sorted by end: [[1,2],[2,3],[1,3],[3,4]]

prev_end = -inf

[1,2]: 1 >= -inf -> keep, prev_end = 2
[2,3]: 2 >= 2 -> keep, prev_end = 3
[1,3]: 1 < 3 -> overlap, remove, count = 1
[3,4]: 3 >= 3 -> keep, prev_end = 4

Answer: 1
```

### Alternative: Sort by Start

```python
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort()

    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            # Overlap - keep the one that ends earlier
            prev_end = min(prev_end, end)
            count += 1

    return count
```

When sorting by start, we must choose which interval to keep based on end time.

### DP Approach (Less Efficient)

Similar to Longest Increasing Subsequence:

```python
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort()
    n = len(intervals)

    # dp[i] = max non-overlapping intervals ending with intervals[i]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if intervals[j][1] <= intervals[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)
```

Time: O(n^2)

### Edge Cases
- No overlaps: return 0
- All overlap: return n - 1
- Nested intervals: keep outer or inner based on strategy

### Related Problems
- Merge Intervals: merge overlapping intervals
- Meeting Rooms: check if any overlap
- Minimum Number of Arrows: similar greedy
