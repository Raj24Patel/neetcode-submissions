class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        v = []
        
        for n in nums:
            counts[n] = counts.get(n,0) + 1

        for n in range(len(nums)+1):
            v.append([])

        
        for num, cnt in counts.items():
            v[cnt].append(num)

        
        res = []

        for i in range(len(v)-1,0,-1):
            for num in v[i]:
                res.append(num)
                if len(res) == k:
                    return res
