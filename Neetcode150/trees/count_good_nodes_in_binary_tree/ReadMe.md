# Count Good Nodes in Binary Tree

## Summary

Given a binary tree root, a node X is "good" if there are no nodes with a value greater than X on the path from root to X. Count all good nodes.

### Key Points
- Track maximum value seen on path from root
- A node is good if its value >= max so far
- Root is always good

### Optimal Approach
DFS while tracking maximum value on current path.

```python
def goodNodes(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0

        count = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)

        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)

        return count

    return dfs(root, root.val)
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

---

## Detailed Explanation

### Problem Analysis

A good node has no greater values above it in the tree. The root is always good (nothing above it). For other nodes, we compare with the maximum value seen on the path from root.

### Why Track Maximum?

Instead of tracking all values on the path, we only need the maximum:
- If current node >= max, it is good AND becomes the new max
- If current node < max, it is not good AND max stays the same

### Step-by-Step Example

For tree:
```
        3
       / \
      1   4
     /   / \
    3   1   5
```

Path to each node and whether it is good:
- 3: path max = 3, 3 >= 3, GOOD
- 1: path max = 3, 1 < 3, not good
- 3: path max = 3, 3 >= 3, GOOD
- 4: path max = 3, 4 >= 3, GOOD
- 1: path max = 4, 1 < 4, not good
- 5: path max = 4, 5 >= 4, GOOD

Count: 4 good nodes

### BFS Approach

```python
from collections import deque

def goodNodes(root: TreeNode) -> int:
    if not root:
        return 0

    count = 0
    queue = deque([(root, root.val)])

    while queue:
        node, max_val = queue.popleft()

        if node.val >= max_val:
            count += 1
            max_val = node.val

        if node.left:
            queue.append((node.left, max_val))
        if node.right:
            queue.append((node.right, max_val))

    return count
```

### Alternative: Iterative DFS

```python
def goodNodes(root: TreeNode) -> int:
    if not root:
        return 0

    count = 0
    stack = [(root, root.val)]

    while stack:
        node, max_val = stack.pop()

        if node.val >= max_val:
            count += 1
            max_val = node.val

        if node.left:
            stack.append((node.left, max_val))
        if node.right:
            stack.append((node.right, max_val))

    return count
```

### Edge Cases
- Single node (root only): count is 1
- All nodes have same value: all are good
- Strictly decreasing from root: only root is good
- Strictly increasing from root: all are good

### Related Problems
- Path Sum: track sum instead of max
- Binary Tree Maximum Path Sum: different path definition
- Longest Univalue Path: track path properties
