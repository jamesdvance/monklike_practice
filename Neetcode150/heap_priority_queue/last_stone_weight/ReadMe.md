# Last Stone Weight

## Summary

Given an array of stone weights, repeatedly smash the two heaviest stones together. If they have equal weight, both are destroyed. Otherwise, the heavier stone's weight becomes the difference. Return the weight of the last remaining stone, or 0 if none remain.

### Key Points
- Need to repeatedly find the two largest elements
- Max-heap provides O(log n) access to maximum
- Python's heapq is min-heap, so negate values

### Optimal Approach
Use a max-heap (simulated with negated values) to always get the heaviest stones.

```python
import heapq

def lastStoneWeight(stones: list[int]) -> int:
    # Negate for max-heap behavior
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)

        if first != second:
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0
```

### Complexity
- Time: O(n log n) - up to n-1 smashes, each with O(log n) heap operations
- Space: O(n) for the heap

---

## Detailed Explanation

### Problem Analysis

Each turn, we need the two heaviest stones. A max-heap gives O(log n) access to the maximum. After smashing:
- If equal: both destroyed, remove both from heap
- If different: replace with difference

### Why Max-Heap?

A max-heap keeps the maximum at the root, allowing O(1) access to the heaviest stone. Python's `heapq` is a min-heap, so we negate values to simulate max-heap behavior.

### Step-by-Step Example

stones = [2, 7, 4, 1, 8, 1]

```
Max-heap (negated): [-8, -7, -4, -1, -2, -1]

Pop 8, 7: smash, 8-7=1, push 1
Heap: [-4, -2, -1, -1, -1]

Pop 4, 2: smash, 4-2=2, push 2
Heap: [-2, -1, -1, -1]

Pop 2, 1: smash, 2-1=1, push 1
Heap: [-1, -1, -1]

Pop 1, 1: smash, equal, both destroyed
Heap: [-1]

Return 1
```

### Alternative: Sorting Each Iteration

```python
def lastStoneWeight(stones: list[int]) -> int:
    while len(stones) > 1:
        stones.sort()
        first = stones.pop()
        second = stones.pop()
        if first != second:
            stones.append(first - second)

    return stones[0] if stones else 0
```

- Time: O(n^2 log n) - sorting each iteration
- Simpler but less efficient

### Simulation vs Optimal

The simulation always produces the correct final result. There is no "strategy" to minimize or maximize the final stone - the order of operations does not matter for the final outcome (though proving this requires more analysis).

### Edge Cases
- Single stone: return its weight
- Two equal stones: return 0
- All stones destroyed: return 0

### Related Problems
- Last Stone Weight II: minimize final stone using DP
- Kth Largest Element in an Array: similar heap usage
- Meeting Rooms II: priority queue for scheduling
