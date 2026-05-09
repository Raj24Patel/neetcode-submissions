class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = [[p,s] for p,s in zip(position, speed)]

        time = 0

        count = 0

        for p,s in sorted(fleets, reverse=True):
            reached = (target - p) / s
            if reached > time:
                time = reached
                count += 1

        
        return count

        