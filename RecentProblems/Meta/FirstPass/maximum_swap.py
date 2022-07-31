"""
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.


Intuition:
Find that first digit that Find the largest such digit that occurs the latest. 

pos = {}

"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        pos = {x:i for i,x in enumerate(num_list)}
        for i, x in enumerate(num_list):
            for j in range(9, int(x),-1): 
                last_pos = pos.get(str(j),-1)
                if last_pos > i:
                    num_list[i], num_list[last_pos] = num_list[last_pos], num_list[i]
                    return int("".join(list(num_list)))

        return num

"""
Other Solution
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        # find index where s[i] < s[i+1], meaning a char can be flipped
        for i in range(n-1):
            if s[i] < s[i+1]: break
        else: return num 
        # keep iterating right find the maximum value index
        max_idx, max_val = i+1, s[i+1]
        for j in range(i+1, n):
            if max_val <= s[j]: max_idx, max_val =j ,s[j]


        left_idx =i
        for j in range(i, -1,-1):
            if s[j] < max_val: left_idx=j 
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]
        return int("".join(s))

