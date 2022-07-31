# Right to left solution
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_h = heights[-1]
        ret_arr = [len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            if heights[i] > max_h:
                ret_arr.append(i)
                max_h = heights[i]

        return ret_arr[::-1] 

# left to right solution
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return stack