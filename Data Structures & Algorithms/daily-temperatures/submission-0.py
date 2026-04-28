class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = []

        for i in range(len(temperatures)):

            for j in range(i, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    results.append(j-i)
                    break
            else:
                results.append(0)
        
        return results

        