class Solution:
    def myAtoi(self, s: str) -> int:
        """
        1. Iterate over string
        2. 
        """
        neg = False
        int_str = ""
        int_chars = [str(c) for c in range(10)]

        neg = False
        int_str = ""
        int_chars = [str(c) for c in range(10)]

        i=0
        while  i < len(s) \
            and s[i] not in int_chars:
            if s[i] in ["+","-"]:
                if i+1 ==len(s) \
                    or s[i+1] not in int_chars:
                    return 0
                else:
                    i+=1
                    break
                    
            elif s[i] not in " ":
                return 0
            
            i+=1
        
        if i > 0 and s[i-1] =="-":
            neg =True
        
        if s == len(s):
            return 0

        for j in range(i,len(s)):
            if s[j] not in int_chars:
                break
            else:
                int_str+=s[j]
        
        if len(int_str)>0:
            myint = int(int_str)
        else:
            return 0 

        if neg:
            myint=myint*-1
            return max(myint, -2**31)
        else:
            return min(myint, (2**31)-1) 