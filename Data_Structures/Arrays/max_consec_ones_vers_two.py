class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Given a binary array nums, return the maximum number of 
        consecutive 1's in the array if you can flip at most one 0.
        
        Approach:
        1. Trivial max-consec problem, but have to keep track of the gap and continue

        2. Two things I missed. 
            1. Didn't reset gap_z to zero after a new one was encountered
            2. Didn't check if a zero could be added to the ones streak before. After gets covered by current case
            3. Now need to account for difference between consecutive vs total zeros
            4. 
        """
        longest_sequence =0 
        left, right =0
        num_zeros =0

        while right < len(nums): 
            if nums[right] ==0:
                num_zeros +=1

            while num_zeros ==2:
                if nums[left] ==0:
                    num_zeros-=1

                left+=1

            longest_sequence = max(longest_sequence, right-left+1) # don't need to sum since all ones
            right +=1



        return longest_sequence




