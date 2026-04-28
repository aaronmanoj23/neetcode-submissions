class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(int(i))          
            else:
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                    
                elif i == "-":
                    stack.append(stack.pop(-2)- stack.pop())
                    
                elif i == "*":
                    stack.append(stack.pop()*stack.pop())

                elif i == "/":
                    stack.append(int(stack.pop(-2)/stack.pop()))   
                        

        return stack[0]

                    
                        

                



                        
        