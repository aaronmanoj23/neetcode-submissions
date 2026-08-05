class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        count = {}

        for num in nums:

            if num not in count:
                count[num] = 1
            else:
                count[num] +=1
            
        freq = [[] for _ in range(len(nums)+1)]

        for num,cnt in count.items():
            freq[cnt].append(num)

        result = []

        for i in range(len(freq)-1, 0, -1):

            if len(freq[i]) == 0:
                continue
            else:
                for num in freq[i]:
                    if len(result) < k:
                        result.append(num)
                    
            if len(result) == k:
                return result
            
