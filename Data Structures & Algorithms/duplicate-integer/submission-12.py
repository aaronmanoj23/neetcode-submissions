class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        bag = []

        for num in nums:
            if num not in bag:
                bag.append(num)
            elif num in bag:
                return True
        
        return False