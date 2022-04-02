from functools import lru_cache
class Solution:

    @lru_cache
    def climbStairs(self, n: int) -> int:
        """
        Climbing Stairs

        Solution
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

        Approach:
        1. Enumerate by always either choosing 1 or two steps until one step away
        """
        if n <2:
            return 1
        
        return self.climbStairs(n-1) +self.climbStairs(n-2)


