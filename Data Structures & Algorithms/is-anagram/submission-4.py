class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}

        for i in s:
            sHash[i] = sHash.get(i, 0) + 1
        
        for i in t:
            tHash[i] = tHash.get(i, 0) + 1
        
        return True if tHash == sHash else False
        