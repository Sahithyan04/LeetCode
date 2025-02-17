# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if root is None:
            return 0
        count = self.traverTree(root, targetSum)
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)
        return count
    def traverTree(self, node, targetSum):
        if node is None:
            return 0
        
        count  = 1 if node.val == targetSum else 0

        count += self.traverTree(node.left, targetSum - node.val)
        count += self.traverTree(node.right, targetSum - node.val)

        return count 
        