class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Thoughts:
            1. normally, removing elem means have to iterate through entire arr
            2. should be able to skip that by using two pointers and writing to i minus some offset (representing the num of dupes)
            as we iterate forward
        """

        i = 0
        offset = 0
        prev = None
        for i in range(len(nums)): # at worst iterate through entire arr
            if nums[i] ==prev:
                offset +=1
            elif offset >0:
                nums[i-offset] = nums[i]

            prev = nums[i]

        return len(nums) - offset