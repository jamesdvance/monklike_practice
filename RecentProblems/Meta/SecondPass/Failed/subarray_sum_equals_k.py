from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        rolling = 0
        sum_dict = defaultdict(int)
        sum_dict[0]=1
        for i in range(len(nums)):
            rolling+=nums[i]
            ret+=sum_dict[rolling-k]
            sum_dict[rolling]+=1

        return ret
