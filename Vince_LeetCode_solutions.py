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
        
    # def __len__(self):
    #     return self.item_count

# This solution works in Spyder, but not in the LeetCode console. Not sure why!
# Object of type ListNode has no len()
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



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carryDigit = 0
        while l1 or l2:
            nextDigit = carryDigit
            carryDigit = 0
            v1, v2 = 0, 0
            
            if l1:
                v1 = l1.val
                nextDigit += v1
                l1 = l1.next
                
            if l2:
                v2 = l2.val
                nextDigit += v2
                l2 = l2.next
                
            if nextDigit >= 10:
                carryDigit += 1
                nextDigit -= 10
            
            res.next = ListNode(nextDigit)
            res = res.next
        
        if carryDigit == 1:
            res.next = ListNode(1)
            res = res.next
                
        return dummy.next


# print(Solution().addTwoNumbers(l1 = ListNode([2,4,3]), l2 = ListNode([5,6,4]))) # --> [7,0,8]
# print("\n")
# print(Solution().addTwoNumbers(l1 = [0], l2 = [0])) # --> [0]
# print("\n")
# print(Solution().addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9])) # --> [8,9,9,9,0,0,1]


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
class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman = ''
        
        while num !=0:
            
            while num // 1000 > 0:
                roman += 'M'
                num -= 1000
            
            if num >= 900:
                roman += 'CM'
                num -= 900
            if num >= 500:
                roman += 'D'
                num -= 500
            if num >= 400:
                roman += 'CD'
                num -= 400
            while num // 100 > 0:
                roman += 'C'
                num -= 100
            if num >= 90:
                roman += 'XC'
                num -= 90
            if num >= 50:
                roman += 'L'
                num -= 50            
            if num >= 40:
                roman += 'XL'
                num -= 40
            while num // 10 > 0:
                roman += 'X'
                num -= 10
            if num == 9:
                roman += 'IX'
                num -= 9
            if num >= 5:
                roman += 'V'
                num -= 5
            if num == 4:
                roman += 'IV'
                num -= 4
            while num > 0:
                roman += 'I'
                num -=1
        return roman    

    # Attempt at a more elegant solution using a dictionary.
    # def intToRoman(self, num: int) -> str:
    #     intRoman = {
    #         1000: 'M',
    #         900: 'CM',
    #         500: 'D',
    #         400: 'CD',
    #         100: 'C',
    #         90: 'XC',
    #         50: 'L',
    #         40: 'XL',
    #         10: 'X',
    #         9: 'IX',
    #         5: 'V',
    #         4: 'IV',
    #         1: 'I'
    #         }
                    
    #     roman = ''
    
    # return roman


print(Solution().intToRoman(1))
print(Solution().intToRoman(3))
print(Solution().intToRoman(4))
print(Solution().intToRoman(5))
print('\n')
print(Solution().intToRoman(9))
print(Solution().intToRoman(10))
print(Solution().intToRoman(11))
print('\n')
print(Solution().intToRoman(49))
print(Solution().intToRoman(50))
print(Solution().intToRoman(55))
print('\n')
print(Solution().intToRoman(89))
print(Solution().intToRoman(90))
print(Solution().intToRoman(91))
print(Solution().intToRoman(98))
print(Solution().intToRoman(99))
print(Solution().intToRoman(100))

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


#%% LeetCode 14: Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        numStrings = len(strs)
        shortest = min(strs, key = len)
        
        if numStrings == 1:
            return strs[0]
        
        for letter in range(len(shortest)):
            for i in range(1, numStrings):
                if strs[i][letter] == strs[0][letter]:
                    if i == (numStrings - 1):
                        common += strs[0][letter]
                else: return common
        return common
        


print(Solution().longestCommonPrefix(strs = ['a']))
#print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))
#print(Solution().longestCommonPrefix(strs = ["dog","racecar","car"]))
#print(Solution().longestCommonPrefix(strs = ['rateres', 'raterasdgasf', 'rateieiei']))


