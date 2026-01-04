# Permutation in String

## Summary

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`. In other words, return true if one of `s1`'s permutations is a substring of `s2`.

### Key Points
- A permutation has the same characters with the same frequencies
- Use a fixed-size sliding window (size of s1)
- Compare character counts between window and s1

### Optimal Approach
Slide a window of size len(s1) over s2. Compare character frequencies at each position.

```python
from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)])

    if s1_count == window_count:
        return True

    for i in range(len(s1), len(s2)):
        # Add new character
        window_count[s2[i]] += 1

        # Remove old character
        old_char = s2[i - len(s1)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        if s1_count == window_count:
            return True

    return False
```

### Complexity
- Time: O(n) where n is len(s2), each comparison is O(26) = O(1)
- Space: O(1) - at most 26 character counts

---

## Detailed Explanation

### Problem Analysis

Two strings are permutations of each other if and only if they have identical character frequency distributions. The problem reduces to: find a substring of s2 with the same character counts as s1.

### Fixed-Size Sliding Window

Since we are looking for a permutation of s1, the window size is fixed at len(s1). We slide this window across s2, updating counts incrementally:
- Add the new character entering the window
- Remove the old character leaving the window
- Compare counts

### Optimized Counting with Matches

Instead of comparing entire count dictionaries, track how many characters have matching counts:

```python
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_count = [0] * 26
    window_count = [0] * 26

    for c in s1:
        s1_count[ord(c) - ord('a')] += 1

    matches = 0
    for i in range(26):
        if s1_count[i] == 0:
            matches += 1  # Both are 0, they match

    for i in range(len(s2)):
        # Add new character
        idx = ord(s2[i]) - ord('a')
        window_count[idx] += 1
        if window_count[idx] == s1_count[idx]:
            matches += 1
        elif window_count[idx] == s1_count[idx] + 1:
            matches -= 1

        # Remove old character (if window is full)
        if i >= len(s1):
            idx = ord(s2[i - len(s1)]) - ord('a')
            window_count[idx] -= 1
            if window_count[idx] == s1_count[idx]:
                matches += 1
            elif window_count[idx] == s1_count[idx] - 1:
                matches -= 1

        if matches == 26:
            return True

    return False
```

This achieves O(1) per position instead of O(26) for dictionary comparison.

### Step-by-Step Example

For `s1 = "ab"`, `s2 = "eidbaooo"`:

```
Initial s1_count: {a:1, b:1}
Window size: 2

i=0,1: window="ei", count={e:1,i:1}, no match
i=2: window="id", count={i:1,d:1}, no match
i=3: window="db", count={d:1,b:1}, no match
i=4: window="ba", count={b:1,a:1}, MATCH!
```

Return True

### Why Delete Zero Counts?

In the Counter approach, we delete keys with zero counts to ensure dictionary comparison works correctly. Counter({'a': 1}) != Counter({'a': 1, 'b': 0}), even though 'b' having count 0 is semantically equivalent to being absent.

### Edge Cases
- s1 longer than s2: impossible to find permutation
- s1 equals s2: trivially true
- s1 and s2 have no common characters: false
- Empty s1: debatable, typically true (empty permutation exists anywhere)

### Alternative: Sorted Substring Comparison

Check if any substring of s2, when sorted, equals sorted s1:

```python
def checkInclusion(s1: str, s2: str) -> bool:
    s1_sorted = sorted(s1)
    for i in range(len(s2) - len(s1) + 1):
        if sorted(s2[i:i + len(s1)]) == s1_sorted:
            return True
    return False
```

- Time: O(n * m log m) where m = len(s1)
- Space: O(m)

This is simpler but much slower.

### Related Problems
- Find All Anagrams in a String: find all starting indices (not just existence)
- Minimum Window Substring: variable window size
- Valid Anagram: compare two full strings
