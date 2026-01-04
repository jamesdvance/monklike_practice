# Design Add and Search Words Data Structure

## Summary

Design a data structure that supports adding words and searching with wildcards. The '.' character matches any single letter.

### Key Points
- Use a Trie for efficient word storage
- Handle wildcards with recursive backtracking
- '.' requires exploring all children at that level

### Optimal Approach
Use a Trie with recursive search for wildcard handling.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end

            char = word[index]

            if char == '.':
                # Try all possible children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)
```

### Complexity
- addWord: O(m) where m is word length
- search without wildcards: O(m)
- search with wildcards: O(26^w * m) worst case, where w is number of wildcards
- Space: O(total characters)

---

## Detailed Explanation

### Problem Analysis

This extends the basic Trie with pattern matching. The key difference is handling '.' which can match any character. This requires exploring multiple paths.

### Why Backtracking?

When we encounter '.', we do not know which character it represents. We must try all possibilities:

```
For pattern "c.t" and words ["cat", "cut", "cot"]:

At '.':
  Try 'a': c-a-t, check if 't' matches next
  Try 'u': c-u-t, check if 't' matches next
  Try 'o': c-o-t, check if 't' matches next
```

All three match, so "c.t" returns true.

### Iterative Approach with BFS

```python
def search(self, word: str) -> bool:
    from collections import deque

    queue = deque([self.root])

    for char in word:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()

            if char == '.':
                for child in node.children.values():
                    queue.append(child)
            elif char in node.children:
                queue.append(node.children[char])

        if not queue:
            return False

    return any(node.is_end for node in queue)
```

### Optimizations

**Limit recursion depth**: If word length is bounded, worst case is manageable.

**Prune early**: If no children exist at a node, return false immediately.

**Cache pattern results**: If the same pattern is searched multiple times, cache results (requires invalidation on addWord).

### Step-by-Step Example

Words: ["bad", "dad", "mad"]
Search: ".ad"

```
At '.': try 'b', 'd', 'm'

Path 'b':
  At 'a': match
  At 'd': match, is_end = true -> return true

(Could continue with 'd' and 'm', but short-circuit on first match)
```

### Edge Cases
- All wildcards: "..." searches for any 3-letter word
- Wildcard at end: "ca." matches any 3-letter word starting with "ca"
- Empty pattern: matches empty word if added
- No wildcards: degenerates to standard trie search

### Related Problems
- Implement Trie: foundation for this problem
- Word Search II: similar wildcard/backtracking concepts
- Regular Expression Matching: more complex pattern matching
