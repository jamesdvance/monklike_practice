# Number of Connected Components in an Undirected Graph

## Summary

Given n nodes labeled 0 to n-1 and a list of undirected edges, return the number of connected components in the graph.

### Key Points
- Each connected component is a maximal set of connected nodes
- Use Union-Find or DFS/BFS to find components
- Count unique roots in Union-Find or count DFS traversals

### Optimal Approach (Union-Find)
Union all edges, then count unique parents.

```python
def countComponents(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1

    for u, v in edges:
        union(u, v)

    # Count unique roots
    return len(set(find(i) for i in range(n)))
```

### Complexity
- Time: O(n + e * alpha(n)) where e is number of edges
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

A connected component is a subgraph where every pair of nodes is connected by some path. We need to count how many such separate components exist.

### Union-Find Approach

1. Initially, each node is its own component (n components)
2. For each edge, union the two nodes (merge components)
3. Count distinct roots at the end

### Alternative: Count During Union

```python
def countComponents(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n))
    components = n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal components
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            components -= 1

    for u, v in edges:
        union(u, v)

    return components
```

Each successful union reduces component count by 1.

### DFS Approach

```python
from collections import defaultdict

def countComponents(n: int, edges: list[list[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            components += 1
            dfs(node)

    return components
```

Each DFS call explores one entire component.

### BFS Approach

```python
from collections import defaultdict, deque

def countComponents(n: int, edges: list[list[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    for node in range(n):
        if node not in visited:
            components += 1
            queue = deque([node])
            visited.add(node)

            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

    return components
```

### Step-by-Step Example

```
n = 5, edges = [[0,1], [1,2], [3,4]]

Union-Find:
Initial: parent = [0,1,2,3,4], components = 5

Edge [0,1]: union(0,1)
  parent = [1,1,2,3,4], components = 4

Edge [1,2]: union(1,2)
  parent = [1,2,2,3,4], components = 3

Edge [3,4]: union(3,4)
  parent = [1,2,2,4,4], components = 2

Answer: 2 components ({0,1,2} and {3,4})
```

### Edge Cases
- No edges: n components (each node is separate)
- Fully connected: 1 component
- Self-loops: should not affect count
- Multiple edges between same nodes: handled naturally

### Related Problems
- Graph Valid Tree: check if exactly 1 component with n-1 edges
- Number of Islands: connected components in a grid
- Redundant Connection: find edge creating cycle in tree
