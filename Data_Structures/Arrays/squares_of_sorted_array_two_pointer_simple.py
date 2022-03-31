class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        From Leetcode's solution
        """
        n = len(nums)
        result = [0]*n # can't append, because we're going to iterate backwards
        left = 0 
        right = n - 1

        for i in range(n-1,-1,-1): # iterate backwards
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -=1
            else:
                square = nums[left]
                left +=1

            result[i] = square * square 

        return result