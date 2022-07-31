"""
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. 
Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.


"""
from collections import deque
class Solution:
	def racecar(self, target: int) -> int:

		# BFS
		q=deque([(0,0,1)]) # moves, position, velocity
		result = float("inf")
		while q:
			moves,pos,vel = q.pop()
			if pos == target:
				result = min(result, moves)

			if moves > result:
				continue

			q.append((moves+1, pos+vel, vel*2))# Accelerate

			if (pos+vel > target and vel > 0) \
				or (pos+vel < target and vel <0):
				q.append((pos, -1 if vel > 0 else 1, moves+1))

		return result


"""
DP Approach
"""
class Solution:
	def racecar(self, target: int) -> int:
	# Case 3 
	def pass_target(i, f):
	    j = 2 ** math.ceil(f) - 1
            return math.ceil(f) + dp(j - i) + 1 # +1 because we need one R to reverse
        
        # Case 1
        def reverse_before_target(i, f):
            j = 2 ** math.floor(f) - 1
            d = i - j
            
            # Move back one step at the time, until it's too far
            ans = float('inf')
            p = 0
            s = 1
            step = 0
            while p < d:
                ans = min(ans, math.floor(f) + step + dp(d+p) + 2) # +2 because we need two R's to face towards target
                step += 1
                p += s
                s *= 2
            
            return ans

        @cache
        def dp(i):
            if i == 1:
                return 1

            f = math.log2(i + 1)
            if f == int(f):
                # Case 2
                return int(f)
            else:
                return min(
                    pass_target(i, f),
                    reverse_before_target(i, f)
                )
        return dp(target)



class Solution:
	def racecar(self, target: int) -> int:
		q = deque([(1,0,0)]) # speed, position,moves
		min_moves = float("inf")
		while q:
			s, p, m = q.pop()

			if p == target:
				min_moves == min(min_moves, m)

			elif m < min_moves:
				q.append((s*2, p+s, m+1))
				if p+s > target and s >0\
					or p+s < target and s<0:
					q.append((-1 if s > 0 else 1, p, m+1))

		return min_moves