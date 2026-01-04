# K Closest Points to Origin

## Summary

Given an array of points on a 2D plane, return the k closest points to the origin (0, 0). Distance is Euclidean distance.

### Key Points
- Distance = sqrt(x^2 + y^2), but we can compare x^2 + y^2 directly
- Use a max-heap of size k to keep track of k closest
- Or use quickselect for O(n) average time

### Optimal Approach (Heap)
Use a max-heap of size k. Push all points, maintaining only k closest.

```python
import heapq

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    # Max-heap of size k (negate distance for max behavior)
    heap = []

    for x, y in points:
        dist = -(x * x + y * y)  # Negate for max-heap
        heapq.heappush(heap, (dist, [x, y]))

        if len(heap) > k:
            heapq.heappop(heap)

    return [point for _, point in heap]
```

### Complexity
- Time: O(n log k)
- Space: O(k)

---

## Detailed Explanation

### Problem Analysis

We need to find the k points with smallest Euclidean distance to origin. Instead of computing actual distance (which involves sqrt), we compare squared distances since sqrt is monotonic.

### Why Max-Heap of Size k?

A max-heap of size k contains the k smallest distances:
- When a new point has smaller distance than the max in heap, it should be included
- We pop the max (farthest of the k closest) and push the new point
- At the end, heap contains k closest points

### Alternative: Min-Heap of All Points

```python
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = [(x*x + y*y, [x, y]) for x, y in points]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]
```

- Time: O(n + k log n)
- Space: O(n)

This builds a min-heap of all points, then pops k smallest.

### Alternative: Quickselect

Partition points to find k closest in O(n) average time:

```python
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    def distance(point):
        return point[0]**2 + point[1]**2

    def partition(left, right, pivot_idx):
        pivot_dist = distance(points[pivot_idx])
        points[pivot_idx], points[right] = points[right], points[pivot_idx]
        store_idx = left

        for i in range(left, right):
            if distance(points[i]) < pivot_dist:
                points[store_idx], points[i] = points[i], points[store_idx]
                store_idx += 1

        points[right], points[store_idx] = points[store_idx], points[right]
        return store_idx

    left, right = 0, len(points) - 1
    while left <= right:
        pivot_idx = (left + right) // 2
        pivot_idx = partition(left, right, pivot_idx)

        if pivot_idx == k:
            break
        elif pivot_idx < k:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1

    return points[:k]
```

- Time: O(n) average, O(n^2) worst
- Space: O(1)

### Sorting Approach (Simple but Slower)

```python
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]
```

- Time: O(n log n)
- Space: O(1) or O(n) depending on sort

### Edge Cases
- k equals n: return all points
- k = 1: return the closest point
- Multiple points at same distance: any ordering is valid

### Related Problems
- Kth Largest Element in an Array: similar selection problem
- Top K Frequent Elements: similar k selection
- Closest Binary Search Tree Value II: k closest in BST
