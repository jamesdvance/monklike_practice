"""
Rules:
1. decimal - ok anywhere
2. e-followed by integer. Can't be first or last
3. +- followed by integer
4. 
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        found_e = False
        found_dec = False
        found_digit = False
        for i, char in enumerate(s):
            if char in ["E","e"]:
                if found_e or not found_digit:
                    return False
                else:
                    found_e=True
                    found_digit = False
            elif char in ["+","-"]:
                if i > 0 and s[i-1] not in ["E","e"]:
                    return False
            elif char==".":
                if found_e or found_dec:
                    return False
                else:
                    found_dec=True
            elif char.isdigit():
                found_digit=True
            else:
                return False

        return found_digit


