# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.g_node = 0
        def func( root ,max_val):
            if  root.val >= max_val:
                self.g_node += 1
                max_val = root.val
            if root.left:
                func(root.left,max_val)
            if root.right:
                func(root.right,max_val)
            return 
        func(root,root.val)              
        return self.g_node   