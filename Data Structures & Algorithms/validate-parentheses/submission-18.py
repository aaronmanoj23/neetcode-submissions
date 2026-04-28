class Solution:
    def isValid(self, s: str) -> bool:
        
        match = {"(": ")", "[": "]", "{": "}"}

        stack = []
        
        if len(s) == 1:
            return False
            
        for char in s:
            
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if len(stack) == 0:
                    return False
                elif char == match[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False
            
        return True