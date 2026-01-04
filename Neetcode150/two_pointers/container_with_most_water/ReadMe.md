# Container With Most Water

## Summary

Given an array `height` where `height[i]` is the height of a vertical line at position `i`, find two lines that together with the x-axis form a container that holds the most water.

### Key Points
- Water contained = min(height[left], height[right]) * (right - left)
- Use two pointers from both ends
- Always move the pointer pointing to the shorter line

### Optimal Approach
Start with the widest container (pointers at both ends). Move the shorter side inward, tracking the maximum area found.

```python
def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

### Complexity
- Time: O(n) - each pointer moves at most n times
- Space: O(1) - only pointer variables

---

## Detailed Explanation

### Problem Analysis

This problem asks for the maximum rectangular area that can be formed using two lines and the x-axis. The area is limited by the shorter line (water would overflow over it) and the distance between lines.

### Why Move the Shorter Line

This is the key insight that makes the algorithm work:

When we have pointers at positions `left` and `right`:
- Current height is `min(height[left], height[right])`
- Current width is `right - left`
- Area = height * width

If we move the taller line:
- Width decreases by 1
- Height stays the same or decreases (limited by the shorter line we kept)
- Area cannot increase

If we move the shorter line:
- Width decreases by 1
- Height might increase (if new line is taller)
- Area might increase if height increase compensates for width decrease

Therefore, moving the shorter line is the only way we might find a larger area.

### Correctness Proof

Consider the optimal solution using lines at indices `i` and `j` (i < j). At some point during our algorithm, either:
1. left = i and right = j: we compute this area
2. left = i and right > j: we will move right toward j (until we reach j or find a taller line)
3. left < i and right = j: we will move left toward i

The key is that we never skip over the optimal solution. If `i` is shorter than some `left < i`, we would have moved left toward i. If `j` is shorter than some `right > j`, we would have moved right toward j.

### Step-by-Step Example

For `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`:

```
left=0, right=8: min(1,7)*8 = 8, move left (1 < 7)
left=1, right=8: min(8,7)*7 = 49, move right (8 > 7)
left=1, right=7: min(8,3)*6 = 18, move right (8 > 3)
left=1, right=6: min(8,8)*5 = 40, move right (equal, either works)
left=1, right=5: min(8,4)*4 = 16, move right (8 > 4)
left=1, right=4: min(8,5)*3 = 15, move right (8 > 5)
left=1, right=3: min(8,2)*2 = 4, move right (8 > 2)
left=1, right=2: min(8,6)*1 = 6, move right (8 > 6)
left >= right: done
```

Maximum area: 49

### Common Misconceptions

**Why not check all pairs?**
That would be O(n^2). The two-pointer approach is O(n) because we prove that moving the taller line cannot improve the result.

**Why not just find the two tallest lines?**
Distance matters too. Two tall lines close together might hold less water than shorter lines far apart.

### Alternative: Brute Force

```python
def maxArea(height: list[int]) -> int:
    max_water = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            water = min(height[i], height[j]) * (j - i)
            max_water = max(max_water, water)
    return max_water
```

- Time: O(n^2)
- Space: O(1)

### Edge Cases
- Two elements: only one container possible
- All same height: any container has same area for equal width
- Decreasing heights: best container uses first and second elements
- One very tall line: might not be in optimal solution if isolated

### Related Problems
- Trapping Rain Water: similar setup but different calculation
- Largest Rectangle in Histogram: related area optimization
- Maximal Rectangle: 2D extension
