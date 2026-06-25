class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        
        for character in strs:
            ordval = [0] * 26
            for ch in character:
                ordval[ord(ch) - ord('a')]  += 1
            
            anagram[tuple(ordval)].append(character)
        
        return list(anagram.values())
            



        