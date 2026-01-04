# Implement Trie (Prefix Tree)

## Summary

Implement a Trie data structure with insert, search, and startsWith operations.

### Key Points
- Each node has up to 26 children (for lowercase letters)
- Mark word endings explicitly
- Shared prefixes share nodes

### Optimal Approach
Use a dictionary or array at each node to store children.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

### Complexity
- Insert: O(m) where m is word length
- Search: O(m)
- startsWith: O(m)
- Space: O(total characters across all words)

---

## Detailed Explanation

### Problem Analysis

A Trie (prefix tree) stores strings by sharing common prefixes. Each edge represents a character, and paths from root to marked nodes represent complete words.

### Structure Visualization

For words ["app", "apple", "api"]:

```
        root
          |
          a
          |
          p
         / \
        p   i (end)
        |
        l (end: "app")
        |
        e (end: "apple")
```

### Array-Based Implementation

Using arrays instead of dictionaries:

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
```

### Why Tries?

Compared to hash sets:
- Tries enable prefix queries (startsWith)
- Tries can enumerate all words with a prefix
- Tries have predictable O(m) operations vs hash collisions

Compared to balanced BST of strings:
- Tries are O(m) vs O(m log n) for BST operations
- Tries use shared prefixes efficiently

### Applications

- Autocomplete systems
- Spell checkers
- IP routing tables
- Search engines
- Word games (Scrabble, Boggle)

### Edge Cases
- Empty string: can be a valid word
- Search for non-existent word: return false
- Prefix of an existing word: startsWith returns true

### Related Problems
- Design Add and Search Words Data Structure: trie with wildcards
- Word Search II: trie for efficient board search
- Replace Words: use trie to find shortest root
