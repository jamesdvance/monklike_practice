# Reverse Integer

## Summary

Given a 32-bit signed integer, reverse its digits. Return 0 if the reversed integer overflows.

### Key Points
- Extract digits using modulo and division
- Build reversed number by multiplying by 10
- Check for overflow before each multiplication

### Optimal Approach
Mathematical digit reversal with overflow check.

```python
def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x:
        digit = x % 10
        x //= 10

        # Check overflow before multiplying
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    result *= sign
    return result if INT_MIN <= result <= INT_MAX else 0
```

### Complexity
- Time: O(log x) - number of digits
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

To reverse 123:
1. Extract 3 (123 % 10), build result = 3
2. Extract 2 (12 % 10), build result = 32
3. Extract 1 (1 % 10), build result = 321

Key challenge: detecting overflow before it happens.

### Why Overflow Check Works

For 32-bit signed integers:
- MAX = 2,147,483,647
- MIN = -2,147,483,648

Before `result = result * 10 + digit`, check:
- `result > (MAX - digit) / 10` would overflow

### Step-by-Step Example

```
x = 123

result = 0
x=123: digit=3, result=3, x=12
x=12: digit=2, result=32, x=1
x=1: digit=1, result=321, x=0

Answer: 321
```

### Example with Negative

```
x = -123

sign = -1, x = 123
(same process)
result = 321

Answer: 321 * -1 = -321
```

### Example with Overflow

```
x = 1534236469

Reversed would be 9646324351 > 2^31 - 1
Return 0
```

### Alternative: String Reversal

```python
def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    sign = -1 if x < 0 else 1
    reversed_str = str(abs(x))[::-1]
    result = sign * int(reversed_str)

    return result if INT_MIN <= result <= INT_MAX else 0
```

Simple but uses extra space for string.

### Alternative: Using Deque

```python
from collections import deque

def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    sign = -1 if x < 0 else 1
    digits = deque()

    x = abs(x)
    while x:
        digits.appendleft(x % 10)
        x //= 10

    result = 0
    multiplier = 1
    while digits:
        result += digits.popleft() * multiplier
        multiplier *= 10

    result *= sign
    return result if INT_MIN <= result <= INT_MAX else 0
```

### Overflow Check Details

The check `result > (INT_MAX - digit) // 10` is equivalent to checking if `result * 10 + digit > INT_MAX` but without risking overflow during the check itself.

```python
# Detailed overflow check (for both bounds)
def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    result = 0
    while x != 0:
        # Python's modulo keeps sign, we need true truncation
        digit = int(x % 10) if x > 0 else int(x % -10)
        x = int(x / 10)  # Truncate toward zero

        # Check overflow
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
            return 0
        if result < INT_MIN // 10 or (result == INT_MIN // 10 and digit < -8):
            return 0

        result = result * 10 + digit

    return result
```

### Why 7 and -8?

- INT_MAX = 2,147,483,647 (ends in 7)
- INT_MIN = -2,147,483,648 (ends in -8)

When result == INT_MAX // 10 (214748364), adding a digit > 7 overflows.

### Pop and Push Digits

```
Pop: digit = x % 10, x = x // 10
Push: result = result * 10 + digit
```

This is like moving digits from one stack to another, reversing order.

### Edge Cases
- x = 0: return 0
- x = 120: return 21 (leading zeros dropped)
- x = -123: return -321 (preserve sign)
- x = 1534236469: return 0 (overflow)

### Language Considerations

In Python, integers don't overflow, so we must explicitly check bounds.
In C/Java, integers wrap on overflow, requiring more careful checks.

### Related Problems
- Palindrome Number: check if same forwards/backwards
- String to Integer (atoi): parse with overflow
- Reverse Bits: binary reversal
