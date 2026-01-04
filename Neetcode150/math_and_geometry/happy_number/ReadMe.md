# Happy Number

## Summary

A happy number is defined by replacing the number with the sum of squares of its digits repeatedly. If this process reaches 1, the number is happy. If it loops endlessly without reaching 1, it's not happy.

### Key Points
- Detect cycle using Floyd's algorithm or a set
- Sum of digit squares eventually cycles or reaches 1
- Numbers that aren't happy enter a cycle containing 4

### Optimal Approach
Floyd's cycle detection.

```python
def isHappy(n: int) -> bool:
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    slow = n
    fast = get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1
```

### Complexity
- Time: O(log n) per iteration, O(log n) iterations
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Starting from any number, the sum of squares of digits will:
1. Eventually reach 1 (happy number)
2. Enter a cycle (not happy)

We need to detect which case we're in.

### Why Does It Always Cycle or Reach 1?

For any n-digit number, the sum of squares is at most 9^2 * n = 81n. For n=13 (largest int), max sum is 81*13 = 1053. So the sequence is bounded and must eventually cycle.

### The Cycle for Unhappy Numbers

All unhappy numbers enter the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

### Hash Set Approach

```python
def isHappy(n: int) -> bool:
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1
```

Space: O(log n) for the set.

### Hardcoded Cycle Check

```python
def isHappy(n: int) -> bool:
    cycle = {4, 16, 37, 58, 89, 145, 42, 20}

    def get_next(num):
        total = 0
        while num > 0:
            total += (num % 10) ** 2
            num //= 10
        return total

    while n != 1 and n not in cycle:
        n = get_next(n)

    return n == 1
```

### Step-by-Step Example

```
n = 19

19 -> 1^2 + 9^2 = 1 + 81 = 82
82 -> 8^2 + 2^2 = 64 + 4 = 68
68 -> 6^2 + 8^2 = 36 + 64 = 100
100 -> 1^2 + 0^2 + 0^2 = 1

Reached 1, so 19 is happy.
```

### Example: Unhappy Number

```
n = 2

2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (cycle!)

Not happy.
```

### String-Based Digit Sum

```python
def isHappy(n: int) -> bool:
    def get_next(num):
        return sum(int(d) ** 2 for d in str(num))

    slow, fast = n, get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1
```

### Edge Cases
- n = 1: immediately happy
- n = 7: happy (7 -> 49 -> 97 -> 130 -> 10 -> 1)
- Single digit: only 1 and 7 are happy

### Related Problems
- Linked List Cycle: Floyd's algorithm
- Add Digits: digit manipulation
- Ugly Number: number properties
