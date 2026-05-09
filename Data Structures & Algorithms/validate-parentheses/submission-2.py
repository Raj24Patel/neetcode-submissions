class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comp = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in comp:
                if stack and stack[-1] == comp[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False
                

