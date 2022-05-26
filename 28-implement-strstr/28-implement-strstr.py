class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            run = 0
            while i + run < len(haystack) and haystack[i + run] == needle[run]:
                run += 1
                
                if run == len(needle):
                    return i
        
        return -1