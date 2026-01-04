# Stack

## Summary

A stack is a Last-In-First-Out (LIFO) data structure. Elements are added (pushed) and removed (popped) from the same end, called the top. Stacks are fundamental for problems involving nested structures, undo operations, and next/previous greater/smaller element queries.

### Core Concepts

**Stack Operations**
- push(x): Add element to top - O(1)
- pop(): Remove and return top element - O(1)
- peek()/top(): Return top element without removing - O(1)
- isEmpty(): Check if stack is empty - O(1)

**When to Use a Stack**
- Matching pairs (parentheses, tags)
- Evaluating expressions
- Backtracking (undo/redo)
- Next greater/smaller element problems
- Maintaining order with constraints

### Monotonic Stack

A special pattern where the stack maintains elements in sorted order (all increasing or all decreasing). Used for "next greater element" type problems where you need to find the nearest larger or smaller element.

---

## Problems in This Section

### Valid Parentheses
Determine if a string of brackets is valid (properly opened and closed).
- Pattern: Stack for matching pairs
- Key insight: Most recent opening bracket must be closed first (LIFO)

### Min Stack
Design a stack that supports O(1) getMin operation.
- Pattern: Auxiliary stack tracking minimums
- Key insight: Track minimum at each stack level

### Evaluate Reverse Polish Notation
Evaluate an expression in postfix notation.
- Pattern: Stack for operands
- Key insight: Operators act on the two most recent operands

### Generate Parentheses
Generate all valid combinations of n pairs of parentheses.
- Pattern: Backtracking with constraints
- Key insight: Can add ) only when open count > close count

### Daily Temperatures
Find days until a warmer temperature for each day.
- Pattern: Monotonic decreasing stack
- Key insight: When warmer day found, all cooler days on stack get their answer

### Car Fleet
Count how many car fleets arrive at the destination.
- Pattern: Stack for fleet leaders
- Key insight: Slower car ahead blocks faster cars behind

### Largest Rectangle in Histogram
Find the largest rectangle that can be formed in a histogram.
- Pattern: Monotonic increasing stack
- Key insight: When shorter bar found, calculate max rectangle for taller bars

---

## Monotonic Stack Pattern

Monotonic stacks maintain elements in sorted order and are used when you need to find the nearest larger or smaller element.

**Monotonic Increasing (for "next smaller")**
```python
stack = []
for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        # arr[i] is the next smaller for arr[stack[-1]]
        process(stack.pop(), i)
    stack.append(i)
```

**Monotonic Decreasing (for "next greater")**
```python
stack = []
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        # arr[i] is the next greater for arr[stack[-1]]
        process(stack.pop(), i)
    stack.append(i)
```

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Valid Parentheses | O(n) | O(n) |
| Min Stack | O(1) per op | O(n) |
| Evaluate Reverse Polish Notation | O(n) | O(n) |
| Generate Parentheses | O(4^n/sqrt(n)) | O(n) |
| Daily Temperatures | O(n) | O(n) |
| Car Fleet | O(n log n) | O(n) |
| Largest Rectangle in Histogram | O(n) | O(n) |

---

## Common Patterns

### Matching Pattern
For every opening symbol, push it. For every closing symbol, pop and check if it matches.

### Evaluation Pattern
For operands, push onto stack. For operators, pop operands, compute, push result.

### Next Greater/Smaller Pattern
Process elements left to right. Pop all elements that have found their answer. Push current element.

### Min/Max Tracking Pattern
Maintain auxiliary structure (second stack, tuple, etc.) to track min/max at each level.

---

## Key Takeaways

1. **LIFO is the key**: When the most recent element needs to be processed first, use a stack.

2. **Monotonic stacks are powerful**: They solve "next greater element" problems in O(n) instead of O(n^2).

3. **Store indices, not just values**: Often you need both the value and its position.

4. **Handle remaining elements**: After processing all elements, the stack may still contain elements that need final processing.

5. **Sentinel values simplify edge cases**: Adding dummy values at the beginning or end can eliminate special-case handling.
