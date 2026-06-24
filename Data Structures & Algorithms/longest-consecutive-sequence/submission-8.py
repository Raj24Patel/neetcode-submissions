class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)

        res = 0

        for n in nums:
            if (n - 1) not in num:
                length = 1
                while (n + length) in num:
                    length += 1
                res = max(length, res)
        
        return res