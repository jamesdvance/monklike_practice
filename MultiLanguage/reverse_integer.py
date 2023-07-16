
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

NOTES:

Edge cases:
* starts with 0
* starts with - 

Handling 64 bit - assume we can't use int 

-231 <= x <= 231 - 1

can check bit_length but a little hacky
"""

# Accepted hacky solution using Python built-ins
class Solution:
    def reverse(self, x: int) -> int:
        max_int, min_int = pow(2,31)-1, pow(-2,31)
        x_str=str(x)
        is_neg = x_str[0] == "-"
        if is_neg:
            x_str = x_str[1:]

        x_str_rev = x_str[::-1]
        if x_str_rev[0] == "0":
            x_str_rev = x_str_rev[1:]
        
        new_int = int(x_str_rev if x_str_rev else "0") 
        return (-new_int if is_neg else new_int) if new_int.bit_length()<32 else 0
    
# True solution 
class Solution:
    def reverse(self, x: int) -> int:
        max_int, min_int = pow(2,31)-1, pow(-2,31)
        rev = 0 
        while x > 0:
            # Add last integer to rev 
            rem = x % 10 
            rev = rev*10 + rem 
            # decrement x
            x = x//10 
            if rev < min_int or rev > max_int:
                return 0 
         
