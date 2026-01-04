# Same Tree

## Summary

Given the roots of two binary trees, check if they are the same. Two trees are the same if they are structurally identical and have the same node values.

### Key Points
- Both structure and values must match
- Recursively compare left and right subtrees
- Base cases: both null (same), one null (different)

### Optimal Approach
Recursively check if current nodes match, then check subtrees.

```python
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
- Time: O(min(n, m)) - compare until difference found
- Space: O(min(h1, h2)) - recursion stack

---

## Detailed Explanation

### Problem Analysis

Two trees are identical if:
1. Both are empty, OR
2. Both are non-empty, have the same root value, and their left and right subtrees are identical

### Base Cases

The logic handles three cases:
1. Both nodes are null: structurally same at this position
2. One is null, the other is not: structurally different
3. Both non-null but different values: value mismatch

### Iterative BFS Approach

```python
from collections import deque

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    queue = deque([(p, q)])

    while queue:
        node1, node2 = queue.popleft()

        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False

        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))

    return True
```

### Iterative DFS Approach

```python
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    stack = [(p, q)]

    while stack:
        node1, node2 = stack.pop()

        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False

        stack.append((node1.left, node2.left))
        stack.append((node1.right, node2.right))

    return True
```

### Short-Circuit Evaluation

The expression `isSameTree(p.left, q.left) and isSameTree(p.right, q.right)` short-circuits: if the left subtrees differ, we do not check the right.

### Edge Cases
- Both empty: true
- One empty, one not: false
- Same structure, different values: false
- Different structures: false

### Related Problems
- Symmetric Tree: check if tree is mirror of itself
- Subtree of Another Tree: check if one tree is subtree
- Flip Equivalent Binary Trees: same structure with possible flips
