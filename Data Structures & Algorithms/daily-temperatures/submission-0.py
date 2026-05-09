class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temp, val]
        res = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                indTemp , indDay = stack.pop()
                res[indDay] = ind - indDay
            stack.append([temp, ind])
        
        return res
        
        