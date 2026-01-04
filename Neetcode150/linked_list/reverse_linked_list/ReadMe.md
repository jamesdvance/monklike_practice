# Reverse Linked List

## Summary

Given the head of a singly linked list, reverse the list and return the reversed list.

### Key Points
- Iterative: use three pointers (prev, curr, next)
- Recursive: reverse rest of list, then fix pointers
- Modify links in-place without extra data structures

### Optimal Approach (Iterative)
Track previous, current, and next nodes. Reverse the link direction at each step.

```python
def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    return prev
```

### Complexity
- Time: O(n) - visit each node once
- Space: O(1) - only using pointers

---

## Detailed Explanation

### Problem Analysis

Reversing a linked list is a fundamental operation that appears in many problems. The key is to change the direction of each next pointer while traversing the list.

### Iterative Approach Step-by-Step

For list 1 -> 2 -> 3 -> None:

```
Initial: prev=None, curr=1

Step 1: next=2, 1.next=None, prev=1, curr=2
        None <- 1  2 -> 3 -> None

Step 2: next=3, 2.next=1, prev=2, curr=3
        None <- 1 <- 2  3 -> None

Step 3: next=None, 3.next=2, prev=3, curr=None
        None <- 1 <- 2 <- 3

Return prev (which is 3)
```

### Recursive Approach

```python
def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None

    return new_head
```

The recursive approach:
1. Recurse to the end of the list
2. The last node becomes the new head
3. On the way back, reverse each link

For 1 -> 2 -> 3:
- reverseList(1) calls reverseList(2) calls reverseList(3)
- reverseList(3) returns 3 (base case)
- At node 2: 2.next.next = 2 makes 3 -> 2, then 2.next = None
- At node 1: 1.next.next = 1 makes 2 -> 1, then 1.next = None

Space: O(n) due to recursion stack.

### Common Mistakes
- Losing reference to the next node before reversing
- Forgetting to set the old head's next to None
- Wrong return value (returning curr instead of prev)

### Edge Cases
- Empty list: return None
- Single node: return that node
- Two nodes: simple swap

### Related Problems
- Reverse Linked List II: reverse between positions m and n
- Palindrome Linked List: uses reverse as subroutine
- Reverse Nodes in k-Group: reverse in groups of k
