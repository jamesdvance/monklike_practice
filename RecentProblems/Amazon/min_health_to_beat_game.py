
"""
2214. Minimum Health to Beat Game

You are playing a game that has n levels numbered from 0 to n - 1. You are given a 0-indexed integer array 
damage where damage[i] is the amount of health you will lose to complete the ith level.

You are also given an integer armor. You may use your armor ability at most once during the game on any level 
which will protect you from at most armor damage.

You must complete the levels in order and your health must be greater than 0 at all times to beat the game.

Return the minimum health you need to start with to beat the game.



"""

"""
Blind solution attempt
min health = min unavoidable health lost + 1 

Seems like some kind of dp where you take either the previous cumulative damage or the cumulative damage plus the armor
May have to work back to front 

Input: damage = [2,7,4,3], armor = 4
sum = 16. 16 - 4 = 12 + 1 = 13
Output: 13

test: 10
2 + 7 - 4 < 4 + 3 

Two pointer, where one end has to be greater than the other end  - 4

"""


"""
Prefix Sums
O(2N)
[2,7,4,3]
pref_sum = [2,9,13,16]
new_d = 0,min_dmg = 0 + 0 + 16-2 = 14
new_d = 5, min_dmg = 2 + 3 +16-9 = 5 +7 =12 
new_d = 0, min_dmg = 13 - 4 + 0 + 16-13 = 9 + 3 = 12
new_d = 0 min_dmg = 16-3 + 0 + 16 -16 = 13
"""

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
    	min_dam = float("inf")
    	# 1. Create Prefix Sums List
    	pref_sum = []
    	rolling_sum = 0
    	for d in damage:
    		rolling_sum+=d 
    		pref_sum.append(rolling_sum)

    	# 2. Find the minimum damage possible at this point by comparing the damage at point i using armor against the 
    	for i,d in enumerate(damage):
    		# 
    		new_d = 0 if armor >= d else d- armor  # this is the remainder or damage left after applying armor at i
    		total_damage = pref_sum[i] - damage[i] \
    			+ new_d \
    			# Total damage in rest of 
    			+ pref_sum[-1] - pref_sum[i]
    		min_dam = min(total_damage, min_dam)
    	return min_dam + 1 

# Same, but more succinct
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        min_dmg = float("inf")
        pref_sum = [] 
        rolling = 0 
        for d in damage:
            rolling+=d 
            pref_sum.append(rolling)
            
        for i,d in enumerate(damage):
            # maximum damage in this turn
            turn_dam = max(d-armor,0)
            min_dmg = min(min_dmg,
                         pref_sum[i]-damage[i] + turn_dam + (pref_sum[-1]-pref_sum[i]))
        
        return min_dmg+1
"""
One Liner
O(2N)

You subtract all of the damage by either the armor, or 
Take the minimum of armor and max damage because if armor protects you from *at most* armor damage at any level.
So max armor can protect is itself or the max damage amount
"""

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
    	return sum(damage)-min(armor, max(damage))+1