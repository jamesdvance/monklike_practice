# This fails due to time limit exceeded

class Solution:

    def isMatch(self, s: str, p: str) -> bool:


        def dfs(i, j):
            # Stopping criteria 1: We've reached the end of both expressions
            if i >= len(s) and j >= len(p):
                return True 
            
            # We've reached the end of the pattern but haven't traversed the whole string
            if j >= len(p):
                return False 
            
            # Note, if we've reached the end of the string, the pattern might still be a match
        
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # Handle the star case
            if (j+1) < len(p) and p[j+1] == "*":
                return ( 
                        dfs(i, j+2) # move forward in the pattern
                        or 
                        match and dfs(i+1,j) # move forward in the string and keep searching the same pattern
                    )
            
            if match:
                return dfs(i + 1, j +  1)
            
            return False 
        
        return dfs(0,0)