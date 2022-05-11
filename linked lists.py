# -*- coding: utf-8 -*-
'''
Linked List Notebook
=====

Big Idea:


Topics Covered
==============

* LeetCode implementations of linked lists
* Solutions to several LeetCode problems pertaining to linked lists

Created on Wed May 11 12:53:47 2022

@author: vmgon
'''

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