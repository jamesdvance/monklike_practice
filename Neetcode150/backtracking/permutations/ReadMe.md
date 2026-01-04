# Permutations

## Summary

Given an array `nums` of distinct integers, return all possible permutations.

### Key Points
- Permutations are ordered arrangements
- Each element appears exactly once in each permutation
- Total permutations = n! for n elements

### Optimal Approach
Backtracking with used tracking to avoid repeating elements.

```python
def permute(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()

    backtrack([])
    return result
```

### Complexity
- Time: O(n! * n) - n! permutations, each takes O(n) to check membership and copy
- Space: O(n) for recursion depth

---

## Detailed Explanation

### Problem Analysis

A permutation uses all elements exactly once. For n elements, there are n choices for the first position, n-1 for the second, etc., giving n! total permutations.

### Decision Tree

For nums = [1, 2, 3]:

```
                   []
               /   |   \
             1     2     3
            / \   / \   / \
          12  13 21  23 31  32
          |   |   |   |   |   |
         123 132 213 231 312 321
```

### Optimized with Used Array

Using a boolean array instead of checking membership:

```python
def permute(nums: list[int]) -> list[list[int]]:
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    backtrack([])
    return result
```

### Swap-Based Approach (In-Place)

Swap elements to generate permutations without extra space for `current`:

```python
def permute(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
```

This swaps elements into position, generating permutations by varying which element is at each index.

### Iterative Approach

Build permutations by inserting each number at all positions:

```python
def permute(nums: list[int]) -> list[list[int]]:
    result = [[]]

    for num in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_result.append(perm[:i] + [num] + perm[i:])
        result = new_result

    return result
```

### Edge Cases
- Single element: return [[element]]
- Two elements: return [[a,b], [b,a]]

### Related Problems
- Permutations II: with duplicate elements
- Next Permutation: find lexicographically next permutation
- Permutation Sequence: find kth permutation
