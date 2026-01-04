# Kth Largest Element in an Array

## Summary

Given an integer array and an integer k, return the kth largest element. This is the kth largest in sorted order, not the kth distinct element.

### Key Points
- Three main approaches: sort, heap, quickselect
- Quickselect gives O(n) average time
- Heap gives O(n log k) time

### Optimal Approach (Quickselect)
Use quickselect to find the kth largest in O(n) average time.

```python
import random

def findKthLargest(nums: list[int], k: int) -> int:
    k = len(nums) - k  # Convert to kth smallest (0-indexed)

    def quickselect(left, right):
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]

        # Move pivot to end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        # Partition
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1

        # Move pivot to final position
        nums[store_idx], nums[right] = nums[right], nums[store_idx]

        if store_idx == k:
            return nums[store_idx]
        elif store_idx < k:
            return quickselect(store_idx + 1, right)
        else:
            return quickselect(left, store_idx - 1)

    return quickselect(0, len(nums) - 1)
```

### Complexity
- Time: O(n) average, O(n^2) worst case
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Finding the kth largest is equivalent to finding the (n-k+1)th smallest. We can:
1. Sort and index: O(n log n)
2. Use a heap: O(n log k)
3. Use quickselect: O(n) average

### Heap Approach

Min-heap of size k:

```python
import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
```

Or using heapq.nlargest:

```python
def findKthLargest(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
```

### Why Quickselect Works

Quickselect is like quicksort but only recurses on one side:
1. Pick a pivot and partition around it
2. If pivot is at position k, we found the answer
3. If pivot position < k, recurse on right side
4. If pivot position > k, recurse on left side

Unlike quicksort (which recurses on both sides), quickselect only explores one partition, giving O(n) average time.

### Random Pivot Importance

A random pivot prevents worst-case O(n^2) on sorted or nearly-sorted input. Without randomization, a sorted array would cause the worst case every time.

### Step-by-Step Example

nums = [3, 2, 1, 5, 6, 4], k = 2

kth largest = 2nd largest = 5
Convert: find (6-2) = 4th smallest (0-indexed)

```
Partition around pivot (say 4):
[3, 2, 1] [4] [5, 6]
pivot at index 3

k=4 > 3, recurse on right [5, 6]
Partition around pivot (say 5):
[] [5] [6]
pivot at index 4

k=4, found! return 5
```

### Comparison of Approaches

| Approach | Time (avg) | Time (worst) | Space |
|----------|------------|--------------|-------|
| Sort | O(n log n) | O(n log n) | O(1)* |
| Min-Heap | O(n log k) | O(n log k) | O(k) |
| Quickselect | O(n) | O(n^2) | O(1) |

*Depends on sort implementation

### Edge Cases
- k = 1: find maximum
- k = n: find minimum
- All elements same: return that element
- Duplicates: handled correctly (not distinct kth)

### Related Problems
- Kth Largest Element in a Stream: online version
- Top K Frequent Elements: similar selection
- Find Median from Data Stream: k = n/2
