# Meeting Rooms II

## Summary

Given an array of meeting time intervals, return the minimum number of conference rooms required.

### Key Points
- Track overlapping meetings at any point in time
- Use min-heap to track earliest ending meeting
- Or use line sweep with start/end events

### Optimal Approach (Min-Heap)
Use heap to track active meetings.

```python
import heapq

def minMeetingRooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    # Min-heap of end times
    heap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        # If current meeting starts after earliest ending meeting
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, intervals[i][1])

    return len(heap)
```

### Complexity
- Time: O(n log n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

At any point in time, the number of rooms needed equals the number of concurrent meetings. We need the maximum concurrent meetings.

### Min-Heap Approach

The heap contains end times of active meetings. When a new meeting starts:
1. Remove meetings that have ended (end time <= start time)
2. Add the new meeting
3. Heap size = rooms needed for this moment

We only remove the earliest ending meeting because:
- If it hasn't ended, no other meeting has ended either
- We only need to free one room per new meeting

### Step-by-Step Example

```
intervals = [[0,30],[5,10],[15,20]]

Sorted: [[0,30],[5,10],[15,20]]

heap = [30] (first meeting ends at 30)

[5,10]: 5 < 30 -> can't reuse room
heap = [10, 30]

[15,20]: 15 >= 10 -> reuse room (pop 10)
heap = [30]
push 20: heap = [20, 30]

Max rooms needed: 2
```

### Line Sweep Approach

```python
def minMeetingRooms(intervals: list[list[int]]) -> int:
    events = []
    for start, end in intervals:
        events.append((start, 1))   # Meeting starts
        events.append((end, -1))    # Meeting ends

    events.sort()

    rooms = 0
    max_rooms = 0

    for time, delta in events:
        rooms += delta
        max_rooms = max(max_rooms, rooms)

    return max_rooms
```

Sort events, +1 at start, -1 at end. Track maximum concurrent.

### Two Pointers on Sorted Arrays

```python
def minMeetingRooms(intervals: list[list[int]]) -> int:
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)

    rooms = 0
    end_ptr = 0

    for start in starts:
        if start >= ends[end_ptr]:
            end_ptr += 1  # Reuse a room
        else:
            rooms += 1    # Need new room

    return rooms
```

### Visualization

```
Time:    0   5   10   15   20   30
Meeting1: [======================]
Meeting2:     [===]
Meeting3:              [====]

Max concurrent: 2 (at time 5-10, meetings 1 and 2)
```

### Edge Cases
- Empty intervals: 0 rooms
- No overlaps: 1 room
- All overlap at same time: n rooms
- Back-to-back meetings: can reuse same room

### Related Problems
- Meeting Rooms: check if any overlap
- Car Pooling: capacity constraint
- Maximum Number of Events: scheduling with constraint
