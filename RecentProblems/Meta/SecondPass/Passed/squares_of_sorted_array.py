class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l,r = 0 , len(nums)-1
        ret = [] 
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ret.append(nums[l]**2)
                l+=1
            else:
                ret.append(nums[r]**2)
                r-=1

        return ret[::-1]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l,r = 0 , len(nums)-1
        ret = [0] *len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l]) > abs(nums[r]):
                ret[i] = nums[l]**2
                l+=1
            else:
                ret[i] = nums[r]**2
                r-=1

        return ret