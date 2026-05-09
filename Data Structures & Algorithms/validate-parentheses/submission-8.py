class Solution:
    def isValid(self, s: str) -> bool:
        checker = {')':'(', '}':'{', ']':'['}

        stack = []

        for i in s:
            if i in checker:
                if stack and checker[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        
        return len(stack) == 0
        