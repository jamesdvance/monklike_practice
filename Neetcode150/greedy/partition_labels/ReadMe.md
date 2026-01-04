# Partition Labels

## Summary

Given a string, partition it into as many parts as possible so that each letter appears in at most one part. Return the size of each part.

### Key Points
- Find the last occurrence of each character
- Extend partition until all characters in it are complete
- Start new partition when current one is complete

### Optimal Approach
Greedy with last occurrence tracking.

```python
def partitionLabels(s: str) -> list[int]:
    last = {c: i for i, c in enumerate(s)}

    result = []
    start = 0
    end = 0

    for i, c in enumerate(s):
        end = max(end, last[c])

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result
```

### Complexity
- Time: O(n)
- Space: O(1) - at most 26 characters

---

## Detailed Explanation

### Problem Analysis

For any character c in a partition, all occurrences of c must be in that partition. So the partition must extend at least to the last occurrence of c.

As we extend, we might encounter new characters that push the end even further.

### The Greedy Insight

1. For current partition, track the farthest we must go (end)
2. When we reach end, all characters in this partition are complete
3. Start a new partition

### Step-by-Step Example

```
s = "ababcbacadefegdehijhklij"

last = {a:8, b:5, c:7, d:14, e:15, f:11, g:13, h:19, i:22, j:23, k:20, l:21}

i=0 'a': end = max(0, 8) = 8
i=1 'b': end = max(8, 5) = 8
i=2 'a': end = max(8, 8) = 8
i=3 'b': end = max(8, 5) = 8
i=4 'c': end = max(8, 7) = 8
i=5 'b': end = max(8, 5) = 8
i=6 'a': end = max(8, 8) = 8
i=7 'c': end = max(8, 7) = 8
i=8 'a': end = max(8, 8) = 8
     i == end, partition [0,8] size = 9

i=9 'd': end = max(9, 14) = 14
i=10 'e': end = max(14, 15) = 15
i=11 'f': end = max(15, 11) = 15
i=12 'e': end = max(15, 15) = 15
i=13 'g': end = max(15, 13) = 15
i=14 'd': end = max(15, 14) = 15
i=15 'e': end = max(15, 15) = 15
     i == end, partition [9,15] size = 7

i=16 'h': end = max(16, 19) = 19
i=17 'i': end = max(19, 22) = 22
i=18 'j': end = max(22, 23) = 23
i=19 'h': end = max(23, 19) = 23
i=20 'k': end = max(23, 20) = 23
i=21 'l': end = max(23, 21) = 23
i=22 'i': end = max(23, 22) = 23
i=23 'j': end = max(23, 23) = 23
     i == end, partition [16,23] size = 8

Answer: [9, 7, 8]
```

### Alternative: Two Pass with Intervals

```python
def partitionLabels(s: str) -> list[int]:
    # Find first and last occurrence of each character
    first = {}
    last = {}

    for i, c in enumerate(s):
        if c not in first:
            first[c] = i
        last[c] = i

    # Create intervals for each character
    intervals = [(first[c], last[c]) for c in first]
    intervals.sort()

    # Merge intervals
    result = []
    curr_start, curr_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= curr_end:
            curr_end = max(curr_end, end)
        else:
            result.append(curr_end - curr_start + 1)
            curr_start, curr_end = start, end

    result.append(curr_end - curr_start + 1)
    return result
```

This is essentially interval merging.

### Why Greedy Works

Once we've seen a character, we MUST include all its occurrences. This creates a "must-extend-to" point. We keep extending until no character in the current partition has occurrences beyond our end.

### Edge Cases
- Single character: [1]
- All same characters: [n]
- All unique characters: [1, 1, 1, ...]

### Related Problems
- Merge Intervals: similar merging logic
- Non-overlapping Intervals: maximizing partitions
- Minimum Number of Arrows to Burst Balloons: interval covering
