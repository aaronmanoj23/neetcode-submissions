class Solution:
    def isValid(self, s: str) -> bool:
        

        match = {")": "(", "]":"[", "}": "{"}

        stack = []

        for char in s:

            if char in match:

                if not stack:
                    return False

                top = stack.pop()

                if match[char] != top:
                    return False

            else:

                stack.append(char)
            

        if stack:
            return False
        else:
            return True