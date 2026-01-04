# Detect Squares

## Summary

Design a data structure to add points and count axis-aligned squares that can be formed with a query point as one corner.

### Key Points
- Store point counts (duplicates allowed)
- For a query point, find diagonal points that could form squares
- Verify the other two corners exist

### Optimal Approach
Hash map for point counts, iterate over possible diagonals.

```python
from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.point_count = defaultdict(int)
        self.points_at_x = defaultdict(list)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.point_count[(x, y)] += 1
        self.points_at_x[x].append(y)

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        result = 0

        for y2 in self.points_at_x[x1]:
            if y2 == y1:
                continue

            side = abs(y2 - y1)

            # Two possible squares (left and right of x1)
            for x2 in [x1 + side, x1 - side]:
                result += self.point_count[(x2, y1)] * self.point_count[(x2, y2)]

        return result
```

### Complexity
- add: O(1)
- count: O(n) where n is points with same x as query
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

For axis-aligned squares, if we fix one corner (x1, y1), the opposite diagonal corner (x2, y2) must satisfy:
- |x2 - x1| = |y2 - y1| (side length)
- The square is axis-aligned

Given query point (x1, y1), we:
1. Find all points on the same vertical line (x = x1)
2. For each such point (x1, y2), calculate side length
3. Check if the two remaining corners exist

### Why Multiply Counts?

If there are multiple copies of a point, each copy can form a different square. So we multiply the counts of the two corners we're checking.

### Alternative: Store All Points

```python
from collections import Counter

class DetectSquares:
    def __init__(self):
        self.point_count = Counter()

    def add(self, point: list[int]) -> None:
        self.point_count[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        result = 0

        for (x2, y2), count in self.point_count.items():
            # Check if (x2, y2) can be diagonal of square with (x1, y1)
            side = abs(x2 - x1)
            if side == 0 or side != abs(y2 - y1):
                continue

            # Check if other two corners exist
            result += count * self.point_count[(x1, y2)] * self.point_count[(x2, y1)]

        return result
```

This iterates over all points, O(n) per count.

### Step-by-Step Example

```
add([3, 10])
add([11, 2])
add([3, 2])

count([11, 10]):
  Query point: (11, 10)
  Points with x=11: (11, 2)
  Side = |10 - 2| = 8

  Check square with (11, 2) as diagonal:
    Other corners: (11+8, 10), (11+8, 2) = (19, 10), (19, 2) -> not present
    Other corners: (11-8, 10), (11-8, 2) = (3, 10), (3, 2) -> both present!

  Result: 1 * 1 = 1

add([11, 2])  # Duplicate

count([11, 10]):
  Now (11, 2) has count 2
  Check square with (11, 2):
    (3, 10) count = 1, (3, 2) count = 1
    Result: 2 * 1 * 1 = 2
```

### Optimized with Point-to-Y Mapping

```python
from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.point_count = defaultdict(int)
        self.x_to_ys = defaultdict(set)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.point_count[(x, y)] += 1
        self.x_to_ys[x].add(y)

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        result = 0

        for y2 in self.x_to_ys[x1]:
            if y2 == y1:
                continue

            side = abs(y2 - y1)

            for dx in [side, -side]:
                x2 = x1 + dx
                c1 = self.point_count[(x2, y1)]
                c2 = self.point_count[(x2, y2)]
                cnt_same_y = self.point_count[(x1, y2)]
                result += c1 * c2 * cnt_same_y

        return result
```

Wait, there's an issue - we're counting the diagonal point but it's on the same x. Let me fix:

```python
def count(self, point: list[int]) -> int:
    x1, y1 = point
    result = 0

    # For each point that shares x with query
    for y2 in self.x_to_ys[x1]:
        if y2 == y1:
            continue

        side = y2 - y1
        # The diagonal must be at (x1 + side, y1) and (x1 + side, y2)
        # Or at (x1 - side, y1) and (x1 - side, y2)
        # Wait, diagonal is at (x1 + side, y2) relative to (x1, y1)

        for x2 in [x1 + abs(side), x1 - abs(side)]:
            c1 = self.point_count[(x1, y2)]
            c2 = self.point_count[(x2, y1)]
            c3 = self.point_count[(x2, y2)]
            result += c1 * c2 * c3

    return result
```

### Edge Cases
- No points: count returns 0
- Query point not in set: still valid (it's the query, not stored)
- Duplicate points: each forms a separate square

### Related Problems
- Valid Square: check if four points form square
- Minimum Area Rectangle: find rectangle with points
- Number of Boomerangs: distance-based counting
