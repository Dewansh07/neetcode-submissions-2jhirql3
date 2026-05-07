# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, float('-inf'))

            left_gain, left_max = dfs(node.left)
            right_gain, right_max = dfs(node.right)

            max_gain = node.val+ max(0, left_gain, right_gain)

            max_through_node = node.val + max(0,left_gain) + max(0,right_gain)

            max_path = max(max_through_node, left_max, right_max)
            
            return (max_gain, max_path)
        
        return dfs(root)[1]
