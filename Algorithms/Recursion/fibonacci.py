from functools import lru_cache

class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        #self.cache = {}
        if n < 2:
            return n 
        
        #elif n in self.cache:
        #    return self.cache[n]
        
        else:
            res = self.fib(n-1) + self.fib(n-2)
            #self.cache[n] = res 
            return res