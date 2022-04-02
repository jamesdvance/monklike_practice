class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not hasattr(self,'i'):
            self.i =0
            
        if not hasattr(self, 'n'):
            self.n = len(s)-1
            
        s[self.i], s[self.n] = s[self.n],s[self.i]
        self.i+=1
        self.n-=1
        if self.i < self.n:
            s =self.reverseString(s)
        
        return s