class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        pastN = set()
        newN = n
        limit = 30
        count = 0
        
        while newN not in pastN and count < limit:
            
            digits = []
            pastN.add(newN)
            
            for i in str(newN):
                i = (int(i) ** 2)
                digits.append(i)
                
            newN = sum(digits)
            
            if newN == 1: return True
            count += 1
        return False