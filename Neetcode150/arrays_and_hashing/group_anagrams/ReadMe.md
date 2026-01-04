# Group Anagrams

## Summary

Given an array of strings `strs`, group the anagrams together. An anagram is a word formed by rearranging the letters of another word using all original letters exactly once.

### Key Points
- Anagrams share the same sorted character sequence or character count signature
- Use the signature as a hash map key to group strings
- Two common signatures: sorted string or character count tuple

### Optimal Approach
Create a signature for each string and use it as a dictionary key. All anagrams will have the same signature.

```python
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

### Complexity
- Time: O(n * k log k) where n is number of strings and k is max string length
- Space: O(n * k) to store all strings in the hash map

---

## Detailed Explanation

### Problem Analysis

Group Anagrams extends the Valid Anagram concept to multiple strings. The challenge is efficiently determining which strings belong together. Since anagrams are rearrangements of the same characters, they share a canonical form that can serve as a grouping key.

### Signature Strategies

**Sorted String Signature**
The simplest approach - sort each string to get its canonical form.

```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

Time per string: O(k log k) for sorting

**Character Count Signature**
Count frequency of each character and use the count array as a key.

```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        groups[key].append(s)
    return list(groups.values())
```

Time per string: O(k) for counting

The count-based approach has better theoretical complexity O(n * k) vs O(n * k log k), but in practice the sorting approach is often faster for short strings due to Python's optimized sort.

### Why Tuple for Key?

Dictionary keys must be hashable. Lists are mutable and unhashable, but tuples are immutable and hashable. Converting the sorted list or count array to a tuple allows it to serve as a dictionary key.

### Edge Cases
- Empty string: forms its own group (sorted empty string is empty)
- Single character strings: each unique character forms a group
- All strings are anagrams: single group in output
- No anagrams exist: each string in its own group

### Implementation Details

**Using defaultdict**
`defaultdict(list)` automatically creates an empty list for new keys, avoiding KeyError and simplifying the code.

**Order of Output**
The problem typically does not require groups in any particular order, nor strings within groups to be ordered. However, be aware that dictionary iteration order in Python 3.7+ is insertion order.

### Related Problems
- Valid Anagram: the foundation for this problem
- Find All Anagrams in a String: sliding window approach
- Anagram Mappings: mapping indices between anagrams
