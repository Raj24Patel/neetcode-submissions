class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2
            #left neighbor
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            #right neighbor
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = l + 1
            else:
                return m 
        
        