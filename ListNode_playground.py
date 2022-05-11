# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:08:02 2022

@author: vmgon

This is my playground for exploring the ListNode class used in several LeetCode
problems.

"""

from typing import List
from typing import Optional


#%% Preliminaries: ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        copy = ListNode()
        copy.val = self.val
        copy.next = self.next
        i = 0
        while copy != None and i < 20:
            if copy.next:
                print('Value: ', copy.val, 'Next: ', copy.next.val)
            else:
                print('Value: ', copy.val, 'Next: None')
            # copy.val = copy.next.val if copy.next else None
            if copy.next:
                copy.val = copy.next.val
            else:
                copy = None
            
            if copy!= None:
                if copy.val != None:
                    copy.next = copy.next.next if copy.next.next else None
            i += 1
        print("All done!\n\n")

# class Solution:    
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if head.next = Null:
#             return head
                
#         last = ListNode()
#         current = ListNode()
#         last.val = head.next.val
#         last.next = head.next.next
        
#         i = 0
#         while last.val != None and i < 20:
#             current.val = head.val
#             current.next = head.next
#             if last.val < current.val:
#                 print('Value: ', copy.val, 'Next: ', copy.next.val)
#             else:
#                 print('Value: ', copy.val, 'Next: None')
#             # copy.val = copy.next.val if copy.next else None
#             if copy.next:
#                 copy.val = copy.next.val
#             else:
#                 copy = None
            
#             if copy!= None:
#                 if copy.val != None:
#                     copy.next = copy.next.next if copy.next.next else None
#             i += 1
#         print("All done!\n\n")
#         return head

class Solution:        
    def insertionSortList(self, head):
        if head is None:
            return None
        helper = ListNode(-1000)
        pre, curr = helper, head
        while curr is not None:
            next_step = curr.next
            while pre.next and pre.next.val < curr.val:
                pre = pre.next
            curr.next = pre.next
            pre.next = curr
            pre = helper
            curr = next_step
        return helper.next

a = ListNode()
b = ListNode()
c = ListNode()
pointer = ListNode()

#%% Testing the printNode method
c.val = 'Chicago'
c.next = None
b.val = 'Boston'
b.next = c
a.val = 'Austin'
a.next = b
pointer.val = None
pointer.next = a

pointer.printNode()


#%% Testing the printNode method


# Pointer print
# tempPointer = pointer
# while tempPointer != None:
#     print(pointer.val, pointer.next)
#     pointer = pointer.next


# Pointer dump:
# while pointer != None:
#     print(pointer.val, pointer.next)
#     pointer = pointer.next


# list1 = [1, 2, 4] and list2 = [1, 3, 4]
c1 = ListNode(4, None)
b1 = ListNode(2, c1)
list1 = ListNode(1, b1)
list1.printNode()

c2 = ListNode(4, None)
b2 = ListNode(3, c2)
list2 = ListNode(1, b2)
list2.printNode()

#%% Testing [4,2,1,3]
n1 = ListNode()
n2 = ListNode()
n3 = ListNode()
n4 = ListNode()

n4.val = 3
n4.next = None
n3.val = 1
n3.next = n4
n2.val = 2
n2.next = n3
n1.val = 4
n1.next = n2
pointer.val = None
pointer.next = n1

pointer.printNode()
Solution().insertionSortList(head = n1).printNode()
