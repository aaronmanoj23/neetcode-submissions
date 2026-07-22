class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = {}
        results = []
        for str in strs:

            key = ''.join(sorted(str))
            
            if key not in hash:
                hash[key] = []
            
            hash[key].append(str)

        for values in hash:
            results.append(hash[values])
        
        return results
        
        