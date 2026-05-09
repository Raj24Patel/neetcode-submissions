class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force  =

        x = {}

        for i, v in enumerate(nums):
            match = target - v
            if match in x:
                return [x[match],i]
            
            x[v] = i


        