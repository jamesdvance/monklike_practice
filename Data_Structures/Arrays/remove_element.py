class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Approaches:
            1. Iterate through array. If you find a val, replace it with the val at the end of the list and increment num of vals and decrement where to iterate
            2. Once you've made it to where the number of vals is less than the remaining items in the list, stop iterating
                because everything past that point should already be swapped into the array
        """
        i=0
        n = len(nums)
        while i < n:
            if nums[i] ==val:
                nums[i] = nums[n-1]
                n-=1
            
            else:
                i+=1

                
        return n