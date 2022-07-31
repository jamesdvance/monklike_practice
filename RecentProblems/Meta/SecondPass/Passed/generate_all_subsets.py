class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(cur_arr, idx):
            nonlocal visited
            nonlocal ret_arr
            if tuple(cur_arr) in visited:
                return

            visited.add(tuple(cur_arr))
            ret_arr.append(cur_arr)

            for i in range(idx, len(nums)):
                cur_arr.append(nums[i])
                backtrack(cur_arr.copy(), i+1)
                cur_arr.pop()           

        ret_arr =[]
        visited = set()
        backtrack([], 0)
        return ret_arr
