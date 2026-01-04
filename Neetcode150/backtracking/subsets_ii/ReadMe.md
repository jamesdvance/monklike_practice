# Subsets II

## Summary

Given an integer array `nums` that may contain duplicates, return all possible subsets. The solution must not contain duplicate subsets.

### Key Points
- Sort array to group duplicates together
- Skip duplicate elements at the same recursion level
- Include duplicates at different levels is allowed

### Optimal Approach
Sort first, then skip duplicates when they would create duplicate subsets.

```python
def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    def backtrack(index, current):
        result.append(current[:])

        for i in range(index, len(nums)):
            # Skip duplicates at the same level
            if i > index and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

### Complexity
- Time: O(n * 2^n) worst case
- Space: O(n) for recursion depth

---

## Detailed Explanation

### Problem Analysis

The challenge is avoiding duplicate subsets when input has duplicates. For example, [1, 2, 2] should not produce [1, 2] twice.

### Why Sort and Skip?

Sorting groups duplicates together. The skip condition `i > index and nums[i] == nums[i-1]` ensures:
- First occurrence of a value can be included
- Subsequent occurrences at the same level are skipped

### Visualization

For nums = [1, 2, 2]:

Without duplicate handling:
```
[], [1], [1,2], [1,2,2], [1,2'], [2], [2,2'], [2']
                         ^^^^            ^^^^  ^^^
                      duplicates
```

With duplicate handling:
```
[], [1], [1,2], [1,2,2], [2], [2,2]
```

### The Key Insight

At each recursion level, we choose which element to add next. If we have [1, 2, 2]:
- At level 0: can choose 1, 2 (first), or 2 (second)
- Choosing 2 (second) without first 2 creates same subset as choosing 2 (first)
- So skip 2 (second) at this level

But within a path, we can include both 2s:
- [1] -> [1, 2] -> [1, 2, 2] is valid

### Alternative: Using a Set

Less efficient but simpler:

```python
def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = set()

    def backtrack(index, current):
        result.add(tuple(current))

        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return [list(s) for s in result]
```

### Iterative Approach

Track how many new subsets to add when encountering duplicates:

```python
def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = [[]]
    start = 0

    for i in range(len(nums)):
        # If duplicate, only add to subsets created in last iteration
        if i > 0 and nums[i] == nums[i - 1]:
            new_subsets = [subset + [nums[i]] for subset in result[start:]]
        else:
            new_subsets = [subset + [nums[i]] for subset in result]

        start = len(result)
        result.extend(new_subsets)

    return result
```

### Edge Cases
- All elements same: [1,1,1] -> [[], [1], [1,1], [1,1,1]]
- No duplicates: same as Subsets I
- Single element: [[], [element]]

### Related Problems
- Subsets: without duplicates
- Permutations II: permutations with duplicates
- Combination Sum II: combinations with duplicates
