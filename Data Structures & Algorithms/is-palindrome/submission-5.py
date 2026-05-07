class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ss = s.replace(" ", "")

        l, r = 0, len(ss) - 1

        while l<r:

            
            if ss[l].isalnum() and ss[r].isalnum() is False:
                r-=1
            elif ss[l].isalnum() is False and ss[r].isalnum():
                l+=1
            elif ss[l].isalnum() and ss[r].isalnum():
                
                if ss[l].lower() == ss[r].lower():
                    l += 1
                    r -=1 
                
                else:
                    return False
            else:
                l+=1
                r-=1
        
        return True

        


        