"""
1. For-loop, multiply x but itself n times

"""
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n<0:
            x= 1/x
            n=-1*n 

        ans =1
        for i in range(n):
            ans*ans*x
        return ans

"""
Optimized
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n<0:
            x= 1/x
            n=-1*n 

        ans=1
        cur_prod=x
        while n >0:
            if n%2==1:
                ans*=cur_prod
            cur_prod*=cur_prod
            n//=2

        return ans

# Iterative
"""
2**3 = 8
ans=1
cur_prod=2
ans = 1*2
cur_prod = 4 aka 2**1 + 2**1

"""
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n<0:
            x= 1/x
            n=-1*n 

        ans=1
        cur_prod=x
        while n>0:
            if n%2==1:
                ans*=cur_prod
            cur_prod*=cur_prod

        return ans

# Recursive:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        return self.fastPow(x,n)

    def fastPow(self, x,n):
        if n==0:
            return 1.0
        half = self.fastPow(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x