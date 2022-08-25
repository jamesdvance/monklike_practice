"""
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
 

"""

class TicTacToe:

    def __init__(self, n: int):
    	self.rows = [0]*n
    	self.cols = [0]*n 
    	self.player_val ={1:-1, 2:1}
    	self.diag =0
    	self.antidiag =0 
    	self.n=n 
        

    def move(self, row: int, col: int, player: int) -> int:
    	n=self.n
    	val = self.player_val[player]
    	self.rows[row] +=val 
    	self.cols[col] +=val
    	if row ==col:
    		self.diag+=val 
    	if col == n -row-1:
    		self.antidiag+=val 

    	if abs(self.rows[row] ) ==n \
    		or abs(self.cols[col]) ==n \
    		or abs(self.diag) ==n \
    		or abs(self.antidiag) ==n:
    		return player
    	else:
    		return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)