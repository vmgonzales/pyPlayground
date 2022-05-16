class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max = sum(accounts[0])
        
        for i in range(1, len(accounts)):
            rowSum = sum(accounts[i])
            if rowSum > max:
                max = rowSum
        
        return max