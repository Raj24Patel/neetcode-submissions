class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 ... 25
        # p // ... . ciel
        # ^ <= h -> res

        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r-l) //2

            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/mid)
            
            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
