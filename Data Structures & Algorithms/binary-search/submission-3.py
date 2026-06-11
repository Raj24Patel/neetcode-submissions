class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) -1#6

        while l <= r:
            mid = (l + r) // 2 #3
            if nums[mid] < target:#4
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid



        return -1
