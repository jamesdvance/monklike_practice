# Plus One

## Summary

Given a large integer represented as an array of digits, add one to the integer and return the resulting array.

### Key Points
- Handle carry from right to left
- Most cases: just increment last digit
- Edge case: all 9s become all 0s with leading 1

### Optimal Approach
Process from right, handle carries.

```python
def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # All digits were 9
    return [1] + digits
```

### Complexity
- Time: O(n)
- Space: O(1) extra space (or O(n) for the new array case)

---

## Detailed Explanation

### Problem Analysis

Adding 1 is simple unless we have a carry:
- If digit < 9: increment and return
- If digit = 9: set to 0, carry to next digit
- If all digits are 9: need one more digit

### Why This Works

We only continue the loop when there's a carry (digit was 9). The moment we find a digit < 9, we increment it and return - no more carries needed.

### Step-by-Step Example

```
digits = [1, 2, 3]

i=2: digits[2]=3 < 9, digits[2]=4
return [1, 2, 4]
```

### Example with Carry

```
digits = [1, 2, 9]

i=2: digits[2]=9, digits[2]=0
i=1: digits[1]=2 < 9, digits[1]=3
return [1, 3, 0]
```

### Example: All 9s

```
digits = [9, 9, 9]

i=2: digits[2]=9, digits[2]=0
i=1: digits[1]=9, digits[1]=0
i=0: digits[0]=9, digits[0]=0

Loop ends, all digits are 0.
return [1] + [0, 0, 0] = [1, 0, 0, 0]
```

### Alternative: Explicit Carry

```python
def plusOne(digits: list[int]) -> list[int]:
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        total = digits[i] + carry
        digits[i] = total % 10
        carry = total // 10

        if carry == 0:
            return digits

    if carry:
        return [1] + digits

    return digits
```

### Converting to Integer (Simple but Limited)

```python
def plusOne(digits: list[int]) -> list[int]:
    num = int(''.join(map(str, digits))) + 1
    return [int(d) for d in str(num)]
```

Works but might overflow for very large numbers.

### Recursive Approach

```python
def plusOne(digits: list[int]) -> list[int]:
    def add_one(digits, i):
        if i < 0:
            return [1] + digits

        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0
        return add_one(digits, i - 1)

    return add_one(digits, len(digits) - 1)
```

### Edge Cases
- Single digit 0-8: increment directly
- [9]: becomes [1, 0]
- [9, 9, 9]: becomes [1, 0, 0, 0]

### Related Problems
- Add Binary: similar with base 2
- Add Two Numbers (Linked List): same concept
- Multiply Strings: more complex arithmetic
