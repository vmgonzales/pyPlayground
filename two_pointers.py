# -*- coding: utf-8 -*-
'''
Two Pointers Patterns
=====================

Big Idea: 


Topics Covered
==============

* Two pointer algorithms

Created on Fri May 27 05:39:44 2022

@author: vmgon
'''


#%% LeetCode 42: Trapping Rain Water

# This solution seems to work, but it exceeds the time limit
#class Solution:
    # def trap(self, height: List[int]) -> int:
        
    #     ans = 0
        
    #     # Proceed layerwise, from the bottom
    #     while height:
            
    #         thisRow = 0
            
    #         # Chop off the ends
    #         while height and height[0] == 0:
    #             del height[0]
    #         while height and height[-1] == 0:
    #             del height[-1]
                
    #         # Count all the fillable spaces, and subtract one level
    #         for i in range(len(height)):
    #             if height[i] == 0:
    #                 thisRow += 1
    #             if height[i] > 0:
    #                 height[i] -= 1
            
    #         ans += thisRow
            
    #     return ans

from typing import List

# Time limit STILL exceeded!
# class Solution:           
#     def trap(self, height: List[int]) -> int:
        
#         ans = 0
        
#         # Chop off the ends
#         while height and height[0] == 0:
#             del height[0]
#         while height and height[-1] == 0:
#             del height[-1]
        
#         if len(height) <= 2: return 0
        
#         # Proceed left-to-right, omitting first and last blocks
#         maxL, maxR = height[0], height[-1]
#         for i in range (1, len(height) - 1):
            
#             maxL = max(maxL, height[i - 1])
            
#             # Find new maxR... have to use loop!
#             maxR = 0
#             for j in range (i+1, len(height)):
                
#                 if height[j] > maxR:
#                     maxR = height[j]
        
#             thisCol = max(0, min(maxL, maxR) - height[i])
#             ans += thisCol
#             #print('Col', i, thisCol, 'maxL', maxL, 'maxR', maxR, 'height',
#                   #height, 'Ans so far:', ans)
            
#         return ans
    
class Solution:           
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += max(0, min(maxL, maxR) - height[l])
                
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += max(0, min(maxL, maxR) - height[r])
        
        return res


print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap(height = [4,2,0,3,2,5]))
print(Solution().trap(height = [0, 1, 0]))
print(Solution().trap(height = [0, 1, 1, 2, 3, 0]))
print(Solution().trap(height = [5, 0, 1, 0, 5]))

#%% LeetCode 125: Valid Palindrome

# Solution with no pointers. Cleans string, then compares it to reversed string.
# Runtime: 86.92%, but memory 21.67%

# class Solution:
#   def isPalindrome(self, s: str) -> bool:

#     # Remove punctuation
#     s = re.sub(r'[^a-zA-Z0-9]+', '', s)

#     # Force lowercase
#     s = s.lower()

#     return s == s[::-1]

import re

# Here's another solution with two pointers
#Runtime 90.93%, Memory 26.95%

# class Solution:
#   def isPalindrome(self, s: str) -> bool:

#     # Remove punctuation
#     s = re.sub(r'[^a-zA-Z0-9]+', '', s)

#     # Force lowercase
#     s = s.lower()

#     first, last = 0, len(s)-1
#     while first < last:
#         if s[first] != s[last]: return False
#         first += 1
#         last -=1
    
#     return True

# Trying to further improvements...
# Runtime terrible! 5.04%, memory 46.09%
class Solution:
    def isPalindrome(self, s: str) -> bool:
                
        first, last = 0, len(s)-1
        while first < last:
            # In Python, if you want to call a function inside an object,
            # you have to use self.
            while first < last and not self.alphaNum(s[first]):
                first += 1
            while first < last and not self.alphaNum(s[last]):
                last -= 1
                
            if s[first].lower() != s[last].lower(): return False
            first += 1
            last -=1
        
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))

# Test cases
print(Solution().isPalindrome(s = "abba"), 'True')
print(Solution().isPalindrome(s = "abcd"), 'False')
print(Solution().isPalindrome(s = "abcdedcba"), 'True')
print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"), 'True')
print(Solution().isPalindrome(s = "race a car"), 'False')
print(Solution().isPalindrome(s = " "), 'True')
print(Solution().isPalindrome(s = "0P"), 'False')
