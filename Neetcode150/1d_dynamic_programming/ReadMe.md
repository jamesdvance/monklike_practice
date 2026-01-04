# 1D Dynamic Programming

## Summary

Dynamic programming solves problems by breaking them into overlapping subproblems and storing solutions to avoid recomputation. 1D DP uses a single dimension to track state.

### Core Concepts

1. **Optimal Substructure**: Solution can be built from optimal solutions to subproblems
2. **Overlapping Subproblems**: Same subproblems are solved multiple times
3. **State Definition**: What dp[i] represents
4. **Recurrence Relation**: How to compute dp[i] from previous states
5. **Base Cases**: Starting values for the DP

### Common 1D DP Patterns

- Linear sequence: dp[i] depends on dp[i-1], dp[i-2], etc.
- Knapsack variants: track achievable sums/values
- String problems: dp on prefixes or positions

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Climbing Stairs](./climbing_stairs/) | Fibonacci | dp[i] = dp[i-1] + dp[i-2] |
| [Min Cost Climbing Stairs](./min_cost_climbing_stairs/) | Fibonacci + cost | dp[i] = cost[i] + min(dp[i-1], dp[i-2]) |
| [House Robber](./house_robber/) | Take/skip | dp[i] = max(dp[i-1], dp[i-2] + nums[i]) |
| [House Robber II](./house_robber_ii/) | Circular take/skip | Solve two linear problems |
| [Longest Palindromic Substring](./longest_palindromic_substring/) | Expand around center | O(n^2) expand or Manacher O(n) |
| [Palindromic Substrings](./palindromic_substrings/) | Expand around center | Count during expansion |
| [Decode Ways](./decode_ways/) | Counting paths | 1 or 2 digit decoding |
| [Coin Change](./coin_change/) | Unbounded knapsack | min(dp[i-coin] + 1) for each coin |
| [Maximum Product Subarray](./maximum_product_subarray/) | Track max AND min | Negatives can flip sign |
| [Word Break](./word_break/) | String segmentation | dp[i] = any(dp[j] and s[j:i] in dict) |
| [Longest Increasing Subsequence](./longest_increasing_subsequence/) | LIS | O(n log n) with binary search |
| [Partition Equal Subset Sum](./partition_equal_subset_sum/) | 0/1 Knapsack | Can we reach target = sum/2? |

---

## Common Patterns

### Pattern 1: Fibonacci-like

```python
def fibonacci_pattern(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1
```

### Pattern 2: Take or Skip

```python
def take_or_skip(nums):
    prev2, prev1 = 0, 0

    for num in nums:
        curr = max(prev1, prev2 + num)  # skip or take
        prev2, prev1 = prev1, curr

    return prev1
```

### Pattern 3: Unbounded Knapsack

```python
def unbounded_knapsack(items, target):
    dp = [0] * (target + 1)

    for i in range(1, target + 1):
        for item in items:
            if item <= i:
                dp[i] = max(dp[i], dp[i - item] + value(item))

    return dp[target]
```

### Pattern 4: 0/1 Knapsack

```python
def zero_one_knapsack(items, target):
    dp = [False] * (target + 1)
    dp[0] = True

    for item in items:
        for j in range(target, item - 1, -1):  # Backwards!
            dp[j] = dp[j] or dp[j - item]

    return dp[target]
```

### Pattern 5: String Segmentation

```python
def can_segment(s, word_set):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
```

### Pattern 6: Longest Increasing Subsequence

```python
import bisect

def lis(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

---

## Space Optimization Techniques

### 1. Two Variables (Fibonacci-like)

When dp[i] only depends on dp[i-1] and dp[i-2]:
```python
prev2, prev1 = base_cases
for ...:
    curr = compute(prev1, prev2)
    prev2, prev1 = prev1, curr
```

### 2. Single Array (Knapsack)

When transitioning from previous row:
```python
# 0/1 Knapsack: iterate backwards
for j in range(target, item - 1, -1):
    dp[j] = dp[j] or dp[j - item]

# Unbounded: iterate forwards
for j in range(item, target + 1):
    dp[j] = max(dp[j], dp[j - item] + value)
```

---

## Key Takeaways

1. **Identify the state**: What information do you need at each step?
2. **Write the recurrence**: How does the current state depend on previous states?
3. **Handle base cases**: What are the initial values?
4. **Optimize space**: Often O(n) can become O(1) or O(target)
5. **Direction matters**: 0/1 knapsack iterates backwards; unbounded iterates forwards
6. **Track extremes**: For products, track both max and min
7. **Binary search**: LIS and similar problems can be O(n log n)
