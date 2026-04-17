class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {target: []}
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!= j:
                    if nums[i] + nums[j] == target:
                        dict[target].append(i)
                        dict[target].append(j)
                        return dict[target]
                    
        


                



        