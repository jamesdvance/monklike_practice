class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    	ret_sum =0
    	cur_streak=0
    	for i in range(2,len(nums)):
    		if  nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
    			cur_streak+=1
    			ret_sum+=cur_streak
    		else:
    			cur_streak=0
    	return ret_sum



