class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0 , len(numbers) - 1

        while l < r:
            sumN = numbers[l] + numbers[r]
            if sumN < target:
                l += 1
            if sumN > target:
                r -=1
            if sumN == target:
                return [l+1, r+1]
        