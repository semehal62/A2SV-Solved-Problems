# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recur(nums):
            if not nums:
                return
            if len(nums) == 1:
                return TreeNode(nums[0])

            
            maxi = max(nums)
            idx = nums.index(maxi)

            root = TreeNode(maxi)
            root.left = recur(nums[:idx])
            root.right = recur(nums[idx+1:])

            return root

        return recur(nums
        )
