"""

"""

class Solution:
    def myAtoi(self, s: str) -> int:

        i=0
        while i < len(s)and s[i]==" ":
            i+=1

        ret_dig = ""
        sign = "pos"
        if i <len(s):
            if s[i]=="-":
                sign="neg"
                i+=1
            elif s[i]=="+":
                i+=1
            while i< len(s) and s[i].isdigit():
                ret_dig+=s[i]
                i+=1

        if len(ret_dig)==0:
            return 0
        if sign == "neg":
            return max(-2**31, -1*int(ret_dig))
        else:
            return min(2**31-1, int(ret_dig))