#%% LeetCode 17: Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0: return []
        
        wordList = []
        dict = {2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y', 'z']}
        
        # I'm thinking this should be recursive.
        for i in range (len(digits)):
            for letter in dict[digits[i]]:
                wordList += (letter + letterCombinations ())
        
        return wordList
            
            


#%% LeetCode 20: Valid Parenthesis
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftBracketSet = {'(', '{', '['}
        rightBracketSet = {')', '}', ']'}
        bracketDict = {')': '(', '}': '{', ']': '['}
        stack = ''
        for i in s:
            #print('Looking at: ', i, '\n')
            if i in leftBracketSet:
                #print("Add to stack!")
                stack += i
            elif i in rightBracketSet and len(stack) == 0:
                return False
            elif i in rightBracketSet and len(stack) > 0:
                #print('Remove?', i, stack[-1])
                if bracketDict[i] == stack[-1]:
                    stack = stack[:-1]
                    #print('Remove: ', i, '\n')
                else:
                    #print('Not in stack!')
                    return False  
            else:
                pass
       
        #print("Last part!")
        if stack == '':
            return True
        else:
            return False



#%% LeetCode 21: Merge Two Sorted Lists
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

# This solutions works in Spyder, but not in LeetCode -- I blame the ListNode class.
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         list1 += list2
#         list1.sort()
#         return list1

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #print(list1)
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            #print(list1, list2, dummy, tail)
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list 1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next


# Test cases -- must define list1 and list2 as above!
(Solution().mergeTwoLists(list1, list2)).printNode()
#print(Solution().mergeTwoLists(list1 = [], list2 = []))
#print(Solution().mergeTwoLists(list1 = [], list2 = [0]))


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


#%% LeetCode 74: Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute forece -- check every element
        rows = len(matrix[0])
        cols = len(matrix)
        print(rows, cols)
        for i in range(rows * cols):
            if matrix[i//rows][i%rows] == target:
                return True
        return False

print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))


#%% LeetCode 83: Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        
        while pointer:
            if pointer.next and pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        
        return head


#%% LeetCode 88: Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
                

#%% LeetCode 118: Pascal's Triangle
from math import comb
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        allRows = []
        for i in range(numRows):
            rowI = []
            
            for j in range(i + 1):
                rowI.append(comb(i, j))
            
            allRows.append(rowI)
    
        return allRows

# Test cases:

print(Solution().generate(numRows = 1))
print(Solution().generate(numRows = 2))
print(Solution().generate(numRows = 3))
print(Solution().generate(numRows = 4))
print(Solution().generate(numRows = 5))


#%% LeetCode 119: Pascal's Triangle 2

from math import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        thisRow = []
        
        for j in range(rowIndex + 1):
                thisRow.append(comb(rowIndex, j))
    
        return thisRow

# Test cases

print(Solution().getRow(rowIndex = 0))
print(Solution().getRow(rowIndex = 1))
print(Solution().getRow(rowIndex = 2))
print(Solution().getRow(rowIndex = 3))
print(Solution().getRow(rowIndex = 4))


#%% LeetCode 121: Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1
             
        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, currentProfit)
            else:
                left = right
            right += 1
                
        return maxProfit

# Test Cases

print(Solution().maxProfit(prices = [7,1,5,3,6,4]))
print(Solution().maxProfit(prices = [7,6,4,3,1]))


#%% LeetCode 122: Best Time to Buy and Sell Stock II


#%% LeetCode 123: Best Time to Buy and Sell Stock III


#%% LeetCode 125: Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Remove punctuation and force lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        return s == s[::-1]

print(Solution().isPalindrome(s = "abba"))
print(Solution().isPalindrome(s = "abcd"))
print(Solution().isPalindrome(s = "abcdedcba"))
print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))
print(Solution().isPalindrome(s = "race a car"))
print(Solution().isPalindrome(s = " "))
print(Solution().isPalindrome(s = "0P"))


