class Solution:
    def minAddToMakeValid(self, s: str) -> int:
    	cnt = 0
    	res =0
    	for i in range(len(s)):
    		if s[i] == "(":
    			cnt+=1 
    		else:
    			cnt-=1 

    		if cnt <0:
    			res+=1
    			cnt+=1 


    	res = res + cnt # add final open parenthesis 
    	return res
