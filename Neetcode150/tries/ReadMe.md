# Tries

## Summary

A Trie (prefix tree) is a tree-like data structure used to efficiently store and retrieve strings. Each path from root to a node represents a prefix, and complete words are marked at their ending nodes.

### Core Concepts

**Structure**
- Root node is empty
- Each edge represents a character
- Each node can have up to 26 children (for lowercase letters)
- Nodes mark whether they end a complete word

**When to Use Tries**
- Prefix matching (autocomplete)
- Dictionary with search and startsWith
- Word validation in games (Scrabble, Boggle)
- IP routing (longest prefix matching)

**Complexity**
- Insert: O(m) where m is word length
- Search: O(m)
- Prefix search: O(m)
- Space: O(alphabet_size * m * n) worst case

---

## Problems in This Section

### Implement Trie
Build a basic Trie with insert, search, and startsWith operations.
- Pattern: Tree traversal with character nodes
- Key insight: Shared prefixes share nodes

### Design Add and Search Words Data Structure
Extend Trie to support wildcard searches with '.'.
- Pattern: Trie + backtracking for wildcards
- Key insight: '.' requires exploring all children

### Word Search II
Find all words from a list that can be formed on a character board.
- Pattern: Trie + DFS on grid
- Key insight: Trie prunes invalid paths early

---

## Implementation Choices

### Dictionary vs Array Children

**Dictionary**:
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```
- Flexible character set
- Memory efficient for sparse tries
- Slightly slower access

**Array**:
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
```
- Fixed alphabet size
- O(1) child access
- Uses more memory if sparse

### Storing Words vs is_end Flag

**Flag only**:
```python
node.is_end = True
```
Requires reconstructing word from path.

**Store word**:
```python
node.word = "complete_word"
```
Convenient for collecting results without path tracking.

---

## Common Patterns

### Basic Trie Operations

```python
def insert(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end = True

def search(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end
```

### Wildcard Search

```python
def searchWithWildcard(node, word, index):
    if index == len(word):
        return node.is_end

    char = word[index]
    if char == '.':
        return any(searchWithWildcard(child, word, index + 1)
                   for child in node.children.values())
    else:
        if char not in node.children:
            return False
        return searchWithWildcard(node.children[char], word, index + 1)
```

### Trie-Guided Grid Search

```python
def dfs(row, col, node):
    char = board[row][col]
    if char not in node.children:
        return

    next_node = node.children[char]
    if next_node.word:
        result.append(next_node.word)

    board[row][col] = '#'  # mark visited
    for neighbor in neighbors:
        dfs(neighbor, next_node)
    board[row][col] = char  # restore
```

---

## Complexity Summary

| Problem | Insert | Search | Space |
|---------|--------|--------|-------|
| Implement Trie | O(m) | O(m) | O(total chars) |
| Add and Search Words | O(m) | O(26^w * m)* | O(total chars) |
| Word Search II | O(W * L) build | O(m*n*4^L) | O(W * L) |

*w = number of wildcards in pattern

---

## Key Takeaways

1. **Prefix sharing is the power**: Tries efficiently store words with common prefixes.

2. **Prune early**: In grid searches, use the Trie to avoid exploring paths that cannot form any word.

3. **Handle wildcards with backtracking**: '.' requires exploring all possibilities at that position.

4. **Clean up after yourself**: Remove found words or prune empty branches to optimize repeated searches.

5. **Choose the right child structure**: Dictionaries for flexibility, arrays for speed with fixed alphabets.
