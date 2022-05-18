class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        index = 0
        while index < len(word1) and index < len(word2):
            ans += word1[index]
            ans += word2[index]
            index += 1
        
        for i in range(index, len(word1)):
            ans += word1[i]
        for i in range(index, len(word2)):
            ans += word2[i]
        
        return ans