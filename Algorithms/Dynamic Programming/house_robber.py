class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        Rob houses with none touching 
        Top - down
        Base case: 
            * dp(0) = nums[0]
            * dp(1) = max(nums[0], nums[1])

        Recurrence Relation:
            * dp(i) = max(dp[i-1], dp[i-2]+nums[i])         
        """
        n=len(nums)
        if n==1:
            return nums[0]
        
        memo = {}
        memo[0] = nums[0]
        
        memo[1] = max(nums[0], nums[1])
        def robHouse(i):
            """
            
            """
            if i not in memo:
                memo[i] = max(robHouse(i-1), robHouse(i-2)+nums[i])
            
            return memo[i]
            
        
        return robHouse(n-1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        Rob houses with none touching 
        Bottom Up
        Base case: 
            * dp(0) = nums[0]
            * dp(1) = max(nums[0], nums[1])

        Recurrence Relation:
            * dp(i) = max(dp[i-1], dp[i-2]+nums[i])         
        """
        n=len(nums)
        if n == 1:
            return nums[0]
        max_vals = [nums[0], max(nums[0],nums[1])]

        for i in range(2,n):
            max_vals.append(max(max_vals[i-1], max_vals[i-2]+nums[i]))

        return max_vals[n-1]






