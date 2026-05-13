class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        if len(s)==1:
            return 1
        count=0
        max1=0
        prev=0
        length=0
        for j in range(len(s)):
            length=j
            while length<len(s):

                for i  in range(length,len(s),1):
                    ch=s[i]
                    if ch  in s[length:length+count]:
                        prev=max(prev,count)
                        length+=count
                        count=0
                        break
                    else:
                        count+=1
                        prev=max(prev,count)
            max1=max(max1,prev)    
        return max1



        