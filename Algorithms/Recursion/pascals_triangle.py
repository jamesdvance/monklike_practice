class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        build a list of lists attribute
        to save space, delete the i -2th list
        """
        triangle=[[1]]
        def triangle_builder(triangle, i):
            row = [1]*(i+1)
            for j in range(i+2):# length of a given row is ith row +1
                if j !=0 and j < len(triangle[0]):
                    row[j] = triangle[0][j-1] + triangle[0][j]
                    
            triangle.append(row)
            triangle.pop(0)
            return triangle
        
        i=1
        while i <= rowIndex:
            triangle = triangle_builder(triangle,i)
            i+=1
            
        return triangle[len(triangle)-1]