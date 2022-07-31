class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l=0 
        max_seq =1
        for r in range(1,len(nums)):
            if nums[r] <= nums[r-1]:
                l=r 

            max_seq = max(r-l+1, max_seq)

        return max_seq
