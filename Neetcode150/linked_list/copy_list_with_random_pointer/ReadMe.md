# Copy List with Random Pointer

## Summary

Given a linked list where each node has a next pointer and a random pointer (which can point to any node or null), create a deep copy of the list.

### Key Points
- Cannot simply copy nodes because random pointers may point to nodes not yet created
- Use hash map to track original -> copy mapping
- Alternative: interleave copied nodes with originals

### Optimal Approach (Hash Map)
First pass creates all copy nodes and maps originals to copies. Second pass sets next and random pointers.

```python
def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None

    old_to_new = {}

    # First pass: create all nodes
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: set pointers
    curr = head
    while curr:
        copy = old_to_new[curr]
        copy.next = old_to_new.get(curr.next)
        copy.random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]
```

### Complexity
- Time: O(n)
- Space: O(n) for the hash map

---

## Detailed Explanation

### Problem Analysis

The challenge is that random pointers can point forward or backward in the list. When copying a node, its random target might not exist yet. The hash map solution separates creation from linking.

### O(1) Space Solution: Interleaving

Interleave copied nodes with originals, then separate:

```python
def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None

    # Step 1: Create interleaved copies
    # A -> A' -> B -> B' -> C -> C'
    curr = head
    while curr:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next

    # Step 2: Set random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the lists
    dummy = Node(0)
    copy_curr = dummy
    curr = head

    while curr:
        copy_curr.next = curr.next
        copy_curr = copy_curr.next
        curr.next = curr.next.next
        curr = curr.next

    return dummy.next
```

Time: O(n), Space: O(1) (excluding output)

### Step-by-Step: Interleaving Method

Original: A -> B -> C with randoms A->C, B->A, C->B

Step 1 (Interleave):
```
A -> A' -> B -> B' -> C -> C' -> None
```

Step 2 (Set random for copies):
- A.random = C, so A'.random = C.next = C'
- B.random = A, so B'.random = A.next = A'
- C.random = B, so C'.random = B.next = B'

Step 3 (Separate):
```
Original: A -> B -> C
Copy: A' -> B' -> C'
```

### Why old_to_new.get() with None default?

When curr.next or curr.random is None, we want to set the copy's pointer to None:
```python
copy.next = old_to_new.get(curr.next)  # Returns None if curr.next is None
```

This is equivalent to:
```python
copy.next = old_to_new[curr.next] if curr.next else None
```

### Edge Cases
- Empty list: return None
- Single node with random pointing to itself
- Single node with random = None
- All random pointers are None (like regular linked list)

### Related Problems
- Clone Graph: similar idea with graph nodes
- Clone Binary Tree With Random Pointer: tree version
- Copy List with Next and Arbitrary Pointer: similar problem
