# Binary Search

## Summary

Given a sorted array of integers `nums` and a target value `target`, return the index if the target is found. If not, return -1.

### Key Points
- Array must be sorted for binary search to work
- Repeatedly divide search space in half
- Compare middle element to target to determine which half to search

### Optimal Approach
Compare target with middle element. If equal, return index. If target is smaller, search left half. If larger, search right half.

```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### Complexity
- Time: O(log n) - search space halves each iteration
- Space: O(1) - only using pointers

---

## Detailed Explanation

### Problem Analysis

Binary search is the foundational divide-and-conquer algorithm for searching sorted arrays. It achieves O(log n) time by eliminating half the remaining elements at each step.

### Why It Works

If the array is sorted:
- If nums[mid] < target, target cannot be in nums[0..mid], so search nums[mid+1..right]
- If nums[mid] > target, target cannot be in nums[mid..n-1], so search nums[left..mid-1]
- If nums[mid] == target, we found it

### The Mid Calculation

```python
mid = left + (right - left) // 2
```

This is equivalent to `(left + right) // 2` but avoids potential integer overflow in languages with fixed-size integers. In Python, integers have arbitrary precision, but this pattern is good practice.

### Loop Condition: <= vs <

Using `left <= right`:
- When left == right, we still have one element to check
- Loop exits when left > right (search space is empty)

Using `left < right`:
- Loop exits when left == right
- Requires post-loop check or different termination logic
- Often used in "find boundary" variants

### Recursive Version

```python
def search(nums: list[int], target: int) -> int:
    def binary_search(left, right):
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)

    return binary_search(0, len(nums) - 1)
```

The recursive version is cleaner but uses O(log n) stack space.

### Common Variations

**Find leftmost (first) occurrence:**
```python
def searchLeft(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if left < len(nums) and nums[left] == target else -1
```

**Find rightmost (last) occurrence:**
```python
def searchRight(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left - 1 if left > 0 and nums[left - 1] == target else -1
```

### Python's bisect Module

```python
import bisect

# Find insertion point for target
index = bisect.bisect_left(nums, target)

# Check if target exists
if index < len(nums) and nums[index] == target:
    return index
return -1
```

### Edge Cases
- Empty array: return -1
- Single element: check if it equals target
- Target smaller than all elements: return -1
- Target larger than all elements: return -1
- Duplicate elements: standard binary search returns any matching index

### Common Mistakes
- Off-by-one errors in left/right updates
- Wrong loop condition
- Integer overflow in mid calculation (in other languages)
- Forgetting to handle empty array

### Related Problems
- Search in Rotated Sorted Array: modified binary search
- Find Minimum in Rotated Sorted Array: find rotation point
- Search a 2D Matrix: binary search on 2D structure
