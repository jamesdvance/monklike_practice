# Valid Parentheses

## Summary

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if brackets are closed in the correct order and each open bracket has a matching close bracket.

### Key Points
- Use a stack to track opening brackets
- When closing bracket encountered, check if it matches the most recent opening bracket
- Valid if stack is empty at the end

### Optimal Approach
Push opening brackets onto stack. For closing brackets, check if the top of stack is the matching opener.

```python
def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0
```

### Complexity
- Time: O(n) - single pass through string
- Space: O(n) - stack can hold up to n/2 opening brackets

---

## Detailed Explanation

### Problem Analysis

This is the quintessential stack problem. The key insight is that the most recent opening bracket must be closed first (LIFO - Last In, First Out), which is exactly what a stack provides.

### Why a Stack?

Consider `"([{}])"`:
- See `(`, push
- See `[`, push
- See `{`, push
- See `}`, must match `{` (most recent), pop
- See `]`, must match `[` (most recent), pop
- See `)`, must match `(` (most recent), pop
- Empty stack, valid

The nested structure requires us to match the innermost pair first, then work outward.

### Alternative: Counter-Based (Only Works for Single Bracket Type)

For just `()` characters:
```python
def isValid(s: str) -> bool:
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return count == 0
```

This fails for multiple bracket types because it does not track which type of bracket to close.

### Common Invalid Cases

1. **Mismatched types**: `"(]"` - closing bracket does not match opening
2. **Wrong order**: `")("` - closing before opening
3. **Unclosed**: `"(("` - opening brackets left on stack
4. **Extra closing**: `"())"` - more closing than opening

### Edge Cases
- Empty string: valid (no brackets to mismatch)
- Single character: invalid (cannot be paired)
- All opening: invalid (stack not empty)
- All closing: invalid (stack empty when trying to match)

### Implementation Variations

**Using a mapping for openers instead**:
```python
def isValid(s: str) -> bool:
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in pairs:
            stack.append(pairs[char])  # Push expected closer
        elif not stack or stack.pop() != char:
            return False

    return not stack
```

This pushes the expected closing bracket, making the comparison simpler.

### Related Problems
- Generate Parentheses: create all valid combinations
- Longest Valid Parentheses: find longest valid substring
- Remove Invalid Parentheses: make string valid with minimum removals
- Valid Parenthesis String: with wildcard character
