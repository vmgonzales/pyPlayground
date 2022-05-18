class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Boundary case
        if n == 0: return False
        if n < 0: return False
    
        logThree = log(n) / log(3)
        
        #print(logThree, round(logThree))
        if isclose(logThree, round(logThree), rel_tol=1e-12): return True
        else: return False