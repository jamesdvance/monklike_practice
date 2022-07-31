class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forwardSum = [1]*n
        for i in range(n):
            forwardSum[i] = nums[i] if i ==0 else nums[i]*nums[i-1]

        backwardSum = [1]*n
        for i in range(n-1,-1,-1):
            backwardSum[i] = nums[i] if i ==n-1 else nums[i]*backwardSum[i+1]

        ret_arr = []
        for i in range(len(nums)):
            bwk_tot = 1 if i == len(nums)-1 else backwardSum[i+1]
            fwd_tot = 1 if i==0 else forwardSum[i-1]
            ret_arr.append(bwk_tot*fwd_tot)

        return ret_arr