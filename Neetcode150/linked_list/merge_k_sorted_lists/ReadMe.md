# Merge k Sorted Lists

## Summary

Given an array of k sorted linked lists, merge them into one sorted linked list.

### Key Points
- Use a min-heap to always get the smallest current element
- Or use divide-and-conquer, merging pairs recursively
- Heap approach: O(n log k), D&C: O(n log k)

### Optimal Approach (Heap)
Use a min-heap containing one node from each list. Pop smallest, add to result, push that node's next.

```python
import heapq

def mergeKLists(lists: list[ListNode]) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    heap = []

    # Add first node from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

### Complexity
- Time: O(n log k) where n is total nodes and k is number of lists
- Space: O(k) for the heap

---

## Detailed Explanation

### Problem Analysis

This extends "Merge Two Sorted Lists" to k lists. The naive approach of merging one at a time is O(nk). Using a heap or divide-and-conquer achieves O(n log k).

### Why Include Index in Heap?

Python's heapq compares tuples element-by-element. If two nodes have the same value, it tries to compare the nodes, which fails. Including the list index as a tiebreaker prevents this:

```python
(val, index, node)  # index ensures unique ordering
```

### Heap Approach Visualization

For lists: [1->4->5], [1->3->4], [2->6]

```
Initial heap: [(1, 0, node1_1), (1, 1, node2_1), (2, 2, node3_1)]

Pop (1, 0, node1_1): result = 1, push (4, 0, node1_4)
Heap: [(1, 1, node2_1), (2, 2, node3_1), (4, 0, node1_4)]

Pop (1, 1, node2_1): result = 1->1, push (3, 1, node2_3)
Heap: [(2, 2, node3_1), (4, 0, node1_4), (3, 1, node2_3)]

Pop (2, 2, node3_1): result = 1->1->2, push (6, 2, node3_6)
...
```

### Divide and Conquer Approach

Recursively merge pairs of lists:

```python
def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists:
        return None

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwoLists(l1, l2))
        lists = merged

    return lists[0]

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

Time: O(n log k), Space: O(1) (or O(log k) for recursive version)

### Comparison of Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Merge one at a time | O(nk) | O(1) | Slow for large k |
| Min-heap | O(n log k) | O(k) | Clean, efficient |
| Divide & Conquer | O(n log k) | O(1) | Can be done in-place |

### Edge Cases
- Empty list of lists: return None
- List containing empty lists: filter them out
- Single list: return that list
- All lists empty: return None

### Related Problems
- Merge Two Sorted Lists: base case for D&C
- Sort List: merge sort on linked list
- Smallest Range Covering Elements from K Lists: related heap problem
