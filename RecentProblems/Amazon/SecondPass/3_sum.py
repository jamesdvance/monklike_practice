class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


 return []

        self.ret = set() 
        nums.sort() # O(NLogN)
        i=0
        for i in range(len(nums)):
            if nums[i] > 0:
                break 

        if nums[i] < 0:
            return []

        tried = set()
        for j in range(0,i):
            if nums[j] not in tried:
                tried.add(nums[j])
                self.twoSum(nums[j]*-1, nums[j+1:])
RR
        return list(self.ret)

    def twoSum(self,tgt:int, nums:List[int]):
        for i in range(len(nums)):
            sum_hash = set(nums[:i]+nums[i+1:])
            num = nums[i]
            if tgt-num in sum_hash:
                self.ret.add(tuple(sorted([tgt*-1,num, tgt-num])))