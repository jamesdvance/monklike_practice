
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        k_prop = k/(2**(n-1))
        m=1

        def build_table(table,n,m,k,k_prop):
            if n ==0:
                return table[len(table)-1][k-1]
            else:
                new_row = ""
                for i in range(len(table[len(table)-1])):
                    char = table[len(table)-1][i]
                    if char == "0":
                        new_row+="01"
                    elif char=="1":
                        new_row+="10"
                    
                    if len(new_row) > ceil(k_prop*(2**(m-1))):
                        break
                    
                    if n ==1 and len(new_row)>=k:
                        break
                        
                table.append(new_row)
                        
                return build_table(table, n-1,m+1, k,k_prop)
            
        return build_table(["0"], n-1,m+1, k,k_prop)

"""
Attempt 2: Split in half (only traverse half the binary tree)
Important facts:
1. The first half is the complement of the second half
2. The first half of the string is always the same as the string N-1

Therefore

if k is in the first half, it is the kth element in N-1
if k is in the second half, it is the compliment of the # in the K-2^(n-1) position in N-1.
Because the first half is the compliment of the second half
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n ==1:
            return 0 if k ==1 else 1 # we come down to an imaginary 'row' with 01

        half =2**(n-1) # length of n-1 row
        if k <= half:
            return self.kthGrammar(n-1, k) # 
        else:
            res = self.kthGrammar(n-1,k-half)
            return 1 if res ==0 else 0