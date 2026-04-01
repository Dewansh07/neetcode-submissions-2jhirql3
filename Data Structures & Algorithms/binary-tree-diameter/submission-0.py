# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum_depth = 0

        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)

            self.maximum_depth = max(self.maximum_depth, left+right)

            return max(left,right)+1

        depth(root)
        return self.maximum_depth