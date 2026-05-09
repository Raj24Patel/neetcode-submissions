class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] #index value

        maxV = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx , height = stack.pop()
                maxV = max(maxV, height * (i - idx))
                start = idx
            
            stack.append([start, h])
        
        for i , h in stack:
            maxV = max(maxV, h * (len(heights)-i))
        
        return maxV