# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sums(self,root,gparent,parent):
        if not root:
            return 0
        
        if gparent % 2 == 0:
            curr = root.val
        else:
            curr = 0

        left = self.sums(root.left,parent,root.val)
        right = self.sums(root.right,parent,root.val)

        return curr + left + right




    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return self.sums(root,-1,-1) 
        