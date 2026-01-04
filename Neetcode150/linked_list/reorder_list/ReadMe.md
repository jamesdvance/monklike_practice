# Reorder List

## Summary

Given a singly linked list L0 -> L1 -> ... -> Ln-1 -> Ln, reorder it to L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

### Key Points
- Find the middle of the list
- Reverse the second half
- Merge the two halves alternately

### Optimal Approach
Three steps: find middle, reverse second half, merge alternately.

```python
def reorderList(head: ListNode) -> None:
    if not head or not head.next:
        return

    # Find middle (slow will be at middle)
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev, curr = None, slow.next
    slow.next = None  # Cut the list
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Merge two halves
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The reordering takes nodes from alternating ends. For [1, 2, 3, 4, 5]:
- Result: [1, 5, 2, 4, 3]
- Take from front: 1, 2, 3
- Take from back: 5, 4
- Interleave: 1, 5, 2, 4, 3

### Step 1: Find Middle

Use slow/fast pointers. When fast reaches the end, slow is at the middle:

```
1 -> 2 -> 3 -> 4 -> 5
     s         f
          s              f (off the end)
```

For even length [1, 2, 3, 4]:
```
1 -> 2 -> 3 -> 4
     s         f
```

Slow ends at position before the second half.

### Step 2: Reverse Second Half

After finding middle, reverse nodes after slow:

```
Before: 1 -> 2 -> 3 -> 4 -> 5
              |
             slow

After cut: 1 -> 2 -> 3    4 <- 5
                      |         |
                    slow      prev
```

### Step 3: Merge Alternately

Interleave nodes from both halves:

```
First:  1 -> 2 -> 3
Second: 5 -> 4

Step 1: 1 -> 5 -> 2 -> 3, remaining second: 4
Step 2: 1 -> 5 -> 2 -> 4 -> 3, remaining second: None
```

### Alternative: Using a Stack

Store second half in a stack, then interleave:

```python
def reorderList(head: ListNode) -> None:
    if not head:
        return

    # Find middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Store second half in stack
    stack = []
    curr = slow.next
    slow.next = None
    while curr:
        stack.append(curr)
        curr = curr.next

    # Interleave
    curr = head
    while stack:
        node = stack.pop()
        node.next = curr.next
        curr.next = node
        curr = node.next
```

Space: O(n/2) = O(n) for the stack.

### Edge Cases
- Empty list or single node: no change needed
- Two nodes: swap them
- Odd length: middle node stays in place
- Even length: both halves same size

### Related Problems
- Palindrome Linked List: similar middle finding and reversal
- Reverse Linked List: subroutine
- Middle of the Linked List: finding middle
