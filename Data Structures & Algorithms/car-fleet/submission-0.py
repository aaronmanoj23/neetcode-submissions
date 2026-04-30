class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        carmap = {}

        for i in range(len(position)):
            carmap[position[i]] = speed[i]
        
        for position, speed in sorted(carmap.items(), reverse = True):
            
            time = (target-position)/speed

            if not stack:

                stack.append(time)
            else:

                if time > stack[-1]:

                    stack.append(time)
            
        return len(stack)




    


        


