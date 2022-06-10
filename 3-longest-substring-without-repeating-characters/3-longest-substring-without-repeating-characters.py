class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Test for edge cases and return appropriate values
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        
        # Initialize a set for letters in the current word, and value for max and current word length
        curChars = set(s[0])
        maxLen, curLen = 1, 1
        startCurWord = 0
        last = 0
        
        # Iterate through all characters after s[0]
        for i in range(1, len(s)):
            #print('Preview, Index', i, 'Last word', s[startCurWord:startCurWord + curLen], curLen, maxLen, curChars)
            # No duplicate detected
            if s[i] not in curChars:
                curLen += 1
                curChars.add(s[i])
            
            # Duplicate detected
            else:
                startCurWord += 1
                while s[startCurWord - 1] != s[i]:
                    curChars.remove(s[startCurWord - 1])
                    startCurWord += 1
                    
                curLen = i - startCurWord + 1
                            
            if curLen > maxLen:
                maxLen = curLen
            
            #print('Index', i, 'Current word', s[startCurWord:startCurWord + curLen], curLen, maxLen)
        return maxLen