# -*- coding: utf-8 -*-
'''
Trees
=====

Big Idea: Exploring problems related to trees.


Topics Covered
==============

* 

Created on Sun May 15 18:59:59 2022

@author: vmgon
'''

#%% LeetCode 94: Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        ans = []
        if root.left:
            ans += self.inorderTraversal(root.left)
        # Carefull here... root.val can be 0, which would mean root.val = False
        if root.val != None:
            ans += [root.val]
        if root.right:
            ans += self.inorderTraversal(root.right)
        return ans
    
    
#%% LeetCode 144: Binary Tree Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        ans = []
        # Carefull here... root.val can be 0, which would mean root.val = False
        if root.val != None:
            ans += [root.val]
        if root.left:
            ans += self.preorderTraversal(root.left)
        if root.right:
            ans += self.preorderTraversal(root.right)
        return ans



#%% LeetCode 145: Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        ans = []
        if root.left:
            ans += self.postorderTraversal(root.left)
        if root.right:
            ans += self.postorderTraversal(root.right)
        # Carefull here... root.val can be 0, which would mean root.val = False
        if root.val != None:
            ans += [root.val]
        return ans
