"""

"""
from collections import Counter, defaultdict 
from itertools import combinations
def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
	users = defaultdict(list)

	for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: x[0], x[1]): # Sort by username, timestamp
		user[user].append(site)

	patterns  = Counter()

	for user, site in users.items():
		patterns.update(Counter(set(combinations(sites, 3))))

	return max(sorted(patterns), key=patterns.get)
