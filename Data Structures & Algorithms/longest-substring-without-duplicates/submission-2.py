class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        index_doublon = 0
        if n==0:
            return 0
        L=[1]*n
        tmp= s[0]
        for i in range(1,n):
            if s[i] not in tmp:
                tmp+=s[i]
                L[i]=len(tmp)                
            else:
                index_doublon = tmp.index(s[i])
                tmp=tmp[index_doublon+1:]
                tmp=tmp+s[i]
                L[i]=max(L)
                print(tmp)
        return max(L)
