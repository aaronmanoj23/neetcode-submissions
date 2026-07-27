class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for str in strs:

            sort = tuple(sorted(str))

            anagrams[sort].append(str)

        return list(anagrams.values())