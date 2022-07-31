"""
BFS From all empty land

"""
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        ret_sum =0
        houses_count = 0

        # BFS
        for i in range(j)
        q = deque()
        



"""
BFS From All Houses to Empty Land (Optimized)
"""

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]

        total_sum = [[0]*cols for _ in range(rows)]

        def bfs():str