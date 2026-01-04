# Backtracking

## Summary

Backtracking is an algorithmic technique for finding all (or some) solutions by incrementally building candidates and abandoning ("backtracking" from) candidates that fail to satisfy constraints. It is essentially a depth-first search through the solution space.

### Core Concepts

**The Backtracking Template**
```python
def backtrack(state):
    if is_solution(state):
        record_solution(state)
        return

    for choice in available_choices(state):
        if is_valid(choice, state):
            make_choice(choice, state)
            backtrack(state)
            undo_choice(choice, state)  # Backtrack
```

**When to Use Backtracking**
- Generate all permutations, combinations, or subsets
- Solve constraint satisfaction problems (N-Queens, Sudoku)
- Search for paths in a graph or grid
- Find all solutions that satisfy certain criteria

**Key Properties**
- Explores solution space systematically
- Prunes invalid branches early
- Uses recursion with state modification and restoration

---

## Problems in This Section

### Subsets
Generate all possible subsets of an array.
- Pattern: Include/exclude decision at each element
- Key insight: 2^n subsets for n elements

### Combination Sum
Find combinations that sum to a target (with unlimited reuse).
- Pattern: Try each candidate, subtract from target
- Key insight: Use start index to avoid duplicates, allow same index for reuse

### Permutations
Generate all ordered arrangements of elements.
- Pattern: Track used elements, try all available
- Key insight: n! permutations for n elements

### Subsets II
Generate subsets when input has duplicates.
- Pattern: Sort + skip duplicates at same level
- Key insight: `if i > start and nums[i] == nums[i-1]: continue`

### Combination Sum II
Combinations summing to target (each element used once, with duplicates).
- Pattern: Combine Combination Sum with Subsets II logic
- Key insight: Move to next index after using element

### Word Search
Find if a word exists in a character grid.
- Pattern: DFS from each cell, mark visited
- Key insight: Modify grid in-place for visited tracking

### Palindrome Partitioning
Partition string into all possible palindrome substrings.
- Pattern: Try all cuts, recurse on remainder
- Key insight: Check if prefix is palindrome before recursing

### Letter Combinations of a Phone Number
Generate letter combinations from digit string.
- Pattern: Iterate through mappings for each digit
- Key insight: Cartesian product of letter choices

### N-Queens
Place n non-attacking queens on an n x n board.
- Pattern: Place row by row, track columns and diagonals
- Key insight: Use sets for O(1) conflict checking

---

## Common Patterns

### Subset/Combination Pattern
```python
def backtrack(start, current):
    result.append(current[:])  # Record at every state
    for i in range(start, len(nums)):
        current.append(nums[i])
        backtrack(i + 1, current)
        current.pop()
```

### Permutation Pattern
```python
def backtrack(current):
    if len(current) == len(nums):
        result.append(current[:])
        return
    for num in nums:
        if num not in current:  # Or use used[] array
            current.append(num)
            backtrack(current)
            current.pop()
```

### Grid Search Pattern
```python
def dfs(row, col, index):
    if index == len(target):
        return True
    if out_of_bounds or visited or no_match:
        return False

    mark_visited(row, col)
    result = dfs(neighbors)
    unmark_visited(row, col)
    return result
```

### Constraint Satisfaction Pattern
```python
def backtrack(position):
    if position == end:
        record_solution()
        return

    for choice in choices:
        if is_valid(choice, position):
            place(choice, position)
            backtrack(next_position)
            remove(choice, position)
```

---

## Handling Duplicates

When input contains duplicates, sort first and skip consecutive duplicates:

```python
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue  # Skip duplicate at same level
    # ... proceed with choice
```

The condition `i > start` is crucial - it only skips duplicates at the same recursion level, not across different paths.

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Subsets | O(n * 2^n) | O(n) |
| Combination Sum | O(n^(T/M)) | O(T/M) |
| Permutations | O(n! * n) | O(n) |
| Subsets II | O(n * 2^n) | O(n) |
| Combination Sum II | O(2^n) | O(n) |
| Word Search | O(m*n*4^L) | O(L) |
| Palindrome Partitioning | O(n * 2^n) | O(n) |
| Letter Combinations | O(4^n * n) | O(n) |
| N-Queens | O(n!) | O(n) |

T = target, M = min candidate, L = word length

---

## Key Takeaways

1. **State modification and restoration**: Always undo changes after recursion to maintain clean state for other branches.

2. **Pruning is essential**: Check validity before recursing to avoid exploring dead ends.

3. **Index management prevents duplicates**: Using a `start` index ensures each combination is generated once.

4. **Sort for duplicate handling**: Sorting groups duplicates, making them easy to skip.

5. **In-place marking for grids**: Modify the grid to mark visited cells, restore after backtracking.

6. **Sets for O(1) conflict checking**: In constraint problems like N-Queens, use sets to quickly check if a placement is valid.

7. **Early termination**: Return immediately when a solution is found (if only one is needed) or when constraints are violated.
