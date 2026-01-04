# Clone Graph

## Summary

Given a reference to a node in a connected undirected graph, return a deep copy of the graph. Each node contains a value and a list of its neighbors.

### Key Points
- Use a hash map to track original-to-clone mapping
- DFS or BFS to traverse the graph
- Handle cycles by checking if node was already cloned

### Optimal Approach
Use DFS with a hash map to clone nodes as we traverse.

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Node) -> Node:
    if not node:
        return None

    clones = {}

    def dfs(node):
        if node in clones:
            return clones[node]

        clone = Node(node.val)
        clones[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)
```

### Complexity
- Time: O(V + E) where V is nodes and E is edges
- Space: O(V) for the hash map and recursion stack

---

## Detailed Explanation

### Problem Analysis

Cloning a graph requires:
1. Creating new nodes with the same values
2. Connecting them with the same structure
3. Handling cycles (nodes can be neighbors of each other)

The hash map prevents infinite loops by storing already-cloned nodes.

### Step-by-Step Example

```
Original: 1 -- 2
          |    |
          4 -- 3

DFS from node 1:
- Create clone of 1, add to map
- Visit neighbor 2: create clone, add to map
- Visit neighbor 3: create clone, add to map
- Visit neighbor 4: create clone, add to map
- Backtrack and connect neighbors
```

### BFS Alternative

```python
from collections import deque

def cloneGraph(node: Node) -> Node:
    if not node:
        return None

    clones = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for neighbor in curr.neighbors:
            if neighbor not in clones:
                clones[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            clones[curr].neighbors.append(clones[neighbor])

    return clones[node]
```

BFS processes nodes level by level.

### Why Hash Map with Original Node as Key?

Using the original node as a key allows:
1. O(1) lookup to check if already cloned
2. O(1) retrieval of the corresponding clone
3. Cycle detection without extra structures

### Iterative DFS

```python
def cloneGraph(node: Node) -> Node:
    if not node:
        return None

    clones = {node: Node(node.val)}
    stack = [node]

    while stack:
        curr = stack.pop()

        for neighbor in curr.neighbors:
            if neighbor not in clones:
                clones[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
            clones[curr].neighbors.append(clones[neighbor])

    return clones[node]
```

### Edge Cases
- Null input: return None
- Single node with no neighbors: return clone of single node
- Single node pointing to itself: handle self-loop
- Two nodes connected to each other: handle mutual reference

### Related Problems
- Copy List with Random Pointer: similar cloning concept
- Clone Binary Tree with Random Pointer: tree version
- Clone N-ary Tree: simpler tree cloning
