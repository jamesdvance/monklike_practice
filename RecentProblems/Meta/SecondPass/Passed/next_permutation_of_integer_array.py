# 1. Find first non-decreasing number
# 2. swap number with the lastest number 
# 3. reverse rest of array
# [1,2,3,3,2,1] -> [1,3,1,2,2,3] 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found =False
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                found =True
                break 

        # check if i == 1 
        if not found:
            nums.reverse()

        else:
            for j in range(len(nums)-1,i-1,-1):
                if nums[j] > nums[i-1]:
                    nums[i-1],nums[j] = nums[j],nums[i-1]
                    break 

            l = i 
            r = len(nums)-1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1







