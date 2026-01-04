# Graph Valid Tree

## Summary

Given n nodes labeled 0 to n-1 and a list of undirected edges, determine if these edges form a valid tree. A valid tree has no cycles and is fully connected.

### Key Points
- A tree with n nodes has exactly n-1 edges
- Must be fully connected (one component)
- Must have no cycles

### Optimal Approach
Check edge count and use Union-Find to verify connectivity without cycles.

```python
def validTree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # Cycle detected
        parent[px] = py
        return True

    for u, v in edges:
        if not union(u, v):
            return False

    return True
```

### Complexity
- Time: O(n * alpha(n)) which is nearly O(n)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

A graph is a valid tree if and only if:
1. It has exactly n-1 edges (necessary for n nodes)
2. It is connected (all nodes reachable from any node)
3. It has no cycles

If we have exactly n-1 edges and no cycles, the graph must be connected (and thus a tree).

### Why Check Edge Count First?

- Fewer than n-1 edges: cannot connect all nodes
- More than n-1 edges: must have a cycle
- Exactly n-1 edges: might be a tree (need to verify no cycle)

### Union-Find Cycle Detection

When we try to union two nodes that already have the same root, we've found a cycle. If we process all n-1 edges without finding a cycle, we have a valid tree.

### DFS Approach

```python
from collections import defaultdict

def validTree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return False  # Cycle
            if not dfs(neighbor, node):
                return False
        return True

    # Check for cycle starting from node 0
    if not dfs(0, -1):
        return False

    # Check if all nodes are connected
    return len(visited) == n
```

### BFS Approach

```python
from collections import defaultdict, deque

def validTree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {0}
    queue = deque([0])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append(neighbor)

    return len(visited) == n
```

With exactly n-1 edges, if we can reach all n nodes from node 0, it's a valid tree.

### Step-by-Step Example

```
n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]

Edge count: 4 = n-1 = 4 ✓

Union-Find:
[0,1]: union(0,1) -> success
[0,2]: union(0,2) -> success
[0,3]: union(0,3) -> success
[1,4]: union(1,4) -> success

All edges processed, no cycle found.
Answer: True (valid tree)
```

### Invalid Example (Cycle)

```
n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

Edge count: 5 != n-1 = 4
Answer: False (too many edges)
```

### Edge Cases
- n = 1, edges = []: single node is a valid tree
- n = 2, edges = [[0,1]]: valid tree
- Disconnected graph: not a valid tree
- Graph with cycle: not a valid tree

### Related Problems
- Number of Connected Components: count components
- Redundant Connection: find edge creating cycle
- Minimum Spanning Tree problems
