# Search in Rotated Sorted Array

## Summary

A sorted array has been rotated at an unknown pivot. Given the rotated array and a target, return the index of target if found, otherwise -1. All elements are unique.

### Key Points
- Array is sorted but rotated (e.g., [4,5,6,7,0,1,2])
- At least one half is always sorted
- Determine which half is sorted and if target is in that range

### Optimal Approach
At each step, identify the sorted half and determine if target is within that range.

```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

### Complexity
- Time: O(log n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

In a rotated sorted array, the rotation creates a "pivot point" where the order breaks. For example, [4,5,6,7,0,1,2] has the pivot between 7 and 0. The key insight is that at any mid point, at least one half of the array is properly sorted.

### Identifying the Sorted Half

Compare nums[left] with nums[mid]:
- If nums[left] <= nums[mid]: left half [left, mid] is sorted
- Otherwise: right half [mid, right] is sorted

### Decision Logic

Once we know which half is sorted, we check if target is in that range:
- If target is in the sorted half, search there
- Otherwise, search the other half

For the sorted left half [left, mid]:
- Target is in this range if: nums[left] <= target < nums[mid]

For the sorted right half [mid, right]:
- Target is in this range if: nums[mid] < target <= nums[right]

### Step-by-Step Example

For `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`:

```
left=0, right=6, mid=3, nums[mid]=7
nums[0]=4 <= nums[3]=7, left half sorted
target=0 not in [4,7), so left=4

left=4, right=6, mid=5, nums[mid]=1
nums[4]=0 <= nums[5]=1, left half sorted
target=0 in [0,1), so right=4

left=4, right=4, mid=4, nums[mid]=0
Found! return 4
```

### Why nums[left] <= nums[mid]?

We use `<=` instead of `<` to handle the case when left == mid (subarray of 1 or 2 elements). In this case, the "left half" is just nums[left], which is trivially sorted.

### Alternative: Find Pivot First

Find the rotation point, then binary search in the appropriate half:

```python
def search(nums: list[int], target: int) -> int:
    n = len(nums)

    # Find pivot (minimum element)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    pivot = left

    # Determine which half to search
    if target >= nums[pivot] and target <= nums[n - 1]:
        left, right = pivot, n - 1
    else:
        left, right = 0, pivot - 1

    # Standard binary search
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

This is clearer but requires two passes.

### Edge Cases
- Array not rotated (rotation by 0 or n): standard binary search works
- Single element: check if it equals target
- Two elements: handle carefully in sorted half detection
- Target not present: return -1

### Related Problems
- Search in Rotated Sorted Array II: with duplicates (harder)
- Find Minimum in Rotated Sorted Array: find the pivot point
- Find Minimum in Rotated Sorted Array II: with duplicates
