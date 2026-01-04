# Word Search II

## Summary

Given an m x n board of characters and a list of words, return all words that can be found on the board. Each word must be constructed from adjacent cells (horizontal or vertical), and the same cell cannot be used twice per word.

### Key Points
- Build a Trie from the word list for efficient prefix checking
- DFS from each cell, using Trie to prune invalid paths
- Remove found words from Trie to avoid duplicates

### Optimal Approach
Build Trie from words, DFS on board with Trie-guided pruning.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        # Build trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        result = []
        rows, cols = len(board), len(board[0])

        def dfs(row, col, node):
            char = board[row][col]

            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            # Mark as visited
            board[row][col] = '#'

            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if board[new_row][new_col] != '#':
                        dfs(new_row, new_col, next_node)

            # Restore
            board[row][col] = char

            # Prune trie (optimization)
            if not next_node.children:
                del node.children[char]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return result
```

### Complexity
- Time: O(m * n * 4^L) where L is max word length
- Space: O(W * L) for Trie where W is number of words

---

## Detailed Explanation

### Problem Analysis

The naive approach would search for each word independently using DFS, giving O(W * m * n * 4^L). By building a Trie first, we can search for all words simultaneously, pruning paths that do not match any word prefix.

### Why Trie Helps

Without Trie: For each cell, for each word, check if word can be formed.
With Trie: For each cell, follow the Trie to check all words with matching prefix.

The Trie prunes the search space by telling us immediately when the current path cannot lead to any word.

### Storing Complete Words

Instead of just marking is_end, we store the actual word at the end node:
```python
node.word = word
```

This simplifies collecting results without reconstructing the path.

### Avoiding Duplicates

When we find a word, set `node.word = None` to prevent adding it again.

### Trie Pruning Optimization

After DFS, if a node has no children, we can remove it:
```python
if not next_node.children:
    del node.children[char]
```

This prevents future searches from exploring dead-end paths.

### Step-by-Step Example

Board:
```
o a a n
e t a e
i h k r
i f l v
```
Words: ["oath", "pea", "eat", "rain"]

Build Trie:
```
root -> o -> a -> t -> h (word: "oath")
     -> p -> e -> a (word: "pea")
     -> e -> a -> t (word: "eat")
     -> r -> a -> i -> n (word: "rain")
```

Start DFS at each cell. From (0,0) 'o':
- Follow o -> a (at (0,1))
- Follow a -> t (at (1,1))
- Follow t -> h (at (2,1))
- Found "oath"

Continue from other cells...

Result: ["eat", "oath"]

### Edge Cases
- No words found: return empty list
- All words found: return all words
- Single cell board: check single-character words
- Overlapping words: handled by continuing search after finding a word

### Related Problems
- Word Search: single word version
- Boggle: similar board game problem
- Implement Trie: foundation structure
