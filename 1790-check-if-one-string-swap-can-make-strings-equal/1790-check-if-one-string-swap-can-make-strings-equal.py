class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swapIndex = []
        if s1 == s2: return True
        if len(s1) != len(s2): return False
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                swapIndex.append(i)
        if len(swapIndex) != 2: return False
        
        elif s1[swapIndex[0]] == s2[swapIndex[1]] and s1[swapIndex[1]] == s2[swapIndex[0]]:
            return True
        
        else:
            return False