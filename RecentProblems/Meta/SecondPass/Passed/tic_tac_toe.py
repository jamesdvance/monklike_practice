class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.antidiag =0

    def move(self, row: int, col: int, player: int) -> int:
        n=self.n
        if player ==1:
            val =1
        else:
            val =-1

        self.rows[row]+=val
        self.cols[col]+=val
        if row==col:
            self.diag+=val
        if row == (n-col):
            self.antidiag+=val

        if abs(self.rows[row])==n \
            or abs(self.cols[col]) ==n \
            or abs(self.diag) == n \
            or abs(self.antidiag) == n:
            return player

        else:
            return 0       


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)