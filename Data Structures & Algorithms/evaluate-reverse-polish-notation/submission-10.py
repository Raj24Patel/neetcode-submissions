class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            if i == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(int(a)+int(b))

            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b)-int(a))
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/int(a)))

            elif i == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b)*int(a))

            else:
                stack.append(int(i))
        
        return stack[0]
    