class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        stack = []
    
        for num in nums:
            if num not in stack:
                stack.append(num)
            else:
                return True
        
        return False
