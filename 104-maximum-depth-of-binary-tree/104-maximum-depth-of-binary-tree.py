# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        if not root.left and not root.right:
            #print('Nothing below', root.val)
            return 1
        
        maxDepth = 1
        
        if root.left:
            #print('Looking left to', root.left)
            curDepth = 1 + self.maxDepth(root.left)
            if curDepth > maxDepth:
                maxDepth = curDepth
        
        if root.right:
            #print('Looking right to', root.right)
            curDepth = 1 + self.maxDepth(root.right)
            if curDepth > maxDepth:
                maxDepth = curDepth
        
        return maxDepth