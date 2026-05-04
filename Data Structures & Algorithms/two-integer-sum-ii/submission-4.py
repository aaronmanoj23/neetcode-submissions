class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        prev = {}
        res = []

        for i in range(len(numbers)):
        
            diff = target - numbers[i]
        
            if numbers[i] not in prev:
                prev[numbers[i]] = i +1
            
            if diff in prev:
                if diff != numbers[i]:
                    res.append(prev[diff])
                    res.append(prev[numbers[i]])
                    return res
