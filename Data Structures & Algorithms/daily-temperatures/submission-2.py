class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # index, temperature

        res = [0] * len(temperatures)

        for ind, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                day , temp = stack.pop()
                res[day] = ind - day

            stack.append([ind, val])
        
        return res
        