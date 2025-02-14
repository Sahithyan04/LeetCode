# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        seq1 = self.Seq(root1)
        seq2 = self.Seq(root2)
        return seq1 == seq2
    def Seq(self,root):
        if not root:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        
        l = self.Seq(root.left)
        r = self.Seq(root.right)

        return l + r

            
        