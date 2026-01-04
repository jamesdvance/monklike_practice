# Linked List Cycle

## Summary

Given the head of a linked list, determine if the list has a cycle.

### Key Points
- Use Floyd's cycle detection (slow and fast pointers)
- Slow moves one step, fast moves two steps
- If they meet, there is a cycle

### Optimal Approach
Fast pointer catches up to slow pointer if there is a cycle.

```python
def hasCycle(head: ListNode) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

A cycle exists if some node's next pointer points to an earlier node. The challenge is detecting this without modifying the list or using O(n) extra space.

### Floyd's Tortoise and Hare

The algorithm uses two pointers:
- Slow (tortoise): moves one step at a time
- Fast (hare): moves two steps at a time

If there is no cycle, fast reaches the end. If there is a cycle, fast eventually catches up to slow from behind.

### Why They Must Meet

Consider the cycle like a circular track:
- When slow enters the cycle, fast is somewhere in the cycle
- Fast gains one position on slow each step (moves 2, slow moves 1)
- Eventually, fast catches up

If slow is at position p and fast is d positions behind (in cycle of length c):
- After d steps, fast has gained d positions and they meet

### Step-by-Step Example

For list 3 -> 2 -> 0 -> -4 -> (back to 2):

```
       +--<--<--<--+
       |          |
3 -> 2 -> 0 -> -4-+
     ^
     cycle starts here

Step 0: slow=3, fast=3
Step 1: slow=2, fast=0
Step 2: slow=0, fast=2 (wrapped around)
Step 3: slow=-4, fast=-4

slow == fast at -4, cycle detected!
```

### Alternative: Hash Set

Track visited nodes:

```python
def hasCycle(head: ListNode) -> bool:
    visited = set()

    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next

    return False
```

Time: O(n), Space: O(n)

### Finding the Cycle Start

To find where the cycle begins (Linked List Cycle II):

```python
def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

Mathematical proof: If the cycle starts at position m and the meeting point is k positions into the cycle, then moving from head and from meeting point at the same speed will meet at the cycle start.

### Edge Cases
- Empty list: no cycle
- Single node without cycle: no cycle
- Single node pointing to itself: has cycle
- Cycle at the beginning vs middle

### Related Problems
- Linked List Cycle II: find where cycle starts
- Happy Number: cycle detection in number sequence
- Find the Duplicate Number: cycle detection in array
