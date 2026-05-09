class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftm = height[l]
        rightm = height[r]
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                leftm = max(leftm, height[l])
                res += leftm - height[l]


            else:
                r -= 1
                rightm = max(rightm, height[r])
                res += rightm - height[r]
        
        return res