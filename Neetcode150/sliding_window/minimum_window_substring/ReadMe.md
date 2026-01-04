# Minimum Window Substring

## Summary

Given strings `s` and `t`, find the minimum window substring of `s` that contains all characters of `t` (including duplicates). If no such window exists, return an empty string.

### Key Points
- Variable-size sliding window problem
- Expand window until all characters of t are covered
- Contract from left to find minimum valid window
- Track character frequencies and count of satisfied characters

### Optimal Approach
Use a sliding window that expands to include all required characters, then contracts to find the minimum size.

```python
from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    t_count = Counter(t)
    required = len(t_count)
    formed = 0

    window_count = {}
    left = 0
    min_len = float('inf')
    min_window = ""

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]

            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1

    return min_window
```

### Complexity
- Time: O(|s| + |t|) - each character of s visited at most twice
- Space: O(|s| + |t|) - for character count dictionaries

---

## Detailed Explanation

### Problem Analysis

This is the hardest sliding window problem in the standard set. The key challenges are:
1. Tracking when all characters of t are satisfied (including duplicates)
2. Efficiently shrinking the window to find the minimum
3. Handling the case when t has duplicate characters

### The "Formed" Counter

We use two levels of counting:
- `t_count`: frequency of each character needed
- `window_count`: frequency of each character in current window
- `formed`: number of unique characters whose required frequency is met

When `formed == required` (number of unique characters in t), the window is valid.

### Why Track Unique Characters Satisfied?

Consider `t = "AAB"`:
- `t_count = {'A': 2, 'B': 1}`
- `required = 2` (two unique characters)

As we scan:
- See one 'A': window_count['A'] = 1, not yet equal to t_count['A'] = 2
- See second 'A': window_count['A'] = 2, now equals t_count['A'], so formed++
- See 'B': window_count['B'] = 1, equals t_count['B'], so formed++
- Now formed = 2 = required, window is valid

### Step-by-Step Example

For `s = "ADOBECODEBANC"`, `t = "ABC"`:

```
t_count = {A:1, B:1, C:1}, required = 3

Expand until valid:
right=0 'A': formed=1
right=1 'D': formed=1
right=2 'O': formed=1
right=3 'B': formed=2
right=4 'E': formed=2
right=5 'C': formed=3, VALID! window="ADOBEC", len=6

Contract:
left=1: remove 'A', formed=2, no longer valid

Continue expanding:
right=6 'O': formed=2
right=7 'D': formed=2
right=8 'E': formed=2
right=9 'B': formed=2
right=10 'A': formed=3, VALID! window="DOBECODEBA", len=10 (not better)

Contract:
left=2: remove 'D', still valid (formed=3)
...continue contracting...
left=5: remove 'C', formed=2, no longer valid

right=11 'N': formed=2
right=12 'C': formed=3, VALID! window="BANC", len=4

Contract:
left=9: remove 'B', formed=2
```

Minimum window: "BANC"

### Alternative: Filtered String

For very long s with sparse relevant characters:

```python
def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    t_count = Counter(t)

    # Create filtered list of (index, char) for relevant chars
    filtered = [(i, c) for i, c in enumerate(s) if c in t_count]

    required = len(t_count)
    formed = 0
    window_count = {}

    left = 0
    min_len = float('inf')
    min_left, min_right = 0, 0

    for right in range(len(filtered)):
        char = filtered[right][1]
        window_count[char] = window_count.get(char, 0) + 1

        if window_count[char] == t_count[char]:
            formed += 1

        while formed == required:
            start = filtered[left][0]
            end = filtered[right][0]

            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_left, min_right = start, end

            left_char = filtered[left][1]
            window_count[left_char] -= 1
            if window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1

    return "" if min_len == float('inf') else s[min_left:min_right + 1]
```

### Edge Cases
- t longer than s: impossible, return ""
- t equals s: return s
- t has characters not in s: return ""
- Multiple valid windows of same size: return any (typically first)
- t has duplicate characters: must appear that many times in window

### Common Mistakes
- Not handling duplicate characters in t
- Off-by-one in window boundaries
- Forgetting to check if character is in t before updating formed

### Related Problems
- Permutation in String: fixed window, exact match
- Find All Anagrams in a String: fixed window, find all positions
- Substring with Concatenation of All Words: word-level matching
