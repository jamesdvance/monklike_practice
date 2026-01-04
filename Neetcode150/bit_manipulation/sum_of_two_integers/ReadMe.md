# Sum of Two Integers

## Summary

Calculate the sum of two integers without using the + or - operators.

### Key Points
- XOR gives sum without carry
- AND + left shift gives carry
- Repeat until no carry remains

### Optimal Approach
Bit manipulation with carry propagation.

```python
def getSum(a: int, b: int) -> int:
    # Python handles arbitrary precision, need to mask
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & MASK
        b = carry & MASK

    # Handle negative numbers
    return a if a <= MAX_INT else ~(a ^ MASK)
```

### Complexity
- Time: O(1) - at most 32 iterations for 32-bit integers
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

In binary addition:
- 0 + 0 = 0 (no carry)
- 0 + 1 = 1 (no carry)
- 1 + 0 = 1 (no carry)
- 1 + 1 = 0 (carry 1)

XOR gives the sum bits without carry.
AND gives where carries occur.
Left shift positions the carry for the next column.

### Why This Works

```
a = 5 = 101
b = 3 = 011

Step 1:
  sum (XOR): 101 ^ 011 = 110 (6)
  carry (AND << 1): (101 & 011) << 1 = 001 << 1 = 010 (2)

Step 2:
  a = 110, b = 010
  sum: 110 ^ 010 = 100 (4)
  carry: (110 & 010) << 1 = 010 << 1 = 100 (4)

Step 3:
  a = 100, b = 100
  sum: 100 ^ 100 = 000 (0)
  carry: (100 & 100) << 1 = 100 << 1 = 1000 (8)

Step 4:
  a = 000, b = 1000
  sum: 000 ^ 1000 = 1000 (8)
  carry: 0

Answer: 8 (which is 5 + 3)
```

### Half Adder and Full Adder

This simulates a ripple-carry adder:
- **Half adder**: sum = a XOR b, carry = a AND b
- We propagate carries until none remain

### Python-Specific Handling

Python integers have arbitrary precision (no overflow), but we need to simulate 32-bit behavior:

```python
MASK = 0xFFFFFFFF  # 32 ones
MAX_INT = 0x7FFFFFFF  # Max positive 32-bit int

# Mask results to 32 bits
a = (a ^ b) & MASK

# At end, convert back if negative
if a > MAX_INT:
    a = ~(a ^ MASK)  # Convert from 2's complement
```

### Step-by-Step with Negative Numbers

```
a = -1 = ...11111111 (32 1s in 2's complement)
b = 1 = ...00000001

XOR: ...11111110
AND << 1: 00000010

XOR: ...11111100
AND << 1: 00000100

...continues until carry is 0

Result: 0
```

### Alternative: Recursion

```python
def getSum(a: int, b: int) -> int:
    if b == 0:
        return a
    return getSum(a ^ b, (a & b) << 1)
```

Without Python's arbitrary precision handling (works in most languages).

### Language Comparison

In Java/C++:
```java
int getSum(int a, int b) {
    while (b != 0) {
        int carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}
```

Simpler because integers naturally overflow/wrap.

### Subtraction

Subtraction: a - b = a + (-b) = a + (~b + 1)

```python
def getSubtract(a: int, b: int) -> int:
    return getSum(a, getSum(~b, 1))
```

### Multiplication Using Addition

```python
def multiply(a: int, b: int) -> int:
    result = 0
    while b > 0:
        if b & 1:
            result = getSum(result, a)
        a <<= 1
        b >>= 1
    return result
```

### Visual: Binary Addition

```
    1 0 1 1   (11)
  + 0 1 1 0   (6)
  ---------

XOR:  1 1 0 1   (sum without carry)
AND:  0 0 1 0   (where both are 1)
<<1:  0 1 0 0   (carry shifted)

    1 1 0 1
  + 0 1 0 0
  ---------
XOR:  1 0 0 1
AND:  0 1 0 0
<<1:  1 0 0 0

    1 0 0 1
  + 1 0 0 0
  ---------
XOR:  0 0 0 1
AND:  1 0 0 0
<<1: 1 0 0 0 0

... (continues until carry is 0)

Final: 1 0 0 0 1 = 17 = 11 + 6
```

### Edge Cases
- One operand is 0: return the other
- Same numbers: equivalent to 2*n (left shift by 1)
- Opposite numbers: return 0 (a + (-a))

### Related Problems
- Add Binary: string-based, similar concept
- Add Two Numbers: linked list, digit-by-digit
- Multiply Strings: extended arithmetic
