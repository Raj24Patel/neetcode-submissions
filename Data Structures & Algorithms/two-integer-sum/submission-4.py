class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in check:
                return [check[ans], i]

            check[nums[i]] = i
        