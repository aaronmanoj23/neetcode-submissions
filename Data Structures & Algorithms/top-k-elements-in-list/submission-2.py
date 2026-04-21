class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        arr = []
        for n, occ in count.items():
            arr.append([n, occ])
        arr.sort(key=lambda x: -x[1])
        results = []
        for i in range(k):
            results.append(arr[i][0])
        return results
         