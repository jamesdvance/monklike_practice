# Task Scheduler

## Summary

Given tasks represented by characters and a cooldown period n between same tasks, find the minimum time to complete all tasks. The CPU can be idle.

### Key Points
- Most frequent tasks determine the minimum time
- Interleave different tasks to minimize idle time
- Use a max-heap for greedy task selection

### Optimal Approach (Math Formula)
Calculate based on the most frequent task.

```python
from collections import Counter

def leastInterval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for count in counts.values() if count == max_count)

    # Formula: (max_count - 1) * (n + 1) + num_max
    min_time = (max_count - 1) * (n + 1) + num_max

    # At minimum, we need len(tasks) time
    return max(min_time, len(tasks))
```

### Complexity
- Time: O(n) where n is number of tasks
- Space: O(1) - at most 26 different tasks

---

## Detailed Explanation

### Problem Analysis

Consider tasks with cooldown n=2:
- Task A appears 3 times
- Must have at least 2 other slots between A's: A _ _ A _ _ A

The minimum structure is determined by the most frequent task. Other tasks fill the gaps.

### The Formula Explained

For the most frequent task with count `max_count`:
- We need `max_count - 1` gaps between them
- Each gap has `n + 1` slots (the task itself plus n cooldown)
- Final structure: `(max_count - 1) * (n + 1) + num_max`

```
n = 2, tasks = [A, A, A, B, B, B]
max_count = 3, num_max = 2

A _ _ A _ _ A
A B _ A B _ A B

Time = (3-1) * (2+1) + 2 = 8
```

### Why max(formula, len(tasks))?

When there are many different tasks, all gaps get filled and we might need more time than the formula suggests:

```
n = 1, tasks = [A, A, B, B, C, C, D, D]
Formula: (2-1) * (1+1) + 4 = 6
But we have 8 tasks, so answer is 8
```

### Heap + Queue Approach

Simulate the process using a max-heap and cooldown queue:

```python
from collections import Counter, deque
import heapq

def leastInterval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    heap = [-count for count in counts.values()]
    heapq.heapify(heap)

    time = 0
    queue = deque()  # (available_time, remaining_count)

    while heap or queue:
        time += 1

        if heap:
            count = heapq.heappop(heap) + 1  # Decrement (add 1 to negative)
            if count != 0:
                queue.append((time + n, count))

        if queue and queue[0][0] == time:
            heapq.heappush(heap, queue.popleft()[1])

    return time
```

This simulates each time unit, useful for understanding but slower.

### Step-by-Step Example

tasks = ["A","A","A","B","B","B"], n = 2

```
Counts: A=3, B=3
max_count = 3, num_max = 2

Frame structure:
Slot: [A, _, _] [A, _, _] [A]
Fill B:  [A, B, _] [A, B, _] [A, B]

Time = (3-1) * 3 + 2 = 8
```

Alternatively:
```
A B idle A B idle A B
1 2  3   4 5  6   7 8
```

### Edge Cases
- n = 0: no cooldown, return len(tasks)
- All tasks same: (count - 1) * (n + 1) + 1
- Many unique tasks: return len(tasks)

### Related Problems
- Rearrange String K Distance Apart: similar constraint
- Reorganize String: no adjacent same characters
- CPU Scheduling algorithms: real-world analog
