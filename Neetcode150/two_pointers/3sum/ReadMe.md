# 3Sum

## Summary

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

### Key Points
- Sort the array first to enable two-pointer technique and duplicate skipping
- Fix one element, then use Two Sum II on the remainder
- Skip duplicates at each level to avoid duplicate triplets

### Optimal Approach
Sort the array. For each element, use two pointers on the remaining elements to find pairs that sum to the negative of the fixed element.

```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Early termination: if smallest is positive, no solution possible
        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result
```

### Complexity
- Time: O(n^2) - O(n log n) for sort plus O(n^2) for nested loops
- Space: O(1) or O(n) depending on sort implementation

---

## Detailed Explanation

### Problem Analysis

3Sum extends Two Sum to three elements. The key insight is that we can reduce it to Two Sum by fixing one element: if we need `a + b + c = 0`, then for fixed `a`, we need `b + c = -a`. This is exactly Two Sum II on a sorted array.

### Why Sort First

Sorting enables:
1. Two-pointer technique for the inner loop
2. Easy duplicate skipping (duplicates are adjacent)
3. Early termination (if current element > 0, no valid triplet)

### Handling Duplicates

The trickiest part is avoiding duplicate triplets. We skip duplicates at two levels:

1. **First element**: Skip if `nums[i] == nums[i-1]`
2. **Second and third elements**: After finding a triplet, skip while values repeat

```python
# Example: [-2, -2, 0, 0, 2, 2]
# After finding [-2, 0, 2], skip duplicate -2s, 0s, and 2s
```

### Step-by-Step Example

For `nums = [-1, 0, 1, 2, -1, -4]`:

After sorting: `[-4, -1, -1, 0, 1, 2]`

- i=0, nums[i]=-4, target=4
  - left=1 (-1), right=5 (2): sum=1, too small, left++
  - left=2 (-1), right=5 (2): sum=1, too small, left++
  - ...no valid pair

- i=1, nums[i]=-1, target=1
  - left=2 (-1), right=5 (2): sum=1, found! Add [-1, -1, 2]
  - left=3 (0), right=4 (1): sum=1, found! Add [-1, 0, 1]

- i=2, nums[i]=-1, skip (duplicate of i=1)

- i=3, nums[i]=0, target=0
  - left=4 (1), right=5 (2): sum=3, too big, right--
  - left >= right, done

Result: `[[-1, -1, 2], [-1, 0, 1]]`

### Alternative: Hash Set for Deduplication

Instead of careful duplicate skipping, use a set:

```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = set()

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            if nums[left] + nums[right] == target:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

    return [list(t) for t in result]
```

This is simpler but slightly slower due to set operations.

### Edge Cases
- Array with fewer than 3 elements: return empty list
- All zeros: return [[0, 0, 0]]
- No valid triplet: return empty list
- All negative or all positive: return empty list

### Common Mistakes
- Forgetting to skip duplicates
- Off-by-one in duplicate skipping loops
- Not moving both pointers after finding a match
- Forgetting to sort

### Related Problems
- Two Sum II: the inner loop of 3Sum
- 4Sum: add another level of iteration
- 3Sum Closest: find triplet with sum closest to target
- 3Sum Smaller: count triplets with sum less than target
