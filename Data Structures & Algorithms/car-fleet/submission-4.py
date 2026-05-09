class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [[p,s] for p,s in zip(position, speed)]

        time = 0
        count = 0
        for p,s in sorted(fleet, reverse=True):
            if time < (target - p) / s:
                count += 1
                time = (target - p )/s
        
        return count



        