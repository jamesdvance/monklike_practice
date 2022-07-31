# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows,cols = binaryMatrix.dimensions()
        r, c = 0, cols-1

        last =0
        while r <rows and c >0:
            if binaryMatrix.get(r,c)  ==0:
                r+=1
            else:
                c-=1
            
        if c ==0 and binaryMatrix.get(r,c)==1:
            return 0 

        return c+1 if c < cols-1 else -1






                
