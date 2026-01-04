# Koko Eating Bananas

## Summary

Koko has `piles` of bananas and `h` hours to eat them all. She can eat at most `k` bananas per hour from one pile. Find the minimum integer `k` such that she can eat all bananas within `h` hours.

### Key Points
- Binary search on the answer (eating speed k)
- For each speed, check if all bananas can be eaten in time
- Hours needed for pile p at speed k: ceil(p/k)

### Optimal Approach
Binary search on k from 1 to max(piles). For each k, calculate total hours needed.

```python
import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    def canFinish(speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid  # Try smaller speed
        else:
            left = mid + 1  # Need faster speed

    return left
```

### Complexity
- Time: O(n log m) where n is number of piles and m is max pile size
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

This is a classic "binary search on answer" problem. Instead of searching for an element in an array, we search for the minimum value of a parameter (eating speed) that satisfies a condition.

### Why Binary Search Works

- If Koko can finish with speed k, she can also finish with any speed > k
- If Koko cannot finish with speed k, she cannot finish with any speed < k
- This monotonic property enables binary search

The search space is [1, max(piles)]:
- Minimum possible speed is 1 (eat at least 1 banana per hour)
- Maximum needed speed is max(piles) (finish largest pile in 1 hour)

### Hours Calculation

For each pile of size p at eating speed k:
- Koko spends ceil(p/k) hours on that pile
- She must finish one pile before moving to the next

```python
# Three ways to calculate ceiling division
hours = math.ceil(pile / speed)
hours = (pile + speed - 1) // speed
hours = -(-pile // speed)  # Negative floor trick
```

### Binary Search Pattern

We use `left < right` with `right = mid` pattern to find the leftmost valid speed:

```python
while left < right:
    mid = (left + right) // 2
    if canFinish(mid):
        right = mid      # mid works, but maybe smaller works too
    else:
        left = mid + 1   # mid doesn't work, need larger
```

When loop exits, left == right and is the minimum valid speed.

### Step-by-Step Example

For `piles = [3, 6, 7, 11]`, `h = 8`:

Search space: [1, 11]

```
mid=6: hours = 1+1+2+2 = 6 <= 8, works, right=6
mid=3: hours = 1+2+3+4 = 10 > 8, fails, left=4
mid=5: hours = 1+2+2+3 = 8 <= 8, works, right=5
mid=4: hours = 1+2+2+3 = 8 <= 8, works, right=4
left=4, right=4, done
```

Answer: 4

### Edge Cases
- h equals number of piles: must eat each pile in 1 hour, answer is max(piles)
- h is very large: answer is 1
- Single pile: answer is ceil(pile/h)

### The "Binary Search on Answer" Pattern

This pattern applies when:
1. You need to find the minimum/maximum value satisfying a condition
2. The condition is monotonic (if it holds for x, it holds for all greater/smaller x)
3. Checking the condition for a specific value is efficient

Other examples:
- Capacity to ship packages within D days
- Split array largest sum
- Magnetic force between balls

### Related Problems
- Minimum Speed to Arrive on Time: similar pattern
- Split Array Largest Sum: binary search on the maximum sum
- Capacity To Ship Packages Within D Days: nearly identical structure
