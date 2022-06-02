class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        print(m,n)
        
        # Ensure matrix is square!
        if m > n:
            for i in range(m):
                matrix[i] = matrix[i] + [0] * (m - n)
        elif m < n:
            for i in range(n-m):
                matrix = matrix + [[0] * n]
        
        # Proceed with matrix transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Return matrix to original size
        if m > n:
            matrix = matrix[:n]
        elif m < n:
            for k in range(n):
                matrix[k] = matrix[k][:m]
        
        return matrix