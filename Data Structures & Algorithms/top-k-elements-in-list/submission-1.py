class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        result = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] +=1
        print(count)

        while k > 0:
            top_count = max(count, key = count.get)
            result.append(top_count)
            del count[top_count]
            k -= 1
        return result

         