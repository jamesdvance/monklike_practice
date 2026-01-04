# Contains Duplicate

## Summary

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Key Points
- This is a fundamental problem for understanding hash-based data structures
- The optimal solution uses a hash set for O(1) lookups
- Trade-off between time complexity (sorting vs hashing) and space complexity

### Optimal Approach
Use a hash set to track seen elements. As you iterate through the array, check if the current element exists in the set. If it does, return true. Otherwise, add it to the set.

```python
def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Complexity
- Time: O(n) - single pass through the array
- Space: O(n) - hash set stores up to n elements

---

## Detailed Explanation

### Problem Analysis

The Contains Duplicate problem is often the first problem in interview preparation because it introduces the concept of using auxiliary data structures to optimize lookup operations. The naive approach of comparing every pair of elements would require O(n^2) time, which is impractical for large inputs.

### Alternative Approaches

**Sorting Approach**
Sort the array first, then check adjacent elements for duplicates.

```python
def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```

- Time: O(n log n) due to sorting
- Space: O(1) if sorting in-place, O(n) if not

This approach is useful when space is at a premium and the input can be modified.

**Early Termination Optimization**
The hash set approach naturally supports early termination - we return as soon as a duplicate is found rather than processing the entire array.

### Edge Cases
- Empty array: return false (no duplicates possible)
- Single element: return false
- All elements are the same: return true on second element
- All elements are unique: return false after checking all

### When to Use This Pattern
The "seen set" pattern applies to many problems:
- Finding pairs that sum to a target (Two Sum)
- Detecting cycles in linked lists
- Finding the first non-repeating character
- Checking for valid sudoku configurations
