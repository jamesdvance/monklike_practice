"""
nums i+1 >= nums i -1

"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            elif changed:
                return False
            else:
                if i ==0 or nums[i+1]>=nums[i-1]:
                    nums[i]=nums[i+1]
                else:
                    nums[i+1] = nums[i]

                changed = True 

        return True


