# Sliding Window

## Summary

The sliding window technique maintains a contiguous subarray or substring that "slides" across the data structure. It is a specialized form of the two-pointer technique where both pointers move in the same direction.

### Core Concepts

**Fixed-Size Window**
- Window size is predetermined
- Slide by adding one element and removing one element
- Examples: permutation matching, moving averages

**Variable-Size Window**
- Window expands and contracts based on validity conditions
- Expand until invalid, contract until valid
- Examples: minimum window substring, longest substring without repeats

**When to Use Sliding Window**
- Finding contiguous subarrays with specific properties
- Substring problems with character constraints
- Optimizing from O(n*k) to O(n) for window-based queries

### The Pattern

```
left = 0
for right in range(n):
    # Add element at right to window

    while window is invalid:
        # Remove element at left from window
        left += 1

    # Update result
```

---

## Problems in This Section

### Best Time to Buy and Sell Stock
Find maximum profit from one buy and one sell transaction.
- Pattern: Track running minimum
- Key insight: Optimal buy point for any sell day is the minimum price before it

### Longest Substring Without Repeating Characters
Find the longest substring with all unique characters.
- Pattern: Variable-size window with set/map
- Key insight: When repeat found, jump left pointer past previous occurrence

### Longest Repeating Character Replacement
Find longest substring achievable by replacing at most k characters.
- Pattern: Variable-size window with frequency counting
- Key insight: Valid window needs (size - max_freq) <= k replacements

### Permutation in String
Check if s2 contains a permutation of s1.
- Pattern: Fixed-size window (size of s1)
- Key insight: Permutations have identical character frequencies

### Minimum Window Substring
Find smallest substring of s containing all characters of t.
- Pattern: Variable-size window with "formed" counter
- Key insight: Track unique characters fully satisfied, not total characters

### Sliding Window Maximum
Find maximum in each window of size k.
- Pattern: Monotonic deque
- Key insight: Maintain decreasing deque of candidates for maximum

---

## Window Types Comparison

| Type | Size | Contract When | Expand When |
|------|------|---------------|-------------|
| Fixed | k elements | Always (after reaching size k) | Always |
| Variable (valid) | Dynamic | Window becomes invalid | Always |
| Variable (optimal) | Dynamic | Found valid, looking for smaller | Window becomes valid |

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Best Time to Buy and Sell Stock | O(n) | O(1) |
| Longest Substring Without Repeating Characters | O(n) | O(min(n, m))* |
| Longest Repeating Character Replacement | O(n) | O(1) |
| Permutation in String | O(n) | O(1) |
| Minimum Window Substring | O(n + m) | O(n + m) |
| Sliding Window Maximum | O(n) | O(k) |

*m is the size of the character set

---

## Common Data Structures

**Hash Map/Counter**
- Track character frequencies in window
- O(1) add/remove/lookup

**Hash Set**
- Track unique elements in window
- O(1) membership testing

**Monotonic Deque**
- Maintain elements in sorted order
- Front always has min/max
- O(1) amortized operations

---

## Key Techniques

### Incremental Updates
Instead of recalculating window properties from scratch, update incrementally:
- Add new element's contribution
- Remove old element's contribution
- O(1) per slide instead of O(k)

### The "Formed" Pattern
For problems requiring all elements of a set to be covered:
- Count unique elements fully satisfied
- Window valid when formed equals required
- More efficient than checking all counts each time

### Monotonic Structures
For min/max queries over windows:
- Maintain candidates in sorted order
- Remove elements that can never be the answer
- Front of structure is always the current answer

---

## Key Takeaways

1. **Identify the window type**: Fixed-size or variable-size determines the structure of your solution.

2. **Choose the right auxiliary structure**: Frequency counts for matching problems, monotonic deque for min/max problems.

3. **Update incrementally**: The power of sliding window comes from O(1) updates per position.

4. **Variable windows need two conditions**: One for when to expand (usually always), one for when to contract.

5. **Watch for the jump optimization**: In "longest without repeats," jumping left past the previous occurrence is faster than sliding one by one.
