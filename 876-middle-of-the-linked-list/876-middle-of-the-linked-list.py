# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case
        if head.next == None: return head
        
        middle = head
        
        print('Starting with: ', head.val)
        while head and head.next:
            if head.next:
                middle = middle.next
                head = head.next
            if head:
                if head.next: head = head.next
        
        return middle