# Binary Tree Maximum Path Sum

## Summary

Given a binary tree, find the maximum path sum. A path is any sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can only appear once in the path.

### Key Points
- Path does not need to go through root
- Path can start and end at any nodes
- Track both max path through node and max path ending at node

### Optimal Approach
At each node, calculate the max path that could go through it, while returning the max path that ends at it.

```python
def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        # Max sum of paths going down left and right
        # Take 0 if negative (don't include that subtree)
        left_max = max(0, dfs(node.left))
        right_max = max(0, dfs(node.right))

        # Max path through this node
        path_through_node = node.val + left_max + right_max
        max_sum = max(max_sum, path_through_node)

        # Return max path ending at this node (can only go one direction)
        return node.val + max(left_max, right_max)

    dfs(root)
    return max_sum
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

---

## Detailed Explanation

### Problem Analysis

A path can:
1. Be just a single node
2. Go from one node down through children
3. Go up through a node and down through another child

The key insight is separating two concepts:
- **Path through node**: left_subtree -> node -> right_subtree
- **Path ending at node**: node + best of (left_subtree OR right_subtree)

Only the latter can be extended by the parent.

### Why max(0, ...) for Subtrees?

If a subtree's max path sum is negative, it is better to not include it at all. Taking 0 effectively prunes that subtree from our path.

### Visualization

```
       -10
       /  \
      9   20
         /  \
        15   7
```

At node 20:
- left_max = 15
- right_max = 7
- path_through_20 = 20 + 15 + 7 = 42
- return 20 + max(15, 7) = 35

At node -10:
- left_max = max(0, 9) = 9
- right_max = max(0, 35) = 35
- path_through_-10 = -10 + 9 + 35 = 34
- max_sum = max(max_sum, 34) (but 42 is still larger)

Final answer: 42 (path 15 -> 20 -> 7)

### Why Return Only One Direction?

When returning to the parent, we can only extend the path in one direction. A path like:
```
left_child <- node -> right_child
```
cannot be extended because there is no way to include the parent and both children while keeping the path connected.

### Edge Cases
- Single negative node: return that node (path must include at least one node)
- All negative values: return the least negative (max single node)
- All positive: sum of all nodes (might not be true if branching)

### Common Mistakes
- Returning the path through node instead of path ending at node
- Not handling negative values correctly
- Assuming path must go through root

### Related Problems
- Diameter of Binary Tree: similar pattern, counting edges
- Path Sum: check if path with target sum exists
- Longest Univalue Path: longest path with same values
