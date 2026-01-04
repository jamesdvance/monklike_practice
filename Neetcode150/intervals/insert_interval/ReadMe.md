# Insert Interval

## Summary

Given a sorted list of non-overlapping intervals and a new interval, insert the new interval and merge if necessary, returning the sorted list.

### Key Points
- Add intervals before the new one (no overlap)
- Merge overlapping intervals with the new one
- Add intervals after the new one (no overlap)

### Optimal Approach
Single pass through intervals.

```python
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

### Complexity
- Time: O(n)
- Space: O(n) for the result

---

## Detailed Explanation

### Problem Analysis

Since intervals are sorted and non-overlapping:
1. Intervals ending before newInterval starts: no overlap, keep as-is
2. Intervals overlapping with newInterval: merge into newInterval
3. Intervals starting after newInterval ends: no overlap, keep as-is

### Overlap Condition

Two intervals [a, b] and [c, d] overlap if:
- a <= d AND c <= b

Equivalently, they DON'T overlap if:
- b < c (first ends before second starts) OR
- d < a (second ends before first starts)

### Step-by-Step Example

```
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

Phase 1 - Before newInterval:
  [1,2]: 2 < 4 -> add to result
  [3,5]: 5 >= 4 -> stop

result = [[1,2]]

Phase 2 - Merge overlapping:
  [3,5]: 3 <= 8 -> merge: newInterval = [min(4,3), max(8,5)] = [3,8]
  [6,7]: 6 <= 8 -> merge: newInterval = [3, max(8,7)] = [3,8]
  [8,10]: 8 <= 8 -> merge: newInterval = [3, max(8,10)] = [3,10]
  [12,16]: 12 > 10 -> stop

result = [[1,2], [3,10]]

Phase 3 - After newInterval:
  [12,16]: add

result = [[1,2], [3,10], [12,16]]
```

### Alternative: Simpler Logic

```python
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []

    for i, interval in enumerate(intervals):
        if interval[1] < newInterval[0]:
            # interval is before newInterval
            result.append(interval)
        elif interval[0] > newInterval[1]:
            # interval is after newInterval, insert newInterval and rest
            result.append(newInterval)
            return result + intervals[i:]
        else:
            # Overlapping, merge
            newInterval = [min(newInterval[0], interval[0]),
                          max(newInterval[1], interval[1])]

    result.append(newInterval)
    return result
```

### Binary Search Optimization

Find insertion point with binary search:

```python
import bisect

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    # Find where newInterval starts
    starts = [i[0] for i in intervals]
    left = bisect.bisect_left(starts, newInterval[0])

    # Find where newInterval ends
    ends = [i[1] for i in intervals]
    right = bisect.bisect_right(ends, newInterval[1])

    # Merge with overlapping intervals
    if left > 0 and intervals[left - 1][1] >= newInterval[0]:
        left -= 1
        newInterval[0] = intervals[left][0]

    if right < len(intervals) and intervals[right][0] <= newInterval[1]:
        newInterval[1] = intervals[right][1]
        right += 1

    return intervals[:left] + [newInterval] + intervals[right:]
```

### Edge Cases
- Empty intervals: return [newInterval]
- newInterval before all: prepend
- newInterval after all: append
- Complete overlap of all intervals: single merged interval

### Related Problems
- Merge Intervals: merge all overlapping
- Non-overlapping Intervals: minimum removals
- Meeting Rooms II: count overlaps
