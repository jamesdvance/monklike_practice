# Serialize and Deserialize Binary Tree

## Summary

Design an algorithm to serialize a binary tree to a string and deserialize the string back to the original tree structure.

### Key Points
- Use preorder traversal with null markers
- Null markers indicate absent children
- Delimiter separates values

### Optimal Approach
Preorder traversal with "N" for null nodes.

```python
class Codec:
    def serialize(self, root: TreeNode) -> str:
        result = []

        def preorder(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode:
        values = data.split(",")
        self.index = 0

        def build():
            if values[self.index] == "N":
                self.index += 1
                return None

            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = build()
            node.right = build()
            return node

        return build()
```

### Complexity
- Time: O(n) for both serialize and deserialize
- Space: O(n) for the string representation

---

## Detailed Explanation

### Problem Analysis

Serialization converts a tree structure to a linear format (string). The challenge is encoding enough information to reconstruct the exact tree, including structure.

### Why Null Markers?

Without null markers, we cannot distinguish between different tree shapes:
```
  1        1
 /          \
2            2
```

With null markers:
- First tree: "1,2,N,N,N"
- Second tree: "1,N,2,N,N"

### Step-by-Step Example

For tree:
```
    1
   / \
  2   3
     / \
    4   5
```

Serialize:
```
Visit 1: "1"
Visit 2: "1,2"
Visit 2's left (null): "1,2,N"
Visit 2's right (null): "1,2,N,N"
Visit 3: "1,2,N,N,3"
Visit 4: "1,2,N,N,3,4"
Visit 4's left (null): "1,2,N,N,3,4,N"
Visit 4's right (null): "1,2,N,N,3,4,N,N"
Visit 5: "1,2,N,N,3,4,N,N,5"
Visit 5's left (null): "1,2,N,N,3,4,N,N,5,N"
Visit 5's right (null): "1,2,N,N,3,4,N,N,5,N,N"
```

Result: "1,2,N,N,3,4,N,N,5,N,N"

Deserialize:
```
Index 0: val=1, create node 1
Index 1: val=2, create node 2 (left of 1)
Index 2: N, left of 2 is null
Index 3: N, right of 2 is null
Index 4: val=3, create node 3 (right of 1)
...
```

### BFS Approach

Use level-order traversal:

```python
class Codec:
    def serialize(self, root):
        if not root:
            return "N"

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")

        return ",".join(result)

    def deserialize(self, data):
        values = data.split(",")
        if values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root
```

### Alternative Formats

**JSON-like nested format**:
```
{"val":1,"left":{"val":2},"right":{"val":3}}
```

**Parentheses format**:
```
1(2(,),3(4(,),5(,)))
```

### Edge Cases
- Empty tree: serialize as "N"
- Single node: serialize as "value,N,N"
- Very large values: ensure string parsing handles them

### Related Problems
- Serialize and Deserialize BST: can use BST property
- Serialize and Deserialize N-ary Tree
- Construct Binary Tree from Preorder and Inorder: related reconstruction
