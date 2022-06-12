"""
Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Rephrase: Given the definition of an island being connected ones, in the matrix, return the maximum number of connected ones

Examples: 

Datastructures: 
Will use a recursive stack for depth first search
Need a set to determine if visited
Will need a counter for max area and current area

Outline: 

Start at 0,0. Look at each of its connected vertices (always 4)
if a. exists, b. is 1, and c. hasn't been visited, perform dfs on it

During each dfs:
increment current area
Iterate across edges
return sum of total edges from its area

Will want to traverse all nodes in the matrix, 

[[0,1,0,0],
[1,1,0,0],
[0,0,1,1]] -> 3

from 0..2 
	from 0..3
0,1

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    	visited = set()
    	max_area =0
    	
    	def dfs(x:int,y:int, cur_area:int)->int:
    		visited.add((x,y))

    		for next_x, next_y in ((0,-1),(0,1),(1,0),(-1,0)):
    			if next_x + x >=0 and next_x+x <len(grid)\
    				and next_y+y >=0 and next_y + y < len(grid[0])\
    				and (next_x+x, next_y+y) not in visited \
    				and grid[next_x+x][next_y+y] ==1:
    				cur_area = dfs(next_x+x, next_y+y, cur_area+1)

    		return cur_area


    	for x in range(len(grid)):
    		for y in range(len(grid[0])):
    			if (x,y) not in visited and grid[x][y] ==1:
    				max_area = max(max_area, dfs(x,y,1))

    			visited.add((x,y))

    	return max_area

 