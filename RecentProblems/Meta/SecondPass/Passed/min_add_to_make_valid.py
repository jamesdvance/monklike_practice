class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ctr = 0
        res = 0
        for char in s:
            if char=="(":
                ctr+=1
            elif char==")":
                if ctr:
                    ctr-=1
                else:
                    res+=1
        return res+ctr 