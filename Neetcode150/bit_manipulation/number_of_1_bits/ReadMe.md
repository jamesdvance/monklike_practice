# Number of 1 Bits (Hamming Weight)

## Summary

Given an unsigned integer, return the number of '1' bits (also known as the Hamming weight).

### Key Points
- Use n & (n-1) to clear rightmost set bit
- Each iteration removes one 1-bit
- Count iterations until n becomes 0

### Optimal Approach
Brian Kernighan's algorithm.

```python
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```

### Complexity
- Time: O(k) where k is number of set bits
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The key insight is: n & (n-1) clears the rightmost set bit.

Why? n-1 flips all bits from the rightmost 1 to the end:
```
n     = ...1000
n-1   = ...0111
n&(n-1) = ...0000
```

### Why n & (n-1) Works

```
n = 12 = 1100
n-1 = 11 = 1011
n & (n-1) = 1000 = 8

n = 8 = 1000
n-1 = 7 = 0111
n & (n-1) = 0000 = 0

Two iterations = two 1-bits in 12
```

### Step-by-Step Example

```
n = 11 (binary: 1011)

Iteration 1:
  n = 1011
  n-1 = 1010
  n & (n-1) = 1010
  count = 1

Iteration 2:
  n = 1010
  n-1 = 1001
  n & (n-1) = 1000
  count = 2

Iteration 3:
  n = 1000
  n-1 = 0111
  n & (n-1) = 0000
  count = 3

Answer: 3
```

### Alternative: Check Each Bit

```python
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

Time: O(32) for 32-bit integer - always checks all bits.

### Alternative: Built-in

```python
def hammingWeight(n: int) -> int:
    return bin(n).count('1')
```

Or:
```python
def hammingWeight(n: int) -> int:
    return n.bit_count()  # Python 3.10+
```

### Bit Manipulation Visualization

```
Number: 23 = 10111

10111  (23)
& 10110  (22)
= 10110  (22) -> cleared bit 0

10110  (22)
& 10101  (21)
= 10100  (20) -> cleared bit 1

10100  (20)
& 10011  (19)
= 10000  (16) -> cleared bit 2

10000  (16)
& 01111  (15)
= 00000  (0) -> cleared bit 4

4 iterations = 4 set bits
```

### Lookup Table Approach

For repeated calls, precompute counts:

```python
class Solution:
    def __init__(self):
        self.table = [bin(i).count('1') for i in range(256)]

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += self.table[n & 0xff]
            n >>= 8
        return count
```

Process 8 bits at a time with O(1) lookup.

### Recursive Version

```python
def hammingWeight(n: int) -> int:
    if n == 0:
        return 0
    return 1 + hammingWeight(n & (n - 1))
```

### Applications

1. **Population count**: Used in SIMD instructions
2. **Hamming distance**: XOR then count bits
3. **Power of 2 check**: n & (n-1) == 0
4. **Bit manipulation problems**: Building block

### Edge Cases
- n = 0: return 0
- n = 2^31 - 1 (all 1s): return 31
- n = 1: return 1

### Related Problems
- Counting Bits: count 1s for 0 to n
- Hamming Distance: XOR then count
- Power of Two: single 1-bit check
