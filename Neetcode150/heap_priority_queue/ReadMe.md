# Heap / Priority Queue

## Summary

Heaps are tree-based data structures that maintain a partial ordering. A min-heap keeps the smallest element at the root; a max-heap keeps the largest. Python's `heapq` module implements a min-heap.

### Core Concepts

1. **Heap Property**: Parent is smaller (min-heap) or larger (max-heap) than children
2. **Complete Binary Tree**: Filled level by level, left to right
3. **Array Representation**: Parent at i, children at 2i+1 and 2i+2
4. **Key Operations**: O(log n) push/pop, O(1) peek

### When to Use Heaps

- Finding k largest/smallest elements
- Merging k sorted sequences
- Scheduling with priorities
- Streaming median or percentiles
- Greedy algorithms requiring repeated min/max selection

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Kth Largest Element in a Stream](./kth_largest_element_in_a_stream/) | Min-heap of size k | Maintain k largest; root is kth |
| [Last Stone Weight](./last_stone_weight/) | Max-heap simulation | Negate values for max-heap in Python |
| [K Closest Points to Origin](./k_closest_points_to_origin/) | Max-heap of size k | Keep k smallest distances |
| [Kth Largest Element in an Array](./kth_largest_element_in_an_array/) | Quickselect or Heap | O(n) average with quickselect |
| [Task Scheduler](./task_scheduler/) | Greedy with heap or math | Most frequent task determines structure |
| [Design Twitter](./design_twitter/) | K-way merge | Merge sorted tweet lists from followed users |
| [Find Median from Data Stream](./find_median_from_data_stream/) | Two heaps | Max-heap for lower half, min-heap for upper |

---

## Common Patterns

### Pattern 1: Min-Heap of Size K (Find K Largest)

```python
import heapq

def k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap  # Contains k largest elements
```

The smallest of the k largest is always at the root.

### Pattern 2: Max-Heap via Negation

```python
import heapq

def max_heap_example(nums):
    # Negate values to simulate max-heap
    heap = [-num for num in nums]
    heapq.heapify(heap)

    largest = -heapq.heappop(heap)  # Negate back
    return largest
```

Python only has min-heap, so negate values for max-heap behavior.

### Pattern 3: Two Heaps for Median

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []   # Max-heap (negated) for lower half
        self.high = []  # Min-heap for upper half

    def add(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

Partition elements around the median for O(1) retrieval.

### Pattern 4: K-Way Merge

```python
import heapq

def merge_k_sorted(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

Merge multiple sorted sequences efficiently.

### Pattern 5: Heap with Delayed Removal

```python
import heapq
from collections import Counter

class LazyHeap:
    def __init__(self):
        self.heap = []
        self.removed = Counter()

    def push(self, val):
        heapq.heappush(self.heap, val)

    def remove(self, val):
        self.removed[val] += 1

    def pop(self):
        self._clean()
        return heapq.heappop(self.heap)

    def top(self):
        self._clean()
        return self.heap[0]

    def _clean(self):
        while self.heap and self.removed[self.heap[0]] > 0:
            self.removed[heapq.heappop(self.heap)] -= 1
```

When arbitrary removal is needed, mark as removed and clean lazily.

---

## Complexity Summary

| Operation | Time | Notes |
|-----------|------|-------|
| heappush | O(log n) | Add element |
| heappop | O(log n) | Remove and return smallest |
| heapify | O(n) | Build heap from list |
| heap[0] | O(1) | Peek at smallest |
| heapq.nlargest(k, iterable) | O(n log k) | Find k largest |
| heapq.nsmallest(k, iterable) | O(n log k) | Find k smallest |

---

## Key Takeaways

1. **Min-heap of size k** finds k largest elements efficiently
2. **Negate values** for max-heap behavior in Python
3. **Two heaps** partition data for streaming median
4. **K-way merge** combines sorted sequences in O(n log k)
5. **Quickselect** can be faster than heap for single queries (O(n) vs O(n log k))
6. **Lazy deletion** handles removal when indices are unknown
7. **Heap with tuples** allows custom ordering: `(priority, tiebreaker, value)`
