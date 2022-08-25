"""

You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board 
(i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. 
Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, 
you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, 
but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.


Two options: BFS or DFS 

BFS with a queue, DFS - a recursive backtracking function

BFS makes sense to find the shortest path, so 

r-c 
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

    	visited = set([1])
    	n = len(board)

    	flat_board = []
    	for i in range(n-1, -1,-1):
    		cur_row = list(board[i])
    		if i%2==0:
    			cur_row.reverse()
    		flat_board+=cur_row

    	q = deque([(1,0)])
    	n2 = n*n
    	while q:
    		pos, moves = q.popleft()
    		for i in range(1,7):
    			new_pos = pos+i
    			if new_pos == n2:
    				return moves+1 

    			elif new_pos not in visited:
    				visited.add(new_pos)
    				if flat_board[new_pos-1] == -1:
    					q.append((new_pos, moves+1))
    				else:
    					if flat_board[new_pos-1]==n2:
    						return moves+1
    					if flat_board[new_pos-1] not in visited:
	    					visited.add(flat_board[new_pos-1])
	    					q.append((flat_board[new_pos-1], moves+1))

    	return -1 







