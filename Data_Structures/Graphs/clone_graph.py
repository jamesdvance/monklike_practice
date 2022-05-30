"""
Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


Rephrase: Create a clone of an existing UNDIRECTED graph and return one of the nodes

Inputs: A single node. Output, a single node

Edge cases: A null node; a node with no neighbors. A graph with cycles

Data structures: 
* Queue for breadth-first search.Holds all current neighbors to traverse
* Set containing seen nodes, since these nodes are connected. May not be necessary 
* A new graph. The new graph will likely be traversed and modified during the process
* A dictionary containing all of the new nodes and their neighbors

Pseudo:

First, create a stack and set
Add node to stack
Next, initialize a new node, with value same as given node, and empty list of neighbors
As neighbors are added to new node, add original neighbors to queue
finally, add node to seen set

now, pop first neighbor node out of queue
check a dictionary for is value. If it is seen, pull the node from the dictionary
create a new node, and add it to the new node's neighbors list
assign it as new node (shallow copy)


"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
    	if not node:
    		return

    	nodes_dict = {node.val:Node(val=node.val, [])}
    	nodes_queue = deque([node])

    	while nodes_queue:
    		n = nodes_queue.popleft()

    		for neighbor in n.neighbors:
	    		if neighbor.val not in nodes_dict:
	    			nodes_dict[neighbor.val]=Node(val=neighbor.val, [])
	    			nodes_queue.append(neighbor)
	    			
	    		nodes_dict[n.val].neighbors.append(nodes_dict[neighbor.val])

    	return nodes_dict[node.val]

"""
Depth-first search

[[2,4],[1,3],[2,4],[1,3]]

rec_stack = [2,4]
new_node.neighbors = 2
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
    	nodes = {}

    	def dfs(node:'Node')->'Node':
    		"Takes an old node and returns a clone"
    		if not node:
    			return

    		new_node = Node(val=node.val)
    		nodes[node.val] = new_node
    		if node.neighbors:
    			new_node.neighbors = []
    			for neighbor in node.neighbors:
    				if neighbor.val in nodes:
    					neighbor_node = nodes[neighbor.val]
    				else:
    					neighbor_node = dfs(neighbor)
    					nodes[neighbor.val] = neighbor_node

    				new_node.neighbors.append(neighbor_node)

    		return new_node

    	return dfs(node)

"""
Leetcode DFS Solution
"""
class Solution:
    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
    	if not node:
    		return node 

    	if node in self.visited:
    		return self.visited[node]

    	clone_node = Node(node.val,[])
    	self.visited[node] = clone_node

    	if node.neighbors:
    		clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

    	return clone_node

"""
Leetcode BFS solution
"""
from collections import deque
class Solution(object):

    def cloneGraph(self, node):

    	if not node:
    		return node 

    	visited = {}

    	queue = deque([node])
    	visited[node] = Node(node.val, [])

    	while queue:
    		n = queue.popleft()

    		for neighbor in n.neighbors:
    			if neighbor not in visited:
	    			visited[neighbor] = Node(neighbor.val, [])
	    			queue.append(neighbor)
	    		visted[n].neighbors.append(visited[neighbor])

	   return visited[node]