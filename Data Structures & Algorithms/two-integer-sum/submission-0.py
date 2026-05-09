class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in prev:
                return [prev[diff], index]
            
            prev[value] = index
        