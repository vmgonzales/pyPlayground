# -*- coding: utf-8 -*-
"""
Created on Mon May  2 07:24:59 2022

@author: vmgon
"""

from typing import List
from typing import Optional

#%% LeetCode 1: Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0, len(nums)):
            for j in range(i+1, len(nums)):
                # print('[', i, j,']', nums[i], nums[j], '=', (nums[i] + nums[j]), '?=', target)
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))


#%% LeetCode 2: Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __len__(self):
        return self.item_count

# This solution works in Spyder, but not in the LeetCode console. Not sure why!
# class Solution:
#     def addTwoNumbers(self, l1, l2) -> List[int]:
#         l3 = []
#         carryDigit = 0
#         while l1 or l2:
#             newDigit = carryDigit
#             carryDigit = 0
            
#             #print(l1, l2, l3)
#             if len(l1) > 0:
#                 newDigit += l1.pop(0)
#             if len(l2) > 0:
#                 newDigit += l2.pop(0)
#             if newDigit >= 10:
#                 carryDigit += 1
#                 newDigit -= 10
#             l3.append(newDigit)
#         if carryDigit > 0:
#             l3.append(1)
#         return l3


# This solution is not mine, but it works.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            
            val = carry + v1 + v2
            res.next = ListNode(val%10)
            res, carry = res.next, val//10
            
        if carry:
            res.next = ListNode(carry)
            
        return dummy.next
    

print(Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
print("\n")
print(Solution().addTwoNumbers(l1 = [0], l2 = [0]))
print("\n")
print(Solution().addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))


#%% LeetCode 4: Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two arrays while maintaining sort
        nums1 += nums2
        nums1.sort()
        
        # Find median -- case odd number of elements
        if len(nums1) % 2 != 0:
            medianIndex = len(nums1) // 2
            median = nums1[medianIndex]
            return median
        
        # Find median -- case even number of elements
        else:
            medianIndex = len(nums1) // 2
            median = (nums1[medianIndex - 1] + nums1[medianIndex]) / 2
            return median

print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))


#%% LeetCode 9: Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         
#         #print("X = ", x)
#         if(x < 0):
#             #print("Less than zero.")
#             return False
#         
#         if(x == 0):
#             #print("Zero.")
#             return True
#         
#         x = str(x)
#         #print("X = ", x, "Length = ", len(x))
#         
#         if (len(x) == 1):
#             return True
# 
#         elif ((len(x) == 2) and (x[0] == x[1])):
#             return True
#         
#         elif ((len(x) == 2) and (x[0] != x[1])):
#             return False
#                 
#         elif(x[0] == x[len(x) - 1]):
#             nextX = x[1: len(x) - 1]
#             nextX = int(nextX)
#             print("Initiating recursion, X, NextX = ", x, nextX)
#             return(self.isPalindrome(nextX))
#           
#         else:
#             return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
                
                #print("X = ", x)
        if(x < 0):
            #print("Less than zero.")
            return False
                
        if(x == 0):
            #print("Zero.")
            return True
                
        x = str(x)

        return x == x[::-1]

print(Solution().isPalindrome(x = -1234))
print(Solution().isPalindrome(x = 10))
print(Solution().isPalindrome(x = 1234))
print(Solution().isPalindrome(x = 123432))
print(Solution().isPalindrome(x = 0))
print(Solution().isPalindrome(x = 1))
print(Solution().isPalindrome(x = 101))
print(Solution().isPalindrome(x = 1234321))

print(Solution().isPalindrome(x = 1000021))


#%% LeetCode 12: Integer to Roman


#%% LeetCode 13: Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
          'M': 1000}
        
        last = s[-1]
        for t in reversed(s):
          #print(t, last)
          if t == 'C' and last in ['D', 'M']:
            total -= roman[t]
            
          elif t == 'X' and last in ['L', 'C']:
            total -= roman[t]
            
          elif t == 'I' and last in ['V', 'X']:
            total -= roman[t]
            
          else:
            total += roman[t]
          last = t
          
        return total


print(Solution().romanToInt(s = 'I'), '\n')

print(Solution().romanToInt(s = 'IV'))
print(Solution().romanToInt(s = 'V'))
print(Solution().romanToInt(s = 'VI'), '\n')

print(Solution().romanToInt(s = 'IX'))
print(Solution().romanToInt(s = 'X'))
print(Solution().romanToInt(s = 'XI'), '\n')

print(Solution().romanToInt(s = 'XL'))
print(Solution().romanToInt(s = 'LI'))
print(Solution().romanToInt(s = 'LIII'), '\n')

print(Solution().romanToInt(s = 'XCIII'))
print(Solution().romanToInt(s = 'C'))
print(Solution().romanToInt(s = 'MXCIV'))


#%% LeetCode 36: Valid Sudoku


from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        # Convert board from chars to integers
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == '.':
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
    
        # Check each row for digits in the range [1, 9] w/o repetition
        for i in range(9):
      
            thisRow = board[i]
            digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            #print("Looking at row: ", i)
      
            for j in range(9):
        
                if thisRow[j] in digits:
                    digits.remove(thisRow[j])
                elif thisRow[j] == 0:
                    pass
                else:
                    #print("Bad Row")
                    return False
        
        # Check each column for digits in the range [1,9] w/o repetition
        for j in range(9):
            
            thisCol = [row[j] for row in board]
            digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
      
            for i in range(9):
            
                if thisCol[i] in digits:
                    digits.remove(thisCol[i])
                elif thisCol[i] == 0:
                    pass
                else:
                    #print("Bad column.")
                    return False
        
        #Check each 3x3 sub-box for digits [1,9] w/o repetition
        for m in range(3):
            for n in range(3):
                digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                
                # Looking at each sub-box individually:
                for i in range(3):
                    for j in range(3):
                        
                        if board[i + 3 * m][j + 3 * n] in digits:
                            digits.remove(board[i + 3 * m][j + 3 * n])
                        elif board[i + 3 * m][j + 3 * n] == 0:
                            pass
                        else:
                            # print("Bad sub-box: ", m + 1, n + 1)
                            return False
        
        # If rows, columns, and 3x3 boxes are good --> puzzle is valid!
        return True

#%% LeetCode 36 test cases
# Valid sudoku test case
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))


# Bad row test case
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6","2",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

# Bad column test case.
board = [["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

# Another bad column test case
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
["6",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))


# Bad 3x3 box test case (lower right).
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","9","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))


#%% LeetCode 53: Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndingHere = maxSoFar = nums[0]
        
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
            
        return maxSoFar

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray(nums = [1]))
print(Solution().maxSubArray(nums = [5,4,-1,7,8]))


#%% LeetCode 387: First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        doubles = set()
        singles = set()
        
        # Identify singles set, i.e. unique characthers in s
        for i in range(len(s)):
            if s[i] in doubles:
                pass
            elif s[i] in singles:
                singles.remove(s[i])
                doubles.add(s[i])
            else:
                singles.add(s[i])
        
        # Return first element in singles
        for i in range(len(s)):
            if s[i] in singles:
                return i
            else:
                pass
        return(-1)


print(Solution().firstUniqChar(s = "leetcode"))
print(Solution().firstUniqChar(s = "loveleetcode"))
print(Solution().firstUniqChar(s = "aabb"))


#%% LeetCode 566: Reshape The Matrix

import numpy as np
#from numpy import reshape

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # Return original matrix if transformation is not possible
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        
        newMatrix = np.reshape(mat, (r, c))
        return newMatrix

print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))
#print(Solution().matrixReshape())