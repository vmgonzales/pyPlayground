class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][len(mat) - i - 1]
        
        # Subtract the middle element, which was counted twice (odd sizes only)
        if len(mat) % 2 == 1:
            sum -= mat[len(mat) // 2][len(mat) // 2]
        
        return sum