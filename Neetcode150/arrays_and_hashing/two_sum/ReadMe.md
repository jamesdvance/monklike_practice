# Two Sum

## Summary

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution, and you cannot use the same element twice.

### Key Points
- Use a hash map to store values and their indices
- For each element, check if its complement (target - current) exists in the map
- Single pass solution is possible by checking before adding to map

### Optimal Approach
Iterate through the array once. For each element, calculate its complement. If the complement exists in the hash map, return both indices. Otherwise, add the current element to the map.

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Complexity
- Time: O(n) - single pass through the array
- Space: O(n) - hash map stores up to n elements

---

## Detailed Explanation

### Problem Analysis

Two Sum is arguably the most famous interview problem and serves as an introduction to the "complement lookup" pattern. The key insight is that instead of searching for pairs (O(n^2)), we can search for a specific complement value in O(1) using a hash map.

### Why This Works

For any pair of numbers that sum to target: `a + b = target`, we can rearrange to `b = target - a`. So for each number `a` we encounter, we ask: "Have I already seen `target - a`?" The hash map makes this lookup constant time.

### Alternative Approaches

**Brute Force**
Check every pair of elements.

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

- Time: O(n^2)
- Space: O(1)

**Two Pointers (if indices not required)**
Sort the array and use two pointers from both ends.

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        if current_sum == target:
            return [sorted_nums[left][0], sorted_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

- Time: O(n log n) due to sorting
- Space: O(n) for storing index-value pairs

This is more complex for Two Sum but becomes the preferred approach for Three Sum and similar problems.

### Edge Cases
- Array with two elements: the only possible pair
- Negative numbers: complement calculation still works
- Zero in array: handle normally
- Duplicate values: hash map stores latest index, but we check before adding

### Common Mistakes
- Returning the same index twice (using an element with itself)
- Forgetting to return indices vs values
- Off-by-one errors with index handling

### The Two Sum Pattern Family
This problem introduces a pattern used across many problems:
- Three Sum: fix one element, then Two Sum on remainder
- Four Sum: fix two elements, then Two Sum
- Two Sum II (sorted array): two pointers approach
- Two Sum III (data structure design): optimize for add vs find operations
