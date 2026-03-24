# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self,p,q):
            if not p and not q:
                return True

            if (p and q) and (p.val == q.val):
                return (self.recur(p.left,q.left)) and (self.recur(p.right,q.right))
            else:
                return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def search(root,subRoot):
            if not root:
                return False

            if self.recur(root,subRoot):
                return True
            
            return search(root.left,subRoot) or search(root.right,subRoot)

        return search(root,subRoot)         
        
            


