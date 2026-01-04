# Median of Two Sorted Arrays

## Summary

Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted arrays. The overall runtime complexity should be O(log(m+n)).

### Key Points
- Binary search on the smaller array to find the partition point
- Partition divides both arrays such that left half has (m+n+1)/2 elements
- Median is derived from the elements at the partition boundary

### Optimal Approach
Binary search on the smaller array to find the correct partition that balances both arrays.

```python
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    half_len = (m + n + 1) // 2

    while left <= right:
        i = (left + right) // 2  # Partition point in nums1
        j = half_len - i          # Partition point in nums2

        # Handle edge cases with infinity
        nums1_left = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right = float('inf') if i == m else nums1[i]
        nums2_left = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right = float('inf') if j == n else nums2[j]

        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Found correct partition
            if (m + n) % 2 == 1:
                return max(nums1_left, nums2_left)
            else:
                return (max(nums1_left, nums2_left) +
                        min(nums1_right, nums2_right)) / 2
        elif nums1_left > nums2_right:
            right = i - 1  # Move partition left in nums1
        else:
            left = i + 1   # Move partition right in nums1

    return 0.0
```

### Complexity
- Time: O(log(min(m, n)))
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The median divides a sorted collection into two equal halves. For two sorted arrays, we need to find a partition such that:
1. Left half has (m+n+1)//2 elements (extra element goes to left if odd total)
2. All elements in left half <= all elements in right half

### The Partition Concept

If we partition nums1 at index i and nums2 at index j:
- Left half: nums1[0..i-1] and nums2[0..j-1]
- Right half: nums1[i..m-1] and nums2[j..n-1]

For the partition to be valid:
- nums1[i-1] <= nums2[j] (left of nums1 <= right of nums2)
- nums2[j-1] <= nums1[i] (left of nums2 <= right of nums1)

### Why Binary Search on Smaller Array

We binary search on the smaller array for efficiency (fewer iterations). The constraint j = half_len - i ensures the total left half size is correct.

### Finding the Median

Once we find the correct partition:
- For odd total: median = max(nums1[i-1], nums2[j-1])
- For even total: median = (max(left elements) + min(right elements)) / 2

### Step-by-Step Example

For nums1 = [1, 3], nums2 = [2]:

m=2, n=1, half_len=2

```
i=1, j=1
nums1_left=1, nums1_right=3
nums2_left=2, nums2_right=inf

1 <= inf and 2 <= 3: valid partition
Total is odd, median = max(1, 2) = 2
```

For nums1 = [1, 2], nums2 = [3, 4]:

m=2, n=2, half_len=2

```
i=1, j=1
nums1_left=1, nums1_right=2
nums2_left=3, nums2_right=4

1 <= 4 but 3 > 2: invalid, need more from nums1
left=2

i=2, j=0
nums1_left=2, nums1_right=inf
nums2_left=-inf, nums2_right=3

2 <= 3 and -inf <= inf: valid
Total is even, median = (max(2,-inf) + min(inf,3)) / 2 = (2+3)/2 = 2.5
```

### Why Use Infinity?

When i=0, there are no elements from nums1 in the left half, so nums1_left should not constrain the partition. Using -inf ensures the condition nums1_left <= nums2_right is always satisfied.

Similarly, when i=m, there are no elements from nums1 in the right half, so nums1_right should not constrain. Using inf ensures nums2_left <= nums1_right is always satisfied.

### Common Mistakes
- Not handling edge cases (empty partition)
- Incorrect half_len calculation
- Wrong median formula for odd vs even
- Not searching on the smaller array

### Alternative: O(log(m+n)) with Kth Element

Find the kth element in merged arrays:

```python
def findMedianSortedArrays(nums1, nums2):
    total = len(nums1) + len(nums2)
    if total % 2 == 1:
        return findKth(nums1, nums2, total // 2 + 1)
    else:
        return (findKth(nums1, nums2, total // 2) +
                findKth(nums1, nums2, total // 2 + 1)) / 2

def findKth(nums1, nums2, k):
    if not nums1:
        return nums2[k - 1]
    if not nums2:
        return nums1[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])

    mid1 = nums1[k // 2 - 1] if k // 2 <= len(nums1) else float('inf')
    mid2 = nums2[k // 2 - 1] if k // 2 <= len(nums2) else float('inf')

    if mid1 < mid2:
        return findKth(nums1[k // 2:], nums2, k - k // 2)
    else:
        return findKth(nums1, nums2[k // 2:], k - k // 2)
```

### Related Problems
- Kth Smallest Element in Two Sorted Arrays: generalization
- Merge Two Sorted Lists: simpler O(m+n) approach
- Find K Closest Elements: related binary search
