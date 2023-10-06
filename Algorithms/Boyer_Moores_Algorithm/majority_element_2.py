class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        cache = defaultdict(int)
        for num in nums:
            cache[num]+=1

            if len(cache) > 2:
                new_cache = defaultdict(int)
                for k, v in cache.items():
                    if v -1 > 0:
                        new_cache[k] = v-1

                cache = new_cache
                
        return_list = []
        for k,v in cache.items():
            if v > 0 and nums.count(k) > n//3:
                return_list.append(k)
        
        return return_list
