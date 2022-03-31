class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
        Return any array that satisfies this condition. 

        Approach:
        1. Reminds of dutch nat'l flag problem. 
        2. Iterating sequentially likely won't work. 
        3. Would need to check that all odds have been moved.
        4. May want to iterate once through and count the odds or use a two-pointer technique to track where the odds are
        5. One trivial solution: create an even array and and an odd array and combine them

        It + count: could iterate a second time and swap with last items until the # is reached

        Two-pointer: keep swapping with the end and appending to the end and then stop before pointer1 =pointer2

        Beware all evens or all odds
        """ 

        n = len(nums) -1
        i = 0
        while i < n:

            while nums[i] % 2 != 0 and i< n:

                nums[i], nums[n] = nums[n],nums[i]

                n-=1

            i+=1

        return nums

