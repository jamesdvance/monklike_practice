# Combination Sum

## Summary

Given an array of distinct integers `candidates` and a target integer `target`, return all unique combinations where the chosen numbers sum to target. The same number may be chosen unlimited times.

### Key Points
- Each candidate can be used multiple times
- Combinations must be unique (order does not matter)
- Use backtracking with remaining target tracking

### Optimal Approach
Backtrack through candidates, subtracting from target and allowing reuse.

```python
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def backtrack(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            # Pass i (not i+1) to allow reuse
            backtrack(i, remaining - candidates[i], current)
            current.pop()

    backtrack(0, target, [])
    return result
```

### Complexity
- Time: O(n^(T/M)) where T is target and M is minimum candidate
- Space: O(T/M) for recursion depth

---

## Detailed Explanation

### Problem Analysis

This problem differs from standard combinations in two ways:
1. Elements can be reused
2. We seek a specific sum, not all subsets

The key insight is using a `start` index to avoid duplicate combinations while allowing the same element to be picked again.

### Why start Index?

Without `start`, we might generate [2,3] and [3,2] as separate combinations. By only considering candidates from `start` onwards, we ensure each combination is generated exactly once in sorted order.

### Decision Tree

For candidates = [2, 3, 6, 7], target = 7:

```
                        target=7
                     /    |    \    \
                  2       3     6    7
                 /|\      |     |
               2  3 6    3 6   (done)
              /|  |
            2  3  (done: 2+2+3=7)
           /
         (done: 2+2+2+... exceeds)
```

### Optimization: Sort and Prune

Sort candidates and break early when candidate exceeds remaining:

```python
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []

    def backtrack(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # Prune: remaining candidates are too large

            current.append(candidates[i])
            backtrack(i, remaining - candidates[i], current)
            current.pop()

    backtrack(0, target, [])
    return result
```

### Step-by-Step Example

candidates = [2, 3, 6, 7], target = 7

```
backtrack(0, 7, [])
  i=0: append 2, backtrack(0, 5, [2])
    i=0: append 2, backtrack(0, 3, [2,2])
      i=0: append 2, backtrack(0, 1, [2,2,2])
        i=0: 2 > 1, return
      i=1: append 3, backtrack(1, 0, [2,2,3])
        remaining=0, add [2,2,3] to result
    i=1: append 3, backtrack(1, 2, [2,3])
      i=1: 3 > 2, return
  i=1: append 3, backtrack(1, 4, [3])
    i=1: append 3, backtrack(1, 1, [3,3])
      i=1: 3 > 1, return
  i=2: append 6, backtrack(2, 1, [6])
    i=2: 6 > 1, return
  i=3: append 7, backtrack(3, 0, [7])
    remaining=0, add [7] to result

Result: [[2,2,3], [7]]
```

### Edge Cases
- Target is 0: return [[]] (empty combination)
- No valid combination: return []
- Single candidate equals target: return [[candidate]]

### Related Problems
- Combination Sum II: each candidate used once, with duplicates
- Combination Sum III: k numbers that sum to n
- Coin Change: count ways, not enumerate
