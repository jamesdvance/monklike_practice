# Counting Bits

## Summary

Given an integer n, return an array of length n+1 where ans[i] is the number of 1-bits in i.

### Key Points
- Use DP with bit manipulation
- ans[i] = ans[i >> 1] + (i & 1)
- Or: ans[i] = ans[i & (i-1)] + 1

### Optimal Approach
DP using right shift relationship.

```python
def countBits(n: int) -> list[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
```

### Complexity
- Time: O(n)
- Space: O(n) for output

---

## Detailed Explanation

### Problem Analysis

Key insight: The number of 1-bits in i relates to previously computed values.

Two approaches:
1. `i >> 1` removes last bit, so `ans[i] = ans[i >> 1] + (i & 1)`
2. `i & (i-1)` removes rightmost 1, so `ans[i] = ans[i & (i-1)] + 1`

### Why Right Shift Works

```
i = 6 = 110
i >> 1 = 3 = 11
i & 1 = 0

count(6) = count(3) + 0 = 2 + 0 = 2

i = 7 = 111
i >> 1 = 3 = 11
i & 1 = 1

count(7) = count(3) + 1 = 2 + 1 = 3
```

Shifting right divides by 2, and we add back the last bit.

### Step-by-Step Example

```
n = 5

ans = [0, 0, 0, 0, 0, 0]

i=1: ans[1] = ans[0] + 1 = 0 + 1 = 1
i=2: ans[2] = ans[1] + 0 = 1 + 0 = 1
i=3: ans[3] = ans[1] + 1 = 1 + 1 = 2
i=4: ans[4] = ans[2] + 0 = 1 + 0 = 1
i=5: ans[5] = ans[2] + 1 = 1 + 1 = 2

ans = [0, 1, 1, 2, 1, 2]
```

### Alternative: Using n & (n-1)

```python
def countBits(n: int) -> list[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans
```

`i & (i-1)` clears the rightmost 1-bit, giving a smaller number.

### Alternative: Offset Pattern

```python
def countBits(n: int) -> list[int]:
    ans = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        ans[i] = 1 + ans[i - offset]

    return ans
```

Pattern: bits in i = 1 + bits in (i - highest_power_of_2_less_than_i)

### Brute Force (For Comparison)

```python
def countBits(n: int) -> list[int]:
    return [bin(i).count('1') for i in range(n + 1)]
```

Time: O(n * log n) since each number has O(log n) bits.

### Pattern Visualization

```
n  binary  count  relationship
0    0      0     base case
1    1      1     ans[0] + 1
2   10      1     ans[1] + 0
3   11      2     ans[1] + 1
4  100      1     ans[2] + 0
5  101      2     ans[2] + 1
6  110      2     ans[3] + 0
7  111      3     ans[3] + 1
8 1000      1     ans[4] + 0
```

Even numbers: same as n/2 (just add a 0 bit)
Odd numbers: one more than n/2 (add a 1 bit)

### Mathematical Analysis

For any integer i:
- If i is even: rightmost bit is 0, so count(i) = count(i/2)
- If i is odd: rightmost bit is 1, so count(i) = count(i/2) + 1

Combined: count(i) = count(i >> 1) + (i & 1)

### Most Significant Bit Approach

```python
def countBits(n: int) -> list[int]:
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        # Find position of MSB
        msb = i.bit_length() - 1
        ans[i] = 1 + ans[i - (1 << msb)]

    return ans
```

### Edge Cases
- n = 0: return [0]
- n = 1: return [0, 1]
- Large n: O(n) time is optimal

### Related Problems
- Number of 1 Bits: single number
- Power of Two: single bit check
- Hamming Distance: XOR then count
