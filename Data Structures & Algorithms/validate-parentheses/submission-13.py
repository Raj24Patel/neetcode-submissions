class Solution:
    def isValid(self, s: str) -> bool:
        checker = {')' : '(', ']':'[', '}':'{'}
        stack = []
        
        for paran in s:
            if paran in checker and stack:
                if stack[-1] != checker[paran]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(paran)
        
        return True if len(stack) == 0 else False
