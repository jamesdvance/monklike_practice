# Construct Binary Tree from Preorder and Inorder Traversal

## Summary

Given preorder and inorder traversals of a tree, construct the binary tree.

### Key Points
- Preorder first element is root
- Find root in inorder to split left and right subtrees
- Recursively build subtrees

### Optimal Approach
Use preorder to identify root, use inorder to split subtrees.

```python
def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        root_idx = inorder_map[root_val]
        left_size = root_idx - in_start

        root.left = build(pre_start + 1, pre_start + left_size,
                         in_start, root_idx - 1)
        root.right = build(pre_start + left_size + 1, pre_end,
                          root_idx + 1, in_end)

        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

### Complexity
- Time: O(n) - each node processed once
- Space: O(n) - hash map and recursion stack

---

## Detailed Explanation

### Problem Analysis

**Preorder traversal**: root, left subtree, right subtree
**Inorder traversal**: left subtree, root, right subtree

The first element of preorder is always the root. Finding this element in inorder tells us how many nodes are in the left subtree (everything to its left) and right subtree (everything to its right).

### Step-by-Step Example

For preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]:

```
Step 1: Root = preorder[0] = 3
        In inorder: [..., 3, ...]
        Left of 3: [9] (size 1)
        Right of 3: [15,20,7] (size 3)

Step 2: Build left subtree
        preorder section: [9]
        inorder section: [9]
        Root = 9, no children

Step 3: Build right subtree
        preorder section: [20,15,7]
        inorder section: [15,20,7]
        Root = 20
        Left of 20 in inorder: [15]
        Right of 20 in inorder: [7]

Result:
    3
   / \
  9  20
    /  \
   15   7
```

### Why Hash Map?

Without a hash map, finding root in inorder takes O(n) per call, giving O(n^2) total. The hash map provides O(1) lookup.

### Index Calculation

For node at preorder[pre_start]:
- Left subtree in preorder: [pre_start+1, pre_start+left_size]
- Right subtree in preorder: [pre_start+left_size+1, pre_end]
- Left subtree in inorder: [in_start, root_idx-1]
- Right subtree in inorder: [root_idx+1, in_end]

### Simpler but Less Efficient Version

Create new arrays for each recursive call:

```python
def buildTree(preorder, inorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:idx+1], inorder[:idx])
    root.right = buildTree(preorder[idx+1:], inorder[idx+1:])

    return root
```

This is O(n^2) due to array slicing and index lookup.

### Related Constructions

**From Inorder and Postorder**:
- Postorder last element is root
- Build right subtree first (postorder is left, right, root)

**From Preorder and Postorder**:
- Only works for full binary trees (every node has 0 or 2 children)

### Edge Cases
- Single node: return that node
- Skewed tree (all left or all right)
- Complete binary tree

### Related Problems
- Construct Binary Tree from Inorder and Postorder Traversal
- Construct Binary Search Tree from Preorder Traversal: BST property helps
- Serialize and Deserialize Binary Tree: related encoding problem
