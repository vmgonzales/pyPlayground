# -*- coding: utf-8 -*-
'''
Basic Data Types Notebook
=========================

Big Idea:


Topics Covered
==============

* Solutions for LeetCode poblems.
* Solutions from Elements of Programming Interviews (Aziz, Lee, and Prakash 2014)

Created on Wed May 11 12:48:30 2022

@author: vmgon
'''

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
