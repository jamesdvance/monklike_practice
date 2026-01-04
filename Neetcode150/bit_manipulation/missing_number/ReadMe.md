# Missing Number

## Summary

Given an array containing n distinct numbers in the range [0, n], find the missing number.

### Key Points
- XOR all indices and values; duplicates cancel
- Or use math: expected_sum - actual_sum
- Both approaches are O(n) time, O(1) space

### Optimal Approach
XOR-based solution.

```python
def missingNumber(nums: list[int]) -> int:
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

If array had all numbers 0 to n, XORing all would give 0.
With one missing, we get the missing number as the result.

Alternatively: sum(0 to n) - sum(nums) = missing number.

### Why XOR Works

```
nums = [3, 0, 1] (missing 2)
n = 3

XOR all: 0 ^ 1 ^ 2 ^ 3 ^ 3 ^ 0 ^ 1
       = (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ 2
       = 0 ^ 0 ^ 0 ^ 2
       = 2
```

All paired numbers cancel, leaving the missing one.

### Step-by-Step Example

```
nums = [0, 1, 3]
n = 3

result = 3 (initialize with n)

i=0: result ^= 0 ^ 0 = 3 ^ 0 ^ 0 = 3
i=1: result ^= 1 ^ 1 = 3 ^ 1 ^ 1 = 3
i=2: result ^= 2 ^ 3 = 3 ^ 2 ^ 3 = 2

Answer: 2
```

### Alternative: Math Formula

```python
def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual
```

Uses Gauss's formula: sum(0..n) = n*(n+1)/2

### Alternative: Hash Set

```python
def missingNumber(nums: list[int]) -> int:
    num_set = set(nums)
    for i in range(len(nums) + 1):
        if i not in num_set:
            return i
```

Time: O(n), Space: O(n)

### Alternative: Sorting

```python
def missingNumber(nums: list[int]) -> int:
    nums.sort()
    for i, num in enumerate(nums):
        if i != num:
            return i
    return len(nums)
```

Time: O(n log n), Space: O(1) or O(n) depending on sort.

### XOR Detailed Trace

```
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = 9

XOR indices 0-8: 0^1^2^3^4^5^6^7^8
XOR values: 9^6^4^2^3^5^7^0^1 = 0^1^2^3^4^5^6^7^9
XOR with n=9: adds 9

Full XOR: 0^1^2^3^4^5^6^7^8^9 ^ 0^1^2^3^4^5^6^7^9
        = (pairs cancel) ^ 8
        = 8

Answer: 8
```

### Comparison of Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| XOR | O(n) | O(1) | No overflow risk |
| Math | O(n) | O(1) | Potential overflow for large n |
| Set | O(n) | O(n) | Extra memory |
| Sort | O(n log n) | O(1)* | Modifies input |

### Binary Search (Sorted Input)

If input were sorted:
```python
def missingNumber(nums: list[int]) -> int:
    nums.sort()
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > mid:
            right = mid
        else:
            left = mid + 1

    return left
```

### Cyclic Sort Approach

```python
def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    i = 0

    while i < n:
        j = nums[i]
        if j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n
```

Place each number at its index, find the misplaced one.

### Edge Cases
- [0]: missing 1
- [1]: missing 0
- [0, 1, 2, ..., n-1]: missing n

### Related Problems
- Single Number: XOR-based
- Find All Numbers Disappeared: similar pattern
- First Missing Positive: harder variant
