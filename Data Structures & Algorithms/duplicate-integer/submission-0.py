class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_set = set()
        for i in nums:
            if i in h_set:
                return True
            h_set.add(i)
        
        return False

         