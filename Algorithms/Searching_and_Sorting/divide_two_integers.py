
"""
To not exceed the timelimit, will likely have to use a similar solution but 
subtract each digit, long division style.

Long division steps: 
1. Divide the full divisor by the first digit in the dividend, keeping the quotient and remainder
2. Carry the remainder to start the new dividend. Append the next digit to the divisor to create t he next dividend

101; 20
3;5
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def stringify(i:int):
            i_s = str(i)
            if i_s[0]=='-':
                return i_s[1:], True
            else:
                return i_s, False

        def divide_digits(end:str,sor:str):
            end, sor = int(end), int(sor)
            q =0
            while end-sor >= 0:
                end-=sor
                q+=1

            rem = sor-q
            return q, rem

        def make_neg(i:int):
            return int("-"+str(i))

        dividend_str, end_neg = stringify(dividend)
        divisor_str, sor_neg = stringify(divisor)
        final_neg = (end_neg and not sor_neg) or (sor_neg and not end_neg)
        orig_div_len = len(dividend_str)

        loop_div = dividend_str[0]
        final_q = ""
        for i in range(orig_div_len): # while i < 2
            q, rem = divide_digits(loop_div, divisor_str)
            final_q +=str(q)
            print(i)
            if i < orig_div_len -1:
                loop_div = str(rem)+str(divisor_str[i+1])
        
        if final_neg:
            return max(-2**31, make_neg(int(final_q)))
        
        else:
            return min(2**31, int(final_q))
        


"""
This solution exceeded time limit
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        q = 0
        def myabs(i:int):
            i_s = str(i)
            if i_s[0]=='-':
                return int(i_s[1:]), True
            else:
                return i, False
            
        def make_neg(i:int):
            return int("-"+str(i))
            
        end_abs, end_neg = myabs(dividend)
        sor_abs, sor_neg = myabs(divisor)
        final_neg = (end_neg and not sor_neg) or (sor_neg and not end_neg)
            
        while end_abs-sor_abs >= 0:
            end_abs-=sor_abs
            q+=1
            
        if final_neg:
            return max(-2**31, make_neg(q))
        
        else:
            return min(2**31, q)

"""
Attempt # 3
Long division steps:
divide entire divisor by first digit in dividend

425, -25
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def stringify(i:int):
            i_s = str(i)
            if i_s[0]=='-':
                return i_s[1:], True
            else:
                return i_s, False
            
        def make_neg(i:int):
            return int("-"+str(i))

        s_dividend,is_neg_dividend = stringify(dividend)
        s_divisor, is_neg_divisor  = stringify(divisor)

        quotient_str = ""
        rem_str = ""
        for j in range(len(s_dividend)):
            mini_dividend = int(rem_str + s_dividend[j])
            quot, rem = self.divide_small(mini_dividend, int(s_divisor))
            quotient_str += str(quot)
            rem_str = str(rem)

        if (is_neg_divisor and not is_neg_dividend) \
            or (is_neg_dividend and not is_neg_divisor):
            return max(-2**31, make_neg(int(quotient_str)))
        
        else:
            return min(2147483647, int(quotient_str))

    def divide_small(self, dividend:int, divisor:int)->tuple: 
          
        total =0
        while dividend - divisor >= 0:
            total+=1
            dividend-=divisor 

        return total, dividend

