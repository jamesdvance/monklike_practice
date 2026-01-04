# Reverse Nodes in k-Group

## Summary

Given the head of a linked list, reverse the nodes k at a time and return the modified list. If the number of remaining nodes is less than k, leave them as is.

### Key Points
- Check if k nodes exist before reversing
- Reverse exactly k nodes, then recurse or iterate for next group
- Connect reversed groups properly

### Optimal Approach
For each group of k nodes: check if k nodes exist, reverse them, connect to next group (recursively or iteratively).

```python
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # Check if we have k nodes
    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1

    if count < k:
        return head  # Not enough nodes, don't reverse

    # Reverse k nodes
    prev, curr = None, head
    for _ in range(k):
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # head is now tail of reversed group, connect to next group
    head.next = reverseKGroup(curr, k)

    return prev  # prev is new head of this group
```

### Complexity
- Time: O(n)
- Space: O(n/k) for recursion stack (can be O(1) with iteration)

---

## Detailed Explanation

### Problem Analysis

This problem combines counting, reversing, and list manipulation. The key insight is to process the list in chunks of k, reversing each chunk independently and then connecting them.

### The Algorithm Steps

1. **Count k nodes**: Verify we have at least k nodes remaining
2. **Reverse k nodes**: Standard list reversal for exactly k nodes
3. **Connect groups**: The old head becomes the tail of the reversed segment and should point to the next group's result
4. **Recurse/iterate**: Process the next group

### Step-by-Step Example

For list 1 -> 2 -> 3 -> 4 -> 5 with k = 2:

```
Initial: 1 -> 2 -> 3 -> 4 -> 5

Group 1 (nodes 1, 2):
- Count: 2 >= k, proceed
- Reverse: 2 -> 1
- head (1) will point to next group's result

Group 2 (nodes 3, 4):
- Count: 2 >= k, proceed
- Reverse: 4 -> 3
- head (3) will point to next group's result

Group 3 (node 5):
- Count: 1 < k, return as is

Result: 2 -> 1 -> 4 -> 3 -> 5
```

### Iterative Approach

```python
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        # Check if k nodes exist
        kth = prev_group_end
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        # Mark group boundaries
        group_start = prev_group_end.next
        next_group_start = kth.next

        # Reverse k nodes
        prev, curr = next_group_start, group_start
        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Connect previous group to this reversed group
        prev_group_end.next = prev

        # Move to next group
        prev_group_end = group_start
```

Time: O(n), Space: O(1)

### Key Insight: Pointer Connections

After reversing a group:
- `prev` points to the new head of the reversed group (was the kth node)
- `head` (the original first node) is now the tail
- `curr` points to the first node of the next group

We need to:
1. Connect the previous group's tail to `prev`
2. Connect `head` (now tail) to the next group's result

### Edge Cases
- k = 1: no change needed
- k = list length: reverse entire list
- k > list length: no change
- List with exactly k nodes: reverse all

### Common Mistakes
- Off-by-one in counting k nodes
- Losing reference to next group's start
- Incorrect pointer updates when connecting groups

### Related Problems
- Reverse Linked List: base case
- Reverse Linked List II: reverse from position m to n
- Swap Nodes in Pairs: special case with k = 2
