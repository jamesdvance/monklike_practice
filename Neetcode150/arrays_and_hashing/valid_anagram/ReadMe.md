# Valid Anagram

## Summary

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram uses the same characters with the same frequencies, just rearranged.

### Key Points
- Anagrams have identical character frequency distributions
- Use a hash map (Counter) to count character occurrences
- Strings must have the same length to be anagrams

### Optimal Approach
Count the frequency of each character in both strings and compare the counts.

```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

Or without imports:

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True
```

### Complexity
- Time: O(n) where n is the length of the strings
- Space: O(k) where k is the size of the character set (26 for lowercase English letters)

---

## Detailed Explanation

### Problem Analysis

The Valid Anagram problem tests understanding of character frequency counting. Two strings are anagrams if and only if they contain the exact same characters with the exact same frequencies. This insight leads directly to the hash map solution.

### Alternative Approaches

**Sorting Approach**
If two strings are anagrams, their sorted versions will be identical.

```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

- Time: O(n log n) due to sorting
- Space: O(n) for the sorted copies

This is simpler to write but less efficient than the hash map approach.

**Single Counter with Decrement**
Instead of creating two counters, increment for the first string and decrement for the second:

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    return all(c == 0 for c in count)
```

This uses a fixed-size array when the character set is known (lowercase English letters).

### Edge Cases
- Empty strings: two empty strings are anagrams of each other
- Different lengths: cannot be anagrams
- Single character strings: anagram only if identical
- Unicode characters: ensure your solution handles the expected character set

### Follow-up: What if inputs contain Unicode characters?
The hash map approach naturally extends to Unicode since Python dictionaries can use any hashable key. The array-based approach would need modification to handle the larger character space, making the hash map preferable for Unicode input.

### Related Problems
- Group Anagrams: group strings that are anagrams of each other
- Find All Anagrams in a String: sliding window variant
- Minimum Number of Steps to Make Two Strings Anagram
