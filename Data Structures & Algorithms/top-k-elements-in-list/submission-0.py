class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i = 0
        counter = {i: nums.count(i) for i in nums}
         
        freq = []
        
        while i < k:
            top = max(counter, key=lambda k: counter[k])
            freq.append(top)
            counter.pop(top)

            i += 1


        return freq