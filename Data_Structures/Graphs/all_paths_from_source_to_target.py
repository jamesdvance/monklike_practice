"""
All Paths From Source to Target
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all 
possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from 
node i (i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]. It acts as a dictionary, where graph[i] holds all the paths you can traverse at i
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

1. Rephrase: With a directed graph with no cycles, find all paths, period
2. Inpts: List of integer lists. OUtputs: List of integer lists
3. data structures: 
* Stack holding lists of existing paths. When the path cannot go further, it is added to the output list
* dictionary holding True/False value of visited for each node. Although its acyclic so may not be as important
4. Edge cases and examples: 
Only one edge
5. Pseudo
Will use depth first search 

initialize stack by enumerating paths from 0
enter while loop
pop last path from stack
visit last item in stack via index
enumerate paths from current stack, by appending a list and adding to the stack
pop last item and continue until reaching an empty list. Then add to paths output list


edge cases:
[[4,3,1],[3,2,4],[3],[4],[]]
paths_stack = [[0,4],[0,3],[0,1]]
path = [0,1]
i = 1
paths_stack = [[0,4],[0,3],[0,1,3],[0,1,2],[0,1,3]]
path = [0,1,3]
i = 3
paths_stack = [[0,4],[0,3],[0,1,3],[0,1,2],[0,1,3,4]]
path = [0,1,3,4]
i=4
paths_list = [0,1,3,4]
paths_stack = [[0,4],[0,3],[0,1,3],[0,1,2]]
path = [0,1,2]
i =2
paths_stack = [[0,4],[0,3],[0,1,3],[0,1,2,3]]
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        paths_stack = []
        paths_list = []

        for endpt in graph[0]:
            paths_stack.append([0,endpt])

        while paths_stack:
            path = paths_stack.pop()
            i = path[-1] # last node 
            if i == len(graph)-1:
                paths_list.append(path)
            elif len(graph[i])>0:
                for endpt in graph[i]:
                    paths_stack.append(path+[endpt])

        return paths_list

"""
Leetcode solution (recursive)
* doesn't keep a stack of existing paths, uses recursion
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)
            if node == len(graph)-1:
                paths.append(path.copy())
                return

            next_nodes = graph[node] 
            for next_node in next_nodes:
                dfs(next_node)
                path.pop() # path has exhausted all nodes from this node

        paths = []
        path = []
        if not graph or len(graph) ==0:
            return paths 
        dfs(0)
        return paths