# Word Ladder

## Summary

Given a beginWord, endWord, and a word list, find the length of the shortest transformation sequence from beginWord to endWord, where each step changes exactly one letter and each intermediate word must be in the word list.

### Key Points
- Model as a graph: words are nodes, single-letter changes are edges
- Use BFS for shortest path in unweighted graph
- Pattern matching with wildcards for efficient neighbor finding

### Optimal Approach
Use BFS with wildcard pattern preprocessing.

```python
from collections import defaultdict, deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList:
        return 0

    # Build pattern -> words mapping
    word_len = len(beginWord)
    patterns = defaultdict(list)

    for word in wordList:
        for i in range(word_len):
            pattern = word[:i] + '*' + word[i+1:]
            patterns[pattern].append(word)

    # BFS
    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()

        for i in range(word_len):
            pattern = word[:i] + '*' + word[i+1:]

            for neighbor in patterns[pattern]:
                if neighbor == endWord:
                    return length + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, length + 1))

            patterns[pattern] = []  # Avoid revisiting

    return 0
```

### Complexity
- Time: O(M^2 * N) where M is word length and N is word list size
- Space: O(M^2 * N) for the pattern mapping

---

## Detailed Explanation

### Problem Analysis

This is a shortest path problem in an implicit graph:
- Nodes: words in the word list (plus beginWord)
- Edges: words that differ by exactly one letter
- Goal: shortest path from beginWord to endWord

BFS guarantees the shortest path in an unweighted graph.

### Why Pattern Matching?

Naive approach: for each word, compare with all other words to find neighbors - O(N * M) per word.

Pattern approach: precompute patterns like "h*t" -> ["hot", "hat", "hit"]. Finding neighbors is O(M) patterns * O(1) lookup.

### Step-by-Step Example

```
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

Patterns:
*ot -> [hot, dot, lot]
h*t -> [hot]
ho* -> [hot]
d*t -> [dot]
do* -> [dot, dog]
*og -> [dog, log, cog]
...

BFS:
Start: "hit", length = 1

Level 1: "hit"
  Neighbors via *it, h*t, hi*: "hot"
  Queue: [("hot", 2)]

Level 2: "hot"
  Neighbors via *ot: "dot", "lot"
  Queue: [("dot", 3), ("lot", 3)]

Level 3: "dot"
  Neighbors: "dog"
  Queue: [("lot", 3), ("dog", 4)]

Level 3: "lot"
  Neighbors: "log"
  Queue: [("dog", 4), ("log", 4)]

Level 4: "dog"
  Neighbors via *og: "cog" - FOUND!
  Return 5
```

### Bidirectional BFS (Optimization)

Search from both ends simultaneously, meeting in the middle.

```python
from collections import defaultdict

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList:
        return 0

    word_len = len(beginWord)
    word_set = set(wordList)

    front = {beginWord}
    back = {endWord}
    visited = set()
    length = 1

    while front and back:
        # Always expand the smaller set
        if len(front) > len(back):
            front, back = back, front

        next_front = set()
        for word in front:
            for i in range(word_len):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]

                    if new_word in back:
                        return length + 1

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        next_front.add(new_word)

        front = next_front
        length += 1

    return 0
```

Bidirectional BFS reduces time from O(b^d) to O(b^(d/2)) where b is branching factor and d is depth.

### Direct Neighbor Generation

Instead of pattern preprocessing, generate all possible neighbors:

```python
def get_neighbors(word, word_set):
    neighbors = []
    for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c != word[i]:
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    neighbors.append(new_word)
    return neighbors
```

This is O(26 * M) per word, efficient when word list is large.

### Edge Cases
- endWord not in wordList: return 0
- beginWord equals endWord: edge case (usually return 1 or 0)
- No transformation possible: return 0

### Related Problems
- Word Ladder II: find all shortest paths
- Minimum Genetic Mutation: same problem with genes
- Open the Lock: similar BFS with state transitions
