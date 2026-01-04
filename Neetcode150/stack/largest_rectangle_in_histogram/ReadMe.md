# Largest Rectangle in Histogram

## Summary

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

### Key Points
- For each bar, find how far left and right it can extend
- Use a monotonic increasing stack
- When a shorter bar is found, the previous taller bars can be processed

### Optimal Approach
Maintain a stack of increasing heights. When a shorter bar is encountered, pop taller bars and calculate their maximal rectangles.

```python
def largestRectangleArea(heights: list[int]) -> int:
    stack = []  # Stack of (index, height)
    max_area = 0

    for i, h in enumerate(heights):
        start = i

        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx

        stack.append((start, h))

    # Process remaining bars
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))

    return max_area
```

### Complexity
- Time: O(n) - each bar pushed and popped at most once
- Space: O(n) - stack can hold all bars

---

## Detailed Explanation

### Problem Analysis

For each bar, the largest rectangle with that bar's height extends from the first shorter bar on the left to the first shorter bar on the right. The challenge is finding these boundaries efficiently.

### Why Monotonic Increasing Stack

We maintain a stack where heights increase from bottom to top. When we encounter a height shorter than the stack top:
- The stack top can extend no further to the right (blocked by current bar)
- We can calculate the maximum rectangle for that height
- The popped bar's start index becomes the current bar's potential start (since current bar can extend left through the popped bar's space)

### The Start Index Trick

When we pop a bar and add a new shorter bar, the new bar's "start" position is set to the popped bar's start. This is because the new bar can extend left through all the popped (taller) bars.

### Step-by-Step Example

For `heights = [2, 1, 5, 6, 2, 3]`:

```
i=0, h=2: stack=[(0,2)]
i=1, h=1: 1<2, pop (0,2), area=2*(1-0)=2, start=0
          stack=[(0,1)]
i=2, h=5: stack=[(0,1), (2,5)]
i=3, h=6: stack=[(0,1), (2,5), (3,6)]
i=4, h=2: 2<6, pop (3,6), area=6*(4-3)=6, start=3
          2<5, pop (2,5), area=5*(4-2)=10, start=2
          stack=[(0,1), (2,2)]
i=5, h=3: stack=[(0,1), (2,2), (5,3)]

Remaining:
(5,3): area=3*(6-5)=3
(2,2): area=2*(6-2)=8
(0,1): area=1*(6-0)=6

Maximum: 10
```

### Alternative: Using Sentinel Values

Add 0 at both ends to avoid special handling:

```python
def largestRectangleArea(heights: list[int]) -> int:
    heights = [0] + heights + [0]
    stack = [0]
    max_area = 0

    for i in range(1, len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area
```

The leading 0 ensures we never have an empty stack. The trailing 0 forces all remaining bars to be processed.

### Alternative: For Each Bar, Find Boundaries

```python
def largestRectangleArea(heights: list[int]) -> int:
    n = len(heights)
    left = [0] * n  # First smaller bar to the left
    right = [n] * n  # First smaller bar to the right

    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    max_area = 0
    for i in range(n):
        max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))

    return max_area
```

This explicitly computes left and right boundaries for each bar.

### Connection to Other Problems

This problem is a building block for:
- Maximal Rectangle: largest rectangle in a binary matrix
- Trapping Rain Water: similar stack-based approach

### Edge Cases
- Single bar: area is just that bar's height
- All same height: entire histogram is the rectangle
- Strictly increasing: each bar extends from start
- Strictly decreasing: each bar has width 1

### Related Problems
- Maximal Rectangle: 2D version in binary matrix
- Container With Most Water: related but different (only endpoints matter)
- Trapping Rain Water: similar monotonic stack usage
