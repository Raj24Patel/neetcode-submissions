class Solution:
    def isValid(self, s: str) -> bool:
        idnt = {')':'(', '}':'{', ']':'['}#O(1)
        stack = []

        for para in s:
            if para in idnt:
                #check if its in stack[-1]
                if stack and idnt[para] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(para)
        
        return len(stack) == 0


        