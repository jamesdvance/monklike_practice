class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[],
            [1,1,1,1,1]]
        mod = 10**9+7 
        a,e,i,o,u = 0,1,2,3,4 
        for num in range(2, n+1):
            dp.append([0,0,0,0,0])
            # a 
            dp[num][a] = dp[num-1][e] + dp[num-1][u] + dp[num-1][i]
            # e
            dp[num][e] = dp[num-1][a] + dp[num-1][i]
            # i
            dp[num][i] = dp[num-1][e] + dp[num-1][o] 
            # o 
            dp[num][o] = dp[num-1][i] 
            # u 
            dp[num][u] = dp[num-1][o]  + dp[num-1][i]

        return sum(dp[n]) % mod
            
             



