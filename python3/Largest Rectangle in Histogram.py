class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size  = len(heights)
        stack = [-1]
        maxA  = 0
        for i in range(size):
            #for each h, find it's L and R
            while (stack[-1] != -1 and heights[i] <= heights[stack[-1]]):
                #h is R for all elements in stack(except the first one: -1)
                    preI = stack.pop()
                    area = heights[preI] * (i - stack[-1] - 1)
                    maxA = max(maxA, area)    
            stack.append(i)
        while (stack[-1] != -1):
            #h is R for all elements in stack(except the first one: -1)
            preI = stack.pop()
            area = heights[preI] * (size - stack[-1] - 1)
            maxA = max(maxA, area) 
        return maxA