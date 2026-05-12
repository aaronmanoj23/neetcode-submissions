class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+':lambda x, y: int(x)+int(y),
                '-':lambda x, y: int(x)-int(y),
                '*':lambda x, y: int(x)*int(y),
                '/':lambda x, y: int(x)/int(y)}
        opstack = []
        for c in tokens:
            if c in ops.keys():
                y = opstack.pop()
                x = opstack.pop()
                ans = ops[c](x, y)
                opstack.append(ans)
            else:
                opstack.append(c)
        return int(opstack[0])