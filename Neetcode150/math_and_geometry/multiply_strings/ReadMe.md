# Multiply Strings

## Summary

Given two non-negative integers represented as strings, return their product as a string. Cannot use built-in big integer libraries.

### Key Points
- Simulate grade-school multiplication
- Each digit i * j contributes to position i+j and i+j+1
- Handle carries after all multiplications

### Optimal Approach
Grade-school multiplication with position tracking.

```python
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1

            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10

    # Build result string, skip leading zeros
    result_str = ''.join(map(str, result))
    return result_str.lstrip('0') or '0'
```

### Complexity
- Time: O(m * n)
- Space: O(m + n)

---

## Detailed Explanation

### Problem Analysis

In grade-school multiplication:
- Multiply each digit of num1 with each digit of num2
- Position the result correctly (shifted by position)
- Add up all partial products

### Position Formula

When multiplying num1[i] and num2[j]:
- The result goes into positions i+j and i+j+1
- i+j+1 is the ones place, i+j is the tens place (for this particular product)

### Why (m + n) Space?

Maximum product of m-digit and n-digit numbers has at most m+n digits.
Example: 99 * 99 = 9801 (2 digits * 2 digits = 4 digits)

### Step-by-Step Example

```
num1 = "123", num2 = "45"

result = [0, 0, 0, 0, 0]

i=2 (3), j=1 (5): 3*5=15
  p1=3, p2=4
  result[4] = 15 % 10 = 5
  result[3] = 15 // 10 = 1
  result = [0, 0, 0, 1, 5]

i=2 (3), j=0 (4): 3*4=12
  p1=2, p2=3
  total = 12 + 1 = 13
  result[3] = 3, result[2] += 1
  result = [0, 0, 1, 3, 5]

i=1 (2), j=1 (5): 2*5=10
  p1=2, p2=3
  total = 10 + 3 = 13
  result[3] = 3, result[2] += 1 = 2
  result = [0, 0, 2, 3, 5]

i=1 (2), j=0 (4): 2*4=8
  p1=1, p2=2
  total = 8 + 2 = 10
  result[2] = 0, result[1] += 1
  result = [0, 1, 0, 3, 5]

i=0 (1), j=1 (5): 1*5=5
  p1=1, p2=2
  total = 5 + 0 = 5
  result[2] = 5, result[1] += 0
  result = [0, 1, 5, 3, 5]

i=0 (1), j=0 (4): 1*4=4
  p1=0, p2=1
  total = 4 + 1 = 5
  result[1] = 5, result[0] += 0
  result = [0, 5, 5, 3, 5]

Answer: "5535"
```

### Alternative: Carry at the End

```python
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            result[i + j + 1] += int(num1[i]) * int(num2[j])

    # Process carries
    carry = 0
    for i in range(len(result) - 1, -1, -1):
        result[i] += carry
        carry = result[i] // 10
        result[i] %= 10

    result_str = ''.join(map(str, result))
    return result_str.lstrip('0') or '0'
```

### Edge Cases
- Either number is "0": return "0"
- One number is "1": return the other
- Leading zeros in result: must strip

### Related Problems
- Add Strings: simpler addition
- Add Binary: base 2 addition
- Plus One: increment by 1
