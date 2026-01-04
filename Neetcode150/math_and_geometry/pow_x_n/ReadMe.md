# Pow(x, n)

## Summary

Implement pow(x, n), which calculates x raised to the power n.

### Key Points
- Use exponentiation by squaring for O(log n)
- Handle negative exponents: x^(-n) = 1 / x^n
- Handle edge case of n = -2^31

### Optimal Approach
Binary exponentiation (exponentiation by squaring).

```python
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2

    return result
```

### Complexity
- Time: O(log n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Naive approach (multiply n times) is O(n). We can do better using the property:
- x^n = (x^2)^(n/2) if n is even
- x^n = x * (x^2)^((n-1)/2) if n is odd

### Binary Exponentiation Insight

We express n in binary and use:
- x^1, x^2, x^4, x^8, ... (squares)
- Multiply result by x^(2^k) for each bit k that is set

Example: x^13 = x^(1101 binary) = x^8 * x^4 * x^1

### Step-by-Step Example

```
x = 2, n = 10

n = 10 = 1010 binary

result = 1
n=10 (even): x = 4, n = 5
n=5 (odd): result = 1 * 4 = 4, x = 16, n = 2
n=2 (even): x = 256, n = 1
n=1 (odd): result = 4 * 256 = 1024, x = 65536, n = 0

Answer: 1024
```

### Recursive Approach

```python
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        half = myPow(x, n // 2)
        return half * half
    else:
        return x * myPow(x, n - 1)
```

Space: O(log n) for recursion stack.

### Handling n = -2^31

In some languages, -(-2^31) overflows. Solutions:
1. Use n = -n after converting x to 1/x (Python handles big ints)
2. Handle separately: if n == -2^31, return myPow(x, n+1) / x

### Bitwise Version

```python
def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1

    return result
```

### Why This Works

For n = 13 = 1101 binary:
- Bit 0 is set: multiply by x^1
- Bit 2 is set: multiply by x^4
- Bit 3 is set: multiply by x^8

Result: x^1 * x^4 * x^8 = x^13

### Edge Cases
- n = 0: return 1 (any x)
- x = 0, n > 0: return 0
- x = 1: return 1 (any n)
- n < 0: compute 1 / x^(-n)

### Related Problems
- Sqrt(x): inverse operation
- Super Pow: modular exponentiation
- Power of Two/Three/Four: special cases
