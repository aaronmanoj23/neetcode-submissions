class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {}

        for num in nums:

            if num not in count:
                count[num] =1
            else:
                count[num] +=1
            
        bucket = [[] for i in range(len(nums) + 1)]

        for key,value in count.items():

            bucket[value].append(key)
        
        results = []

        for num in reversed(bucket):

            if len(num) == 0:
                continue

            if len(results) < k:
                for n in num:
                    results.append(n)
            if len(results) == k:
                return results




