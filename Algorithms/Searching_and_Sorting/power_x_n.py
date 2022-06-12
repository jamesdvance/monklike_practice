"""
Solution:
Brute force would be to:
1. convert x to 1/x if n is negative
2. then multiply x by itself n times 
3. Include catch in case n =0

More optimal: Fast Power Algorithm Recursive
Since (x**n)**2 = x**2n, can use this property to get solution quicker
1. if n = 1 return float 1 
2. otherwise, keep recursively reducing n by getting x**n/2
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x 
            n = -n

        return self.fastPow(x, n)

    def fastPow(self, x:float, n:int)->float:
        if n == 0:
            return 1.0

        half = self.fastPow(x,n//2)
        if n % 2 ==0:
            return half * half 
        else:
            return half * half * x 
        
"""
Iterative Solution
Binary Exponentiation

Works based on x**2+x**b = x**(a+b)

aka a*4 + a*4
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n 

        ans = 1 
        current_product = x 

        while n >0:
            if n%2==1:
                ans*=current_product 
            current_product = current_product*current_product
            n = n//2

        return ans

