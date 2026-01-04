# Longest Substring Without Repeating Characters

## Summary

Given a string `s`, find the length of the longest substring without repeating characters.

### Key Points
- Use a sliding window that expands and contracts
- Track characters in current window with a set or hash map
- When a repeat is found, shrink window from the left

### Optimal Approach
Use a sliding window with a hash map storing the last index of each character. When a repeat is found, jump the left pointer past the previous occurrence.

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Complexity
- Time: O(n) - each character visited at most twice
- Space: O(min(n, m)) where m is the character set size

---

## Detailed Explanation

### Problem Analysis

This is a classic sliding window problem. The window represents a valid substring (no repeats). We expand the window by moving right. When we encounter a repeat, we shrink from the left until the window is valid again.

### Two Approaches

**Set-Based (Shrink One by One)**
```python
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

This shrinks the window one character at a time until the repeat is removed.

**Hash Map (Jump to Position)**
The optimal version stores the index of each character. When a repeat is found, we can jump `left` directly past the previous occurrence rather than shrinking one by one.

The condition `char_index[char] >= left` is crucial - it ensures we only consider characters that are actually in the current window.

### Step-by-Step Example

For `s = "abcabcbb"`:

```
right=0, char='a': window="a", max=1
right=1, char='b': window="ab", max=2
right=2, char='c': window="abc", max=3
right=3, char='a': 'a' at index 0 >= left(0), left=1, window="bca", max=3
right=4, char='b': 'b' at index 1 >= left(1), left=2, window="cab", max=3
right=5, char='c': 'c' at index 2 >= left(2), left=3, window="abc", max=3
right=6, char='b': 'b' at index 4 >= left(3), left=5, window="cb", max=3
right=7, char='b': 'b' at index 6 >= left(5), left=7, window="b", max=3
```

Result: 3

### Why Check `char_index[char] >= left`?

Consider string `"abba"`:
- At index 3 ('a'), we have seen 'a' before at index 0
- But by then, left = 2 (moved after seeing second 'b')
- The 'a' at index 0 is no longer in our window
- Without the check, we would incorrectly move left backward

### Edge Cases
- Empty string: return 0
- Single character: return 1
- All same characters: return 1
- All unique characters: return length of string

### Common Mistakes
- Forgetting to check if the previous occurrence is in the current window
- Off-by-one errors when calculating window size
- Not updating the character index after processing

### The Sliding Window Pattern

This problem exemplifies the variable-size sliding window:
1. Expand window (move right pointer)
2. Check validity condition
3. If invalid, shrink window (move left pointer) until valid
4. Update result

### Related Problems
- Longest Repeating Character Replacement: similar window with character changes
- Minimum Window Substring: find minimum window containing all target characters
- Substring with Concatenation of All Words: word-based window
