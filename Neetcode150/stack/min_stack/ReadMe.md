# Min Stack

## Summary

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

### Key Points
- Standard stack operations must remain O(1)
- Need to track minimum at each state of the stack
- Two approaches: auxiliary stack or storing pairs

### Optimal Approach
Maintain a second stack that tracks the minimum at each level of the main stack.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### Complexity
- Time: O(1) for all operations
- Space: O(n) for both stacks

---

## Detailed Explanation

### Problem Analysis

The challenge is that when we pop an element that was the minimum, we need to know the new minimum without scanning the entire stack. The solution is to track the minimum at each "level" of the stack.

### Why the Min Stack Works

The min stack only stores a value when it becomes the new minimum (or equals the current minimum). When we pop, we only remove from min stack if the popped value equals the current minimum. This works because:

1. If we pushed a smaller value, it went on min stack
2. If we pop that smaller value, we remove it from min stack
3. The new top of min stack is the minimum of remaining elements

### Why Use <= Instead of <

We use `val <= self.min_stack[-1]` to handle duplicates. If we have two 0s and only push on strict <, we would only track one 0. When we pop the first 0, we would incorrectly pop from min stack even though another 0 remains.

### Alternative: Store Pairs

Store (value, min_so_far) for each element:

```python
class MinStack:
    def __init__(self):
        self.stack = []  # Each element is (value, min_at_this_point)

    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

This is simpler but uses more memory when min changes infrequently.

### Alternative: Store Difference from Min

For memory optimization when values are close together:

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if diff < 0:
                self.min_val = val

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.min_val = self.min_val - diff  # Restore previous min
        if not self.stack:
            self.min_val = None

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.min_val
        return self.min_val + diff

    def getMin(self) -> int:
        return self.min_val
```

This uses O(n) space for differences instead of absolute values, which can be smaller.

### Edge Cases
- Single element: it is both top and min
- All same elements: min stack grows with main stack
- Strictly decreasing: min stack equals main stack
- Strictly increasing: min stack has only first element

### Related Problems
- Max Stack: same concept with maximum
- Design a Stack With Increment Operation: stack with additional operation
- Online Stock Span: similar "lookback" concept
