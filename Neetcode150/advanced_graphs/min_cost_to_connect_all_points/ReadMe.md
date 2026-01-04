# Min Cost to Connect All Points

## Summary

Given an array of points on a 2D plane, return the minimum cost to connect all points. The cost of connecting two points is their Manhattan distance. This is a Minimum Spanning Tree (MST) problem.

### Key Points
- Connect all nodes with minimum total edge weight
- Use Prim's or Kruskal's algorithm
- Edge weight = Manhattan distance = |x1-x2| + |y1-y2|

### Optimal Approach (Prim's Algorithm)
Use a min-heap to greedily add the cheapest edge.

```python
import heapq

def minCostConnectPoints(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0

    # Calculate Manhattan distance
    def dist(i, j):
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    visited = set()
    heap = [(0, 0)]  # (cost, node)
    total_cost = 0

    while len(visited) < n:
        cost, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += cost

        for neighbor in range(n):
            if neighbor not in visited:
                heapq.heappush(heap, (dist(node, neighbor), neighbor))

    return total_cost
```

### Complexity
- Time: O(n^2 log n) - n^2 edges, each pushed to heap
- Space: O(n^2) for the heap in worst case

---

## Detailed Explanation

### Problem Analysis

This is the Minimum Spanning Tree problem:
- Every point is a node
- Every pair of points has an edge (complete graph)
- Edge weight = Manhattan distance
- Find subset of edges that connects all nodes with minimum total weight

### Prim's Algorithm

1. Start from any node
2. Add it to the MST
3. Push all edges from this node to a min-heap
4. Pop the minimum edge to an unvisited node
5. Add that node to MST, push its edges
6. Repeat until all nodes are in MST

### Kruskal's Algorithm Alternative

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def minCostConnectPoints(points: list[list[int]]) -> int:
    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))

    edges.sort()
    uf = UnionFind(n)
    total_cost = 0
    edges_used = 0

    for cost, u, v in edges:
        if uf.union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break

    return total_cost
```

Kruskal's: Sort all edges, add smallest that doesn't create cycle.

### Optimized Prim's (No Explicit Heap)

```python
def minCostConnectPoints(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0

    # min_dist[i] = minimum distance from i to any node in MST
    min_dist = [float('inf')] * n
    min_dist[0] = 0
    in_mst = [False] * n
    total_cost = 0

    for _ in range(n):
        # Find node with minimum distance to MST
        u = -1
        for i in range(n):
            if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                u = i

        in_mst[u] = True
        total_cost += min_dist[u]

        # Update distances
        for v in range(n):
            if not in_mst[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                min_dist[v] = min(min_dist[v], dist)

    return total_cost
```

Time: O(n^2), Space: O(n). Better for dense graphs.

### Step-by-Step Example

```
points = [[0,0], [2,2], [3,10], [5,2], [7,0]]

Prim's starting from node 0:
MST = {0}
Edges from 0: (4, 1), (13, 2), (7, 3), (7, 4)
Pop (4, 1), add 1 to MST, cost = 4

MST = {0, 1}
Edges from 1: (9, 2), (3, 3), (7, 4)
Pop (3, 3), add 3 to MST, cost = 4 + 3 = 7

MST = {0, 1, 3}
Edges from 3: (10, 2), (4, 4)
Pop (4, 4), add 4 to MST, cost = 7 + 4 = 11

MST = {0, 1, 3, 4}
Remaining: (9, 2) or (10, 2) -> use (9, 2)
Add 2, cost = 11 + 9 = 20

Total: 20
```

### Comparison: Prim's vs Kruskal's

| Aspect | Prim's | Kruskal's |
|--------|--------|-----------|
| Approach | Grow tree from one node | Add edges globally |
| Data Structure | Min-heap | Union-Find |
| Better for | Dense graphs | Sparse graphs |
| Time | O(E log V) with heap | O(E log E) |

### Edge Cases
- Single point: return 0
- Two points: return distance between them
- All points on a line: MST is the path along the line

### Related Problems
- Connecting Cities With Minimum Cost: weighted MST
- Optimize Water Distribution: MST with virtual node
- Find Critical and Pseudo-Critical Edges: MST edge analysis
