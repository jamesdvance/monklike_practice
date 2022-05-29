"""
Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge 
between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, 
or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

Notes: 
Since we aren't worried about enumerating all paths, don't need to unmark 'seen'


Pseudo:
find source node. 
Add all nodes from source node into stack. Don't need to add edges, because this is bidirectional and we just want to know if any path exists
add node into seen set 
if node not end

10
[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
7
5

stack1 = [[0,7],[0,8],[2,0],[0,4]]
[0,4]
seen = (0)
stack2 = [[0,7],[0,8],[2,0],[4,7]]
[4,7]
seen = (0,4,7)
stack3 = [[0,7],[0,8],[2,0]
[2,0]
seen = (0,4,7,2,)
stack4 = [[0,7],[0,8]]
[0,8]
seen = (0,4,2,8)

"""
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # if the edge starts with the source, will start there. So, will cycle through edges until source is found, then cycle through
        # edges from their until no more source
        # find all edges from node
        # TAKES TOO LONG TO FINISH FOR LC. Because it requires finding each node's edges each time
        # The neighbors dict (neighbors = defaultdict(list)) solves this in solution below

        seen = set([source])
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        
        nodes_stack = [source]
        while len(nodes_stack) > 0:
            node = nodes_stack.pop()
            if node == destination:
                return True
            if node not in seen:
                nodes_stack+=neighbors[node]
                seen.add(node)

        return False
                
"""
DFS Recursive
"""


"""
DFS Recursive
"""
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        neighbors = defaultdict(list) # dictionary initialized with empty list as default
        for n1, n2 in edges:
            # bi-directional graph
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        def dfs(node, end,seen):
            if node == end:
                return True 
            if node in seen:
                return False

            seen.add(node)
            for n in neighbors[node]:
                if dfs(n,end,seen):
                    return True 

            return False 

        seen = set()
        return dfs(source,destination, seen)

"""
Leetcode Official Solution

Uses adjacency list
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        adjacency_list = [[] for  _ in range(n)] 
        for a,b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        stack = [start]
        seen = set()

        while stack:
            node = stack.pop()
            if node==end:
                return True

            if node in seen:
                continue 

            seen.add(node)

            for neighbor in adjacency_list[node]:
                stack.append(neighbor)

        return False