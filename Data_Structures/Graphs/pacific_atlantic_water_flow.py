"""
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to 
neighboring cells directly north, south, east, and west if the neighboring cell's 
height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Rephrase: Return all vextexes where there is a path of edges to both the 0th X dimension or 0th y dimension and the len(x)-1 
dim or len(y)-1 dim, such that each element along the path is <= its parent element. 
This includes the direction (x+1,y+1), aka diagonal. 

Outputs: Is a list of lists, each inner list, represents a vertex of dimensions x,y which could reach both 'oceans'
Vertexes can be returned in any order

Data structures:
an adjency list could be a good way to determine if a node is connected to to a node that is connected to either border
a visited set should avoid duplication
the final list of vertices should be given all nodes along a connected path to both 'coasts'
the root node of a path to 

DFS - search all nodes that are lower among these edges ((1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0))

stopping criteria, found an edge or can't find any more 

Solution below gives wrong answer
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    	ret_arr = [] 
    	visited = set()
    	# build adjacency list based on greater than or less than paradigm
    	adj_list = {}

    	def dfs(x,y, edges:dict):

    		# Check for stopping criteria
    		if x == 0 or y == 0:
    			edges["pacific"] = True 
    		if x ==len(heights)-1 or y == len(heights[0]) -1:
    			edges["atlantic"] = True
    		
    		for n_x, n_y in ((1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)):
    			new_x, new_y =x+n_x,y+n_y
    			if new_x >= 0 and new_x < len(heights) \
    				and new_y >= 0 and new_y < len(heights[0]) \
    				and (new_x, new_y) not in visited \
    				and heights[new_x][new_y] <= heights[x][y]:
    				edges["edges"].append((new_x,new_y))
    				visited.add((new_x, new_y))
    				edges = dfs(new_x, new_y, edges)

    		return edges

    	for x in range(len(heights)):
    		for y in range(len(heights[0])):
    			if (x,y) not in visited:
    				visited.add((x,y))
    				edges = dfs(x,y, {"pacific":False,"atlantic":False, "edges":[(x,y)]})
    				if edges["pacific"] and edges["atlantic"]:
    					ret_arr += edges["edges"]

    				
    	return ret_arr


"""
Leetcode DFS

1. create sets for pacific_reachable and atlantic_reachable
2. Use DFS to iterate from each point along either atlantic or pacific coast, updating the atlantic_reachable and 
pacific_reachable sets
3. DFS adds node to 'reachable' only if new node's value is greater than or equal to than existing node's value 
3. return the itersection of those two sets
4. If both terminate at a mountain top, I don't understand how the intersection of the sets, returns the entire path
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

"""
Leetcode BFS

1. initialize two queues, for atlantic ocean and for pacific ocean resp. 
2. two sets to track visited for both oceans
3. fill queue's with cells, adjacent to each ocean (termination points for both oceans)
4. Perform BFS from each ocean. Return a set of all nodes that can flow into that ocean
5. Return the intersection of that set 
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: