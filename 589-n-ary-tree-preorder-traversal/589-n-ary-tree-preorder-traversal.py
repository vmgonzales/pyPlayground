"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        values = []
        if not root: return []
        if root.val != None:
            # Note -- appending root.val IN BRACKETS, to make it a list item
            values += [root.val]
        if root.children:
            for node in root.children:
                # Note -- NOT appending values here in a bracket, since the method returns a list!
                values += self.preorder(node)
        return(values)
        print(values)