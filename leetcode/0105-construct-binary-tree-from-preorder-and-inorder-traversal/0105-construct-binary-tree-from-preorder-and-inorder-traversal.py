# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def exchange(preorder,inorder):
            if not inorder:
                return 
            if len(inorder) == 1:
                node = TreeNode(inorder[0])
                return node

            l = inorder.index(preorder[0])

            root = TreeNode(preorder[0])

            root.left = exchange(preorder[1:l+1],inorder[:l])
            root.right = exchange(preorder[l+1:],inorder[l+1:])

            return root


        return exchange(preorder,inorder)
        