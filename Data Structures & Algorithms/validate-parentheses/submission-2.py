class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for i in s:

            if i in mapping:
                if len(stack):
                    top = stack.pop()
                else:
                    top = '#'
                if top != mapping[i]:
                    return False
            else:
                stack.append(i)
        return True if len(stack)==0 else False