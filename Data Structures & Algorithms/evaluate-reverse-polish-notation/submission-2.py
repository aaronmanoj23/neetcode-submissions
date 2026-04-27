class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                top, btm = stack.pop(), stack.pop()
                stack.append(btm - top)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                top, btm = stack.pop(), stack.pop()
                stack.append(int(btm / top))
            else:
                stack.append(int(token))
        return stack[0]