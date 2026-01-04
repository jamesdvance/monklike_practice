# Find Minimum in Rotated Sorted Array

## Summary

A sorted array of unique elements has been rotated at an unknown pivot. Find the minimum element.

### Key Points
- Minimum is at the rotation point (pivot)
- Compare mid with right to determine which half contains minimum
- The unsorted half contains the pivot

### Optimal Approach
Binary search comparing mid element with right element to find the pivot.

```python
def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum is in the right half
            left = mid + 1
        else:
            # Minimum is in the left half (including mid)
            right = mid

    return nums[left]
```

### Complexity
- Time: O(log n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

In a rotated sorted array, all elements before the pivot are greater than all elements after the pivot. The minimum element is exactly at the pivot point.

For array [4, 5, 6, 7, 0, 1, 2]:
- Pivot is at index 4 (value 0)
- Elements before pivot: [4, 5, 6, 7] - all greater than elements after
- Elements after pivot: [0, 1, 2] - all smaller

### Why Compare with Right?

We compare nums[mid] with nums[right] because:
- If nums[mid] > nums[right]: the array is not sorted from mid to right, so minimum is in (mid, right]
- If nums[mid] <= nums[right]: the array is sorted from mid to right, so minimum is in [left, mid]

Comparing with nums[left] is trickier because of edge cases when the array is not rotated.

### Loop Condition: left < right

We use `left < right` because:
- We are finding a position, not a specific value
- When left == right, we have found the minimum
- The condition `right = mid` (not mid - 1) ensures we do not skip the minimum

### Step-by-Step Example

For `nums = [3, 4, 5, 1, 2]`:

```
left=0, right=4, mid=2, nums[mid]=5
5 > nums[right]=2, minimum in right half
left=3

left=3, right=4, mid=3, nums[mid]=1
1 <= nums[right]=2, minimum in left half (including mid)
right=3

left=3, right=3, done
return nums[3]=1
```

### Alternative: Compare with nums[0]

Another valid approach:

```python
def findMin(nums: list[int]) -> int:
    if nums[0] <= nums[-1]:
        return nums[0]  # Not rotated

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= nums[0]:
            left = mid + 1  # Minimum is after mid
        else:
            right = mid  # Minimum is at or before mid

    return nums[left]
```

This first checks if the array is rotated at all.

### Handling Non-Rotated Arrays

The algorithm handles non-rotated arrays correctly:
- For [1, 2, 3, 4, 5], nums[mid] is always <= nums[right]
- This causes right to decrease until left == right == 0
- nums[0] is the minimum, which is correct

### Edge Cases
- Not rotated: minimum is first element
- Rotated by n-1 (e.g., [2, 1]): minimum is last element
- Single element: return that element
- Two elements: compare and return smaller

### Related Problems
- Find Minimum in Rotated Sorted Array II: with duplicates
- Search in Rotated Sorted Array: find specific target
- Find Peak Element: find local maximum
