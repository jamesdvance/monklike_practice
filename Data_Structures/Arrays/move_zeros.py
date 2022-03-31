class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Thoughts:
            1. Maintaining order means plain swap won't work
            2. Could achieve O(N^2) by copying the array backwards each time a zero is found
            3. Will need an offset to show how long to copy backwards
            4. Don't need to keep iterating after reaching offset from the end
            5. May be a way to keep swapping during the backwards copy
        """

        n = len(nums)
        offset = 0
        for i in range(n):

            if nums[i] ==0:
                offset +=1

            elif offset > 0:
                nums[i-offset] = nums[i]  

        for i in range(n-offset,n,1):
            nums[i] =0

