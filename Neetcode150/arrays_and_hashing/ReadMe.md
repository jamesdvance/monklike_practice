# Arrays and Hashing

## Summary

Arrays and hashing form the foundation of algorithm problem-solving. This category focuses on using hash-based data structures (dictionaries, sets) to optimize array operations from O(n^2) to O(n) time complexity.

### Core Concepts

**Hash Maps (Dictionaries)**
- Provide O(1) average-case lookup, insertion, and deletion
- Map keys to values for quick retrieval
- Essential for counting frequencies, storing indices, and caching computations

**Hash Sets**
- Provide O(1) average-case membership testing
- Store unique elements
- Useful for duplicate detection and complement lookups

**Trade-offs**
- Time vs Space: Hash structures trade O(n) space for O(1) operations
- Ordering: Standard hash structures do not maintain insertion order (though Python dicts do as of 3.7)

### Common Patterns

1. **Frequency Counting**: Count occurrences of elements using a dictionary
2. **Seen Set**: Track previously encountered elements for duplicate detection or complement finding
3. **Two-Pass Processing**: First pass to build a hash structure, second pass to query it
4. **Prefix/Suffix Computation**: Precompute cumulative results for range queries

### When to Use Hashing

- Need O(1) lookups instead of O(n) linear search
- Counting occurrences or frequencies
- Finding pairs or groups with specific properties
- Detecting duplicates or unique elements
- Grouping elements by some property

---

## Problems in This Section

### Contains Duplicate
The simplest introduction to using a set for O(1) membership testing. Check if any element appears twice in an array.
- Pattern: Seen set
- Key insight: Set membership is O(1)

### Valid Anagram
Determine if two strings are anagrams by comparing character frequencies.
- Pattern: Frequency counting
- Key insight: Anagrams have identical character counts

### Two Sum
Find two numbers that sum to a target by storing complements in a hash map.
- Pattern: Complement lookup
- Key insight: For each number, its needed partner is (target - number)

### Group Anagrams
Group strings that are anagrams by using a canonical form as the hash key.
- Pattern: Grouping by signature
- Key insight: Sorted string or character count serves as group identifier

### Top K Frequent Elements
Find the k most frequent elements using frequency counting followed by selection.
- Pattern: Frequency counting + selection
- Key insight: Bucket sort achieves O(n) when frequency is bounded by n

### Product of Array Except Self
Calculate products without division using prefix and suffix products.
- Pattern: Prefix/suffix decomposition
- Key insight: Result at i = product of left side * product of right side

### Valid Sudoku
Validate a Sudoku board by checking row, column, and box constraints.
- Pattern: Multiple constraint tracking with sets
- Key insight: Box index = (row // 3) * 3 + (col // 3)

### Encode and Decode Strings
Design a serialization format for a list of strings that handles any characters.
- Pattern: Length-prefix encoding
- Key insight: Prefix each string with its length to avoid delimiter conflicts

### Longest Consecutive Sequence
Find the longest consecutive sequence in O(n) time without sorting.
- Pattern: Set membership + smart iteration
- Key insight: Only count from sequence starts (numbers without predecessors)

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Contains Duplicate | O(n) | O(n) |
| Valid Anagram | O(n) | O(1)* |
| Two Sum | O(n) | O(n) |
| Group Anagrams | O(n * k log k) | O(n * k) |
| Top K Frequent Elements | O(n) | O(n) |
| Product of Array Except Self | O(n) | O(1)** |
| Valid Sudoku | O(1) | O(1) |
| Encode and Decode Strings | O(n) | O(n) |
| Longest Consecutive Sequence | O(n) | O(n) |

*O(1) when character set is fixed (e.g., 26 lowercase letters)
**O(1) excluding the output array

---

## Key Takeaways

1. **Hash structures are your first tool** when you need to speed up lookups or track occurrences.

2. **Consider the key design** when grouping or indexing - the key must uniquely identify what you are tracking.

3. **Prefix/suffix patterns** appear frequently - precomputing cumulative information enables O(1) range queries.

4. **Length-prefix encoding** solves delimiter problems when data can contain any character.

5. **Starting conditions matter** - in Longest Consecutive Sequence, starting only from sequence beginnings reduces O(n^2) to O(n).
