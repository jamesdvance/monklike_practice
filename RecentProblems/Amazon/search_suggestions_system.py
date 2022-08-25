"""
Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Can use a trie or two-pointer


Example:
sorted: ["mobile","moneypot","monitor","mouse","mousepad"],

moo 

moose 
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    	products.sort()
    	l, r= 0, len(products)-1

    	ret = [] 
    	for i in range(len(searchWord)):
    		s = searchWord[0:i+1]

    		while l <= r and (len(products[l]) < i+1 or products[l][0:i+1]!=s):
    			l+=1 

    		while l <= r and (len(products[r]) < i+1 or products[r][0:i+1]!=s):
    			r-=1 

    		r_anch = l+min(3, r-l+1)
    		ret.append(products[l:r_anch])

    	return ret 


"""
Trie
"""