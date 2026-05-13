class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        nonrepeat = set()
        most_len = 0
        l = 0
        for i,c in enumerate(s):
            while c in nonrepeat:
                # CLEAN UP
                nonrepeat.remove(s[l])
                l +=1
            
            nonrepeat.add(c)

            
            most_len = max(most_len,i-l+1)
        
        return most_len

