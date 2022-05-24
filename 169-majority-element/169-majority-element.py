class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] = dict[num] + 1
        
        #print(dict)
        maxKey = max(dict, key=dict.get)
        if dict[maxKey] > math.floor(len(nums) / 2):
            return maxKey
        else: return 0
    