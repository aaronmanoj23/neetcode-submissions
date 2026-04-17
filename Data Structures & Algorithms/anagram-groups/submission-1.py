class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for str in strs:
            str1 = tuple(sorted(str))
            anagrams[str1].append(str)
        
        return list(anagrams.values())