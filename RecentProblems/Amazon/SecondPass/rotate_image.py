"""
Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Swap 
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # work 4 cells at a time and rotate them
        l, r = 0, len(matrix)-1 
        while l < r:
        	for i in range(r-l):
        		top, bottom = l,r

        		# Save topLeft for later
        		topLeft = matrix[top][l + i]

        		# bottom left-> top left
        		matrix[top][l + i] = matrix[bottom - i][l]

        		# bottom right -> bottom left
        		matrix[bottom - i][l] = matrix[bottom][r - i]

        		# top right -> bottom right
        		matrix[bottom][r - i] = matrix[top + i][r]

        		# top left -> top right
        		matrix[top + i][r] = topLeft


        	r-=1
        	l+=1

