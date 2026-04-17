class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        output = []
        for str in strs:
            str1 = tuple(sorted(str))

            if str1 not in anagrams:
                anagrams[str1] = []

            anagrams[str1].append(str)
        
        for key in anagrams:
            output.append(anagrams[key])
        
        return output