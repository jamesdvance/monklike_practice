from collections import defaultdict
from functools import lru_cache

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """Top down
        
        recurrence relation: max(maxPoints(num-1), maxPoints(num-2)+num)
        base_cases: 
        * maxPoints(0) = 0
        * maxPoints(1) = nums_count[1]

        """
        if len(nums)==1:
            return nums[0]
        
        num_points = defaultdict(int)
        max_val = 0 # Need to start iteration here
        for num in nums:
            num_points[num]+=num
            max_val = max(max_val, num)

        @lru_cache
        def max_points(num):
            if num == 0:
                return 0 
            if num ==1:
                return num_points[1]

            return max(max_points(num-1), 
                max_points(num-2)+num_points[num])

        return max_points(max_val)
