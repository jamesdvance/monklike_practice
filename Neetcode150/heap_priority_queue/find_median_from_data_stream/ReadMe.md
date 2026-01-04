# Find Median from Data Stream

## Summary

Design a data structure that supports adding integers and finding the median of all elements added so far.

### Key Points
- Use two heaps: max-heap for lower half, min-heap for upper half
- Balance heaps so sizes differ by at most 1
- Median is either top of larger heap or average of both tops

### Optimal Approach
Maintain two heaps that partition the stream around the median.

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []   # Max-heap (negated) for lower half
        self.high = []  # Min-heap for upper half

    def addNum(self, num: int) -> None:
        # Add to max-heap (low)
        heapq.heappush(self.low, -num)

        # Ensure max of low <= min of high
        if self.low and self.high and -self.low[0] > self.high[0]:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)

        # Balance sizes (low can have at most 1 more element)
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

### Complexity
- addNum: O(log n)
- findMedian: O(1)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

The median of a sorted list is:
- If odd length: the middle element
- If even length: average of two middle elements

To find the median efficiently, we partition elements into two halves:
- Lower half: elements <= median (max-heap to access largest)
- Upper half: elements >= median (min-heap to access smallest)

### Why Two Heaps?

A sorted list would give O(1) median but O(n) insertion. Two heaps give:
- O(log n) insertion (heap push/pop)
- O(1) median (heap tops)

### Invariants to Maintain

1. **Ordering**: max(low) <= min(high)
   - All elements in low are <= all elements in high

2. **Size balance**: |len(low) - len(high)| <= 1
   - Either equal sizes (even total) or low has one more (odd total)

### Step-by-Step Example

Add: 1, 2, 3, 4, 5

```
Add 1: low=[-1], high=[]
       Median = 1

Add 2: low=[-1], high=[2] (balance)
       Median = (1+2)/2 = 1.5

Add 3: low=[-2,-1], high=[3] (add to low, rebalance)
       Median = 2

Add 4: low=[-2,-1], high=[3,4] (balance)
       Median = (2+3)/2 = 2.5

Add 5: low=[-3,-2,-1], high=[4,5]
       Median = 3
```

### Alternative: Add to High First

Different but equivalent logic:

```python
def addNum(self, num: int) -> None:
    heapq.heappush(self.high, num)
    heapq.heappush(self.low, -heapq.heappop(self.high))

    if len(self.low) > len(self.high):
        heapq.heappush(self.high, -heapq.heappop(self.low))
```

This always pushes to high first, then balances.

### Follow-Up: Handle Duplicates

The two-heap approach handles duplicates naturally - they can appear in either heap as long as invariants are maintained.

### Follow-Up: 99th Percentile Instead of Median

Adjust the size ratio:
- low should have 99% of elements
- high should have 1%
- 99th percentile is top of low

### Edge Cases
- Single element: return that element
- Two elements: return average
- All same elements: return that value

### Related Problems
- Sliding Window Median: median over a window
- Kth Largest Element in a Stream: similar streaming problem
- Data Stream as Disjoint Intervals: different stream aggregation
