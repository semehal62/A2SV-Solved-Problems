# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recur(preorder,postorder):
            if len(preorder) == 0:
                return 
            if len(preorder) == 1:
                node = TreeNode(preorder[0])
                return node

            root = TreeNode(preorder[0])
            
            i = postorder.index(preorder[1])
            root.left = recur(preorder[1:i+2],postorder[:i+1])
            root.right = recur(preorder[i+2:],postorder[i+1:-1])

            return root
        return recur(preorder,postorder)







    