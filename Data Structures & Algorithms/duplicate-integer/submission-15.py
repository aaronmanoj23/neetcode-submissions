class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        bag = set()

        for num in nums:
            if num not in bag:
                bag.add(num)
            else:
                return True
        
        return False