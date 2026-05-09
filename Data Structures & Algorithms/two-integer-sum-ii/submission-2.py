class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        cursum = numbers[r] + numbers[l]
        while l < r: 
            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            
            if cursum == target:
                return [l+1,r+1]
            

            cursum = numbers[r] + numbers[l]
        