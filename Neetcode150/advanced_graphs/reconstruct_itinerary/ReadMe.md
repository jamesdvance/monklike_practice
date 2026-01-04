# Reconstruct Itinerary

## Summary

Given a list of airline tickets represented as [from, to] pairs, reconstruct the itinerary starting from "JFK". Use all tickets exactly once. If multiple valid itineraries exist, return the one with the smallest lexical order.

### Key Points
- This is finding an Eulerian path (visit every edge exactly once)
- Use Hierholzer's algorithm with DFS
- Process destinations in lexical order for smallest result

### Optimal Approach
Use DFS with a stack, processing destinations in reverse lexical order.

```python
from collections import defaultdict

def findItinerary(tickets: list[list[str]]) -> list[str]:
    graph = defaultdict(list)

    # Build graph with destinations sorted in reverse order
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    route = []

    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)

    dfs("JFK")
    return route[::-1]
```

### Complexity
- Time: O(E log E) where E is number of tickets (for sorting)
- Space: O(E) for the graph and recursion

---

## Detailed Explanation

### Problem Analysis

This is an Eulerian path problem:
- Every ticket is an edge
- We must use every edge exactly once
- Start from JFK

An Eulerian path exists if and only if:
- At most one vertex has outdegree - indegree = 1 (start)
- At most one vertex has indegree - outdegree = 1 (end)
- All other vertices have equal in/out degree

The problem guarantees a valid itinerary exists.

### Hierholzer's Algorithm

1. Start DFS from source
2. Greedily follow edges, removing them as we go
3. When stuck (no more edges), add current node to result
4. Backtrack and continue
5. Reverse the result

### Why Reverse Lexical Sort?

We want smallest lexical order. By sorting destinations in reverse and using `pop()`, we process them in correct lexical order. The final result is reversed, giving us the correct path.

### Step-by-Step Example

```
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

Graph (after reverse sort):
JFK -> [SFO, ATL]  (pop gives ATL first)
SFO -> [ATL]
ATL -> [SFO, JFK]

DFS from JFK:
- Visit JFK, pop ATL
- Visit ATL, pop JFK
- Visit JFK, pop SFO
- Visit SFO, pop ATL
- Visit ATL, pop SFO
- Visit SFO, no edges, add to route: [SFO]
- Back to ATL, no edges, add: [SFO, ATL]
- Back to SFO, no edges, add: [SFO, ATL, SFO]
- Back to JFK, no edges, add: [SFO, ATL, SFO, JFK]
- Back to ATL, no edges, add: [SFO, ATL, SFO, JFK, ATL]
- Back to JFK, no edges, add: [SFO, ATL, SFO, JFK, ATL, JFK]

Reverse: [JFK, ATL, JFK, SFO, ATL, SFO]
```

### Iterative Version

```python
from collections import defaultdict

def findItinerary(tickets: list[list[str]]) -> list[str]:
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    stack = ["JFK"]
    route = []

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        route.append(stack.pop())

    return route[::-1]
```

### Why This Works

The algorithm builds the path in reverse:
1. We keep going forward until we're stuck
2. When stuck, we've reached a dead end - add to result
3. Backtrack to find unexplored edges
4. The result is built from end to start, so we reverse

### Edge Cases
- Single ticket: ["JFK", destination]
- All from same airport: follow lexical order
- Complex graph with multiple valid paths: algorithm finds lexically smallest

### Related Problems
- Valid Arrangement of Pairs: similar Eulerian path
- Cracking the Safe: Eulerian path on de Bruijn graph
- Course Schedule II: topological ordering
