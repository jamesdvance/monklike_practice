# Remove Nth Node From End of List

## Summary

Given the head of a linked list, remove the nth node from the end of the list and return its head.

### Key Points
- Use two pointers with a gap of n nodes
- When fast reaches the end, slow is just before the target
- Use dummy node to handle edge case of removing head

### Optimal Approach
Advance fast pointer n steps ahead, then move both until fast reaches end.

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove the nth node
    slow.next = slow.next.next

    return dummy.next
```

### Complexity
- Time: O(n) - single pass
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

To remove the nth node from the end, we need to find the (n+1)th node from the end (the node before the target). The two-pointer technique achieves this in one pass.

### Why n+1 Steps?

We move fast n+1 steps ahead so that when fast reaches None (past the end), slow is at the node before the one to remove.

For list [1, 2, 3, 4, 5] with n=2 (remove 4):

```
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
  s
  f

After 3 steps (n+1):
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
  s                 f

Move both:
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
              s                    f

slow is at 3, slow.next is 4 (the node to remove)
```

### Why Dummy Node?

The dummy node handles the case when we need to remove the head:

For list [1] with n=1:
```
dummy -> 1 -> None
  s
  f

After 2 steps:
dummy -> 1 -> None
  s           f

slow.next = slow.next.next = None
dummy.next = None
```

Without dummy, we would need special handling for this case.

### Alternative: Calculate Length

Two passes - first to count, second to remove:

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Count nodes
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    # Handle removing head
    if length == n:
        return head.next

    # Find node before target
    curr = head
    for _ in range(length - n - 1):
        curr = curr.next

    curr.next = curr.next.next
    return head
```

This is O(n) time but requires two passes.

### Edge Cases
- Single node, n=1: remove head, return None
- Remove head: use dummy node
- n equals list length: same as removing head

### Common Mistakes
- Off-by-one errors in step counting
- Forgetting dummy node for head removal
- Moving fast exactly n steps instead of n+1

### Related Problems
- Remove Linked List Elements: remove by value
- Delete Node in a Linked List: remove given node (not head)
- Middle of the Linked List: similar two-pointer technique
