"""

brute fore  2**n

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb_list:list, rem_tgt:int, idx:int):
            nonlocal ret_arr
            if rem_tgt ==0:
                ret_arr.append(comb_list)
                return 
            if rem < 0:
                return
            for j in range(idx, len(candidates)):
                comb_list.append(candidates[j])
                backtrack(comb_list,rem_tgt-candidates[j], j)
                comb_list.pop()


        ret_arr=[]
        backtrack([],target,0)




