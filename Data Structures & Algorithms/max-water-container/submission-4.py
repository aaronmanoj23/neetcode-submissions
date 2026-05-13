class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        greatest = 0

        l = 0

        while l < len(heights) -1:
            r = l +1
            
            while r < len(heights):

                area = min(heights[l], heights[r]) * (r - l)

                if area > greatest:
                    greatest = area

                r +=1
            
            l +=1

        return greatest

