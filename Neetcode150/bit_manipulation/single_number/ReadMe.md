# Single Number

## Summary

Given a non-empty array where every element appears twice except for one, find that single element.

### Key Points
- XOR of a number with itself is 0
- XOR of a number with 0 is the number itself
- XOR is commutative and associative

### Optimal Approach
XOR all elements together.

```python
def singleNumber(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

The key insight is XOR properties:
- a ^ a = 0 (same numbers cancel)
- a ^ 0 = a (identity)
- a ^ b ^ a = b (order doesn't matter)

When we XOR all numbers, pairs cancel out, leaving only the single number.

### Why XOR Works

```
nums = [4, 1, 2, 1, 2]

4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4

Answer: 4
```

All paired numbers cancel each other out.

### Step-by-Step Example

```
nums = [2, 2, 1]

result = 0
result ^= 2  ->  0 ^ 2 = 2
result ^= 2  ->  2 ^ 2 = 0
result ^= 1  ->  0 ^ 1 = 1

Answer: 1
```

### Alternative: Hash Set

```python
def singleNumber(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop()
```

Time: O(n), Space: O(n)

### Alternative: Math Formula

```python
def singleNumber(nums: list[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)
```

If each number appeared twice: sum would be 2 * sum(unique).
Actual sum is less by the amount of the single number.

### Alternative: Python One-liner

```python
from functools import reduce
from operator import xor

def singleNumber(nums: list[int]) -> int:
    return reduce(xor, nums)
```

### XOR Properties Deep Dive

```
XOR Truth Table:
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

Properties:
- Commutative: a ^ b = b ^ a
- Associative: (a ^ b) ^ c = a ^ (b ^ c)
- Self-inverse: a ^ a = 0
- Identity: a ^ 0 = a
```

### Edge Cases
- Single element array: return that element
- All pairs at start, single at end: XOR handles order
- Negative numbers: XOR works on bits, handles negatives

### Variations

**Single Number II**: Every element appears 3 times except one.
```python
def singleNumber(nums: list[int]) -> int:
    ones = twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones
```

**Single Number III**: Two elements appear once, rest twice.
```python
def singleNumber(nums: list[int]) -> list[int]:
    xor = 0
    for num in nums:
        xor ^= num

    # Find rightmost set bit
    diff_bit = xor & (-xor)

    a = 0
    for num in nums:
        if num & diff_bit:
            a ^= num

    return [a, xor ^ a]
```

### Related Problems
- Single Number II: appears 3 times
- Single Number III: two single numbers
- Missing Number: also uses XOR
