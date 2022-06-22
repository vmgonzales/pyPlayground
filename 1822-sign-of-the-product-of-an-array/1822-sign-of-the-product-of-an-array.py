class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if nums.count(0) > 0:
            return 0
        negCount = len([i for i in nums if i < 0])
        #print('Negatives:', negCount)
        if negCount % 2 == 1:
            return -1
        else: return 1