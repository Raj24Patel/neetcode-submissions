class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mark = {}

        for ind, val in enumerate(nums):
            
            total = target - val
            
            if total in mark:
                return [mark[total], ind]
            
            mark[val] = ind

        
        return False
        