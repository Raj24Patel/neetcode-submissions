class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for ind, val in enumerate(nums):
            if val > 0:
                break

            
            if ind > 0 and val == nums[ind - 1]:
                continue
            
            l = ind + 1
            r = len(nums) -1
            while l < r:
                cursum = val + nums[l] + nums[r]
                if cursum > 0:
                    r -= 1
                elif cursum < 0:
                    l += 1

                else:
                    res.append([val, nums[l], nums[r]])
                    l+= 1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+= 1
        return res
        

            


        