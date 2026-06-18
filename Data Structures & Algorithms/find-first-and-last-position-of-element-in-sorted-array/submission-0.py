class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.BinarySearch(nums, target, True)
        right = self.BinarySearch(nums, target, False)
        return [left, right]


    def BinarySearch(self, nums, target, LeftBias):
        l = 0
        r = len(nums) - 1
        i = -1

        while l <= r:
            m =  l + ( r-l) //2 

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                i = m 
                if LeftBias:
                    r = m - 1
                else:
                    l  = m + 1 
        
        return i


        