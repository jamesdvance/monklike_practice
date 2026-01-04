# Math and Geometry

## Summary

Math and geometry problems require understanding mathematical properties and spatial relationships. They often have elegant solutions using mathematical insights rather than brute force.

### Core Concepts

1. **Number Theory**: Divisibility, modular arithmetic, primes
2. **Matrix Operations**: Rotation, transpose, traversal patterns
3. **Digit Manipulation**: Extract, process, and rebuild numbers
4. **Coordinate Geometry**: Points, distances, shapes

### Common Techniques

- Fast exponentiation (O(log n))
- In-place matrix transformations
- Cycle detection for sequence problems
- Hash-based geometric queries

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Rotate Image](./rotate_image/) | Matrix transformation | Transpose then reverse rows |
| [Spiral Matrix](./spiral_matrix/) | Matrix traversal | Track boundaries, shrink inward |
| [Set Matrix Zeroes](./set_matrix_zeroes/) | In-place markers | Use first row/col as flags |
| [Happy Number](./happy_number/) | Cycle detection | Floyd's algorithm or set |
| [Plus One](./plus_one/) | Digit manipulation | Handle carry from right to left |
| [Pow(x, n)](./pow_x_n/) | Fast exponentiation | Binary exponentiation |
| [Multiply Strings](./multiply_strings/) | Grade-school math | Position tracking for products |
| [Detect Squares](./detect_squares/) | Geometry + hashing | Hash points, find diagonals |

---

## Common Patterns

### Pattern 1: Matrix Transpose

```python
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### Pattern 2: Binary Exponentiation

```python
def power(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result
```

### Pattern 3: Digit Sum / Manipulation

```python
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
```

### Pattern 4: Cycle Detection (Floyd's)

```python
def detect_cycle(start, next_func):
    slow = start
    fast = next_func(start)

    while fast != slow:
        if fast is None:
            return False
        slow = next_func(slow)
        fast = next_func(next_func(fast))

    return True
```

### Pattern 5: Spiral Traversal

```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

---

## Mathematical Formulas

### 90-Degree Rotation

Clockwise: (i, j) -> (j, n-1-i)
Counter-clockwise: (i, j) -> (n-1-j, i)

### Manhattan Distance

d = |x1 - x2| + |y1 - y2|

### Euclidean Distance

d = sqrt((x1 - x2)^2 + (y1 - y2)^2)

### GCD (Euclidean Algorithm)

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

---

## Key Takeaways

1. **Use matrix properties** - transpose + reverse = rotate
2. **Binary exponentiation** reduces O(n) to O(log n)
3. **In-place markers** save space for matrix problems
4. **Cycle detection** applies beyond linked lists
5. **Position formulas** (like i+j) help with matrix products
6. **Hash coordinates** for efficient geometric queries
7. **Handle edge cases** - zero, negative, overflow
