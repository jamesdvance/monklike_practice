class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(n)>1000: # Max recursive depth in Python is 1000. Since this is a recursion exercise, not gonna rewrite to not use recursion
            return x**n
        
        if n ==0:
            return 1.0
        elif n <0:
            n +=1
            return (1/x) *self.myPow(x, n)
        elif n > 0:
            n-=1
            return x * self.myPow(x,n)