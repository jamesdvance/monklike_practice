# Linked List

## Summary

A linked list is a linear data structure where elements are stored in nodes, each containing data and a pointer to the next node. Unlike arrays, linked lists provide O(1) insertion and deletion at known positions but O(n) access by index.

### Core Concepts

**Singly Linked List**
- Each node has data and a next pointer
- Can only traverse forward
- Simpler but less flexible

**Doubly Linked List**
- Each node has data, next, and prev pointers
- Can traverse both directions
- Enables O(1) deletion when you have the node

**When to Use Linked Lists**
- Frequent insertions and deletions at arbitrary positions
- Unknown or dynamic size
- Implementing stacks, queues, or LRU caches
- When you need O(1) insertion without shifting elements

### Key Techniques

**Dummy/Sentinel Node**
A dummy node before the real head simplifies edge cases, especially when the head might change.

**Two Pointers**
- Fast/slow for cycle detection and middle finding
- Gap pointers for nth-from-end operations

**Reversal**
Fundamental operation used as a subroutine in many problems.

---

## Problems in This Section

### Reverse Linked List
Reverse a singly linked list by changing link directions.
- Pattern: Three-pointer iteration or recursion
- Key insight: Save next before changing link

### Merge Two Sorted Lists
Merge two sorted lists into one sorted list.
- Pattern: Two-pointer comparison with dummy node
- Key insight: Always pick smaller head, append remainder

### Reorder List
Reorder L0->L1->...->Ln to L0->Ln->L1->Ln-1->...
- Pattern: Find middle, reverse second half, merge alternately
- Key insight: Combine three fundamental operations

### Remove Nth Node From End of List
Remove the nth node from the end in one pass.
- Pattern: Two pointers with n-gap
- Key insight: When fast reaches end, slow is at target

### Copy List with Random Pointer
Deep copy a list with random pointers.
- Pattern: Hash map for node mapping or interleaving technique
- Key insight: Need to handle references to nodes not yet created

### Add Two Numbers
Add two numbers represented as reversed linked lists.
- Pattern: Digit-by-digit addition with carry
- Key insight: Reversed order makes addition natural (ones first)

### Linked List Cycle
Detect if a linked list has a cycle.
- Pattern: Floyd's cycle detection (fast/slow pointers)
- Key insight: If cycle exists, fast catches up to slow

### Find the Duplicate Number
Find duplicate in array using linked list cycle detection.
- Pattern: Treat array as linked list, find cycle start
- Key insight: Values as next pointers, duplicate creates cycle

### LRU Cache
Design a cache with O(1) operations and LRU eviction.
- Pattern: Hash map + doubly linked list
- Key insight: Combine O(1) lookup with O(1) order updates

### Merge k Sorted Lists
Merge k sorted lists into one sorted list.
- Pattern: Min-heap or divide-and-conquer
- Key insight: Heap maintains k candidates for O(log k) selection

### Reverse Nodes in k-Group
Reverse the list in groups of k nodes.
- Pattern: Count, reverse, connect, repeat
- Key insight: Each group is an independent reversal, then link groups

---

## Common Patterns

### Dummy Node Pattern
```python
dummy = ListNode(0)
dummy.next = head
# ... operations that might change head
return dummy.next
```

### Fast/Slow Pointer Pattern
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is at middle (or start of second half)
```

### Reversal Pattern
```python
prev = None
curr = head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev  # new head
```

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Reverse Linked List | O(n) | O(1) |
| Merge Two Sorted Lists | O(m+n) | O(1) |
| Reorder List | O(n) | O(1) |
| Remove Nth From End | O(n) | O(1) |
| Copy Random Pointer | O(n) | O(n)* |
| Add Two Numbers | O(max(m,n)) | O(max(m,n)) |
| Linked List Cycle | O(n) | O(1) |
| Find Duplicate Number | O(n) | O(1) |
| LRU Cache | O(1) per op | O(capacity) |
| Merge k Sorted Lists | O(n log k) | O(k) |
| Reverse in k-Group | O(n) | O(1) |

*O(1) possible with interleaving technique

---

## Key Takeaways

1. **Use dummy nodes liberally**: They simplify code when the head might change.

2. **Draw the pointers**: Linked list problems are visual. Draw before coding.

3. **Save before you change**: Always save the next pointer before modifying links.

4. **Floyd's algorithm is versatile**: Cycle detection appears in non-obvious places (like finding duplicates).

5. **Combine hash maps with lists**: For O(1) lookup with ordering (LRU cache), use both.

6. **Divide and conquer works**: Many k-element problems (merge k lists, reverse k groups) benefit from this approach.
