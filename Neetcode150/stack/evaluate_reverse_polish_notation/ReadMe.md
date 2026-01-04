# Evaluate Reverse Polish Notation

## Summary

Evaluate an expression in Reverse Polish Notation (postfix notation). Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

### Key Points
- RPN eliminates need for parentheses by placing operator after operands
- Use a stack to track operands
- When operator encountered, pop two operands, apply operator, push result

### Optimal Approach
Process tokens left to right. Push numbers onto stack. For operators, pop two numbers, compute result, push back.

```python
def evalRPN(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                # Truncate toward zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]
```

### Complexity
- Time: O(n) - process each token once
- Space: O(n) - stack can hold up to (n+1)/2 numbers

---

## Detailed Explanation

### Problem Analysis

Reverse Polish Notation is an alternative to infix notation that does not require parentheses or operator precedence rules. Operators act on the two most recent operands, making a stack the natural data structure.

### RPN Evaluation Process

For `["2", "1", "+", "3", "*"]`:
- Push 2: stack = [2]
- Push 1: stack = [2, 1]
- See +: pop 1 and 2, push 2+1=3: stack = [3]
- Push 3: stack = [3, 3]
- See *: pop 3 and 3, push 3*3=9: stack = [9]
- Result: 9

This evaluates `((2 + 1) * 3) = 9`.

### Order Matters for - and /

When we pop, we get `b` (second operand) first, then `a` (first operand). The operation is `a op b`, not `b op a`. This matters for non-commutative operators.

For `["4", "13", "5", "/", "+"]`:
- When we see `/`: pop 5 (b), pop 13 (a), compute 13/5 = 2

### Division Truncation

The problem specifies truncation toward zero. In Python 3, `//` truncates toward negative infinity, so we use `int(a / b)` instead:
- 6 / -3 should be -2, and int(-2.0) = -2 (correct)
- 7 / -3 should be -2, and int(-2.33) = -2 (correct)
- -7 // 3 would give -3 in Python (wrong for this problem)

### Alternative: Using a Dictionary

```python
def evalRPN(tokens: list[str]) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)
    }

    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))

    return stack[0]
```

### Why RPN is Useful

1. No operator precedence needed (processed left to right)
2. No parentheses needed
3. Natural for stack-based evaluation (many calculators use this)
4. Used in PostScript, Forth, and some assembly languages

### Converting Infix to RPN

The Shunting Yard algorithm converts infix to RPN:
1. Use an operator stack
2. Numbers go directly to output
3. Operators pop higher/equal precedence operators to output before being pushed
4. Parentheses are handled specially

### Edge Cases
- Single number: just return it
- All addition: simple accumulation
- Negative numbers: parsed as negative integers
- Division resulting in zero: e.g., 1/2 = 0

### Related Problems
- Basic Calculator: evaluate infix with + and -
- Basic Calculator II: infix with +, -, *, /
- Basic Calculator III: infix with parentheses
