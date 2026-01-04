# Top K Frequent Elements

## Summary

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer may be returned in any order.

### Key Points
- First count frequencies using a hash map
- Then select top k elements efficiently
- Three main approaches: heap, bucket sort, or quickselect

### Optimal Approach (Bucket Sort)
Use bucket sort where index represents frequency. This achieves O(n) time.

```python
from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result
```

### Complexity
- Time: O(n) - counting is O(n), bucket sort is O(n)
- Space: O(n) - for the frequency map and buckets

---

## Detailed Explanation

### Problem Analysis

This problem combines frequency counting with selection. The challenge is not just counting (straightforward with a hash map) but efficiently selecting the top k elements from potentially many unique values.

### Alternative Approaches

**Heap-Based Solution**
Maintain a min-heap of size k. For each unique element, add it to the heap. If the heap exceeds size k, remove the smallest.

```python
import heapq
from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

Or manually with a min-heap:

```python
def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]
```

- Time: O(n log k) - heap operations are O(log k)
- Space: O(n + k) - frequency map plus heap

**Quickselect Approach**
Use the quickselect algorithm to find the kth most frequent in O(n) average time.

```python
import random
from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    unique = list(count.keys())

    def partition(left, right, pivot_idx):
        pivot_freq = count[unique[pivot_idx]]
        unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]
        store_idx = left

        for i in range(left, right):
            if count[unique[i]] < pivot_freq:
                unique[store_idx], unique[i] = unique[i], unique[store_idx]
                store_idx += 1

        unique[right], unique[store_idx] = unique[store_idx], unique[right]
        return store_idx

    def quickselect(left, right, k_smallest):
        if left == right:
            return

        pivot_idx = random.randint(left, right)
        pivot_idx = partition(left, right, pivot_idx)

        if k_smallest == pivot_idx:
            return
        elif k_smallest < pivot_idx:
            quickselect(left, pivot_idx - 1, k_smallest)
        else:
            quickselect(pivot_idx + 1, right, k_smallest)

    n = len(unique)
    quickselect(0, n - 1, n - k)
    return unique[n - k:]
```

- Time: O(n) average, O(n^2) worst case
- Space: O(n)

### Why Bucket Sort Works Here

The maximum possible frequency is n (all elements are the same). By creating n+1 buckets (indices 0 to n), we can place each unique element in the bucket corresponding to its frequency. Then we iterate from highest frequency to lowest, collecting elements until we have k.

### Comparison of Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Bucket Sort | O(n) | O(n) | Best when k is large relative to unique elements |
| Heap | O(n log k) | O(n + k) | Best when k is small |
| Quickselect | O(n) avg | O(n) | Good average case, but worst case O(n^2) |

### Edge Cases
- k equals number of unique elements: return all unique elements
- All elements are the same: return that single element
- k = 1: return the single most frequent element

### Related Problems
- Kth Largest Element in an Array: similar selection problem
- Sort Characters By Frequency: frequency-based sorting
- Top K Frequent Words: similar but with lexicographic tiebreaker
