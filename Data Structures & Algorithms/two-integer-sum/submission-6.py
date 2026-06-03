class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            sol = target - n
            if sol in res:
                return[res[sol],i]
            
            res[n] = i 
        