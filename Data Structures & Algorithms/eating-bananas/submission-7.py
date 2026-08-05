import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        least = r = max(piles)
        
        count = 0

        while l <= r:
            k = (l + r) // 2

            for bananas in piles:
                x = math.ceil(bananas/k) 
                count += x
            
            if count <= h:
                least = min(least, k)
                r = k - 1
            else: 
                l = k + 1

            count = 0
        
        return least
            


            