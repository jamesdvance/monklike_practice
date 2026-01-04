# Longest Repeating Character Replacement

## Summary

Given a string `s` and an integer `k`, you can replace at most `k` characters to make any substring contain all the same character. Return the length of the longest such substring.

### Key Points
- Use a sliding window tracking character frequencies
- Valid window: window_size - max_frequency <= k
- The number of replacements needed equals characters that are not the majority

### Optimal Approach
Maintain a sliding window with character counts. A window is valid when the number of characters to replace (window size minus most frequent character) is at most k.

```python
def characterReplacement(s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        # Window is invalid if we need more than k replacements
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

### Complexity
- Time: O(n) - each character visited at most twice
- Space: O(1) - at most 26 character counts

---

## Detailed Explanation

### Problem Analysis

To make a window of length L contain all the same character, we need to replace L - (count of most frequent character) characters. If this value is at most k, the window is valid.

### The Key Insight

For any window, the optimal strategy is to keep the most frequent character and replace all others. This minimizes the number of replacements needed.

```
replacements_needed = window_size - max_frequency_in_window
valid window: replacements_needed <= k
```

### Why We Can Keep max_freq

A subtle optimization: we do not decrease max_freq when shrinking the window. This is valid because:
1. We only care about finding longer valid windows
2. A longer window requires a higher max_freq
3. If max_freq is "stale" (too high), we will shrink the window, but we will not miss a valid answer because any valid window with a smaller max_freq would be smaller than windows we have already found

```python
# Simplified version without explicit max_freq tracking
def characterReplacement(s: str, k: int) -> int:
    count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

This version recalculates max(count.values()) each time, which is O(26) = O(1) for uppercase letters.

### Step-by-Step Example

For `s = "AABABBA"`, `k = 1`:

```
right=0, 'A': count={A:1}, max_freq=1, window=1, valid (1-1<=1)
right=1, 'A': count={A:2}, max_freq=2, window=2, valid (2-2<=1)
right=2, 'B': count={A:2,B:1}, max_freq=2, window=3, valid (3-2<=1)
right=3, 'A': count={A:3,B:1}, max_freq=3, window=4, valid (4-3<=1)
right=4, 'B': count={A:3,B:2}, max_freq=3, window=5, invalid (5-3>1)
  shrink: left=1, count={A:2,B:2}, window=4, valid (4-2>1? no, 4-2=2>1)
  shrink: left=2, count={A:1,B:2}, window=3, valid (3-2<=1)
right=5, 'B': count={A:1,B:3}, max_freq=3, window=4, valid (4-3<=1)
right=6, 'A': count={A:2,B:3}, max_freq=3, window=5, invalid (5-3>1)
  shrink: left=3, count={A:1,B:3}, window=4, valid (4-3<=1)
```

Maximum length: 4 (e.g., "ABBA" -> "AAAA" or "BBBB")

### Alternative: Binary Search

We can binary search on the answer length:

```python
def characterReplacement(s: str, k: int) -> int:
    def canMakeLength(length):
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            if i >= length:
                count[s[i - length]] -= 1
            if i >= length - 1:
                if length - max(count.values()) <= k:
                    return True
        return False

    left, right = 1, len(s)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if canMakeLength(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
```

- Time: O(n log n)
- Space: O(1)

This is less efficient but demonstrates a different approach.

### Edge Cases
- k >= len(s): can make entire string uniform
- All same characters: return length of string
- k = 0: return length of longest run of same character
- Empty string: return 0

### Related Problems
- Longest Substring Without Repeating Characters: no replacements allowed
- Max Consecutive Ones III: binary version (flip 0s to 1s)
- Minimum Window Substring: different window validity condition
