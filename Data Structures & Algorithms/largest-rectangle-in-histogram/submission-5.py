class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #ind, height
        maxarea = 0

        for i, h in enumerate(heights):
            ind = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, (i-index) * height)
                ind = index
            stack.append([ind,h])
        

        for i, h in stack:
            maxarea = max(maxarea, (len(heights) - i ) * h )
        
        return maxarea




        