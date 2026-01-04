# Merge Triplets to Form Target Triplet

## Summary

Given an array of triplets and a target triplet, determine if we can select some triplets and merge them (taking max of each position) to form the target.

### Key Points
- A triplet is usable only if all its values <= corresponding target values
- From usable triplets, check if we can achieve each target value
- Greedy: collect achievable positions

### Optimal Approach
Filter valid triplets, check if all target values are achievable.

```python
def mergeTriplets(triplets: list[list[int]], target: list[int]) -> bool:
    good = set()

    for triplet in triplets:
        # Skip if any value exceeds target
        if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
            continue

        # Mark which target values this triplet can help achieve
        for i in range(3):
            if triplet[i] == target[i]:
                good.add(i)

    return len(good) == 3
```

### Complexity
- Time: O(n) where n is number of triplets
- Space: O(1) - at most 3 elements in set

---

## Detailed Explanation

### Problem Analysis

When we merge triplets, we take the maximum at each position. To achieve target:
1. We need at least one triplet with target[0] in position 0
2. We need at least one triplet with target[1] in position 1
3. We need at least one triplet with target[2] in position 2

But: if any triplet has a value > target in any position, using it would exceed target.

### The Key Insight

A triplet is "valid" if all its values are <= target values. Among valid triplets, we just need to find triplets that match each target position.

### Why This Works

- If triplet[i] > target[i], we can never use this triplet (max would exceed target)
- If all triplet values <= target values, using it is safe
- If triplet[i] == target[i], it helps achieve position i

Since we take max, using multiple valid triplets can only help (never hurt).

### Step-by-Step Example

```
triplets = [[2,5,3], [1,8,4], [1,7,5]]
target = [2,7,5]

Triplet [2,5,3]:
  2 <= 2, 5 <= 7, 3 <= 5 -> Valid
  Position 0: 2 == 2 -> good.add(0)

Triplet [1,8,4]:
  8 > 7 -> Invalid (skip)

Triplet [1,7,5]:
  1 <= 2, 7 <= 7, 5 <= 5 -> Valid
  Position 1: 7 == 7 -> good.add(1)
  Position 2: 5 == 5 -> good.add(2)

good = {0, 1, 2} -> all positions covered

Answer: True
```

Merge [2,5,3] and [1,7,5]:
- max(2,1) = 2
- max(5,7) = 7
- max(3,5) = 5
- Result: [2,7,5] = target

### Alternative: Track Each Position

```python
def mergeTriplets(triplets: list[list[int]], target: list[int]) -> bool:
    can_reach = [False, False, False]

    for triplet in triplets:
        if all(triplet[i] <= target[i] for i in range(3)):
            for i in range(3):
                if triplet[i] == target[i]:
                    can_reach[i] = True

    return all(can_reach)
```

### Why Not Greedy Select Maximum?

We can't just try to maximize each position independently because:
- Triplet [5,1,1] maximizes position 0
- But if target[0] = 3, this triplet is unusable

We must ensure we never exceed target in ANY position.

### Edge Cases
- Single triplet equals target: True
- No valid triplet for some position: False
- All triplets invalid: False

### Related Problems
- Maximum Product of Three Numbers: selecting elements
- 3Sum: working with triplets
- Max Increase to Keep City Skyline: grid max operations
