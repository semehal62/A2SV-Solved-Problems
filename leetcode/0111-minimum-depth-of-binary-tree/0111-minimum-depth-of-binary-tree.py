# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def recur(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            elif not root.left:
                return 1 + recur(root.right)
            elif not root.right:
                return 1 + recur(root.left)
            else:
                return 1 + min(recur(root.left),recur(root.right))

        return recur(root)

        