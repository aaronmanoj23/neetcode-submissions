class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        prev = {"map": []}
        sortednums = sorted(set(nums))
        curr = 0

        for i in range(len(sortednums)):

            if len(prev["map"]) == 0:
                prev["map"].append(sortednums[i])

            elif sortednums[i] - max(prev["map"]) == 1:
                prev["map"].append(sortednums[i])

            else:
                if len(prev["map"]) > curr:
                    curr = len(prev["map"])
                prev["map"] = [sortednums[i]]

        curr = max(curr, len(prev["map"]))
        

        return curr







                

                