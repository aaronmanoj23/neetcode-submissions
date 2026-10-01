class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        bag = []

        for num in nums:
            if num in bag:
                return True
            else:
                bag.append(num)
        
        return False