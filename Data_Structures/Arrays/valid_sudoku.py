"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

"""
Testcase
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

row_offset =0 col_offset= 0
for i in range(3)
for j in range(3)

[0,0]
[0,1]
[0,2]
[1,0]
[1,1]
[1,2]
[2,0]
[2,1]
[2,2]

row_offset =0, col_offset = 1
[0,3]
[0,4]
[0,5]
[1,3]
[1,4]
[1,5]
[2,3]
[2,4]
[2,5]

row_offset = 2, col_offset = 2
[6,6]
[6,7]
[6,8]
[7,6]
[7,7]
[7,8]
[8,3]
[8,4]
[8,5]
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_val = defaultdict(lambda: dict(zip(list(range(1,10)),[0]*9)))
        col_val = defaultdict(lambda: dict(zip(list(range(1,10)),[0]*9)))
        for row_offset in range(3):
            for col_offset in range(3):
                num_ctr = dict(zip(list(range(1,10)),[0]*9))
                for row in range(3):
                    row+=3*row_offset
                    for col in range(3):
                        col+=3*col_offset
                        #print(f"row {row}, col {col}")
                        cell_val = board[row][col]
                        if cell_val != ".":
                            cell_val_int = int(cell_val)
                            num_ctr[cell_val_int] += 1
                            row_val[row][cell_val_int] +=1
                            col_val[col][cell_val_int] +=1
                            if num_ctr[cell_val_int] > 1 \
                                or row_val[row][cell_val_int] > 1\
                                or col_val[col][cell_val_int] >1:
                                   return False
                               