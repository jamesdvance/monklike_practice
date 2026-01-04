# Daily Temperatures

## Summary

Given an array of daily temperatures, return an array where each element is the number of days until a warmer temperature. If there is no future day with a warmer temperature, put 0.

### Key Points
- Use a monotonic decreasing stack
- Stack stores indices of temperatures waiting for a warmer day
- When a warmer temperature is found, pop and calculate the difference

### Optimal Approach
Maintain a stack of indices with decreasing temperatures. When a higher temperature is found, pop all smaller temperatures and record the wait time.

```python
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack of indices

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)

    return result
```

### Complexity
- Time: O(n) - each index pushed and popped at most once
- Space: O(n) - stack can hold all indices in decreasing temperature order

---

## Detailed Explanation

### Problem Analysis

For each day, we need to find the next day with a higher temperature. The naive approach would check each subsequent day, giving O(n^2). The monotonic stack approach achieves O(n) by processing temperatures in a clever order.

### Why Monotonic Decreasing Stack

We maintain a stack where temperatures are in decreasing order from bottom to top. When we encounter a temperature higher than the stack top:
- The stack top has found its "next warmer day"
- We can record the answer and pop it
- Repeat until no smaller temperatures remain

Temperatures that never find a warmer day stay on the stack with result 0 (the default).

### Step-by-Step Example

For `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`:

```
i=0, temp=73: stack=[], push 0, stack=[0]
i=1, temp=74: 74>73, pop 0, result[0]=1-0=1, push 1, stack=[1]
i=2, temp=75: 75>74, pop 1, result[1]=2-1=1, push 2, stack=[2]
i=3, temp=71: 71<75, push 3, stack=[2,3]
i=4, temp=69: 69<71, push 4, stack=[2,3,4]
i=5, temp=72: 72>69, pop 4, result[4]=5-4=1
              72>71, pop 3, result[3]=5-3=2
              72<75, push 5, stack=[2,5]
i=6, temp=76: 76>72, pop 5, result[5]=6-5=1
              76>75, pop 2, result[2]=6-2=4
              push 6, stack=[6]
i=7, temp=73: 73<76, push 7, stack=[6,7]

Remaining on stack: result[6]=0, result[7]=0 (already default)
```

Result: [1, 1, 4, 2, 1, 1, 0, 0]

### Alternative: Right-to-Left with Stack

Process from right to left, maintaining a stack of future warmer days:

```python
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack of (temperature, index)

    for i in range(n - 1, -1, -1):
        while stack and temperatures[i] >= stack[-1][0]:
            stack.pop()

        if stack:
            result[i] = stack[-1][1] - i

        stack.append((temperatures[i], i))

    return result
```

This also works but is slightly less intuitive.

### Alternative: Array-Based Optimization

For bounded temperature values, use an array to track the closest index for each temperature:

```python
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    hottest = 0

    for i in range(n - 1, -1, -1):
        temp = temperatures[i]

        if temp >= hottest:
            hottest = temp
            continue

        days = 1
        while temperatures[i + days] <= temp:
            days += result[i + days]

        result[i] = days

    return result
```

This uses O(1) extra space (excluding output) but is trickier to implement correctly.

### The Monotonic Stack Pattern

This pattern applies whenever you need to find the "next greater element":
- Next Greater Element I, II, III
- Stock Span Problem
- Largest Rectangle in Histogram
- Trapping Rain Water (one approach)

### Edge Cases
- All decreasing temperatures: all results are 0
- All increasing temperatures: all results are 1 (except last is 0)
- All same temperature: all results are 0
- Single day: result is [0]

### Related Problems
- Next Greater Element I: same concept, different setup
- Next Greater Element II: circular array variant
- Online Stock Span: count consecutive smaller/equal days
