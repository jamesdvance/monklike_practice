# Validate Binary Search Tree

## Summary

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST has all left descendants less than the node, and all right descendants greater than the node.

### Key Points
- Each node must be within a valid range
- Left subtree: all values must be < current node
- Right subtree: all values must be > current node
- Pass down min and max bounds

### Optimal Approach
Recursively validate with min/max bounds.

```python
def isValidBST(root: TreeNode) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

---

## Detailed Explanation

### Problem Analysis

A common mistake is to only check that left child < parent < right child. This is insufficient:

```
    5
   / \
  1   6
     / \
    3   7
```

This is INVALID because 3 < 5, but 3 is in the right subtree of 5.

### The Range Approach

Each node must satisfy bounds determined by its ancestors:
- Going left: update max bound to current value
- Going right: update min bound to current value

For the tree above:
- 5: range (-inf, inf), valid
- 1: range (-inf, 5), valid
- 6: range (5, inf), valid
- 3: range (5, 6), INVALID because 3 < 5

### In-Order Traversal Approach

In-order traversal of a BST produces sorted values:

```python
def isValidBST(root: TreeNode) -> bool:
    prev = float('-inf')

    def inorder(node):
        nonlocal prev
        if not node:
            return True

        if not inorder(node.left):
            return False

        if node.val <= prev:
            return False
        prev = node.val

        return inorder(node.right)

    return inorder(root)
```

### Iterative In-Order

```python
def isValidBST(root: TreeNode) -> bool:
    stack = []
    prev = float('-inf')

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if root.val <= prev:
            return False
        prev = root.val

        root = root.right

    return True
```

### Why <= and >= (not < and >)?

BST definition typically requires strict inequality (no duplicates). If duplicates are allowed with left <= parent < right:
```python
if node.val < min_val or node.val >= max_val:  # Adjust accordingly
```

### Edge Cases
- Empty tree: valid
- Single node: valid
- All values same: invalid (unless duplicates allowed)
- Integer min/max values: use float('-inf') and float('inf') to avoid issues

### Common Mistakes
- Only checking immediate children
- Not handling equal values correctly
- Integer overflow when using INT_MIN/INT_MAX as bounds

### Related Problems
- Recover Binary Search Tree: fix a BST with two swapped nodes
- Convert Sorted Array to BST: create valid BST
- Kth Smallest Element in BST: uses BST property
