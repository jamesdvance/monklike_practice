"""
2484. Count Palindromic Subsequences

Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.

Note:

A string is palindromic if it reads the same forward and backward.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:

Input: s = "103301"
Output: 2
Explanation: 
There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301". 
Two of them (both equal to "10301") are palindromic.
Example 2:

Input: s = "0000000"
Output: 21
Explanation: All 21 subsequences are "00000", which is palindromic.
Example 3:

Input: s = "9999900000"
Output: 2
Explanation: The only two palindromic subsequences are "99999" and "00000".

1 <= s.length <= 104
s consists of digits.

"""

from collections import defaultdict 

class Solution(object):
    """
    Need to study this template for sums of subarrays 

    from collections import defaultdict

    def fn(arr, k):
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in arr:
            # do logic to change curr
            ans += counts[curr - k]
            counts[curr] += 1
        
        return ans

    """

    def checkPalidrome(self, s1):
        return s1 ==  s1[::-1]

    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """

        L = len(s)
        if L < 5:
            return 0 
        
        counts = defaultdict(int)
        counts[0] = 1 

        palindrome = self.checkPalidrome(s[:5])

        count = 1 if palindrome else 0
        for i in range(1, L):
            if i + 5 <= L:
                if palindrome and s[i-1] == s[i+5]:
                    count+=1 
                elif self.checkPalidrome(s[i:i+5]):
                    count+=1
                    palindrome = True
                else:
                    palindrome = False

        return count
        



def test_count_pal_subs():
    print("Testing code")
    sol = Solution()
    assert sol.checkPalidrome("aba")

    assert not sol.checkPalidrome("bba")

    ipt = "9999900000"
    assert sol.countPalindromes(ipt) == 2, f"{sol.countPalindromes(ipt)} != 2 for input {ipt}"

    ipt = "0000000"
    assert sol.countPalindromes(ipt) == 21, f"{sol.countPalindromes(ipt)} != 2 for input {ipt}"





test_count_pal_subs()





