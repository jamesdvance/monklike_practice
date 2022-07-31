"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.


Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Hint: Is mathematical

start: 12:55
by: 1:25

Rephrase: rotate the matrix. This means all the 0'th values along axis 0 of the new matrix will form the 0'th values of axis 1

Since it will be rotated inplace, will need to swap
Can only swap two at a  time

Will need to calculate a compliment, and no when to stop so we don't touch already swapped items
To keep track of the compliment, can use a pointer to the max i,j that was swapped, as well as the current k,l

Swap pattern:
The first swap for position 0,0 would be to position 0,n-1
Second swap for position 0,1 would be to position 1, n-1
swap for position 1,1 would be 1, n-1-1
swap for position 1,2 would be 2, n-1-1

swap for position i,j would be position j, n-1-i

stopping criteria:
already swapped would start at 0, n-1 for the first row
for the second row would be 1, n-1-1

so for kth row would start at k, n-1-k

for the last row, n-1,0 would not need to be swapped

Examples
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:
for i in range(3-1=2):
    for j in range(3-0)
i = 0, j=0
output = [[3,2,1],[4,5,6],[7,8,9]] 1
i= 0 j=1 -> 1,3-1-0 =2
output = [[3,6,1],[4,5,2],[7,8,9]]
Found a bug. The 6 needs to move forward
Current iteration, doesn't move it forward.
Will keep iterating 
i= 1 j=0 -> 0,n-1-1 -> 0,1
output = [[3,4,1],[6,5,2],[7,8,9]]
i = 1 j =1, -> 1, 1
output = [[3,4,1],[6,5,2],[7,8,9]]
i = 2 j =1, -> 1, 1
output = [[3,4,1],[6,5,2],[7,8,9]]

Swaps needed:
swaps needed (2,0) -> 0,0
[[7,4,1],[8,5,2],[3,6,9]]
swaps needed (2,1) -> 1,0
[[7,4,1],[8,5,2],[3,6,9]]
swaps needed: (2,2) -> 2,0
[[7,4,1],[8,5,2],[9,6,3]]

Example 2

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
i1 [[11,10,7,5],[2,4,8,1],[13,3,6,9],[15,14,12,16]]
k = 4-1-1 = 2
(1,0),(1,1) -> (2,0), (2,1)
i2 [[11,10,7,5],[13,3,8,1],[2,4,6,9],[15,14,12,16]]
(2,0) -> (0,1)
i3 [[11,2,7,5],[13,3,8,1],[10,4,6,9],[15,14,12,16]]
(2,0),(2,1),(2,2),(2,3) -> (0,0)(1,0)(2,0)(3,0) 

14 [[15,2,7,5],[14,3,8,1],[12,4,6,9],[16,13,10,11]]

BELOW ATTEMPT DOES NOT WORK
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        O(NLogN) Time 
        Constant space
        """
        m = len(matrix)
        for i in range(m-1):# don't need to iterate last row
            for j in range(m-1-i):
                matrix[i][j], matrix[j][m-1-i] = matrix[j][m-1-i], matrix[i][j]

        for i  in range(m):
            matrix[m-1][i], matrix[i][m-1-2] = matrix[i][m-1-2], matrix[m-1][i]

# Finished coding 1:11 
# Solution above is done at 1:34

"""
Leetcode solution 1: Rotate Groups of Four Cells

Uses a similar index matching as above but moves 4 

next_rot mapping
j -> n-1-i
i -> n-1-j
n-1-j->j
n-1-i->i

(x,y) -> (next_rot,x)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        for i in range(n//2+n%2): # only need to traverse over n/2, round up
            for j in range(n//2): # only need to traverse down n/2, round down
                tmp = matrix[n-1-j][i] # save value of first to be rotated into. This is the location of the rotation for [i,j]
                # this is the rotation 
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = tmp

"""
Leetcode Solution 2: Reverse on Diagonal and then Reverse Left to Right
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]