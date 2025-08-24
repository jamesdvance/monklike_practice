
"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

"""


class Solution(object):
    """
    First blind attempt. Does not fully solve the problem. DFS is also too complicated 
    Had a first impulse to cache the rows and cols separately. Should have stuck with that as it allows a simple 2 (M x N) solution
    
    """

    def __init__(self):
        self.cache = set([])
        self.x_len =0
        self.y_len =0 

    def get_cross(self, x,y):
        x_list = [(new_x, y) for new_x in list(range(0,x))+list(range(x+1, self.x_len)) \
                if (new_x, y) not in self.cache and new_x < self.x_len]
        y_list = [(x, new_y) for new_y in list(range(0,y)) + list(range(y+1, self.y_len)) \
                if (x, new_y) not in self.cache and new_y < self.y_len]
        return x_list + y_list
    
    def set_zero(self, curr, indices_list, matrix):
        if curr in self.cache:
            return 

        # if curr[0] >= self.x_len or curr[1] >= self.y_len:
        #     print(f"exception found {curr[0]}, {curr[1]}")

        try:
            if matrix[curr[1]][curr[0]] == 0:
                indices_list.extend(self.get_cross(curr[0], curr[1]))
        except Exception as e:
            print(f"ISsue with indices {curr} and list {indices_list} and matrix {matrix}")
            raise e
            
        else:
            matrix[curr[1]][curr[0]] = 0

        self.cache.add(curr)
        for indices in indices_list:
            self.set_zero(indices, [], matrix)

        return

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #Separate cache for row and col 

        # Iterate over each cell. Only check cell if not already in cache. 

        # If zeros find, go update cells, and add entire rows and cols to cache

        # in the update step of the zeros, if the cell is a zero before we flip it, do the same from its position
        

        return


def test_set_zeros():
    sol = Solution()
    sol.x_len = 10
    sol.y_len = 10
    cross_2_3 = sol.get_cross(2,3)
    matrix  = [[1 for _ in range(10)] for _ in range(10)]
    assert len(cross_2_3) == 18
    assert (2,3) not in cross_2_3
    for curr in cross_2_3:
        assert matrix[curr[0]][curr[1]] == 1, f"Check matrix {matrix}"
    first = cross_2_3[0]
    assert matrix[first[0]][first[1]] == 0, f"Test Failed at point {first} in matrix {matrix}"
    Solution().set_zero(first, cross_2_3[1:], matrix)
    for curr in cross_2_3:
        assert matrix[curr[0]][curr[1]] == 0, f"Test Failed at point {first} in matrix {matrix}"
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0,0,0,0], [0,4,5,0], [0,3,1,0]]


"""

Actual solution
"""

class SolutionBest:

    def setZeroes(self, matrix):
        
        R = len(matrix)
        C = len(matrix[0])

        row_zeros = set([])
        col_zeros = set([])

        for row in range(R):
            for col in range(C):
                if matrix[row][col] == 0:
                    row_zeros.add(row)
                    col_zeros.add(col)
        
        for row in range(R):
            for col in range(C):
                if row in row_zeros or col in col_zeros:
                    matrix[row][col] = 0


        return matrix # do not do in actual problem
    
def test_set_zeros_best():
    
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    new_matrix = SolutionBest().setZeroes(matrix)

    assert matrix == [[0,0,0,0], [0,4,5,0], [0,3,1,0]]

test_set_zeros_best()




    
