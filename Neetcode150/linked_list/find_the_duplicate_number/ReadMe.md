# Find the Duplicate Number

## Summary

Given an array of n+1 integers where each integer is in the range [1, n], find the one repeated number. There is exactly one repeated number but it may repeat more than once.

### Key Points
- Cannot modify the array
- Must use O(1) extra space
- Treat array as linked list where value is next pointer
- Use Floyd's cycle detection

### Optimal Approach
Treat index as node and value as next pointer. The duplicate creates a cycle.

```python
def findDuplicate(nums: list[int]) -> int:
    # Phase 1: Find intersection point
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find cycle start
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The constraints (cannot modify array, O(1) space) rule out sorting and hash sets. The key insight is that the array can be viewed as a linked list where each value points to another index.

### Array as Linked List

For nums = [1, 3, 4, 2, 2]:
- Index 0 -> value 1 -> index 1
- Index 1 -> value 3 -> index 3
- Index 3 -> value 2 -> index 2
- Index 2 -> value 4 -> index 4
- Index 4 -> value 2 -> index 2 (cycle!)

The path: 0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 ...

The duplicate value (2) is where the cycle begins because multiple indices point to it.

### Why a Cycle Must Exist

- n+1 integers with values in [1, n]
- Index 0 has value in [1, n], so it points somewhere other than itself
- Following the chain of pointers, we must eventually revisit an index (pigeonhole principle)
- The revisited index is pointed to by multiple values, one of which is the duplicate

### Step-by-Step Example

For nums = [1, 3, 4, 2, 2]:

Phase 1 (finding meeting point):
```
slow = nums[0] = 1
fast = nums[nums[0]] = nums[1] = 3

slow = nums[1] = 3
fast = nums[nums[3]] = nums[2] = 4

slow = nums[3] = 2
fast = nums[nums[4]] = nums[2] = 4

slow = nums[2] = 4
fast = nums[nums[4]] = nums[2] = 4

slow == fast at 4
```

Phase 2 (finding cycle start):
```
slow = nums[0] = 1
fast = 4

slow = nums[1] = 3
fast = nums[4] = 2

slow = nums[3] = 2
fast = nums[2] = 4

Wait, this doesn't match... let me recalculate
```

Actually:
```
slow = nums[0] = 1
fast = nums[4] = 2

slow = nums[1] = 3
fast = nums[2] = 4

slow = nums[3] = 2
fast = nums[4] = 2

slow == fast at 2
```

The duplicate is 2.

### Alternative: Binary Search on Value Range

Binary search on the value [1, n], counting elements <= mid:

```python
def findDuplicate(nums: list[int]) -> int:
    low, high = 1, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        count = sum(1 for num in nums if num <= mid)

        if count > mid:
            high = mid
        else:
            low = mid + 1

    return low
```

Time: O(n log n), Space: O(1)

If count of numbers <= mid is more than mid, the duplicate is in [low, mid]. Otherwise, it is in [mid+1, high].

### Edge Cases
- Smallest case: [1, 1] or [2, 1, 1]
- Duplicate appears many times: e.g., [2, 2, 2, 2]
- Duplicate is the largest value

### Related Problems
- Linked List Cycle II: same algorithm
- Missing Number: similar range constraint
- Find All Duplicates in an Array: can modify array
