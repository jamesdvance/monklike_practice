# Generate Parentheses

## Summary

Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

### Key Points
- Use backtracking to build valid combinations
- Two choices at each step: add open or close parenthesis
- Valid if: open count <= n, close count <= open count

### Optimal Approach
Recursively build strings, adding `(` when we have not used all, adding `)` when we have more open than close.

```python
def generateParenthesis(n: int) -> list[str]:
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result
```

### Complexity
- Time: O(4^n / sqrt(n)) - Catalan number of valid sequences
- Space: O(n) - recursion depth

---

## Detailed Explanation

### Problem Analysis

This problem generates all valid parentheses combinations. The key insight is that at any point in building the string:
1. We can add `(` if we have not used n of them yet
2. We can add `)` only if we have more `(` than `)` so far

### Why These Rules Ensure Validity

**Open count < n**: We have n pairs, so at most n opening brackets.

**Close count < open count**: At any position, we cannot have more closing than opening brackets (that would mean a `)` without matching `(`).

### Backtracking Tree

For n = 2:
```
                     ""
                     |
                    "("
                   /   \
                "(("   "()"
                 |       |
               "(()"   "()()"
                 |
              "(())"
```

The tree prunes invalid paths (e.g., starting with `)` or having more `)` than `(`).

### Alternative: Iterative with Stack

```python
def generateParenthesis(n: int) -> list[str]:
    result = []
    stack = [('', 0, 0)]  # (current_string, open_count, close_count)

    while stack:
        current, open_count, close_count = stack.pop()

        if len(current) == 2 * n:
            result.append(current)
            continue

        if open_count < n:
            stack.append((current + '(', open_count + 1, close_count))

        if close_count < open_count:
            stack.append((current + ')', open_count, close_count + 1))

    return result
```

### Catalan Numbers

The number of valid combinations is the nth Catalan number:
- C(0) = 1
- C(1) = 1
- C(2) = 2
- C(3) = 5
- C(4) = 14
- C(n) = (2n)! / ((n+1)! * n!)

The Catalan number grows approximately as 4^n / (n^(3/2) * sqrt(pi)).

### Using a List Instead of String

For efficiency, build with a list and join at the end:

```python
def generateParenthesis(n: int) -> list[str]:
    result = []
    current = []

    def backtrack(open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(''.join(current))
            return

        if open_count < n:
            current.append('(')
            backtrack(open_count + 1, close_count)
            current.pop()

        if close_count < open_count:
            current.append(')')
            backtrack(open_count, close_count + 1)
            current.pop()

    backtrack(0, 0)
    return result
```

String concatenation creates new strings, while list append/pop modifies in place.

### Edge Cases
- n = 0: return [""] or [] depending on interpretation
- n = 1: return ["()"]

### Connection to Other Problems

This is a specific case of the Catalan number sequence, which also counts:
- Number of ways to triangulate a polygon
- Number of full binary trees with n+1 leaves
- Number of paths in a grid from (0,0) to (n,n) staying below diagonal
- Number of ways to match n opening brackets with n closing brackets

### Related Problems
- Valid Parentheses: validate a given string
- Longest Valid Parentheses: find longest valid substring
- Remove Invalid Parentheses: make string valid with minimum removals
- Different Ways to Add Parentheses: add parentheses to expression
