class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        You are given two integer arrays nums and multipliers of size n 
        and m respectively, where n >= m. The arrays are 1-indexed.

        You begin with a score of 0. You want to perform exactly m operations. 
        On the ith operation (1-indexed), you will:

        Choose one integer x from either the *start or the end* of the array nums.
        Add multipliers[i] * x to your score.
        Remove x from the array nums.
        Return the maximum score after performing m operations.

        Thoughts:
            * Need to track index while looping across multipliers
            * Need to track deletions from nums (can't just delete them for optionality)
            * with multiplication, want to multiply the highest nums together
            * Only multiply negs with negs

        DP Parts:
            * State variables
                * how much operations have we done so far
                * index of leftmost number remaining in nums, index of rightmost number remaining in nums
            * Recurrence relation
                * to decide whether to take from the left or the right --- 
                    * 
        """


