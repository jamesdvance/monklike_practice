# Add Two Numbers

## Summary

Given two non-empty linked lists representing two non-negative integers in reverse order, add them and return the sum as a linked list.

### Key Points
- Numbers are stored in reverse order (least significant digit first)
- Process digit by digit, tracking carry
- Handle different list lengths and final carry

### Optimal Approach
Traverse both lists simultaneously, adding digits and carry. Create result nodes as you go.

```python
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
```

### Complexity
- Time: O(max(m, n)) where m, n are list lengths
- Space: O(max(m, n)) for the result list

---

## Detailed Explanation

### Problem Analysis

Since digits are stored in reverse order, the head of each list is the ones place. This makes addition straightforward - we can process from head to tail, just like elementary addition from right to left.

### Step-by-Step Example

For l1 = 2 -> 4 -> 3 (represents 342) and l2 = 5 -> 6 -> 4 (represents 465):

```
Position 0 (ones): 2 + 5 + 0 = 7, carry = 0
Position 1 (tens): 4 + 6 + 0 = 10, digit = 0, carry = 1
Position 2 (hundreds): 3 + 4 + 1 = 8, carry = 0

Result: 7 -> 0 -> 8 (represents 807)
342 + 465 = 807 ✓
```

### Handling Different Lengths

The condition `l1 or l2 or carry` handles:
- l1 runs out: treat remaining l1 values as 0
- l2 runs out: treat remaining l2 values as 0
- Both run out but carry remains: create an extra node

Example: 99 + 1 = 100
- l1 = 9 -> 9, l2 = 1
- 9 + 1 = 10, digit = 0, carry = 1
- 9 + 0 + 1 = 10, digit = 0, carry = 1
- 0 + 0 + 1 = 1, digit = 1, carry = 0
- Result: 0 -> 0 -> 1

### In-Place Modification (Less Clean)

Modify one of the input lists to save space:

```python
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = l1
    carry = 0

    while l1:
        total = l1.val + (l2.val if l2 else 0) + carry
        l1.val = total % 10
        carry = total // 10

        if not l1.next and (l2 and l2.next or carry):
            l1.next = ListNode(0)

        l1 = l1.next
        l2 = l2.next if l2 else None

    return head
```

This is trickier and modifies input, so generally not preferred.

### If Numbers Were Not Reversed

If numbers were stored in normal order (most significant first), we would need to:
1. Reverse both lists
2. Add as above
3. Reverse the result

Or use a stack to process from the end.

### Edge Cases
- One list is shorter
- Result has more digits than either input (e.g., 99 + 1 = 100)
- One list is just [0]
- Large numbers (many digits)

### Related Problems
- Add Two Numbers II: numbers stored in normal order
- Add to Array-Form of Integer: similar addition logic
- Plus One: add 1 to number represented as array
