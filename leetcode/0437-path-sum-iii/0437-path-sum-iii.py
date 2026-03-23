# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dict1 = defaultdict(int)
        dict1[0] = 1
        count  = 0

        def recur(root,sums,target):
            nonlocal count
            if not root:
                return 0

            sums += root.val        
            count += dict1[sums-target]

            dict1[sums] += 1
            

            recur(root.left,sums,target) 
            recur(root.right,sums,target)
           
            dict1[sums] -= 1
            if dict1[sums] == 0:
                del dict1[sums]
            

            
        recur(root,0,targetSum)
        return count
        