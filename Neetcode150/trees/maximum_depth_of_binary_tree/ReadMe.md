# Maximum Depth of Binary Tree

## Summary

Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Key Points
- Depth is 1 + max(left_depth, right_depth)
- Can use DFS (recursive) or BFS (level by level)
- Base case: empty tree has depth 0

### Optimal Approach
Recursively find the maximum depth of left and right subtrees.

```python
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack depth equals tree height

---

## Detailed Explanation

### Problem Analysis

The depth (or height) of a tree is defined recursively: the depth of a node is 1 plus the maximum depth of its children. For an empty tree, the depth is 0.

### BFS Approach (Level Order)

Count the number of levels in the tree:

```python
from collections import deque

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth
```

This processes level by level, incrementing depth for each level.

### Iterative DFS

Use a stack with (node, depth) pairs:

```python
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return max_depth
```

### Edge Cases
- Empty tree: depth 0
- Single node: depth 1
- Skewed tree (all left or all right): depth equals number of nodes
- Balanced tree: depth is log(n)

### Depth vs Height

In some definitions:
- **Depth** of a node: distance from root (root has depth 0 or 1)
- **Height** of a tree: distance from root to deepest leaf

This problem uses depth as height, counting nodes (not edges).

### Related Problems
- Minimum Depth of Binary Tree: find shallowest leaf
- Balanced Binary Tree: check if depths differ by at most 1
- Diameter of Binary Tree: longest path between any two nodes
