import numpy as np
#from numpy import reshape

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # Return original matrix if transformation is not possible
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        
        newMatrix = np.reshape(mat, (r, c))
        return newMatrix
    