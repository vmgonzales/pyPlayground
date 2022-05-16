class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
        
        for j in range(zeros):
            nums += [0]
        
        while zeros > 0:
            nums.remove(0)
            zeros -= 1