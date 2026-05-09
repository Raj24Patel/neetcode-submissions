class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        l1 = [0] * 26
        l2 = [0] * 26

        for i in range(n1):
            l1[ord(s1[i]) - 97] += 1
            l2[ord(s2[i]) - 97] += 1

        if l1 == l2:
            return True

        
        for i in range(n1,n2):
            l2[ord(s2[i]) - 97] += 1
            l2[ord(s2[i-n1]) - 97] -= 1
            if l1 == l2:
                return True

        
        return False
