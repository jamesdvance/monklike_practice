# Trees

## Summary

Trees are hierarchical data structures consisting of nodes connected by edges. Binary trees have at most two children per node. Binary Search Trees (BST) maintain the ordering property: left children are smaller, right children are larger.

### Core Concepts

**Tree Terminology**
- Root: topmost node
- Leaf: node with no children
- Height: longest path from root to leaf
- Depth: distance from root to a node

**Binary Tree Properties**
- Each node has at most 2 children
- Complete: all levels filled except possibly last
- Perfect: all leaves at same depth, all internal nodes have 2 children
- Balanced: height difference of subtrees is at most 1

**Binary Search Tree Properties**
- Left subtree values < node value
- Right subtree values > node value
- In-order traversal produces sorted sequence

### Traversal Types

**Depth-First Search (DFS)**
- Pre-order: root, left, right
- In-order: left, root, right (sorted for BST)
- Post-order: left, right, root

**Breadth-First Search (BFS)**
- Level-order: process level by level
- Uses a queue

---

## Problems in This Section

### Invert Binary Tree
Swap left and right children at every node.
- Pattern: DFS with modification
- Key insight: Recursively swap children

### Maximum Depth of Binary Tree
Find the longest path from root to any leaf.
- Pattern: DFS returning height
- Key insight: depth = 1 + max(left_depth, right_depth)

### Diameter of Binary Tree
Find the longest path between any two nodes.
- Pattern: Height calculation with global max tracking
- Key insight: Track left_height + right_height at each node

### Balanced Binary Tree
Check if depths of subtrees differ by at most 1 at every node.
- Pattern: Height with early termination
- Key insight: Return -1 to signal imbalance

### Same Tree
Check if two trees are structurally identical with same values.
- Pattern: Parallel DFS
- Key insight: Compare nodes pairwise

### Subtree of Another Tree
Check if one tree is a subtree of another.
- Pattern: Nested tree comparison
- Key insight: Use isSameTree as helper

### Lowest Common Ancestor of BST
Find the deepest node that is ancestor of both given nodes.
- Pattern: BST navigation
- Key insight: Split point where p and q go different directions

### Binary Tree Level Order Traversal
Return nodes grouped by level.
- Pattern: BFS with level tracking
- Key insight: Process queue size nodes per level

### Binary Tree Right Side View
Return rightmost node at each level.
- Pattern: BFS or DFS right-first
- Key insight: Last node of each level

### Count Good Nodes in Binary Tree
Count nodes with no greater values on path from root.
- Pattern: DFS with path maximum tracking
- Key insight: Node is good if value >= max on path

### Validate Binary Search Tree
Check if tree satisfies BST property.
- Pattern: DFS with range constraints
- Key insight: Pass min/max bounds down

### Kth Smallest Element in BST
Find the kth smallest value.
- Pattern: In-order traversal with counting
- Key insight: In-order of BST is sorted

### Construct Binary Tree from Preorder and Inorder
Rebuild tree from traversal sequences.
- Pattern: Divide and conquer with index mapping
- Key insight: Preorder gives root, inorder gives subtree sizes

### Binary Tree Maximum Path Sum
Find path with maximum sum.
- Pattern: DFS returning max ending at node, tracking global max
- Key insight: Path through node uses both children; path to parent uses one

### Serialize and Deserialize Binary Tree
Convert tree to string and back.
- Pattern: Preorder with null markers
- Key insight: Null markers preserve structure information

---

## Common Patterns

### Height/Depth Pattern
```python
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

### DFS Template
```python
def dfs(node):
    if not node:
        return  # base case

    # pre-order: process here
    dfs(node.left)
    # in-order: process here
    dfs(node.right)
    # post-order: process here
```

### BFS Template
```python
def bfs(root):
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            # process node
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
```

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Invert Binary Tree | O(n) | O(h) |
| Maximum Depth | O(n) | O(h) |
| Diameter | O(n) | O(h) |
| Balanced Binary Tree | O(n) | O(h) |
| Same Tree | O(n) | O(h) |
| Subtree of Another Tree | O(m*n) | O(h) |
| LCA of BST | O(h) | O(1) |
| Level Order Traversal | O(n) | O(n) |
| Right Side View | O(n) | O(n) |
| Count Good Nodes | O(n) | O(h) |
| Validate BST | O(n) | O(h) |
| Kth Smallest in BST | O(h+k) | O(h) |
| Construct from Traversals | O(n) | O(n) |
| Max Path Sum | O(n) | O(h) |
| Serialize/Deserialize | O(n) | O(n) |

h = tree height, which is O(log n) for balanced trees and O(n) for skewed trees.

---

## Key Takeaways

1. **Recursion is natural**: Trees are recursive structures; recursive solutions are often clearest.

2. **Choose the right traversal**: Pre-order for top-down processing, post-order for bottom-up, in-order for BST operations.

3. **BST property is powerful**: It enables O(log n) operations and sorted iteration.

4. **Track global state carefully**: For problems like diameter or max path sum, update a global variable while returning local information.

5. **Null handling is critical**: Most tree functions need a base case for null nodes.

6. **BFS for levels, DFS for paths**: Level-based problems suit BFS; path-based problems often suit DFS.
