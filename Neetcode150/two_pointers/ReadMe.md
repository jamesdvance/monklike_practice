# Two Pointers

## Summary

The two-pointer technique uses two indices to traverse a data structure, typically from opposite ends or at different speeds. This pattern is especially powerful on sorted arrays and when searching for pairs or subarrays with specific properties.

### Core Concepts

**Opposite Direction Pointers**
- Start at both ends of an array
- Move toward each other based on some condition
- Common for: palindrome checks, pair finding, container problems

**Same Direction Pointers**
- Both start at the beginning (or same position)
- Move at different speeds or conditions
- Common for: slow/fast pointer, sliding window foundation

**When to Use Two Pointers**
- Searching for pairs in a sorted array
- Comparing elements from both ends
- Reducing O(n^2) brute force to O(n)
- Problems involving "containers" or ranges

### Key Insight

Two pointers work when you can prove that moving one pointer eliminates possibilities that cannot be optimal. This allows you to make progress toward the solution without checking all pairs.

---

## Problems in This Section

### Valid Palindrome
Check if a string reads the same forwards and backwards after removing non-alphanumeric characters.
- Pattern: Opposite direction pointers
- Key insight: If characters at both ends match, the inner substring determines palindrome status

### Two Sum II (Sorted Array)
Find two numbers in a sorted array that add to a target.
- Pattern: Opposite direction pointers
- Key insight: If sum is too small, move left pointer right; if too large, move right pointer left

### 3Sum
Find all unique triplets that sum to zero.
- Pattern: Fix one element, then Two Sum II on remainder
- Key insight: Sort first to enable two-pointer inner loop and duplicate skipping

### Container With Most Water
Find two lines that form a container holding the most water.
- Pattern: Opposite direction pointers
- Key insight: Always move the shorter line inward (moving the taller line cannot improve the result)

### Trapping Rain Water
Calculate how much water is trapped between bars after rain.
- Pattern: Opposite direction pointers with running maximums
- Key insight: Water at each position is determined by min(left_max, right_max) - height

---

## Pattern: Moving the Limiting Factor

A common theme in two-pointer problems is identifying the "limiting factor" and moving it:

| Problem | Limiting Factor | Action |
|---------|-----------------|--------|
| Two Sum II | Sum vs target | Move based on comparison |
| Container With Most Water | Shorter line | Move the shorter line |
| Trapping Rain Water | Smaller max | Process side with smaller max |

The key is proving that NOT moving the limiting factor cannot lead to a better solution.

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Valid Palindrome | O(n) | O(1) |
| Two Sum II | O(n) | O(1) |
| 3Sum | O(n^2) | O(1)* |
| Container With Most Water | O(n) | O(1) |
| Trapping Rain Water | O(n) | O(1) |

*Excluding output storage; O(n) if counting output

---

## Two Pointers vs Other Techniques

**vs Hash Map**
- Two pointers require sorted input (or pay O(n log n) to sort)
- Two pointers use O(1) space vs O(n) for hash map
- Use hash map when order does not matter and space is acceptable

**vs Sliding Window**
- Sliding window is a special case of two pointers
- Use sliding window for contiguous subarray problems
- Use general two pointers for pair/triplet finding

**vs Binary Search**
- Binary search finds one element in O(log n)
- Two pointers find pairs in O(n)
- For pair problems on sorted arrays, two pointers is usually optimal

---

## Key Takeaways

1. **Sorted input is your friend**: Two pointers often require or benefit from sorted data.

2. **Prove correctness by elimination**: Show that moving one pointer does not skip over optimal solutions.

3. **Handle duplicates carefully**: When finding unique results, skip duplicate values after processing.

4. **The limiting factor moves**: Identify what constrains your answer and move that pointer.

5. **Reduce dimensions**: 3Sum reduces to 2Sum, 4Sum to 3Sum - master the base case.
