class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstOne, lastOne = 0, len(nums) - 1
        i = 0
        
        while i <= lastOne:
            if nums[i] == 0:
                nums[i], nums[firstOne] = nums[firstOne], nums[i]                    
                firstOne += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[lastOne] = nums[lastOne], nums[i]
                lastOne -= 1
            
        return nums