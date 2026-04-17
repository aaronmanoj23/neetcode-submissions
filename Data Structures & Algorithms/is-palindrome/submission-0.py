class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        backwards = ""

        for i in s[::-1]:
            backwards += i

        if backwards == s:
            return True
        else:
            return False
