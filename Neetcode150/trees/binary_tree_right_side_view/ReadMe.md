# Binary Tree Right Side View

## Summary

Given the root of a binary tree, return the values of nodes visible from the right side, ordered from top to bottom.

### Key Points
- The rightmost node at each level is visible
- Use BFS level order and take last node of each level
- Or use DFS, visiting right subtree first

### Optimal Approach (BFS)
Use level order traversal, adding the last node of each level.

```python
from collections import deque

def rightSideView(root: TreeNode) -> list[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(n) - queue size

---

## Detailed Explanation

### Problem Analysis

The right side view consists of the rightmost node at each level. These are the nodes that would be visible if you looked at the tree from the right side.

### DFS Approach (Right First)

Visit right child before left, tracking first node seen at each depth:

```python
def rightSideView(root: TreeNode) -> list[int]:
    result = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(result):
            result.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result
```

By visiting right first, the first node we see at each depth is the rightmost.

### Visualization

```
    1
   / \
  2   3
   \   \
    5   4
```

Right view: [1, 3, 4]
- Level 0: 1 (only node)
- Level 1: 3 (rightmost of 2, 3)
- Level 2: 4 (rightmost of 5, 4)

### Left Side View

For left side view, just change which node to add:
- BFS: `if i == 0` (first node of level)
- DFS: visit left before right

```python
def leftSideView(root: TreeNode) -> list[int]:
    result = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(result):
            result.append(node.val)

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result
```

### Edge Cases
- Empty tree: return []
- Single node: return [root.val]
- Only left children: left children are visible from right
- Only right children: all right children visible

### Common Mistake

Thinking only the rightmost branch is visible. Consider:
```
    1
   /
  2
   \
    3
```
Right view is [1, 2, 3], not just [1].

### Related Problems
- Binary Tree Level Order Traversal: foundation for this approach
- Boundary of Binary Tree: left and right boundaries
- Find Bottom Left Tree Value: leftmost node at deepest level
