# Subtree of Another Tree

## Summary

Given the roots of two binary trees `root` and `subRoot`, return true if there is a subtree of `root` with the same structure and node values as `subRoot`.

### Key Points
- Check if trees match at every node of root
- Use isSameTree as a helper function
- A tree is always a subtree of itself

### Optimal Approach
For each node in root, check if the subtree starting there is identical to subRoot.

```python
def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not subRoot:
        return True
    if not root:
        return False

    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

### Complexity
- Time: O(m * n) where m and n are sizes of root and subRoot
- Space: O(h) for recursion stack

---

## Detailed Explanation

### Problem Analysis

We need to find a node in `root` such that the subtree rooted there is identical to `subRoot`. This requires:
1. Traversing all nodes of `root`
2. At each node, checking if the subtree matches `subRoot`

### Why O(m * n)?

- We visit up to m nodes in root
- At each node, we might compare up to n nodes with subRoot
- Worst case: O(m * n) comparisons

### Optimization: String Matching

Convert trees to strings and use KMP or other string matching:

```python
def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    def serialize(node):
        if not node:
            return "#"
        return f"^{node.val}" + serialize(node.left) + serialize(node.right)

    root_str = serialize(root)
    sub_str = serialize(subRoot)

    return sub_str in root_str
```

The `^` prefix prevents false matches like "12" being found in "123".

Time: O(m + n) with proper string matching, but has overhead.

### Optimization: Tree Hashing

Hash subtrees to quickly eliminate non-matches:

```python
def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    def merkle(node):
        if not node:
            return hash(None)
        left_hash = merkle(node.left)
        right_hash = merkle(node.right)
        return hash((node.val, left_hash, right_hash))

    target_hash = merkle(subRoot)

    def find(node):
        if not node:
            return False
        if merkle(node) == target_hash and isSameTree(node, subRoot):
            return True
        return find(node.left) or find(node.right)

    return find(root)
```

This reduces comparisons by only checking when hashes match.

### Edge Cases
- subRoot is empty: always true (empty tree is subtree of any tree)
- root is empty: false (unless subRoot is also empty)
- subRoot equals root: true
- subRoot is a single node: find that value in root

### Subtle Point: Subtree Definition

A subtree must extend to the leaves. For example:
```
root:     3        subRoot:  3
         / \                / \
        4   5              4   5
       / \
      1   2
```
subRoot is NOT a subtree because in root, node 4 has children but in subRoot it does not.

### Related Problems
- Same Tree: helper function
- Find Duplicate Subtrees: find all duplicate subtrees
- Tree Isomorphism: similar matching problem
