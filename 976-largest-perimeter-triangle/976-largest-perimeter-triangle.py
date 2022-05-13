class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        for i in range(3,len(nums)+1):
            if(nums[i-3] < nums[i-2] + nums[i-1]):
                return sum(nums[i-3:i])
        return 0
            



# # Brute force -- O(n^3) -- time limit exceeded!
# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums.sort()
#         maxLen = 0
        
#         # First, consider nums lists of length 3, no iteration required.
#         if len(nums) == 3:
#             if nums[2] < nums[0] + nums[1]: return sum(nums)
#             else: return 0
        
#         # Next, consider nums lists longer than 3
#         for i in range(len(nums)):
#             for k in range(len(nums) - 1, i, -1):
#                 for j in range(i+1, k):
#                     #print(i, j, k)
#                     curSum = nums[i] + nums[j] + nums[k]
#                     if nums[k] < nums[i] + nums[j] and curSum > maxLen:
#                         maxLen = curSum
#        
#        return maxLen