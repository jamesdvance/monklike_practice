# Balanced Binary Tree

## Summary

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is one where the depth of the two subtrees of every node never differs by more than one.

### Key Points
- Check balance at every node, not just the root
- Can check while computing height (single pass)
- Unbalanced subtree makes entire tree unbalanced

### Optimal Approach
Compute height while checking balance. Return -1 to indicate imbalance.

```python
def isBalanced(root: TreeNode) -> bool:
    def height(node):
        if not node:
            return 0

        left = height(node.left)
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return height(root) != -1
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

---

## Detailed Explanation

### Problem Analysis

A tree is balanced if for every node, the heights of its left and right subtrees differ by at most 1. This must be true for all nodes, not just the root.

### Naive Approach (O(n^2))

Check balance at each node by computing heights separately:

```python
def isBalanced(root: TreeNode) -> bool:
    if not root:
        return True

    left_height = getHeight(root.left)
    right_height = getHeight(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)

def getHeight(node):
    if not node:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))
```

This recomputes heights multiple times, giving O(n^2) in the worst case.

### Optimized Approach Explanation

By returning -1 to signal imbalance, we:
1. Compute height bottom-up
2. Detect imbalance as soon as it occurs
3. Short-circuit the rest of the computation

The function returns:
- The actual height if balanced
- -1 if unbalanced anywhere in the subtree

### Visualization

Balanced:
```
    1
   / \
  2   3
 / \
4   5
```
Heights at each node: 4:1, 5:1, 2:2, 3:1, 1:3
All differences <= 1.

Unbalanced:
```
    1
   /
  2
 /
3
```
At node 1: left_height = 2, right_height = 0, diff = 2 > 1.

### Edge Cases
- Empty tree: balanced (vacuously true)
- Single node: balanced
- Perfect binary tree: balanced
- Linked list: unbalanced if more than 1 node

### Related Problems
- Maximum Depth of Binary Tree: height computation
- Minimum Depth of Binary Tree: shortest path to leaf
- Convert Sorted Array to BST: create balanced BST
