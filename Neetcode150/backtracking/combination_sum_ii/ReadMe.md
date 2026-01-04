# Combination Sum II

## Summary

Given a collection of candidate numbers and a target, find all unique combinations where the candidates sum to target. Each number may only be used once, and the solution must not contain duplicate combinations.

### Key Points
- Each candidate used at most once
- Candidates may have duplicates
- Sort and skip duplicates at same recursion level

### Optimal Approach
Sort candidates, skip duplicates at the same level, move to next index after using an element.

```python
def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []

    def backtrack(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates at the same level
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # Prune: remaining candidates too large
            if candidates[i] > remaining:
                break

            current.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], current)
            current.pop()

    backtrack(0, target, [])
    return result
```

### Complexity
- Time: O(2^n) worst case
- Space: O(n) for recursion depth

---

## Detailed Explanation

### Problem Analysis

This combines elements from:
- Combination Sum: finding combinations that sum to target
- Subsets II: handling duplicates

Key differences from Combination Sum I:
- Each element used once: pass `i + 1` instead of `i`
- Input has duplicates: skip duplicate values at same level

### Why i > start (not i > 0)?

The condition `i > start` ensures we only skip duplicates at the same recursion level, not across levels.

For candidates = [1, 1, 2], target = 3:
- At level 0: can use first 1, skip second 1 (duplicate at same level)
- But if we take first 1, at level 1 we can take second 1

Valid: [1, 2] (using first 1) and [1, 1, ...] paths
Invalid: Starting with second 1 when first 1 available at same level

### Step-by-Step Example

candidates = [10, 1, 2, 7, 6, 1, 5], target = 8

After sorting: [1, 1, 2, 5, 6, 7, 10]

```
backtrack(0, 8, [])
  i=0: [1], backtrack(1, 7, [1])
    i=1: [1,1], backtrack(2, 6, [1,1])
      i=2: [1,1,2], remaining=4, continue...
      i=4: [1,1,6], remaining=0, add!
    i=2: [1,2], backtrack(3, 5, [1,2])
      i=3: [1,2,5], remaining=0, add!
    i=4: [1,6], remaining=1, continue...
    i=5: [1,7], remaining=0, add!
  i=1: skip (duplicate of i=0)
  i=2: [2], backtrack(3, 6, [2])
    i=4: [2,6], remaining=0, add!
  ...

Result: [[1,1,6], [1,2,5], [1,7], [2,6]]
```

### Comparison with Related Problems

| Problem | Element Reuse | Duplicates in Input | Skip Logic |
|---------|---------------|---------------------|------------|
| Combination Sum | Unlimited | No | None |
| Combination Sum II | Once | Yes | i > start |
| Subsets II | Once | Yes | i > start |

### Edge Cases
- All candidates larger than target: return []
- Single candidate equals target: return [[candidate]]
- Multiple same candidates summing to target: [2,2,2], target=4 -> [[2,2]]

### Related Problems
- Combination Sum: unlimited reuse, no duplicates
- Combination Sum III: k numbers summing to n
- Subsets II: same duplicate handling pattern
