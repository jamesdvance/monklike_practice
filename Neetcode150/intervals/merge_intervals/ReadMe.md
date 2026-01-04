# Merge Intervals

## Summary

Given an array of intervals, merge all overlapping intervals and return the non-overlapping intervals.

### Key Points
- Sort intervals by start time
- Iterate and merge overlapping intervals
- Two intervals overlap if first's end >= second's start

### Optimal Approach
Sort then merge.

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            # Overlapping, merge
            result[-1][1] = max(result[-1][1], end)
        else:
            # Non-overlapping, add new interval
            result.append([start, end])

    return result
```

### Complexity
- Time: O(n log n) for sorting
- Space: O(n) for the result

---

## Detailed Explanation

### Problem Analysis

After sorting by start time, overlapping intervals are adjacent. For consecutive intervals [a, b] and [c, d] (where a <= c):
- Overlap if b >= c
- Merge to [a, max(b, d)]

### Why Sort by Start?

Sorting ensures that if interval i doesn't overlap with the current merged interval, no later interval will either (their starts are even larger).

### Step-by-Step Example

```
intervals = [[1,3],[2,6],[8,10],[15,18]]

Sorted: [[1,3],[2,6],[8,10],[15,18]] (already sorted)

result = [[1,3]]

[2,6]: 2 <= 3 -> overlap, merge to [1,6]
result = [[1,6]]

[8,10]: 8 > 6 -> no overlap, add
result = [[1,6],[8,10]]

[15,18]: 15 > 10 -> no overlap, add
result = [[1,6],[8,10],[15,18]]
```

### In-Place Alternative

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])

    write = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[write][1]:
            intervals[write][1] = max(intervals[write][1], intervals[i][1])
        else:
            write += 1
            intervals[write] = intervals[i]

    return intervals[:write + 1]
```

Uses the input array, O(1) extra space (excluding sort).

### Using a Stack

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])

    stack = []
    for interval in intervals:
        if stack and interval[0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], interval[1])
        else:
            stack.append(interval)

    return stack
```

### Edge Cases
- Single interval: return as-is
- No overlaps: return sorted intervals
- All overlap: return single merged interval
- Nested intervals: [1,10], [2,3] -> [1,10]

### Related Problems
- Insert Interval: insert and merge
- Non-overlapping Intervals: minimum removals
- Meeting Rooms: check for any overlap
