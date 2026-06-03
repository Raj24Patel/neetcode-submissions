class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ht = {}
        Hs = {}

        for i in s:
            Hs[i] = Hs.get(i, 0) + 1
        
        for i in t:
            Ht[i] = Ht.get(i,0)+1
        
        return True if Ht == Hs else False