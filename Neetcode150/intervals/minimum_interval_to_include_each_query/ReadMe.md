# Minimum Interval to Include Each Query

## Summary

Given intervals and queries, for each query find the size of the smallest interval containing that query value. Return -1 if no interval contains the query.

### Key Points
- Process queries and intervals together in sorted order
- Use min-heap to track valid intervals by size
- Remove intervals that no longer contain current query

### Optimal Approach
Sort both, use heap to track active intervals.

```python
import heapq

def minInterval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    intervals.sort()
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

    result = [-1] * len(queries)
    heap = []  # (interval_size, interval_end)
    i = 0

    for query_idx, query in sorted_queries:
        # Add intervals that start before or at query
        while i < len(intervals) and intervals[i][0] <= query:
            left, right = intervals[i]
            heapq.heappush(heap, (right - left + 1, right))
            i += 1

        # Remove intervals that end before query
        while heap and heap[0][1] < query:
            heapq.heappop(heap)

        if heap:
            result[query_idx] = heap[0][0]

    return result
```

### Complexity
- Time: O((n + q) log n) where n is intervals, q is queries
- Space: O(n + q)

---

## Detailed Explanation

### Problem Analysis

For each query, we need the smallest interval [left, right] where left <= query <= right. This suggests:
1. Consider intervals in some order
2. Track which intervals are valid for current query
3. Pick the smallest valid interval

### Why Sort Queries?

Processing queries in sorted order allows us to:
1. Add intervals incrementally (as their start becomes relevant)
2. Remove intervals that are no longer valid (end < query)
3. Avoid reprocessing intervals

### The Heap Strategy

The heap contains (size, end) pairs:
- Ordered by size (smallest first)
- We push intervals whose start <= query
- We pop intervals whose end < query
- Top of heap (if valid) is our answer

### Step-by-Step Example

```
intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]

Sorted intervals: [[1,4],[2,4],[3,6],[4,4]]
Sorted queries with indices: [(0,2),(1,3),(2,4),(3,5)]

Query 2 (index 0):
  Add [1,4]: heap = [(4,4)]
  Add [2,4]: heap = [(3,4),(4,4)]
  No removal (all end >= 2)
  result[0] = 3

Query 3 (index 1):
  Add [3,6]: heap = [(3,4),(4,4),(4,6)]
  No removal
  result[1] = 3

Query 4 (index 2):
  Add [4,4]: heap = [(1,4),(3,4),(4,6),(4,4)]
  No removal
  result[2] = 1

Query 5 (index 3):
  No new intervals
  Remove (1,4), (3,4), (4,4) - all end < 5
  heap = [(4,6)]
  result[3] = 4

Answer: [3,3,1,4]
```

### Brute Force Approach

```python
def minInterval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    result = []

    for q in queries:
        min_size = float('inf')
        for left, right in intervals:
            if left <= q <= right:
                min_size = min(min_size, right - left + 1)
        result.append(min_size if min_size != float('inf') else -1)

    return result
```

Time: O(n * q), too slow for large inputs.

### Alternative: Offline Queries with Segment Tree

For competitive programming, segment trees can handle this efficiently, but the heap approach is simpler.

### Edge Cases
- Query outside all intervals: -1
- Multiple intervals of same size: any is valid
- Query exactly at interval boundary: included

### Related Problems
- Range Sum Query: interval/range processing
- My Calendar: interval scheduling
- Skyline Problem: sweepline with intervals
