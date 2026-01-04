# Diameter of Binary Tree

## Summary

Given the root of a binary tree, return the length of the diameter. The diameter is the length of the longest path between any two nodes (measured by number of edges).

### Key Points
- The longest path may or may not pass through the root
- For each node, calculate left_height + right_height
- Track maximum while computing heights

### Optimal Approach
Compute heights recursively while tracking the maximum diameter seen.

```python
def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        # Update diameter if path through this node is longer
        diameter = max(diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return diameter
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

---

## Detailed Explanation

### Problem Analysis

The diameter is the longest path between any two nodes. This path might:
1. Go through the root
2. Be entirely within the left subtree
3. Be entirely within the right subtree

At each node, the path through it has length = left_height + right_height.

### Why Height Helps

For any node:
- left_height = maximum edges going down through left child
- right_height = maximum edges going down through right child
- path through this node = left_height + right_height

By computing this at every node and tracking the maximum, we find the diameter.

### Visualization

```
        1
       / \
      2   3
     / \
    4   5
   /
  6
```

- Height from node 2: left = 2 (4-6), right = 1 (5)
- Path through node 2: 2 + 1 = 3 edges (6-4-2-5)
- Height from node 1: left = 3 (1-2-4-6), right = 1 (1-3)
- Path through node 1: 3 + 1 = 4 edges

But the actual diameter is 4 (6-4-2-5 or similar), found at node 2.

### Alternative: Return Both Values

```python
def diameterOfBinaryTree(root: TreeNode) -> int:
    def dfs(node):
        # Returns (height, max_diameter_in_subtree)
        if not node:
            return (0, 0)

        left_height, left_diameter = dfs(node.left)
        right_height, right_diameter = dfs(node.right)

        current_diameter = left_height + right_height
        max_diameter = max(left_diameter, right_diameter, current_diameter)

        return (1 + max(left_height, right_height), max_diameter)

    return dfs(root)[1]
```

This avoids using nonlocal by returning both values.

### Edges vs Nodes

This problem counts edges. If it counted nodes, the answer would be diameter + 1.
- Path 6-4-2-5 has 3 edges and 4 nodes.

### Edge Cases
- Empty tree: diameter 0
- Single node: diameter 0 (no edges)
- Straight line: diameter is n-1 edges
- Complete binary tree: diameter passes through root

### Related Problems
- Maximum Depth of Binary Tree: height computation
- Binary Tree Maximum Path Sum: similar pattern, sum instead of length
- Longest Univalue Path: path with same value
