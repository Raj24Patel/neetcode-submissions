class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key result, value index

        key = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in key:
                return [key[res], i]
            
            key[n] = i


        