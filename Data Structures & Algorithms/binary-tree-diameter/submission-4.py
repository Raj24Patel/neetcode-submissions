# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0


        def defs(root):
            if not root:
                return 0

            right = defs(root.right)
            left = defs(root.left)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        defs(root)

        return self.res