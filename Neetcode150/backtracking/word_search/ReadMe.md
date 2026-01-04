# Word Search

## Summary

Given an m x n grid of characters and a string word, return true if word exists in the grid. Words can be constructed from adjacent cells (horizontal or vertical), and the same cell cannot be used twice.

### Key Points
- DFS from each cell that matches first character
- Mark cells as visited during search
- Restore cells after backtracking

### Optimal Approach
DFS with in-place marking to track visited cells.

```python
def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(row, col, index):
        if index == len(word):
            return True

        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False

        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'

        # Explore neighbors
        found = (dfs(row + 1, col, index + 1) or
                 dfs(row - 1, col, index + 1) or
                 dfs(row, col + 1, index + 1) or
                 dfs(row, col - 1, index + 1))

        # Restore
        board[row][col] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False
```

### Complexity
- Time: O(m * n * 4^L) where L is word length
- Space: O(L) for recursion depth

---

## Detailed Explanation

### Problem Analysis

This is a classic backtracking problem on a grid. For each starting cell, we try to build the word by exploring adjacent cells. We must track which cells are used in the current path.

### Why Mark In-Place?

Instead of maintaining a separate visited set, we modify the board temporarily:
```python
board[row][col] = '#'  # Mark
# ... explore ...
board[row][col] = temp  # Restore
```

This saves space and is a common grid backtracking technique.

### Optimization: Early Termination

Check character frequency before searching:

```python
def exist(board: list[list[str]], word: str) -> bool:
    from collections import Counter

    # Count characters in board
    board_count = Counter()
    for row in board:
        board_count.update(row)

    # Check if board has enough characters
    word_count = Counter(word)
    for char, count in word_count.items():
        if board_count[char] < count:
            return False

    # Optimization: start from rarer end
    if board_count[word[0]] > board_count[word[-1]]:
        word = word[::-1]

    # ... proceed with DFS ...
```

### Step-by-Step Example

Board:
```
A B C E
S F C S
A D E E
```
Word: "ABCCED"

```
Start at (0,0)='A', matches word[0]
  Mark (0,0), try neighbors
  (0,1)='B' matches word[1]
    Mark (0,1), try neighbors
    (0,2)='C' matches word[2]
      Mark (0,2), try neighbors
      (1,2)='C' matches word[3]
        Mark (1,2), try neighbors
        (2,2)='E' matches word[4]
          Mark (2,2), try neighbors
          (2,1)='D' matches word[5]
            index=6 == len(word), return True!
```

### Visited Set Alternative

Using explicit visited set (cleaner but uses more space):

```python
def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(row, col, index, visited):
        if index == len(word):
            return True

        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            (row, col) in visited or
            board[row][col] != word[index]):
            return False

        visited.add((row, col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if dfs(row + dr, col + dc, index + 1, visited):
                return True

        visited.remove((row, col))
        return False

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0, set()):
                return True

    return False
```

### Edge Cases
- Single cell board: check if it equals word
- Word longer than grid size: impossible
- All same characters: need enough cells

### Related Problems
- Word Search II: find multiple words (use Trie)
- Unique Paths: grid traversal without backtracking
- Surrounded Regions: grid DFS/BFS
