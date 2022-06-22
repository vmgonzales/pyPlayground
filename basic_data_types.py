# -*- coding: utf-8 -*-
'''
Basic Data Types Notebook
=========================

Big Idea:


Topics Covered
==============

* Arrays
* Solutions for LeetCode poblems.
* Solutions from Elements of Programming Interviews (Aziz, Lee, and Prakash 2014)

Created on Wed May 11 12:48:30 2022

@author: vmgon
'''

from typing import List
from typing import Optional

#%% Type casting
# Type casting is converting from one type to another

# Check the type using type()

# Convert to string
str(9.45)




#%% LeetCode 1523: Count Odd Numbers in an Interval Range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low) % 2 == 1:
            return int((high - low + 1) / 2)
        elif low % 2 == 1:
            return int(((high - low) / 2) + 1)
        else: return int((high - low) / 2)


#%% Test cases
print(Solution().countOdds(low = 3, high = 7)) # 3
print(Solution().countOdds(low = 3, high = 8)) # 3
print(Solution().countOdds(low = 4, high = 7)) # 2
print(Solution().countOdds(low = 4, high = 8)) # 2


#%% 1491: Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary = salary[1: -1]
        return mean(salary)

#%% ARRAYS
#%% LeetCode 976: Largest Perimiter Triangle

# Explanation:
# Sort the List to get the top 3 lengths
# Check if the largest length is less than sum of other two
# If 2 is false, drop the max length take next 3 largest length and repeat 1-2
# if 2 is true, return sum of all lengths
# if loop ends, and no possible combination found, return 0


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

#%% Test Cases
print(Solution().largestPerimeter([2, 1, 2])) # 5
print(Solution().largestPerimeter([1, 2, 1])) # 0
print(Solution().largestPerimeter([1, 2, 3, 4, 5])) # 12
print(Solution().largestPerimeter([1, 2, 3, 4, 5, 9999])) # 12
print(Solution().largestPerimeter([1, 2, 3, 9998, 5, 9999])) # 20002


#%% LeetCode 202: Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        pastN = set()
        newN = n
        limit = 30
        count = 0
        
        while newN not in pastN and count < limit:
            
            
            digits = []
            pastN.add(newN)
            
            for i in str(newN):
                i = (int(i) ** 2)
                digits.append(i)
                
            newN = sum(digits)
            #pastN.add(newN)
            
            print(digits, newN, pastN)
            if newN == 1: return True
            count += 1
        return False
    
        
print(Solution().isHappy(n = 1)) # True        
print(Solution().isHappy(n = 2)) # False
print(Solution().isHappy(n = 3)) # True
print(Solution().isHappy(n = 4)) # True
print(Solution().isHappy(n = 5)) # True
print(Solution().isHappy(n = 19)) # True
print(Solution().isHappy(n = 20)) # True
print(Solution().isHappy(n = 21)) # True

#%% EPI Problem 6.1: Dutch National Flag
def dutch_national_flag(a, index):
    length = len(a)
    print ("length: ", length)
    
    pivot = a[index]
    smaller, equal, larger = 0, 0, length - 1
    
    while (equal <= larger):
        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller += 1
            equal += 1
        elif a[equal] == pivot:
            equal += 1
        else:
            a[equal], a[larger] = a[larger], a[equal]
            larger -= 1
    return a

#test_array = [5, 6, 5, 4, 4, 3, 2, 1, 4, 5, 2]
#print (dutch_national_flag(test_array, 6))


#%% LeetCode 1356: Sort Integers by the Number of 1 Bits
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ones = [0] * len(arr)
        for i in range(len(arr)):
            copy = arr[i]
            ones[i] = 0
            while copy:
                ones[i] += copy % 2
                copy = copy // 2
        
        #I don't totally understand the zip function
        return([x for _, x in sorted(zip(ones, arr))])

print(Solution().sortByBits(arr=[0,1,2,3,4,5,6,7,8]))
