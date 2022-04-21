class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
        Once you pay the cost, you can either climb one or two steps.

        You can either start from the step with index 0, or the step with index 1.

        Return the minimum cost to reach the top of the floor.

        Notes:
        * Isn't greedy because we make a choice by climbing two steps to skip one step. If we always took
        the min cost of the 1st or second step, we'd be missing out on the cost of taking one step 
        then having to take another, etc
        * we probably want to work from the top to bottom:
        base  cases: 
            * final_step = cost[len(cost)-1]
            * second_to_last_step = min(cost[len(cost)-2],final_step)

        recurrence relation:
            * minCost(step) = min(minCost(step+1),minCost(step+2))

        bottom-up
        """
        path_cost = [0]*len(cost)
        path_cost[len(cost)-1] = cost[len(cost)-1]
        path_cost[len(cost)-2] = cost[len(cost)-2]
        for i in range(len(cost)-3, -1,-1):
            path_cost[i] = cost[i] + min(path_cost[i+1],path_cost[i+2])

        return min(path_cost[0],path_cost[1])


" Constant space - Leetcode "
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        down_one = down_two = 0
        for i in range(2, len(cost) + 1):
            temp = down_one
            down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = temp

        return down_one