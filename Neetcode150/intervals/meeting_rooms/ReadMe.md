# Meeting Rooms

## Summary

Given an array of meeting time intervals, determine if a person can attend all meetings (no overlapping meetings).

### Key Points
- Sort intervals by start time
- Check if any consecutive intervals overlap
- Overlap: one meeting starts before previous ends

### Optimal Approach
Sort and check for overlaps.

```python
def canAttendMeetings(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True
```

### Complexity
- Time: O(n log n) for sorting
- Space: O(1) extra space (or O(n) for sort)

---

## Detailed Explanation

### Problem Analysis

A person can attend all meetings if and only if no two meetings overlap. After sorting by start time, we only need to check consecutive meetings.

### Why Only Check Consecutive?

After sorting, if meetings i and j overlap where j > i + 1, then either:
- Meeting i and i+1 overlap, OR
- Meeting i+1 and j overlap

So checking only consecutive pairs is sufficient.

### Overlap Condition

Two intervals [a, b] and [c, d] where a <= c:
- Overlap if c < b (second starts before first ends)
- Note: if c == b (exact touch), typically no overlap

### Step-by-Step Example

```
intervals = [[0,30],[5,10],[15,20]]

Sorted: [[0,30],[5,10],[15,20]]

Compare [0,30] and [5,10]:
  5 < 30 -> overlap!

Answer: False
```

### Alternative: Check All Pairs

```python
def canAttendMeetings(intervals: list[list[int]]) -> bool:
    n = len(intervals)

    for i in range(n):
        for j in range(i + 1, n):
            if (intervals[i][0] < intervals[j][1] and
                intervals[j][0] < intervals[i][1]):
                return False

    return True
```

Time: O(n^2), no sorting needed.

### Using Min-Heap (Overkill for This Problem)

```python
import heapq

def canAttendMeetings(intervals: list[list[int]]) -> bool:
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])
    end_time = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < end_time:
            return False
        end_time = intervals[i][1]

    return True
```

### Edge Cases
- Empty intervals: True
- Single meeting: True
- Adjacent meetings [0,1], [1,2]: True (no overlap)
- Nested meeting: False

### Related Problems
- Meeting Rooms II: minimum rooms needed
- Merge Intervals: merge overlapping
- Non-overlapping Intervals: minimum removals
