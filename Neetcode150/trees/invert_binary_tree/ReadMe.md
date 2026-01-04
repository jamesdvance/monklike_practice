# Invert Binary Tree

## Summary

Given the root of a binary tree, invert the tree (mirror it) and return its root.

### Key Points
- Swap left and right children at every node
- Can be done recursively or iteratively
- Classic example of tree traversal with modification

### Optimal Approach
Recursively swap children of each node.

```python
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack depth equals tree height

---

## Detailed Explanation

### Problem Analysis

Inverting a binary tree means swapping left and right subtrees at every level. Each node's left child becomes its right child and vice versa.

### Visualization

```
    4              4
   / \            / \
  2   7    =>    7   2
 / \ / \        / \ / \
1  3 6  9      9  6 3  1
```

### Alternative: Iterative BFS

```python
from collections import deque

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root
```

### Alternative: Iterative DFS

```python
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    stack = [root]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root
```

### Order of Operations

You can swap before or after recursing; both work:
- Pre-order: swap, then recurse
- Post-order: recurse, then swap

The key is that every node gets swapped.

### Edge Cases
- Empty tree: return None
- Single node: return as is
- Only left children: becomes only right children
- Already symmetric: stays the same

### Famous Story

This problem is famous because of a tweet by Homebrew creator Max Howell: "Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so f*** off."

### Related Problems
- Symmetric Tree: check if tree is a mirror of itself
- Same Tree: check if two trees are identical
- Flip Equivalent Binary Trees: similar concept with equivalence
