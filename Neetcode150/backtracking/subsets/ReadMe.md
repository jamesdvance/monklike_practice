# Subsets

## Summary

Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution must not contain duplicate subsets.

### Key Points
- Each element has two choices: include or exclude
- Total subsets = 2^n for n elements
- Can use backtracking or iterative bit manipulation

### Optimal Approach
Backtracking with include/exclude decisions at each element.

```python
def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return

        # Include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()

        # Exclude nums[index]
        backtrack(index + 1, current)

    backtrack(0, [])
    return result
```

### Complexity
- Time: O(n * 2^n) - 2^n subsets, each takes O(n) to copy
- Space: O(n) for recursion depth (excluding output)

---

## Detailed Explanation

### Problem Analysis

The power set of a set with n elements has 2^n subsets. For each element, we decide whether to include it or not. This creates a binary decision tree with 2^n leaves.

### Decision Tree Visualization

For nums = [1, 2, 3]:

```
                    []
                   /  \
               [1]     []
              /   \   /   \
          [1,2] [1] [2]   []
          / \   / \ / \   / \
      [1,2,3][1,2][1,3][1][2,3][2][3][]
```

### Alternative: Iterative Approach

Build subsets by adding each number to existing subsets:

```python
def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result
```

Step by step for [1, 2, 3]:
- Start: [[]]
- Add 1: [[], [1]]
- Add 2: [[], [1], [2], [1,2]]
- Add 3: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

### Alternative: Bit Manipulation

Each subset corresponds to a binary number from 0 to 2^n - 1:

```python
def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = []

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result
```

For [1, 2, 3]:
- 000 -> []
- 001 -> [1]
- 010 -> [2]
- 011 -> [1, 2]
- ...

### Edge Cases
- Empty array: return [[]]
- Single element: return [[], [element]]

### Related Problems
- Subsets II: with duplicate elements
- Combinations: subsets of specific size
- Permutations: ordered arrangements
