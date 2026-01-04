# Bit Manipulation

## Summary

Bit manipulation problems leverage binary representation to solve problems efficiently. They often provide O(1) or O(log n) solutions where other approaches require O(n) or more.

### Core Concepts

1. **XOR Properties**: Self-inverse (a^a=0), identity (a^0=a), commutativity
2. **Masking**: Extract or modify specific bits using AND, OR, XOR
3. **Shifting**: Multiply/divide by powers of 2, iterate through bits
4. **Two's Complement**: How negative numbers are represented in binary

### Common Techniques

- XOR for finding unique elements
- n & (n-1) to clear rightmost set bit
- n & (-n) to isolate rightmost set bit
- Bit masking for 32-bit arithmetic simulation

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Single Number](./single_number/) | XOR cancellation | a ^ a = 0, pairs cancel |
| [Number of 1 Bits](./number_of_1_bits/) | Brian Kernighan | n & (n-1) clears rightmost 1 |
| [Counting Bits](./counting_bits/) | DP + bits | ans[i] = ans[i>>1] + (i&1) |
| [Reverse Bits](./reverse_bits/) | Bit-by-bit | Extract right, build left |
| [Missing Number](./missing_number/) | XOR all | Pairs cancel, missing remains |
| [Sum of Two Integers](./sum_of_two_integers/) | Carry propagation | XOR=sum, AND<<1=carry |
| [Reverse Integer](./reverse_integer/) | Digit extraction | Mod and divide, check overflow |

---

## Common Patterns

### Pattern 1: XOR for Finding Unique Element

```python
def findUnique(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

All paired elements cancel out.

### Pattern 2: Brian Kernighan's Algorithm

```python
def countSetBits(n):
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count
```

Runs in O(k) where k is number of set bits.

### Pattern 3: Bit-by-Bit Processing

```python
def reverseBits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

### Pattern 4: Sum Without Arithmetic

```python
def add(a, b):
    MASK = 0xFFFFFFFF
    while b:
        carry = (a & b) << 1
        a = (a ^ b) & MASK
        b = carry & MASK
    return a if a <= 0x7FFFFFFF else ~(a ^ MASK)
```

XOR gives sum, AND gives carry positions.

### Pattern 5: DP with Bit Relationships

```python
def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
```

---

## Bit Manipulation Cheatsheet

### Basic Operations

| Operation | Code | Description |
|-----------|------|-------------|
| Set bit i | `n \| (1 << i)` | Turn bit i on |
| Clear bit i | `n & ~(1 << i)` | Turn bit i off |
| Toggle bit i | `n ^ (1 << i)` | Flip bit i |
| Check bit i | `(n >> i) & 1` | Get bit i value |
| Clear rightmost 1 | `n & (n - 1)` | Brian Kernighan |
| Isolate rightmost 1 | `n & (-n)` | Two's complement trick |
| Clear all bits | `n & 0` | Set to zero |
| Set all bits | `n \| 0xFFFFFFFF` | All ones |

### XOR Properties

```
a ^ 0 = a          (identity)
a ^ a = 0          (self-inverse)
a ^ b = b ^ a      (commutative)
(a ^ b) ^ c = a ^ (b ^ c)  (associative)
```

### Two's Complement

```
-n = ~n + 1
~n = -n - 1

For n = 5:   0101
~n:          1010  (inverted)
-n:          1011  (inverted + 1)
```

### Power of 2 Checks

```python
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

def nextPowerOfTwo(n):
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1
```

---

## Common Bit Masks

```python
# 32-bit masks
ALL_ONES = 0xFFFFFFFF
MAX_INT = 0x7FFFFFFF  # 2^31 - 1
MIN_INT = 0x80000000  # -2^31 (as unsigned)

# Byte extraction
BYTE_0 = 0x000000FF  # bits 0-7
BYTE_1 = 0x0000FF00  # bits 8-15
BYTE_2 = 0x00FF0000  # bits 16-23
BYTE_3 = 0xFF000000  # bits 24-31

# Alternating patterns
EVEN_BITS = 0x55555555  # 0101...
ODD_BITS = 0xAAAAAAAA   # 1010...
```

---

## Complexity Summary

| Problem | Time | Space | Pattern |
|---------|------|-------|---------|
| Single Number | O(n) | O(1) | XOR all |
| Number of 1 Bits | O(k) | O(1) | Brian Kernighan |
| Counting Bits | O(n) | O(n) | DP |
| Reverse Bits | O(1) | O(1) | Bit-by-bit |
| Missing Number | O(n) | O(1) | XOR all |
| Sum of Two Integers | O(1) | O(1) | Carry loop |
| Reverse Integer | O(log x) | O(1) | Digit by digit |

---

## Python-Specific Considerations

### Arbitrary Precision

Python integers have no size limit, so:
- No overflow (but may need to check bounds)
- Negative numbers don't wrap
- Must mask to simulate 32-bit behavior

```python
# Simulate 32-bit overflow
result = result & 0xFFFFFFFF

# Convert back to signed
if result > 0x7FFFFFFF:
    result = ~(result ^ 0xFFFFFFFF)
```

### Bitwise Operators

```python
&   # AND
|   # OR
^   # XOR
~   # NOT (inverts all bits, including sign)
<<  # Left shift
>>  # Right shift (arithmetic, preserves sign)
```

### Useful Built-ins

```python
bin(n)           # Binary string: '0b1010'
n.bit_length()   # Number of bits needed
n.bit_count()    # Count of 1 bits (Python 3.10+)
int('1010', 2)   # Parse binary string
```

---

## Key Takeaways

1. **XOR is your friend** - pairs cancel, order doesn't matter
2. **n & (n-1) is powerful** - clears rightmost 1, counts bits, checks power of 2
3. **Think in bits** - sometimes a complex problem has an elegant bit solution
4. **Mask for bounds** - in Python, simulate 32-bit with 0xFFFFFFFF
5. **Carry propagation** - XOR for sum, AND << 1 for carry
6. **Right shift divides by 2** - useful for DP relationships
7. **Check overflow explicitly** - Python won't overflow, but problem may require it
