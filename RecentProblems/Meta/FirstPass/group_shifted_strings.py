"""
Create tuples of differences in orders between consecutive
numbers. Dict from those tuples to a list of strings

Intuition: How many shifts for each char in a given string to make it back to a ? 
for A,b,c, this would be 0,1,2. Are they the same distance apart? 


"""
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

    	def get_hash(string:str):
    		key = [] 
    		for a,b in zip(string, string[1:]):
    			key.append(chr((ord(b)-ord(a)) % 26 + ord('a')))
    			return ''.join(key)

    	groups =defaultdict(list)
    	for string in strings:
    		hash_key = get_hash(string)
    		groups[hash_key].append(string)

    	return list(groups.values())

"""

This can be distilled down to just getting the distance between each string in the alphabet.
Convert back to a char, and building a char that becomes a hashkey
"""
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

    	def get_hash(string:str):
    		ret_str =""
    		for a,b in zip(string, string[1:]):
    			ret_str+=chr((ord(b)-ord(a)) % 26 + ord('a'))
    		return ret_str

    	groups =defaultdict(list)
    	for string in strings:
    		hash_key = get_hash(string)
    		groups[hash_key].append(string)

    	return list(groups.values())


"""
Solution with tuple key
"""
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

    	def get_hash(string:str):
    		ret_list = []
    		for a,b in zip(string, string[1:]):
    			ret_list.append((ord(b)-ord(a)) % 26)
    		return tuple(ret_list)

    	groups =defaultdict(list)
    	for string in strings:
    		hash_key = get_hash(string)
    		groups[hash_key].append(string)

    	return list(groups.values())
        