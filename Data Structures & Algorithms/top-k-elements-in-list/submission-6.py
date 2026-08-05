class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:

            if num not in count:
                count[num] = 1
            else:
                count[num] +=1
        
        bucket = [[] for i in range(1, len(nums)+2)]

        for key,value in count.items():

            bucket[value].append(key)

        results = []

        for i in reversed(range(len(bucket))):

            for j in bucket[i]:
                if len(results) < k:
                    results.append(j)
                if len(results) == k:
                    return results




