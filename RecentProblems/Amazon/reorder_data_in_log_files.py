"""
Reorder Data In Log Files

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

 
Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.

Rephrase: Sort in this specific sort order: 

Letter logs first, sorted lexicographically. If exact match, sort by id's
digit logs
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
    	dig_list = [] 
    	let_list = []
    	def sort_func(mystr:str)->tuple:
    		split_list = mystr.split(" ")
    		return (" ".join(split_list[1:]), split_list[0])

    	for log in logs:
    		if log.split(" ")[1][0] in ("0","1","2","3","4","5","6","7","8","9"):
    			dig_list.append(log)

    			let_list.append(log) 

    	let_list.sort(key=lambda x:sort_func(x))
    	return let_list + dig_list

"""
Leetcode solution (samp approach "sorting by keys" but more succinct)
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

    	def get_key(log):
    		_id, rest = log.split(" ",maxsplit=1)
    		return (0, rest,_id) if rest[0].isalpha() else (1,0)

    	return sorted(logs,key=get_key)
