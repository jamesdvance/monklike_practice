# Alien Dictionary

## Summary

Given a sorted list of words in an alien language, derive the order of letters in that language. Return the letters in topological order. If no valid order exists, return empty string.

### Key Points
- Compare adjacent words to find ordering constraints
- Build a directed graph of letter precedences
- Use topological sort to find the order

### Optimal Approach
Build graph from word comparisons, then topological sort.

```python
from collections import defaultdict, deque

def alienOrder(words: list[str]) -> str:
    # Build adjacency list and track all letters
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        # Invalid case: prefix comes after longer word
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    # Topological sort using BFS
    queue = deque([c for c in indegree if indegree[c] == 0])
    result = []

    while queue:
        c = queue.popleft()
        result.append(c)

        for neighbor in graph[c]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(indegree):
        return ""  # Cycle detected

    return "".join(result)
```

### Complexity
- Time: O(C) where C is total characters in all words
- Space: O(1) since alphabet is fixed size (26 or less)

---

## Detailed Explanation

### Problem Analysis

From a sorted list of words, we can derive ordering constraints:
- Compare adjacent words
- Find first differing character
- That gives us: char1 comes before char2

Then we find an order consistent with all constraints (topological sort).

### Why Compare Adjacent Words Only?

If words are sorted: w1 < w2 < w3

Then w1 < w2 and w2 < w3 implies w1 < w3 (transitivity).

We only need adjacent comparisons to capture all constraints.

### Step-by-Step Example

```
words = ["wrt", "wrf", "er", "ett", "rftt"]

Compare adjacent pairs:
"wrt" vs "wrf": t < f
"wrf" vs "er": w < e
"er" vs "ett": r < t
"ett" vs "rftt": e < r

Graph:
t -> f
w -> e
r -> t
e -> r

Edges: t->f, w->e, r->t, e->r
Indegree: w=0, e=1, r=1, t=1, f=1

Topological sort:
Start with indegree 0: w
Remove w, e's indegree -> 0
Remove e, r's indegree -> 0
Remove r, t's indegree -> 0
Remove t, f's indegree -> 0
Remove f

Result: "wertf"
```

### Invalid Cases

1. **Prefix contradiction**: "abc" before "ab" is invalid (longer word with same prefix should come after)

2. **Cycle**: Contradictory orderings create a cycle
   - "a" before "b" and "b" before "a"

### DFS Topological Sort Alternative

```python
def alienOrder(words: list[str]) -> str:
    graph = defaultdict(set)
    all_chars = set(c for word in words for c in word)

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break

    # 0=unvisited, 1=visiting, 2=visited
    state = {c: 0 for c in all_chars}
    result = []

    def dfs(c):
        if state[c] == 1:
            return False  # Cycle
        if state[c] == 2:
            return True

        state[c] = 1
        for neighbor in graph[c]:
            if not dfs(neighbor):
                return False

        state[c] = 2
        result.append(c)
        return True

    for c in all_chars:
        if not dfs(c):
            return ""

    return "".join(reversed(result))
```

### Edge Cases
- Single word: return characters in any order
- All same character: return that character
- Two words, one prefix of other: "ab" before "a" is invalid
- No ordering constraints possible: any order of unique chars is valid

### Related Problems
- Course Schedule II: basic topological sort
- Sequence Reconstruction: verify unique topological order
- Sort Items by Groups Respecting Dependencies: multi-level topological sort
