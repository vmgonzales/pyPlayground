class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # Careful! Bijection means one-to-one mapping!
        
        # Split s into words; must assign s to the result of s.split().
        s = s.split()
        
        # Check the operation above
        #print(s)
        
        # 
        if len(pattern) != len(s): return False
        
        # Create a dictionary for O(1) lookup.
        patDict = {}
        
        for i in range(len(pattern)):
            #print(i, pattern[i], s[i])
            if pattern[i] not in patDict:
                
                # This checks for potential duplicate value (from s), ensuring one-to-one mapping
                if s[i] in patDict.values(): return False
                
                patDict[pattern[i]] = s[i]
                
            else:
                if patDict[pattern[i]] != s[i]:
                    return False
        return True