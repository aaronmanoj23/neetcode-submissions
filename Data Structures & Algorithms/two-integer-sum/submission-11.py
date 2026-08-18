class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashS = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in hashS:
                return [hashS[diff], i]
            else:
                hashS[nums[i]] = i
        