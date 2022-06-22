class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        # Make a dictionary for O(1) lookup
        ans = ''
        dict = {}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(1, 27):
            dict[i] = alpha[i-1]
        
        j = len(s) - 1
        while j >=0:
            
            if s[j] == '#':
                char = s[j-2:j]
                j -= 3
            else:
                char = s[j]
                j -= 1
            num = int(char)
            ans = dict[num] + ans
        
        return ans
        