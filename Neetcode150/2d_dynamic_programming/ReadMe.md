# 2D Dynamic Programming

## Summary

2D DP extends 1D DP by tracking two dimensions of state. Common patterns include two-string problems, grid traversals, and interval problems.

### Core Concepts

1. **State Space**: dp[i][j] represents a subproblem involving two parameters
2. **Two Strings**: Compare prefixes of both strings
3. **Grid Problems**: Position (row, column) as state
4. **Interval DP**: Range [i, j] as state

### Common 2D DP Patterns

- String comparison: LCS, Edit Distance
- Path counting: Unique Paths, grid traversals
- Subset/Knapsack: extended to 2D state
- Interval: Burst Balloons, matrix chain multiplication

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Unique Paths](./unique_paths/) | Grid traversal | dp[i][j] = dp[i-1][j] + dp[i][j-1] |
| [Longest Common Subsequence](./longest_common_subsequence/) | Two strings | Match extends LCS, mismatch takes max |
| [Best Time with Cooldown](./best_time_to_buy_and_sell_stock_with_cooldown/) | State machine | Track hold/sold/rest states |
| [Coin Change II](./coin_change_ii/) | Unbounded knapsack | Coins first for combinations |
| [Target Sum](./target_sum/) | Subset sum | Convert to subset with sum (total+target)/2 |
| [Interleaving String](./interleaving_string/) | Two strings | s3[i+j] must come from s1 or s2 |
| [Longest Increasing Path](./longest_increasing_path_in_a_matrix/) | Grid DFS + memo | Strictly increasing prevents cycles |
| [Distinct Subsequences](./distinct_subsequences/) | Two strings | Match: use or skip; mismatch: skip |
| [Edit Distance](./edit_distance/) | Two strings | Insert, delete, or replace |
| [Burst Balloons](./burst_balloons/) | Interval DP | Think of which balloon to burst LAST |
| [Regular Expression Matching](./regular_expression_matching/) | Two strings | Handle '.' and '*' carefully |

---

## Common Patterns

### Pattern 1: Two String DP

```python
def two_string_dp(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = base_value_1
    for j in range(n + 1):
        dp[0][j] = base_value_2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + match_value
            else:
                dp[i][j] = combine(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]
```

### Pattern 2: Grid Path DP

```python
def grid_dp(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]  # Starting point

    # First row and column
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]
```

### Pattern 3: Interval DP

```python
def interval_dp(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # Base case: single elements
    for i in range(n):
        dp[i][i] = base_value(arr[i])

    # Fill by increasing interval length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):  # Split point
                dp[i][j] = optimize(dp[i][j], dp[i][k], dp[k+1][j], cost(i, k, j))

    return dp[0][n-1]
```

### Pattern 4: Subset Sum / Knapsack

```python
def subset_sum(nums, target):
    dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = True

    for i in range(1, len(nums) + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i-1][j]  # Don't take
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]  # Take

    return dp[len(nums)][target]
```

### Pattern 5: State Machine DP

```python
def state_machine_dp(prices):
    # States: hold, sold, rest
    hold, sold, rest = -prices[0], 0, 0

    for i in range(1, len(prices)):
        prev_hold = hold
        hold = max(hold, rest - prices[i])
        rest = max(rest, sold)
        sold = prev_hold + prices[i]

    return max(sold, rest)
```

---

## Space Optimization Techniques

### 1. Two Rows

When dp[i][j] only depends on row i-1:
```python
prev = [initial values]
for i in range(1, m + 1):
    curr = [0] * (n + 1)
    # Compute curr from prev
    prev = curr
```

### 2. Single Row with Careful Ordering

When dp[i][j] depends on dp[i-1][j-1], dp[i-1][j], dp[i][j-1]:
- For some problems (like edit distance), need to save dp[i-1][j-1] before overwriting
- For 0/1 knapsack in 1D, iterate backwards

### 3. Use Dictionary for Sparse States

When state space is large but few states are reachable:
```python
dp = {(0, 0): 1}
for state, value in dp.items():
    # Add new states
```

---

## Key Takeaways

1. **Identify dimensions**: What changes between subproblems?
2. **Define state clearly**: What does dp[i][j] represent?
3. **Consider all transitions**: How can we reach dp[i][j]?
4. **Handle base cases**: First row/column, empty strings, etc.
5. **Think backwards for intervals**: Which element to process LAST?
6. **Space optimize**: Often O(n^2) can become O(n)
7. **Order matters**: Row-by-row, or by interval length, etc.
