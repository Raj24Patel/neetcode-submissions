class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #ind height
        maxarea = 0
        
        for ind, h in enumerate(heights):
            start = ind

            while stack and stack[-1][1] > h:
                previndx, prevheight = stack.pop()
                maxarea = max(maxarea, prevheight * (ind - previndx))
                start = previndx
                

            stack.append([start,h])


        for ind, h in stack:
            maxarea = max(maxarea, h * (len(heights)-ind))

        return maxarea

        