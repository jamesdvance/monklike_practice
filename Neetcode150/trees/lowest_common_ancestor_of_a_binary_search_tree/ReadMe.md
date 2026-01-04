# Lowest Common Ancestor of a Binary Search Tree

## Summary

Given a binary search tree (BST) and two nodes, find their lowest common ancestor (LCA). The LCA is the deepest node that has both nodes as descendants (a node can be a descendant of itself).

### Key Points
- Use BST property: left < root < right
- If both nodes are smaller, LCA is in left subtree
- If both nodes are larger, LCA is in right subtree
- Otherwise, current node is the LCA

### Optimal Approach
Navigate the BST based on value comparisons.

```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

    return None
```

### Complexity
- Time: O(h) where h is tree height
- Space: O(1) iterative, O(h) recursive

---

## Detailed Explanation

### Problem Analysis

In a BST, values are ordered. This property tells us exactly where to look:
- Both p and q smaller than root: LCA must be in left subtree
- Both p and q larger than root: LCA must be in right subtree
- p and q on different sides (or one equals root): root is the LCA

### Why This Works

The LCA is the first node where p and q "split" - one goes left and one goes right. Once this happens, they can never be in the same subtree again. The split point is the LCA.

### Recursive Version

```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
```

### Step-by-Step Example

For BST:
```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```

Find LCA of 2 and 8:
- At 6: 2 < 6, 8 > 6, split! LCA = 6

Find LCA of 2 and 4:
- At 6: 2 < 6, 4 < 6, go left
- At 2: 2 = 2, 4 > 2, split! LCA = 2

Find LCA of 3 and 5:
- At 6: 3 < 6, 5 < 6, go left
- At 2: 3 > 2, 5 > 2, go right
- At 4: 3 < 4, 5 > 4, split! LCA = 4

### Difference from General Binary Tree LCA

In a general binary tree (not BST), we cannot use value comparisons. We must search both subtrees:

```python
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left or right
```

This is O(n) instead of O(h).

### Edge Cases
- One node is ancestor of the other: that node is the LCA
- p equals root: root is LCA
- Both nodes are in same subtree: LCA is deeper

### Related Problems
- Lowest Common Ancestor of a Binary Tree: general tree, no BST property
- Lowest Common Ancestor III: nodes may not exist in tree
- Smallest Common Region: similar concept with regions
