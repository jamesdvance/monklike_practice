# Binary Search

## Summary

Binary search is a divide-and-conquer algorithm that finds a target value in a sorted collection by repeatedly halving the search space. It achieves O(log n) time complexity, making it essential for searching large datasets.

### Core Concepts

**The Basic Algorithm**
1. Compare target with middle element
2. If equal, return index
3. If target is smaller, search left half
4. If target is larger, search right half
5. Repeat until found or search space is empty

**Prerequisites**
- Collection must be sorted (or have a monotonic property)
- Random access to elements (arrays, not linked lists)

**When to Use Binary Search**
- Searching in sorted arrays
- Finding boundaries (first/last occurrence)
- Searching on answer (optimization problems)
- Problems with monotonic properties

---

## Problems in This Section

### Binary Search
The fundamental algorithm to find a target in a sorted array.
- Pattern: Classic binary search
- Key insight: Halve search space each iteration

### Search a 2D Matrix
Search in a sorted matrix where rows are sorted and each row's first element is greater than the previous row's last.
- Pattern: Treat matrix as 1D sorted array
- Key insight: Convert 1D index to 2D coordinates

### Koko Eating Bananas
Find minimum eating speed to finish all bananas in h hours.
- Pattern: Binary search on answer
- Key insight: Speed has monotonic property (higher speed -> less time)

### Search in Rotated Sorted Array
Search in an array that was sorted then rotated at an unknown pivot.
- Pattern: Modified binary search
- Key insight: One half is always sorted; check if target is in sorted half

### Find Minimum in Rotated Sorted Array
Find the minimum element in a rotated sorted array.
- Pattern: Binary search for pivot point
- Key insight: Compare mid with right to find which half contains minimum

### Time Based Key-Value Store
Design a data structure supporting get operations at specific timestamps.
- Pattern: Binary search for floor value
- Key insight: Store sorted by timestamp, binary search for largest timestamp <= query

### Median of Two Sorted Arrays
Find median of two sorted arrays in O(log(min(m,n))) time.
- Pattern: Binary search on partition point
- Key insight: Find partition that balances elements and satisfies ordering constraints

---

## Binary Search Patterns

### Pattern 1: Find Exact Match
```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

### Pattern 2: Find Leftmost (First Occurrence)
```python
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left  # or -1 if not found
```

### Pattern 3: Find Rightmost (Last Occurrence)
```python
while left < right:
    mid = (left + right + 1) // 2  # Note: ceiling
    if nums[mid] <= target:
        left = mid
    else:
        right = mid - 1
return left
```

### Pattern 4: Binary Search on Answer
```python
while left < right:
    mid = (left + right) // 2
    if condition(mid):  # Check if mid satisfies requirement
        right = mid  # or left = mid for maximum
    else:
        left = mid + 1  # or right = mid - 1
return left
```

---

## Common Pitfalls

**Off-by-One Errors**
- `left <= right` vs `left < right`: affects termination condition
- `mid + 1` vs `mid`: affects whether current element is excluded

**Integer Overflow**
- Use `mid = left + (right - left) // 2` instead of `(left + right) // 2`
- Not an issue in Python but matters in other languages

**Infinite Loops**
- Ensure at least one of `left` or `right` changes each iteration
- For `left = mid`, use ceiling: `mid = (left + right + 1) // 2`

**Wrong Comparison**
- Comparing with wrong endpoint (left vs right)
- Using wrong inequality operator

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Binary Search | O(log n) | O(1) |
| Search a 2D Matrix | O(log(m*n)) | O(1) |
| Koko Eating Bananas | O(n log m) | O(1) |
| Search in Rotated Sorted Array | O(log n) | O(1) |
| Find Minimum in Rotated Sorted Array | O(log n) | O(1) |
| Time Based Key-Value Store | O(log n) per get | O(n) |
| Median of Two Sorted Arrays | O(log(min(m,n))) | O(1) |

---

## Key Takeaways

1. **Sorted or monotonic**: Binary search requires some ordering property.

2. **Halving is the key**: Each step should eliminate roughly half the possibilities.

3. **Boundaries matter**: Pay close attention to left/right updates and loop conditions.

4. **Search on answer**: When asked for minimum/maximum satisfying a condition, binary search on the answer space.

5. **Handle rotations**: Rotated arrays still have one sorted half at any partition point.

6. **Partition for median**: Finding median is about finding the right partition point that balances elements.