#%% LeetCode 136: Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        i = 0
        for i in range(len(nums)//2 + 1):
            if nums[(2 * i) % len(nums)] == nums[(2 * i + 1) % len(nums)]:
                pass
            elif nums[(2 * i + 1) % len(nums)] == nums[(2 * i + 2) % len(nums)]:
                return nums[2 * i]
            else:
                return nums[2 * i + 1]

print(Solution().singleNumber(nums = [2,2,1]))
print(Solution().singleNumber(nums = [4,1,2,1,2]))
print(Solution().singleNumber(nums = [1]))
print(Solution().singleNumber(nums = [1, 2, 2, 3, 3, 4, 4]))
print(Solution().singleNumber(nums = [2, 1, 2, 3, 3, 4, 4]))
print(Solution().singleNumber(nums = [2, 2, 3, 3, 4, 1, 4]))
print(Solution().singleNumber(nums = [2, 2, 3, 3, 4, 4, 1]))
      

#%% LeetCode 141: Linked List Cycle
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:

		slow = head
		fast = head

		while fast != None and fast.next != None:

			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				return True

		return False

# I'm not sure how to implement test cases using an IDE and not LeetCode.    
# print(Solution().hasCycle(head = [3,2,0,-4], pos = 1))
# print(Solution().hasCycle(head = [1,2], pos = 0))
# print(Solution().hasCycle(head = [1], pos = -1))


#%% LeetCode 147: Insertion Sort List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      while head.next != None:
          print(head.val, head.next)
          # head.
        
# Test cases -- difficult w/r/t ListNode class!
#print(Solution().insertionSortList())  


#%% LeetCode 203: Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head
        pointer = dummy
        
        while pointer.next:
            if pointer.next.val == val:
                if pointer.next.next:
                    pointer.next = pointer.next.next
                else:
                    pointer.next = None
            else:
                pointer = pointer.next
        
        return dummy.next


#%% LeetCode 206: Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev

# Recursive solution
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if not head:
#             return None
        
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
#         return newHead

#%% LeetCode 237: Delete Node in a Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # for i in Node:
        #     if i.val == target:
        #         i.val = next.val
        #         i.next = next.next
        #     else:
        #         pass

        node.val = node.next.val
        node.next = node.next.next

a = ListNode(x = 4)
b = ListNode(x = 5)
c = ListNode(x = 1)
d = ListNode(x = 9)

d.val = 9
d.next = None
c.val = 1
c.next = d
b.val = 5
b.next = c
a.val = 4
a.next = b


print(a.deleteNode(b))


#%% LeetCode 242: Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Brute forece, not very elegant
        
        for i in s:
            if i in t:
                # Note that magazine.replace alone won't work!
                s = s.replace(i, '', 1)
                t = t.replace(i, '', 1)
            else:
                return False
        if s == '' and t == '':
            return True
        else:
            return False

print(Solution().isAnagram(s = "anagram", t = "nagaram"))
print(Solution().isAnagram(s = "rat", t = "car"))
print(Solution().isAnagram(s = "anagram", t = "margana"))


#%% LeetCode 383: Ransom Notes

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #ransomNote.sort()
        #magazine.sort()
        
        # Use string replace!
        for i in ransomNote:
            if i in magazine:
                # Note that magazine.replace alone won't work!
                magazine = magazine.replace(i, '', 1)
            else:
                return False
        return True
        

# This solution is really elegant:
# class Solution:
#     def canConstruct(self, ransomNote, magazine):
#         for i in set(ransomNote):
#             if magazine.count(i) < ransomNote.count(i):
#                 return False
#        return True
        
print(Solution().canConstruct(ransomNote = "a", magazine = "b"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "ab"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))


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


#%% LeetCode 456: 132 Pattern
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) <= 2:
            return False
        lowVal = nums[0]
        
        for i in range(1, len(nums)):
            
            # Identify LowVal below
            if nums[i - 1] < lowVal:
                lowVal = nums[i - 1]
                        
            # Check above
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i] and nums[j] > lowVal:
                    return True
        # print("Found no 132s! Lowval: ", lowVal)
        return False


print(Solution().find132pattern(nums = [1,2,3,4])) # False
print(Solution().find132pattern(nums = [3,1,4,2])) # True
print(Solution().find132pattern(nums = [-1,3,2,0])) # True


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


#%% LeetCode 581: Shortest Unsorted Continuous Subarray
from operator import sub
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Brute force
        if len(nums) == 0: return 0
        if len(nums) == 1: return 0
    
        copyNums = list(nums)
        copyNums.sort()
        
        difference = list(map(sub, nums, copyNums))
        #print('Difference: ', difference)

        while difference[0] == 0:
            difference.pop(0)
            if len(difference) == 0: return 0
            
        while difference[-1] == 0:
            difference.pop(-1)
            if len(difference) == 0: return 0
        
        return len(difference)
        
        
print(Solution().findUnsortedSubarray(nums = [2,6,4,8,10,9,15]))
print(Solution().findUnsortedSubarray(nums = [1,2,3,4]))
print(Solution().findUnsortedSubarray(nums = [1]))
#print(Solution().findUnsortedSubarray())


#%% LeetCode 905: Sort Array by Parity
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        # Move odd numbers to end
        while i <= j:
            if nums[i] % 2 == 1:
                print(i, j)
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
            else:
                i += 1
        
        return nums

print(Solution().sortArrayByParity(nums = [3,1,2,4]))
print(Solution().sortArrayByParity(nums = [0]))
print(Solution().sortArrayByParity(nums = [3,1,3,2,4,6,4]))


#%% LeetCode 1679: Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        keepGoing = 1
        while(keepGoing == 1):
            for i in range (0, len(nums)):
                for j in range(i+1, len(nums)):
                    # print('[', i, j,']', nums[i], nums[j], '=', (nums[i] + nums[j]), '?=', target)
                    if nums[i] + nums[j] == k:
                        nums.remove(nums[i])
                        nums.remove(nums[j])
            keepGoing = 0
        return None

print(Solution().maxOperations(nums = [1,2,3,4], k = 5)) # --> 2
print(Solution().maxOperations(nums = [3,1,3,4,3], k = 6)) --> 1
#print(Solution().maxOperations())