class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #ind, temp

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i , t = stack.pop()
                res[i] = ind - i
            
            stack.append([ind,temp])
        
        return res




        