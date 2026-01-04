# Intervals

## Summary

Interval problems involve ranges defined by start and end points. Common operations include merging, finding overlaps, and scheduling.

### Core Concepts

1. **Overlap Detection**: Two intervals [a,b] and [c,d] overlap if a <= d AND c <= b
2. **Sorting Strategy**: Sort by start time or end time depending on the problem
3. **Sweep Line**: Process events (starts and ends) in order
4. **Greedy Selection**: For scheduling, often sort by end time

### Key Patterns

- Merge overlapping intervals
- Find maximum concurrent intervals
- Minimize removals for non-overlapping set
- Query intervals containing a point

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Insert Interval](./insert_interval/) | Merge | Add before, merge overlapping, add after |
| [Merge Intervals](./merge_intervals/) | Sort + merge | Sort by start, extend end when overlapping |
| [Non-overlapping Intervals](./non_overlapping_intervals/) | Greedy | Sort by end, keep earliest-ending non-overlap |
| [Meeting Rooms](./meeting_rooms/) | Overlap check | Sort by start, check consecutive overlaps |
| [Meeting Rooms II](./meeting_rooms_ii/) | Min-heap / sweep | Track concurrent meetings |
| [Minimum Interval](./minimum_interval_to_include_each_query/) | Sorted queries + heap | Process queries in order, track valid intervals |

---

## Common Patterns

### Pattern 1: Merge Overlapping Intervals

```python
def merge_intervals(intervals):
    intervals.sort()
    result = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])

    return result
```

### Pattern 2: Check for Any Overlap

```python
def has_overlap(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return True

    return False
```

### Pattern 3: Count Maximum Concurrent (Line Sweep)

```python
def max_concurrent(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))   # Start event
        events.append((end, -1))    # End event

    events.sort()

    concurrent = 0
    max_concurrent = 0

    for time, delta in events:
        concurrent += delta
        max_concurrent = max(max_concurrent, concurrent)

    return max_concurrent
```

### Pattern 4: Maximum Non-overlapping (Greedy)

```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end

    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            count += 1
            prev_end = end

    return count
```

### Pattern 5: Min-Heap for Concurrent Tracking

```python
import heapq

def min_rooms_needed(intervals):
    intervals.sort()
    heap = []  # End times of active intervals

    for start, end in intervals:
        if heap and start >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end)

    return len(heap)
```

---

## Overlap Conditions

### Two Intervals Overlap

[a, b] and [c, d] overlap if:
```
a <= d AND c <= b
```

Equivalently, they DON'T overlap if:
```
b < c OR d < a
```

### Merging Two Intervals

If overlapping:
```
merged = [min(a, c), max(b, d)]
```

---

## Key Takeaways

1. **Sort first** - by start for merging, by end for scheduling
2. **Sweep line** for counting concurrent intervals
3. **Min-heap** tracks earliest ending active interval
4. **Greedy by end time** maximizes non-overlapping count
5. **Process queries offline** when handling many queries
6. **Boundary conditions** - decide if touching intervals overlap
7. **Two pointers** can replace heap in some cases
