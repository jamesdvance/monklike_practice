"""
Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with searchWord. If there are more than three products with a common 
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

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

# While searchword, 
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    	# binary search solution
    	# 1. Sort Products
    	products.sort()
    	ret_arr = [] 
    	l,r =0, len(products)=1
    	# Check every increasing side of searchWord: 0:1, 0:2, etc
    	for i in range(len(searchWord)):
    		cur_str = searchWord[0:i+1] 
    		# binary search 
    		# move l forward until we equal current string and are not shorter than current search string
    		while l <= r and (len(products[l]) < i+1 \
    			or products[l][0:i+1]!=cur_str):
    			l+=1

    		# move right backward until we equal current string and are not shorter than current search string
    		while l <= r and (len(products[r] < i+1 \
    			or products[r][0:i+1]!=cur_str)):
    			r-=1

    		# Get an offset to be at most 3 words starting at l (the earliest word containing the search string, sorted in alpha order)
    		r_anch = l + min(3, r-l+1) # get past 3 greater than l
    		ret_arr.append(products[l:r_anch])

    	return ret_arr





