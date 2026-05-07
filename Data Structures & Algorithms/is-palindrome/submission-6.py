class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = ''.join(c.lower() for c in s if c.isalnum())

        l,r = 0, len(newS) -1

        while l<r:

            if newS[l] != newS[r]:

                return False
            
            else:

                l+=1
                r-=1
        
        return True