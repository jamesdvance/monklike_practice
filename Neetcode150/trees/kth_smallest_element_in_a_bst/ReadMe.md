# Kth Smallest Element in a BST

## Summary

Given the root of a BST and an integer k, return the kth smallest value in the tree.

### Key Points
- In-order traversal of BST yields sorted values
- Stop traversal after visiting k nodes
- Can be iterative or recursive

### Optimal Approach
Iterative in-order traversal, counting nodes.

```python
def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1

        if k == 0:
            return root.val

        root = root.right
```

### Complexity
- Time: O(H + k) where H is tree height
- Space: O(H) for stack

---

## Detailed Explanation

### Problem Analysis

In a BST, the in-order traversal visits nodes in ascending order. The kth node visited in an in-order traversal is the kth smallest.

### Why In-Order Works

In-order traversal: left -> root -> right

For BST:
- All left descendants are smaller
- Root is visited after all smaller values
- All right descendants are larger

### Step-by-Step Example

For BST:
```
      5
     / \
    3   6
   / \
  2   4
 /
1
```

In-order: 1, 2, 3, 4, 5, 6

- k=1: return 1
- k=3: return 3
- k=5: return 5

### Recursive Approach

```python
def kthSmallest(root: TreeNode, k: int) -> int:
    result = [0]
    count = [0]

    def inorder(node):
        if not node or count[0] >= k:
            return

        inorder(node.left)

        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return

        inorder(node.right)

    inorder(root)
    return result[0]
```

### Follow-Up: Frequent Queries

If we need to find kth smallest frequently and the tree is modified:

**Approach 1: Augmented BST**
Store subtree size in each node. Navigation becomes O(H):
- If left subtree size == k-1, root is kth smallest
- If left subtree size >= k, go left
- If left subtree size < k-1, go right with k = k - left_size - 1

**Approach 2: Order Statistic Tree**
A balanced BST (like Red-Black tree) with size information gives O(log n) for both queries and updates.

### For Kth Largest

Either:
1. Reverse in-order (right -> root -> left), count to k
2. Compute n - k + 1 smallest

```python
def kthLargest(root: TreeNode, k: int) -> int:
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.right  # Go right first

        root = stack.pop()
        k -= 1

        if k == 0:
            return root.val

        root = root.left  # Then left
```

### Edge Cases
- k = 1: smallest element
- k = n: largest element
- k > n: invalid input (problem guarantees k is valid)

### Related Problems
- Validate Binary Search Tree: uses in-order property
- Binary Search Tree Iterator: same iterative in-order pattern
- Second Minimum Node in Binary Tree: specific k value
