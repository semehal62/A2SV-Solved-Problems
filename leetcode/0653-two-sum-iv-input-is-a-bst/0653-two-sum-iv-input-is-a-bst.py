# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dict1 = defaultdict(int)
        def recur(root,k):
            if not root:
                return False

            if dict1[k- root.val] >= 1:
                return True

            dict1[root.val] += 1
            return recur(root.left,k) or recur(root.right,k)
        return recur(root,k)
        