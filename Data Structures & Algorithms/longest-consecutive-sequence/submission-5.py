class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        if len(num) == 0:
            return 0 

        res = 1

        for n in nums:
            if n in num:
                length = 1
                while (n + length) in num:
                    res = max(res, length+1)
                    length += 1
        
        return res