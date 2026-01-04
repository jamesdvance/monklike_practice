# Network Delay Time

## Summary

Given a network of n nodes and weighted directed edges representing signal travel times, find the time for a signal sent from node k to reach all nodes. Return -1 if not all nodes are reachable.

### Key Points
- This is single-source shortest path problem
- Use Dijkstra's algorithm for weighted graphs
- Answer is the maximum of shortest paths to all nodes

### Optimal Approach (Dijkstra's Algorithm)
Use a min-heap to find shortest paths from source to all nodes.

```python
import heapq
from collections import defaultdict

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {k: 0}
    heap = [(0, k)]  # (distance, node)

    while heap:
        d, node = heapq.heappop(heap)

        if d > dist.get(node, float('inf')):
            continue

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    if len(dist) == n:
        return max(dist.values())
    return -1
```

### Complexity
- Time: O(E log V) where E is edges and V is nodes
- Space: O(V + E)

---

## Detailed Explanation

### Problem Analysis

We need to find the shortest time for a signal to reach every node. The answer is the maximum shortest-path distance, since all signals travel in parallel.

If any node is unreachable, return -1.

### Dijkstra's Algorithm

1. Initialize distances: source = 0, others = infinity
2. Use min-heap to process nodes by distance
3. For each node, update neighbors if shorter path found
4. Skip nodes already processed with shorter distance

### Why Dijkstra Works

Dijkstra's algorithm works because:
1. We always process the node with smallest known distance
2. Once a node is processed, its shortest distance is final
3. This greedy approach works for non-negative weights

### Step-by-Step Example

```
times = [[2,1,1], [2,3,1], [3,4,1]], n = 4, k = 2

Graph:
2 -> 1 (weight 1)
2 -> 3 (weight 1)
3 -> 4 (weight 1)

Dijkstra from node 2:
Initial: dist = {2: 0}, heap = [(0, 2)]

Pop (0, 2):
  Neighbor 1: dist[1] = 0 + 1 = 1
  Neighbor 3: dist[3] = 0 + 1 = 1
  heap = [(1, 1), (1, 3)]

Pop (1, 1):
  No neighbors from 1
  heap = [(1, 3)]

Pop (1, 3):
  Neighbor 4: dist[4] = 1 + 1 = 2
  heap = [(2, 4)]

Pop (2, 4):
  No neighbors from 4

dist = {2: 0, 1: 1, 3: 1, 4: 2}
All 4 nodes reached.
Answer: max(0, 1, 1, 2) = 2
```

### Bellman-Ford Alternative

For graphs with negative weights (not this problem):

```python
def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    dist = [float('inf')] * (n + 1)
    dist[k] = 0

    for _ in range(n - 1):
        for u, v, w in times:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    max_dist = max(dist[1:n+1])
    return max_dist if max_dist < float('inf') else -1
```

Time: O(V * E), works with negative weights.

### BFS for Unweighted Graphs

If all weights were 1:

```python
from collections import deque, defaultdict

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append(v)

    dist = {k: 0}
    queue = deque([k])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return max(dist.values()) if len(dist) == n else -1
```

### Edge Cases
- Single node (k): return 0
- Unreachable node: return -1
- Self-loop at source: doesn't affect result

### Related Problems
- Cheapest Flights Within K Stops: Dijkstra with constraint
- Path with Maximum Probability: modified Dijkstra (max instead of min)
- Shortest Path in Binary Matrix: BFS for unweighted
