# Merge Two Sorted Lists

## Summary

Given the heads of two sorted linked lists, merge them into one sorted list by splicing together the nodes.

### Key Points
- Compare heads of both lists, pick smaller
- Use dummy node to simplify edge cases
- Handle remaining nodes when one list is exhausted

### Optimal Approach
Use a dummy node and iterate, always appending the smaller node.

```python
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Append remaining nodes
    current.next = list1 if list1 else list2

    return dummy.next
```

### Complexity
- Time: O(m + n) where m, n are list lengths
- Space: O(1) - only using pointers, reusing existing nodes

---

## Detailed Explanation

### Problem Analysis

This is the linked list version of merging two sorted arrays. The key insight is that we only need to compare the current heads of both lists since they are sorted.

### The Dummy Node Pattern

A dummy node simplifies the code by eliminating special handling for the first node:
- Without dummy: need to set head specially, then loop
- With dummy: loop handles all nodes uniformly, return dummy.next

### Step-by-Step Example

For list1 = 1 -> 2 -> 4 and list2 = 1 -> 3 -> 4:

```
dummy -> None, list1=1, list2=1

list1.val(1) <= list2.val(1): append list1
dummy -> 1, list1=2, list2=1

list1.val(2) > list2.val(1): append list2
dummy -> 1 -> 1, list1=2, list2=3

list1.val(2) <= list2.val(3): append list1
dummy -> 1 -> 1 -> 2, list1=4, list2=3

list1.val(4) > list2.val(3): append list2
dummy -> 1 -> 1 -> 2 -> 3, list1=4, list2=4

list1.val(4) <= list2.val(4): append list1
dummy -> 1 -> 1 -> 2 -> 3 -> 4, list1=None, list2=4

list1 is None: append remaining list2
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

### Recursive Approach

```python
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
```

Space: O(m + n) due to recursion stack.

### Edge Cases
- Both lists empty: return None
- One list empty: return the other list
- Lists of different lengths: handled by appending remainder
- All elements in one list smaller than the other

### Related Problems
- Merge k Sorted Lists: generalization to k lists
- Merge Sorted Array: array version
- Sort List: uses merge sort on linked list
