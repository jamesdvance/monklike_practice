# Advanced Graphs

## Summary

Advanced graph algorithms extend basic traversal to solve optimization problems: finding shortest paths with weights, minimum spanning trees, and handling special constraints.

### Core Concepts

1. **Dijkstra's Algorithm**: Shortest path with non-negative weights
2. **Bellman-Ford**: Shortest path with negative weights or edge constraints
3. **Minimum Spanning Tree**: Connect all nodes with minimum total weight
4. **Topological Sort with Constraints**: Ordering with precedence rules
5. **Eulerian Paths**: Visit every edge exactly once

### When to Use Each Algorithm

- **Dijkstra**: Weighted shortest path, non-negative weights
- **Bellman-Ford**: Negative weights or limited number of edges
- **Prim's/Kruskal's**: Minimum spanning tree
- **Modified BFS/DFS**: Special path constraints (minimax, etc.)

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Reconstruct Itinerary](./reconstruct_itinerary/) | Eulerian Path | Hierholzer's algorithm with lexical ordering |
| [Min Cost to Connect All Points](./min_cost_to_connect_all_points/) | MST (Prim's/Kruskal's) | Manhattan distance as edge weight |
| [Network Delay Time](./network_delay_time/) | Dijkstra | Max of shortest paths to all nodes |
| [Swim in Rising Water](./swim_in_rising_water/) | Modified Dijkstra | Minimize maximum elevation on path |
| [Alien Dictionary](./alien_dictionary/) | Topological Sort | Build ordering from word comparisons |
| [Cheapest Flights Within K Stops](./cheapest_flights_within_k_stops/) | Bellman-Ford | Limit iterations to k+1 edges |

---

## Common Patterns

### Pattern 1: Dijkstra's Algorithm

```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = {source: 0}
    heap = [(0, source)]

    while heap:
        d, node = heapq.heappop(heap)

        if d > dist.get(node, float('inf')):
            continue

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist
```

### Pattern 2: Bellman-Ford

```python
def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None  # Negative cycle

    return dist
```

### Pattern 3: Prim's MST

```python
import heapq

def prim_mst(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = set()
    heap = [(0, 0)]  # (weight, node)
    total = 0

    while len(visited) < n:
        weight, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        total += weight

        for w, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (w, neighbor))

    return total
```

### Pattern 4: Kruskal's MST

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

def kruskal_mst(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    total = 0
    count = 0

    for u, v, w in edges:
        if uf.union(u, v):
            total += w
            count += 1
            if count == n - 1:
                break

    return total if count == n - 1 else -1
```

### Pattern 5: Minimax Path (Modified Dijkstra)

```python
import heapq

def minimax_path(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]  # (max_so_far, r, c)

    while heap:
        max_val, r, c = heapq.heappop(heap)

        if r == n-1 and c == n-1:
            return max_val

        if visited[r][c]:
            continue
        visited[r][c] = True

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                new_max = max(max_val, grid[nr][nc])
                heapq.heappush(heap, (new_max, nr, nc))

    return -1
```

---

## Algorithm Comparison

| Algorithm | Time | Space | Weights | Use Case |
|-----------|------|-------|---------|----------|
| Dijkstra | O(E log V) | O(V) | Non-negative | Standard shortest path |
| Bellman-Ford | O(VE) | O(V) | Any | Negative weights, edge limits |
| Prim's | O(E log V) | O(V) | Any | MST from single node |
| Kruskal's | O(E log E) | O(V) | Any | MST, sparse graphs |
| Floyd-Warshall | O(V^3) | O(V^2) | Any | All-pairs shortest path |

---

## Key Takeaways

1. **Dijkstra** requires non-negative weights; use Bellman-Ford otherwise
2. **Bellman-Ford** can be modified for edge count constraints
3. **MST algorithms** (Prim's/Kruskal's) connect all nodes with minimum cost
4. **Minimax paths** use modified Dijkstra with max instead of sum
5. **Topological sort** from constraints builds ordering from pairwise comparisons
6. **Eulerian paths** visit every edge once; use Hierholzer's algorithm
7. Copy distance arrays in Bellman-Ford to prevent using same-iteration updates
