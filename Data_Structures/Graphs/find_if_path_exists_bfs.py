"""
Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is 
labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges,
 where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
 Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to 
destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Rephrase: find if a single path exists using bfs. As soon as the path is confirmed, return true

psuedo:

create a set to hold visited vertices

Create an adjacency list

add nodes into the queue. 
Find node in adjacency list, add first neighbor into queue
pop next node. add first neighbor into queue. 

[[0,1],[0,2],[3,5],[5,4],[4,3]]

adj_list = [[1,2], [0],[0],[5,4],[5,3],[4,3]]

queue= [0]
node = 0
seen = ()
queue= [1,2]
seen = (0)
node = 1
queue = [2]



"""

class Solution:
	def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

		# adj_list = [[]]*n VULNERABLE TO SHALLOW COPY
		# adj_list = [[] for _ in range(n)] # this would not be vulnerable to shallow copy
		adj_dict = defaultdict(list)

		for n1, n2 in edges:
			adj_dict[n1].append(n2)
			adj_dict[n2].append(n1)

		queue = [source] # always at least one vertice
		seen = set()
		while queue:
			node = queue.pop(0)
			if node == destination:
				return True

			if node not in seen:
				for next_node in adj_dict[node]:
					if next_node == destination:
						return True
					elif next_node not in seen:
						queue.append(next_node)

				seen.add(node)


		return False

"""
Leetcode Solution

"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
    	adjacency_list = [[] or _ in range(n)]
    	for a,b in edges:
    		adjacency_list[a].append(b)
    		adjacency_list[b].append(a)

    	queue = collections.deque([start])
    	seen = set([start])

    	while queue:
    		node = queue.popleft()

    		if node == end:
    			return True 

    		for neighbor in adjacency_list[node]:
    			if neighbor not in seen:
    				seen.add(neighbor)
    				queue.append(neighbor)

    	return False