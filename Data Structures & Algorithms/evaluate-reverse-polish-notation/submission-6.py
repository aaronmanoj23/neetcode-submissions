class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack=[]
        operations=["+","*","/","-"]
        for i,t in enumerate(tokens):
            if t not in operations:
                numStack.append(int(t))
            if t in operations:
                n1=numStack.pop()
                n2=numStack.pop()
                if t=="+":
                    res=n1+n2
                elif t=="-":
                    res=n2-n1
                elif t=="*":
                    res=n2*n1
                elif t=="/":
                    res=int(n2/n1)
                numStack.append(res)
        return int(numStack[0])