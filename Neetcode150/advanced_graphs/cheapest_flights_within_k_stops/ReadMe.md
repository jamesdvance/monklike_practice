# Cheapest Flights Within K Stops

## Summary

Given n cities connected by flights with prices, find the cheapest price from src to dst with at most k stops. Return -1 if no such route exists.

### Key Points
- This is shortest path with a constraint on number of edges
- Standard Dijkstra doesn't work (might skip cheaper but longer paths)
- Use Bellman-Ford variant or modified BFS

### Optimal Approach (Bellman-Ford Variant)
Run k+1 iterations, relaxing all edges each time.

```python
def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    # dist[i] = cheapest price to reach city i
    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(k + 1):
        # Use copy to avoid using updated values in same iteration
        temp = dist.copy()

        for u, v, price in flights:
            if dist[u] != float('inf'):
                temp[v] = min(temp[v], dist[u] + price)

        dist = temp

    return dist[dst] if dist[dst] != float('inf') else -1
```

### Complexity
- Time: O(k * E) where E is number of flights
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

Unlike regular shortest path, we have a constraint: at most k stops means at most k+1 edges.

Standard Dijkstra might find a path with cost 100 using 3 edges, but miss a path with cost 50 using 5 edges (which might be valid if k >= 4).

### Why Bellman-Ford Works

Bellman-Ford relaxes all edges in each iteration:
- After iteration i, we have the shortest paths using at most i edges
- After k+1 iterations, we have paths with at most k+1 edges (k stops)

The key is using a copy of distances: we only use distances from the previous iteration, ensuring we don't use more edges than allowed.

### Step-by-Step Example

```
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0, dst = 3, k = 1 (at most 1 stop, so 2 edges)

Initial: dist = [0, inf, inf, inf]

Iteration 1 (1 edge):
  0->1: temp[1] = min(inf, 0+100) = 100
  1->2: can't use (dist[1] was inf)
  1->3: can't use (dist[1] was inf)
  dist = [0, 100, inf, inf]

Iteration 2 (2 edges):
  0->1: temp[1] = min(100, 0+100) = 100
  1->2: temp[2] = min(inf, 100+100) = 200
  1->3: temp[3] = min(inf, 100+600) = 700
  2->3: can't improve (dist[2] was inf)
  dist = [0, 100, 200, 700]

Answer: dist[3] = 700

Note: Path 0->1->2->3 costs 400 but needs 2 stops (3 edges), not allowed.
```

### BFS with Level Tracking

```python
from collections import defaultdict, deque

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # (cost, city, stops)
    dist = [float('inf')] * n
    dist[src] = 0

    queue = deque([(0, src, 0)])  # (cost, city, stops)

    while queue:
        cost, city, stops = queue.popleft()

        if stops > k:
            continue

        for neighbor, price in graph[city]:
            new_cost = cost + price
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                queue.append((new_cost, neighbor, stops + 1))

    return dist[dst] if dist[dst] != float('inf') else -1
```

Note: This BFS approach needs careful handling - we might need to revisit nodes with fewer stops even if cost is higher.

### Modified Dijkstra

```python
import heapq
from collections import defaultdict

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # (cost, city, stops_remaining)
    heap = [(0, src, k + 1)]
    visited = {}  # city -> min stops used to reach

    while heap:
        cost, city, stops = heapq.heappop(heap)

        if city == dst:
            return cost

        if city in visited and visited[city] >= stops:
            continue
        visited[city] = stops

        if stops > 0:
            for neighbor, price in graph[city]:
                heapq.heappush(heap, (cost + price, neighbor, stops - 1))

    return -1
```

We track stops remaining and skip states that used more edges than a previous visit.

### Why Standard Dijkstra Fails

Dijkstra marks a node "done" after first visit (cheapest cost). But with the k constraint, we might need a more expensive path that uses fewer stops to reach further destinations.

### Edge Cases
- src == dst: return 0
- No path within k stops: return -1
- k >= n-1: standard shortest path
- Direct flight exists: compare with multi-hop

### Related Problems
- Network Delay Time: standard Dijkstra
- Path with Maximum Probability: modified shortest path
- Shortest Path with Alternating Colors: constrained BFS
