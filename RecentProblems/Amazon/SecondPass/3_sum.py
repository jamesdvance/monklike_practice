class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
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

    	return list(self.ret)

    def twoSum(self,tgt:int, nums:List[int]):
    	sum_hash = set(nums)

    for num in nums:
        if tgt-num in sum_hash:
            self.ret.add((tgt*-1,num, tgt-num))