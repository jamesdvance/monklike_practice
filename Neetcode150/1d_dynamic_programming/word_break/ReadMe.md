# Word Break

## Summary

Given a string s and a dictionary of words, determine if s can be segmented into a space-separated sequence of dictionary words.

### Key Points
- dp[i] = can we segment s[0:i]?
- Check all possible last words ending at position i
- Use a set for O(1) word lookup

### Optimal Approach
Bottom-up DP checking all valid word endings.

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can be segmented

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
```

### Complexity
- Time: O(n^2 * m) where m is max word length (for substring)
- Space: O(n)

---

## Detailed Explanation

### Problem Analysis

To segment s[0:i], we need:
1. A valid segmentation of s[0:j] for some j < i
2. s[j:i] to be a dictionary word

### State Definition

dp[i] = True if s[0:i] can be segmented into dictionary words

### Recurrence

dp[i] = any(dp[j] and s[j:i] in wordDict) for j in range(i)

### Optimized with Max Word Length

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    max_len = max(len(w) for w in wordDict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        # Only check words up to max length
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
```

### Top-Down with Memoization

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    memo = {}

    def dp(i):
        if i == len(s):
            return True
        if i in memo:
            return memo[i]

        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and dp(j):
                memo[i] = True
                return True

        memo[i] = False
        return False

    return dp(0)
```

### BFS Approach

```python
from collections import deque

def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)

    visited = set()
    queue = deque([0])

    while queue:
        start = queue.popleft()

        if start in visited:
            continue
        visited.add(start)

        for end in range(start + 1, n + 1):
            if s[start:end] in word_set:
                if end == n:
                    return True
                queue.append(end)

    return False
```

### Step-by-Step Example

```
s = "leetcode"
wordDict = ["leet", "code"]

dp[0] = True (base case)

i=1: s[0:1]="l" not in dict -> dp[1]=False
i=2: s[0:2]="le" not in dict -> dp[2]=False
i=3: s[0:3]="lee" not in dict -> dp[3]=False
i=4: s[0:4]="leet" in dict, dp[0]=True -> dp[4]=True
i=5: no valid word ending at 5 -> dp[5]=False
i=6: no valid word ending at 6 -> dp[6]=False
i=7: no valid word ending at 7 -> dp[7]=False
i=8: s[4:8]="code" in dict, dp[4]=True -> dp[8]=True

Answer: True
```

### Using Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

def wordBreak(s: str, wordDict: list[str]) -> bool:
    # Build trie
    root = TrieNode()
    for word in wordDict:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n):
        if not dp[i]:
            continue

        node = root
        for j in range(i, n):
            if s[j] not in node.children:
                break
            node = node.children[s[j]]
            if node.is_word:
                dp[j + 1] = True

    return dp[n]
```

### Edge Cases
- Empty string: return True (can be segmented trivially)
- Word longer than any dictionary word: check boundary
- Dictionary word is prefix of another: both valid

### Related Problems
- Word Break II: return all segmentations
- Concatenated Words: word made of other words
- Extra Characters in a String: minimize leftover characters
