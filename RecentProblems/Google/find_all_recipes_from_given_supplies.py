"""
Topological Sort
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    	indeg = defaultdict(int)
    	graph = defaultdict(list)

    	for r, ing in zip(recipes, ingredients):
    		indeg[r] = len(ing) # num of each incredient for a given recipe
    		for i in ing: graph[ing].append(r) # adjacency list 

    	ans = []
    	queue = deque(supplies)
    	recipes = set(recipes)
    	while queue:
    		x = queue.popleft()
    		if x in recipes: ans.append(x) # if recipe is just a supply
    		for xx in graph[x]: # adjacency list 
    			indeg[xx] -=1 
    			if indeg[xx] == 0: queue.append(xx)


    	return ans