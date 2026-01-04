# Two Sum II - Input Array Is Sorted

## Summary

Given a 1-indexed sorted array `numbers`, find two numbers that add up to a specific `target`. Return the indices of the two numbers (1-indexed). You may not use the same element twice.

### Key Points
- Array is already sorted - exploit this property
- Two pointers from both ends is optimal
- Guaranteed exactly one solution exists

### Optimal Approach
Use two pointers starting at the beginning and end. If the sum is too small, move the left pointer right. If too large, move the right pointer left.

```python
def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # No solution (won't reach here per problem constraints)
```

### Complexity
- Time: O(n) - each pointer moves at most n times
- Space: O(1) - only two pointers

---

## Detailed Explanation

### Problem Analysis

This problem demonstrates how sorted input enables the two-pointer technique. Unlike the original Two Sum (which uses a hash map), the sorted property allows us to systematically narrow down the search space without additional data structures.

### Why Two Pointers Work on Sorted Arrays

Consider sorted array `[1, 3, 5, 7, 9]` with target `10`:
- Start with smallest (1) + largest (9) = 10. Found it.

If target were `8`:
- 1 + 9 = 10 (too big) -> move right pointer left
- 1 + 7 = 8. Found it.

If target were `12`:
- 1 + 9 = 10 (too small) -> move left pointer right
- 3 + 9 = 12. Found it.

The key insight: if the current sum is too small, making the right pointer smaller cannot help (it would make the sum even smaller). So we must move the left pointer to increase the sum. Vice versa for too large sums.

### Correctness Proof

Assume the solution is at indices `i` and `j` where `i < j`. When pointers are at positions `left` and `right`:
- If `left < i`, we will eventually move left to i (we never skip over the solution)
- If `right > j`, we will eventually move right to j
- We cannot move left past i or right past j without finding the solution

### Comparison with Hash Map Approach

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Two Pointers | O(n) | O(1) | Array is sorted |
| Hash Map | O(n) | O(n) | Array is unsorted |

Two pointers is strictly better when the array is already sorted because it achieves the same time complexity with less space.

### Alternative: Binary Search

For each element, binary search for its complement:

```python
def twoSum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        complement = target - numbers[i]
        left, right = i + 1, len(numbers) - 1

        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1

    return []
```

- Time: O(n log n)
- Space: O(1)

This is worse than two pointers but demonstrates binary search on sorted arrays.

### Edge Cases
- Two elements: only one possible pair
- Duplicate values: handled correctly by two pointers
- Negative numbers: algorithm works the same
- Target requires same value twice: e.g., [1, 2, 2, 3], target=4

### 1-Indexed Output

This problem uses 1-indexed output, which is uncommon. Remember to add 1 to both indices before returning.

### Related Problems
- Two Sum: unsorted version using hash map
- 3Sum: fix one element, then Two Sum II on remainder
- Two Sum Less Than K: find pair with sum less than k
- Two Sum IV - Input is a BST: tree version
