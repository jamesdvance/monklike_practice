from typing import List 
import sys 
from ast import literal_eval

# Scratch
# l = 0, r  = 1
# [1,8,6,7]


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        max_ar = 0 
        while r < l: 
            max_ar = max(min(height[l],height[r]) * (l - r),max_ar)
            if height[r] < height[l]:
                r += 1 
            else:
                l -= 1 

        return max_ar 


if __name__ == 'main':
    height_str: str = sys.argv[1]
    height_list: List = literal_eval(height_str)
    result = Solution().maxArea(height_list)
    ans = int(sys.argv[2])
    assert ans == result 