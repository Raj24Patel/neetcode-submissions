class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (n*2)
        for i in range(n):
            res[i] = nums[i]
            res[i+n] = nums[i]
        
        return res

        """
        list. = []
        n = 3
        indx =  [ 0 1 2 3 4 5]
        list =  [ 1 ? ? 1 ? ?]
        list =  [ 1 2 ? 1 2 ?]
        """
        