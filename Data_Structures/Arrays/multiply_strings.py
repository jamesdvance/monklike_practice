"""
Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

1. Take larger number as first multiplier
2. Iterate through second multiplier from right to left. 

e.g. "562", 26 ->
562
x 26: 
6*2 = 12
6*6 = 36 +1 =37
6*5 = 30 + 3
=3372
11240
14612

Hints: Can I use addition? Can I use multiplication of individual digits? 

562, 26
first = 562
second = 26

d = 6
for i in range(1,1):
    do nothing
prod_str = ""
for j in range(3):
    val = 

"""

class Solution:
    def multiply(self, num1:str, num2:str)-> str:
        n1, n2 = len(num1), len(num2)
        if n2 > n1:
            first, second = num2, num1 
        else:
            first, second = num1, num2 

        del num1, num2 

        max_len = 1
        products = [] # list of lists
        for i in reversed(range(len(second))):
            d = second[i]
            prod_str = ""
            for i in range(i, len(second)-1):
                prod_str+="0"

            ad =0
            for j in reversed(range(len(first))):
                val = int(first[j])
                ind_prod =0
                for _ in range(val):
                    ind_prod+=int(d)
                
                ind_prod+=ad
                print(ind_prod)
                if j < len(first)-1:
                    ad, dig = str(ind_prod)[0:-1], int(str(ind_prod)[-1])
                    ad = 0 if len(ad)==0 else int(ad)
                    print(f"additional {ad}")
                    prod_str = str(dig)+prod_str
                else:
                    prod_str = str(ind_prod)+prod_str


            max_len = max(len(prod_str), max_len)
            products.append(prod_str)

        print(products)
        # Add all products at once
        final_prod = ""
        ad =0
        for k in reversed(range(max_len)):
            k_sum =0 
            for l in range(len(products)):
                if len(products[l]) > k:
                    k_sum+=int(products[l][len(products[l])-1-k])
            
            k_sum +=ad
            if k < max_len-1:
                ad, rem = str(k_sum)[0:-1], int(str(k_sum)[-1])
                ad = 0 if len(ad)==0 else int(ad)
                final_prod=str(rem)+final_prod 
            else:
                final_prod=str(k_sum)+final_prod 

        return final_prod
            

"""
LC Solution


"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return 0 

        # reverse both strings
        first_number = num1[::-1]
        second_number = num2[::-1]

        results

"""
Solution Attempt 2

e.g. "562", 26 ->
562
x 26: 
6*2 = 12
6*6 = 36 +1 =37
6*5 = 30 + 3
=3372
11240
14612

prod=12
"""         

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        n1, n2 = len(num1), len(num2)
        if n2 > n1:
            num2, num1 = list(num1), list(num2)

        # num1 is always longer
        prod_strs = []
        max_len = 1
        for i in range(len(num2)-1,-1,-1):
            prod_str = ""
            for _ in range(i,len(num2)-1):
                prod_str+="0"

            # Multiply each #
            ad =0 
            d = int(num2[i])
            for j in range(len(num1)-1, -1, -1):
                prod = 0
                for _ in range(int(num1[j])):
                    prod+=d 

                prod+=ad
                if j ==0:
                    prod_str = str(prod)+prod_str

                else:
                    if len(str(prod)) > 1:
                        ad=int(str(prod)[0:-1])
                        prod_str = str(prod)[-1] + prod_str
                    else:
                        ad =0
                        prod_str = str(prod) + prod_str

            max_len = max(len(prod_str),max_len)
            prod_strs.append(prod_str )


        cur_sum = 0
        final_sum = ""
        for k in range(max_len-1,-1,-1):
            for prod_str in prod_strs:
                k_idx = k - (max_len - len(prod_str))
                if k_idx >=0:
                    cur_sum+=int(prod_str[k_idx])

            if k ==0:
                final_sum = str(cur_sum)+final_sum

            else:
                if len(str(cur_sum))>1:
                    final_sum = str(cur_sum)[-1] +final_sum
                    cur_sum = int(str(cur_sum)[0:-1])
                else:
                    final_sum = str(cur_sum) + final_sum
                    cur_sum =0

        return str(int(final_sum))








