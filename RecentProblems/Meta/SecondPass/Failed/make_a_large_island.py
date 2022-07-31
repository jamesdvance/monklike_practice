# 1. Larget island =  sum of all largested connected section of 1's 
# 2. Brute force is straightforward: BFS from each cell in the grid. Keep a running sum until they run out of ones visited
# 3. Compare sum to max sum once it returns
# 4. To optimize, we need a way to keeptrackof the exising island

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def bfs(r,c):
            tot =0
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=r+dr
                nc=c+dc 
                grid[dr][dc]

            return tot +1 

        visited = set()


