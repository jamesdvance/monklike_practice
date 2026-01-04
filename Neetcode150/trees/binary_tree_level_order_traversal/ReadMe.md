# Binary Tree Level Order Traversal

## Summary

Given the root of a binary tree, return its level order traversal as a list of lists, where each inner list contains nodes at that level from left to right.

### Key Points
- Use BFS with a queue
- Process all nodes at current level before moving to next
- Track level boundaries by processing queue size at a time

### Optimal Approach
Use BFS, processing one level at a time.

```python
from collections import deque

def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(n) - queue can hold up to n/2 nodes (last level of complete tree)

---

## Detailed Explanation

### Problem Analysis

Level order traversal visits nodes level by level, left to right. This is naturally suited to BFS, where we explore all neighbors (same level) before going deeper.

### Key Insight: Level Size

The trick is using `level_size = len(queue)` before the inner loop. This captures how many nodes are at the current level, allowing us to process exactly that many before moving on.

### Step-by-Step Example

For tree:
```
    3
   / \
  9  20
    /  \
   15   7
```

```
Initial: queue = [3]

Level 0: size = 1
  Pop 3, add to level, enqueue 9, 20
  level = [3], queue = [9, 20]

Level 1: size = 2
  Pop 9, add to level
  Pop 20, add to level, enqueue 15, 7
  level = [9, 20], queue = [15, 7]

Level 2: size = 2
  Pop 15, add to level
  Pop 7, add to level
  level = [15, 7], queue = []

Result: [[3], [9, 20], [15, 7]]
```

### DFS Approach

Can also use DFS, tracking depth:

```python
def levelOrder(root: TreeNode) -> list[list[int]]:
    result = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(result):
            result.append([])

        result[depth].append(node.val)

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result
```

This processes nodes in pre-order but assigns them to levels based on depth.

### Variations

**Reverse Level Order (Bottom-Up)**:
```python
result.insert(0, level)  # or reverse at end
```

**Zigzag Level Order**:
```python
if len(result) % 2 == 1:
    level.reverse()
```

**Right Side View**:
```python
result.append(level[-1])
```

### Edge Cases
- Empty tree: return []
- Single node: return [[root.val]]
- Skewed tree: one node per level

### Related Problems
- Binary Tree Zigzag Level Order Traversal: alternate directions
- Binary Tree Right Side View: rightmost at each level
- Average of Levels in Binary Tree: compute level averages
- N-ary Tree Level Order Traversal: extension to n-ary trees
