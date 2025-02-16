# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # here we are travelling left then right and then swap left and right
        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        # The idea is to swap the nodes at the same level
        temp_root = root.left
        root.left = root.right
        root.right = temp_root

        return root

        # OR
        # # here we are swapping first and then going left and right
        # temp_root = root.left
        # root.left = root.right
        # root.right = temp_root

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

