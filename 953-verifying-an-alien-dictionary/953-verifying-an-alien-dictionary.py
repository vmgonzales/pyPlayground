class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        if len(words) == 1: return True
        
        # Big idea--
        # First: translate aline words into English,
        # Then: use built-in python sort methods
        
        # Make dictionary for O(1) lookup of alphabet and alien letter order
        alpha, dict = {}, {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(0, 26):
            dict[order[i]] = i+1
            alpha[i+1] = alphabet[i]
        
        newWords = []
        for word in words:
            #print(word)
            newWord = ''
            for char in word:
                newWord += alpha[dict[char]]
                
                # This assignment doesn't work:
                #char = alpha[dict[char]]
            #print(newWord)
            newWords += [newWord]
        
        
        # Use sorted() here, not .sort()
        if newWords == sorted(newWords):
            return True
        else:
            return False