class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        newArr = []

        for n in range(len(nums)):

            product = 1

            for i in nums[n +1:]:
                product *= i
            for i in nums[:n]:
                product *= i
            
            newArr.append(product)

                
            

        return newArr
            

