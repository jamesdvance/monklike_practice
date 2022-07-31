"""
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the 
island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal 
to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Rephrase: navigate from m x n
"""
from collections import deque
from typing import List
class Solution:
    " BFS Solution"
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(q):
            reachable = set()
            while q:
                (row,col) = q.popleft()
                reachable.add((row,col))
                for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_row, new_col = row+x,col+y 
                    if new_row<0 or new_row >=len(grid) \
                        or new_col<0 or new_col >= len(grid[0]):
                        continue 
                    
                    if grid[new_row][new_col] < grid[row][col]:
                        continue 
                    
                    q.append((new_row,new_col))

            return reachable
            
    
        atlantic_q = deque()
        pacific_q = deque()
        for i in range(len(grid)):
            pacific_q.append((i,0))
            atlantic_q.append((i,len(grid[0])-1))                

        for i in range(len(grid[0])):
            pacific_q.append((0,i))
            atlantic_q.append((len(grid)-1,i))

        pacific_reachable = bfs(pacific_q)
        atlantic_reachable = bfs(atlantic_q)

        return list(pacific_reachable.intersection(atlantic_reachable))
