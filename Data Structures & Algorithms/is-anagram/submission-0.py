class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        CountT, CountS = {}, {}

        for i in range(len(s)):
            CountT[t[i]] = 1 + CountT.get(t[i], 0) #.get() if the letter never existed in the hashmap then we would get key val error so .get lets us set default to 0 
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
        
        for i in CountT:
            if CountT[i] != CountS.get(i,0):
                return False

        return True

        