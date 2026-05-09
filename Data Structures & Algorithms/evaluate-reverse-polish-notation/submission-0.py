class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            #Operations
            if token == '+':
                stack.append(stack.pop() + stack.pop())

            elif token == '-':
                #[ 5, 6, -]
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif token == '*':
                stack.append(stack.pop() * stack.pop())

            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            
            #Number 
            else:
                stack.append(int(token))
        
        return stack[0]

        