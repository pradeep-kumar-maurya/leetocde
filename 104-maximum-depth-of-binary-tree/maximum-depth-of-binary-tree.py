# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.depth = 0
        def check_max_depth(root):
            if root is None:
                return
            else:
                self.depth += 1

            check_max_depth(root.left)
            check_max_depth(root.right)
            if self.depth > self.max:
                self.max = self.depth

            self.depth -= 1

        check_max_depth(root)
        return self.max
