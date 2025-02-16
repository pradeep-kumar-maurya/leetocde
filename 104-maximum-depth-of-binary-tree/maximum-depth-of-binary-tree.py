# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # The idea is to just find the (max btw left tree and right tree + 1)   
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
