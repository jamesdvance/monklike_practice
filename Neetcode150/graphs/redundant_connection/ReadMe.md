# Redundant Connection

## Summary

Given a graph that started as a tree with n nodes and had one extra edge added, find that edge. The extra edge creates exactly one cycle. Return the edge that appears last in the input that is part of the cycle.

### Key Points
- A tree with n nodes has exactly n-1 edges
- Adding one edge creates one cycle
- Use Union-Find to detect the edge that connects already-connected nodes

### Optimal Approach (Union-Find)
The first edge that connects two already-connected nodes is redundant.

```python
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1))
    rank = [0] * (len(edges) + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # Already connected - cycle!

        # Union by rank
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]

    return []
```

### Complexity
- Time: O(n * alpha(n)) which is nearly O(n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

A tree with n nodes has n-1 edges. Adding one edge creates exactly one cycle. We need to find the edge that, when removed, restores the tree property.

The edge that "completes" the cycle is the one connecting two nodes that are already connected through other edges.

### Union-Find Approach

Process edges in order. When we try to connect two nodes that are already in the same component (same root), we've found the redundant edge.

### Step-by-Step Example

```
edges = [[1,2], [1,3], [2,3]]

Edge [1,2]: union(1,2) -> success
  Components: {1,2}, {3}

Edge [1,3]: union(1,3) -> success
  Components: {1,2,3}

Edge [2,3]: union(2,3) -> already connected!
  find(2) = find(3) = 1
  Return [2,3]
```

### DFS Alternative

Find the cycle using DFS, then return the last edge in the cycle.

```python
from collections import defaultdict

def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    graph = defaultdict(set)

    def has_path(source, target, visited):
        if source == target:
            return True
        visited.add(source)
        for neighbor in graph[source]:
            if neighbor not in visited:
                if has_path(neighbor, target, visited):
                    return True
        return False

    for u, v in edges:
        if graph[u] and graph[v] and has_path(u, v, set()):
            return [u, v]
        graph[u].add(v)
        graph[v].add(u)

    return []
```

This is O(n^2) because we run DFS for each edge.

### Why Return Last Edge?

The problem specifies: if multiple answers exist, return the one that appears last in the input. Since we process edges in order and return immediately when we find the redundant edge, we automatically return the first edge (in processing order) that creates a cycle.

Wait - the problem says return the last edge that appears in the cycle. With Union-Find, processing in order, the edge we return IS the last edge added that would complete the cycle, satisfying the requirement.

### Union-Find Optimizations

1. **Path Compression**: In find(), set parent[x] directly to root
2. **Union by Rank**: Attach smaller tree under root of larger tree

These optimizations give O(alpha(n)) amortized time per operation, where alpha is the inverse Ackermann function (effectively constant).

### Edge Cases
- Three nodes forming a triangle: return last edge
- Linear chain with extra edge at end
- Star graph with one extra edge

### Related Problems
- Redundant Connection II (directed graph version)
- Number of Connected Components in Undirected Graph
- Graph Valid Tree
