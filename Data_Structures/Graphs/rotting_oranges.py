"""
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4


Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Rephrase:
Return number of minutes where all fresh oranges will turn rotten. Return -1 if this will not happen

Thoughts:
Oranges will rot from adjacent to already rotten oranges out
An ideal algo with visit the rotten oranges first and determine if they are next to a fresh orange
Then those oranges get visted, and we start the loop again 
Each pass should calculate 

Data structures:
A queue holding a list of all next-adjacenct oranges makes sense. The first queue would include all already-rotten oranges


Example:
Input: grid = [[1],[2],[1],[2]]
Output: 1

total_fresh =2
q=[(1,0),(3,0)]
visited = (1,0),(3,0))
x= 1, y =0 
y

counter =1

Time: O(2N) = O(N)
Space: O(N)
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

    	# traverse entire grid, adding nodes where rotting oranges exist to a list

    	# Add this list to a queue. Iterate through each rotten orange, adding fresh oranges next to it to another list
    	# if this list is not empty, add to queue and increment counter

    	# return counter

    	rotten = []
    	visited= set()
    	total_fresh = 0
    	for y in range(len(grid)):
    		for x in range(len(grid[0])):
    			if grid[y][x] ==2:
    				rotten.append((y,x))
    				visited.add((y,x))
    			if grid[y][x] ==1:
    				total_fresh +=1
    	
    	counter=0
    	q = deque([rotten]) if len( rotten)>0 else None
    	while q:
    		rotten = q.popleft() 
    		to_rot = []
    		for y,x in rotten:
    			for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
    				y_i = y+i 
    				x_j = x+j 
    				if y_i < 0 or y_i >= len(grid) \
    					or x_j <0 or x_j >= len(grid[0]) \
    					or (y_i,x_j) in visited:
    					continue 

    				if grid[y_i][x_j]==1:
    					to_rot.append((y_i,x_j))
    					total_fresh-=1
    					
    				visited.add((y_i,x_j))

    		if len(to_rot) >0:
    			counter+=1
    			q.append(to_rot)

    	return counter if total_fresh ==0 else -1
