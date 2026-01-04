# Graphs

## Summary

Graphs represent relationships between entities. A graph consists of vertices (nodes) and edges connecting them. Graph problems involve traversal, connectivity, shortest paths, and cycle detection.

### Core Concepts

1. **Representations**: Adjacency list (space-efficient) vs adjacency matrix (fast lookup)
2. **Traversal**: DFS (depth-first) and BFS (breadth-first)
3. **Connectivity**: Union-Find for component queries
4. **Topological Sort**: Ordering nodes in a DAG

### When to Use Each Approach

- **DFS**: Exploring all paths, cycle detection, connected components
- **BFS**: Shortest path in unweighted graphs, level-order traversal
- **Union-Find**: Dynamic connectivity, cycle detection in undirected graphs
- **Topological Sort**: Dependency ordering, task scheduling

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Number of Islands](./number_of_islands/) | Grid DFS/BFS | Mark visited cells, count connected components |
| [Clone Graph](./clone_graph/) | DFS with hash map | Map original to clone to handle cycles |
| [Max Area of Island](./max_area_of_island/) | Grid DFS | Return area from DFS instead of just visiting |
| [Pacific Atlantic Water Flow](./pacific_atlantic_water_flow/) | Reverse BFS | Start from oceans, flow upward |
| [Surrounded Regions](./surrounded_regions/) | Border DFS | Mark border-connected cells as safe |
| [Rotting Oranges](./rotting_oranges/) | Multi-source BFS | All rotten oranges spread simultaneously |
| [Walls and Gates](./walls_and_gates/) | Multi-source BFS | Start from all gates at once |
| [Course Schedule](./course_schedule/) | Topological Sort | Cycle detection in directed graph |
| [Course Schedule II](./course_schedule_ii/) | Topological Sort | Return valid ordering |
| [Redundant Connection](./redundant_connection/) | Union-Find | Edge completing cycle is redundant |
| [Number of Connected Components](./number_of_connected_components_in_an_undirected_graph/) | Union-Find/DFS | Count unique roots or DFS traversals |
| [Graph Valid Tree](./graph_valid_tree/) | Union-Find | n-1 edges, no cycles, connected |
| [Word Ladder](./word_ladder/) | BFS | Shortest transformation sequence |

---

## Common Patterns

### Pattern 1: Grid DFS

```python
def explore_grid(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 1:  # Not valid cell
            return

        grid[r][c] = 0  # Mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dfs(r, c)
```

### Pattern 2: Multi-Source BFS

```python
from collections import deque

def multi_source_bfs(grid, sources):
    rows, cols = len(grid), len(grid[0])
    queue = deque(sources)
    visited = set(sources)

    distance = 0
    while queue:
        distance += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    return distance
```

### Pattern 3: Union-Find

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
            return False  # Already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

### Pattern 4: Topological Sort (Kahn's Algorithm)

```python
from collections import defaultdict, deque

def topological_sort(num_nodes, edges):
    graph = defaultdict(list)
    indegree = [0] * num_nodes

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_nodes else []  # Empty if cycle
```

### Pattern 5: DFS Cycle Detection (Directed Graph)

```python
def has_cycle(num_nodes, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # 0=unvisited, 1=visiting, 2=visited
    state = [0] * num_nodes

    def dfs(node):
        if state[node] == 1:
            return True  # Cycle
        if state[node] == 2:
            return False

        state[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        state[node] = 2
        return False

    return any(dfs(i) for i in range(num_nodes) if state[i] == 0)
```

---

## Complexity Summary

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| DFS | O(V + E) | O(V) | Traversal, cycle detection |
| BFS | O(V + E) | O(V) | Shortest path (unweighted) |
| Union-Find | O(alpha(n)) per op | O(V) | Dynamic connectivity |
| Topological Sort | O(V + E) | O(V) | Ordering dependencies |

---

## Key Takeaways

1. **Grid problems** are graph problems in disguise - each cell is a node
2. **Multi-source BFS** is optimal when starting from multiple sources
3. **Union-Find** excels at dynamic connectivity queries
4. **Topological sort** fails if and only if there's a cycle (directed graphs)
5. **Bidirectional BFS** can dramatically reduce search space
6. **Mark visited** before or immediately after adding to queue to avoid duplicates
7. **n-1 edges + connected + no cycle** = tree property
