# Kth Largest Element in a Stream

## Summary

Design a class that finds the kth largest element in a stream. The class should support adding new numbers and returning the kth largest after each addition.

### Key Points
- Maintain a min-heap of size k
- The root of the heap is always the kth largest
- New elements only matter if larger than current kth largest

### Optimal Approach
Use a min-heap of size k. The smallest element in the heap is the kth largest overall.

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
```

### Complexity
- Constructor: O(n log k) where n is initial array size
- add(): O(log k)
- Space: O(k)

---

## Detailed Explanation

### Problem Analysis

We need to efficiently track the kth largest element as new values are added. A min-heap of size k achieves this:
- The heap contains the k largest elements seen
- The root (minimum of the heap) is the kth largest overall
- Adding an element that is smaller than the kth largest does not change the answer

### Why Min-Heap of Size k?

Consider finding the 3rd largest in [4, 5, 8, 2]:
- Sorted descending: [8, 5, 4, 2]
- 3rd largest = 4

If we keep a min-heap of the 3 largest: [4, 5, 8]
- Min-heap property: root is smallest = 4
- This is our 3rd largest

When we add a new element:
- If smaller than root (kth largest): ignore or pop it after push
- If larger than root: it displaces the current kth largest

### Step-by-Step Example

k = 3, nums = [4, 5, 8, 2]

```
Initial: heapify [4, 5, 8, 2] = [2, 4, 8, 5]
Pop until size 3: [4, 5, 8] (min-heap: root = 4)

add(3): push 3, heap = [3, 4, 8, 5], pop min, heap = [4, 5, 8]
        return 4

add(5): push 5, heap = [4, 5, 8, 5], pop min, heap = [5, 5, 8]
        return 5

add(10): push 10, heap = [5, 5, 10, 8], pop min, heap = [5, 8, 10]
         return 5

add(9): push 9, heap = [5, 8, 10, 9], pop min, heap = [8, 9, 10]
        return 8
```

### Alternative: Sorted List with Binary Search

```python
import bisect

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]
```

- add(): O(n) due to insertion in sorted list
- Less efficient for large streams

### Edge Cases
- Initial array has fewer than k elements: add returns root once heap has k elements
- All elements are the same: kth largest equals that value
- k = 1: always return the maximum

### Related Problems
- Kth Largest Element in an Array: one-time query
- Find Median from Data Stream: similar streaming problem
- Top K Frequent Elements: uses heap for selection
