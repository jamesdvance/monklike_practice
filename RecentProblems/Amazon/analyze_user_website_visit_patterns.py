"""
PROMPT

Analyze User Website Visit Patterns 

You are given two string arrays username and website and an integer array timestamp. 
All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] 
visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], 
and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" 
then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" 
then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at 
different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically 
smallest such pattern.

If you use combinations, it maintains the order of the list. e.g for the list [1,2] the length one combinations will be [1], [2] and never [2], [1]
In this line max(sorted(patterns), key=patterns.get). max will take the first element with the max count. So if you sort by patterns first u get the 
lexicographically smallest pattern of the most common patterns
"""
from collections import Counter, defaultdict 
from itertools import combinations
class Solution:
	def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
		users = defaultdict(list)

		visit_list = sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1]))
		for user, time, site in visit_list: # Sort by username, timestamp
			users[user].append(site)

		patterns  = Counter()

		for user, site in users.items():
			patterns.update(Counter(set(combinations(site, 3)))) # dorder is preserved

		return max(sorted(patterns), key=patterns.get)

"""
Explanation
Intuition: Order of site visits matter. So can use combinations to get all subsequent visits
Data Structures: Counter, 'combinations' iterator
Steps:
1. initialize defaultdict with list to create list of sites visited by each user
2. Create a sorted list of tuples 'visit_list' by zipping username, timestamp,website togther, and sorting by username, then timestamp
3. iterate over the zipped list, appending sites to each user's dict. This ensures the sites are stored in sequential order
4. Create a counter object 'patterns'
5. Iterate over the users dictionary and add each n choose 3 ordered combination of thier sites to the Counter object. The Counter
automatically increments how many are seen and uses a set of the 3 index as the key
6. Finally, we sort the patterns dictionary then return max over the dictionary which returns the key

"""