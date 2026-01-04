# Greedy Algorithms

## Summary

Greedy algorithms make locally optimal choices at each step, hoping to find a global optimum. They work when the problem has the greedy-choice property and optimal substructure.

### Core Concepts

1. **Greedy-Choice Property**: A locally optimal choice leads to a globally optimal solution
2. **Optimal Substructure**: An optimal solution contains optimal solutions to subproblems
3. **No Backtracking**: Once a choice is made, it's never reconsidered

### When to Use Greedy

- Optimization problems (maximize/minimize)
- Scheduling and interval problems
- Problems where local decisions don't affect future options badly
- When DP would be overkill

---

## Problems in This Section

| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| [Maximum Subarray](./maximum_subarray/) | Kadane's Algorithm | Reset when running sum goes negative |
| [Jump Game](./jump_game/) | Farthest reach | Track max reachable position |
| [Jump Game II](./jump_game_ii/) | BFS simulation | Increment jumps when current range exhausted |
| [Gas Station](./gas_station/) | Circular greedy | If total >= cost, solution exists; reset on negative |
| [Hand of Straights](./hand_of_straights/) | Sort + consume | Start groups from smallest available card |
| [Merge Triplets](./merge_triplets_to_form_target_triplet/) | Filter + collect | Only use triplets <= target in all positions |
| [Partition Labels](./partition_labels/) | Last occurrence | Extend partition to cover all occurrences |
| [Valid Parenthesis String](./valid_parenthesis_string/) | Range tracking | Track min/max possible open count |

---

## Common Patterns

### Pattern 1: Kadane's Algorithm (Maximum Subarray)

```python
def max_subarray(nums):
    max_sum = curr_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum
```

Reset when extending would hurt more than starting fresh.

### Pattern 2: Farthest Reach

```python
def can_reach_end(jumps):
    max_reach = 0
    for i, jump in enumerate(jumps):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True
```

Track how far we can go, update as we progress.

### Pattern 3: Sort and Process

```python
def process_sorted(items):
    items.sort()
    result = []

    for item in items:
        # Process in sorted order
        # Make greedy choice based on current item
        pass

    return result
```

Sorting often reveals the optimal order for greedy processing.

### Pattern 4: Two-Pointer Greedy

```python
def greedy_two_pointer(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Make greedy choice from ends
        if should_take_left(arr[left], arr[right]):
            left += 1
        else:
            right -= 1
```

### Pattern 5: Range Tracking

```python
def track_range(s):
    low = high = 0

    for c in s:
        if c == '+':
            low += 1
            high += 1
        elif c == '-':
            low = max(0, low - 1)
            high -= 1
        else:  # wildcard
            low = max(0, low - 1)
            high += 1

        if high < 0:
            return False

    return low == 0
```

Track the range of possible states when choices are flexible.

---

## Greedy Proof Techniques

### 1. Exchange Argument

Show that swapping any non-greedy choice with the greedy choice doesn't worsen the solution.

### 2. Staying Ahead

Show that at every step, the greedy solution is at least as good as any other.

### 3. Structural Argument

Show that the greedy choice is part of some optimal solution.

---

## When Greedy Fails

Greedy doesn't work when local optima don't lead to global optimum:

```
Coin Change: coins = [1, 3, 4], amount = 6
Greedy: 4 + 1 + 1 = 3 coins
Optimal: 3 + 3 = 2 coins
```

Use DP instead when greedy fails.

---

## Key Takeaways

1. **Sort first** when order matters for optimal choices
2. **Track extremes** (min/max) when values affect decisions
3. **Reset wisely** when continuing hurts more than restarting
4. **Prove correctness** - greedy intuition can be wrong
5. **Consider DP** if greedy doesn't obviously work
6. **Local to global** - ensure local optimal leads to global optimal
7. **Range tracking** handles uncertainty in choices
