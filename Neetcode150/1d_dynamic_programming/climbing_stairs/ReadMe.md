# Climbing Stairs

## Summary

You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

### Key Points
- Classic DP problem equivalent to Fibonacci
- dp[i] = dp[i-1] + dp[i-2]
- Can optimize space to O(1)

### Optimal Approach
Use bottom-up DP with constant space.

```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    prev2, prev1 = 1, 2

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

To reach step n, you can come from:
- Step n-1 (taking 1 step)
- Step n-2 (taking 2 steps)

So: ways(n) = ways(n-1) + ways(n-2)

This is exactly the Fibonacci sequence.

### Base Cases

- n = 1: 1 way (take 1 step)
- n = 2: 2 ways (1+1 or 2)

### Full DP Array Approach

```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

Space: O(n)

### Recursive with Memoization

```python
def climbStairs(n: int) -> int:
    memo = {}

    def dp(i):
        if i <= 2:
            return i
        if i in memo:
            return memo[i]
        memo[i] = dp(i-1) + dp(i-2)
        return memo[i]

    return dp(n)
```

### Matrix Exponentiation (O(log n))

```python
def climbStairs(n: int) -> int:
    def multiply(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def power(M, p):
        result = [[1, 0], [0, 1]]  # Identity
        while p:
            if p % 2 == 1:
                result = multiply(result, M)
            M = multiply(M, M)
            p //= 2
        return result

    if n <= 2:
        return n

    M = [[1, 1], [1, 0]]
    result = power(M, n)
    return result[0][0]
```

This uses the property: [F(n+1), F(n)] = [[1,1],[1,0]]^n * [F(1), F(0)]

### Step-by-Step Example

```
n = 5

dp[1] = 1
dp[2] = 2
dp[3] = dp[2] + dp[1] = 2 + 1 = 3
dp[4] = dp[3] + dp[2] = 3 + 2 = 5
dp[5] = dp[4] + dp[3] = 5 + 3 = 8

Answer: 8 ways
```

The paths for n=5:
1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1,
1+2+2, 2+1+2, 2+2+1

### Edge Cases
- n = 0: 1 way (already at top, do nothing)
- n = 1: 1 way
- Large n: use iterative to avoid stack overflow

### Related Problems
- Min Cost Climbing Stairs: add costs to steps
- House Robber: similar recurrence with constraint
- Fibonacci Number: identical problem
