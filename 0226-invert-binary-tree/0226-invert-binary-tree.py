# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root
    def traversal(self, root):
        if root is None:
            return 
        else:
            self.traversal(root.left)
            self.traversal(root.right)
            root.left, root.right = root.right, root.left
