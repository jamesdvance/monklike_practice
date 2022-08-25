# Backtracking
# With the cache check, this is structurally similar to top-down dp
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #@lru_cache
        def backtrack(comb_arr, i, cur_sum):
            nonlocal min_coins
            nonlocal visited
            if len(comb_arr) >= min_coins or cur_sum > amount:
                return
            elif cur_sum == amount:
                min_coins = min(min_coins, len(comb_arr))
                return
            else:
                for j in range(i, len(coins)):
                    if tuple(comb_arr+[coins[j]]) not in visited:
                        comb_arr+=[coins[j]]
                        backtrack(comb_arr, j, cur_sum+coins[j])
                        visited.add(tuple(comb_arr))
                        comb_arr.pop()

        min_coins = float("inf")
        visited = set()
        backtrack([], 0, 0)
        return -1 if min_coins == float("inf") else min_coins

"""
Bottom-Up DP
Double-nested loop
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1]*(amount+1) # at amount 0, 0 coins are needed 
        dp[0]=0

        for a in range(1,amount+1): 
            for c in coins:
                if a-c >=0:
                    dp[a] = min(dp[a], # current solution
                        1 + dp[a-c]) # taking this coin and the amount of coins that make up its complement at a - c

        return dp[amount] if dp[amount] != amount + 1 else -1

"""
Pure DP top down
"""

