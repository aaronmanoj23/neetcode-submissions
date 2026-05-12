class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append([p, s])
        
        cars = sorted(cars, key = lambda x: x[0], reverse = True)
        
        fleets = []
        
        for car in cars:
            time = (target - car[0]) / car[1]
            if len(fleets) == 0 or time > fleets[-1]:
                fleets.append(time)
            
        return len(fleets)
        
        