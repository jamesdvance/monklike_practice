# Trapping Rain Water

## Summary

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water can be trapped after raining.

### Key Points
- Water at each position = min(max_left, max_right) - height[i]
- Multiple approaches: precompute arrays, two pointers, or stack
- Two-pointer solution is optimal for both time and space

### Optimal Approach (Two Pointers)
Track the maximum heights seen from left and right. At each step, process the side with the smaller maximum.

```python
def trap(height: list[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water
```

### Complexity
- Time: O(n) - single pass through the array
- Space: O(1) - only a few variables

---

## Detailed Explanation

### Problem Analysis

Water trapped above any bar depends on the tallest bars to its left and right. The water level at position `i` is determined by the minimum of these two maximums (water would flow over the lower side). Water trapped at position `i` equals this level minus the bar's own height.

### The Core Formula

```
water_at[i] = max(0, min(max_left[i], max_right[i]) - height[i])
```

### Why Two Pointers Work

The insight is that we do not need to know both left_max and right_max to process a position. If `left_max < right_max`, we know the water level at `left` is determined by `left_max` regardless of what right_max actually is - we only need to know it is at least as big.

When `left_max < right_max`:
- Water at left position is bounded by left_max
- We can process left position and move left pointer
- left_max will not be affected by future right positions

### Alternative Approaches

**Precomputed Arrays**
Calculate left_max and right_max arrays first:

```python
def trap(height: list[int]) -> int:
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water
```

- Time: O(n)
- Space: O(n)

**Monotonic Stack**
Use a stack to track decreasing heights and calculate trapped water when we find a taller bar:

```python
def trap(height: list[int]) -> int:
    stack = []
    water = 0

    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break

            width = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[bottom]
            water += width * bounded_height

        stack.append(i)

    return water
```

- Time: O(n)
- Space: O(n)

This calculates water layer by layer horizontally, rather than column by column.

### Step-by-Step Example (Two Pointers)

For `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`:

```
Initial: left=0, right=11, left_max=0, right_max=1, water=0

left_max(0) < right_max(1):
  left=1, left_max=1, water += 1-1 = 0

left_max(1) <= right_max(1):
  right=10, right_max=2, water += 2-2 = 0

left_max(1) < right_max(2):
  left=2, left_max=1, water += 1-0 = 1

... continuing until left meets right
```

Total water: 6

### Visualization

```
       #
   #   ##
 # ## ####
############
```

Water fills the gaps between bars up to the limiting height.

### Edge Cases
- Empty array: return 0
- Single or two elements: cannot trap water
- Monotonically increasing or decreasing: no water trapped
- Flat array: no water trapped
- Valley shape: maximum trapping potential

### Common Mistakes
- Off-by-one errors when comparing left_max and right_max
- Forgetting to update max values before calculating water
- Not handling empty input

### Related Problems
- Container With Most Water: maximize area with two lines
- Largest Rectangle in Histogram: related bar problem
- Product of Array Except Self: similar prefix/suffix concept
