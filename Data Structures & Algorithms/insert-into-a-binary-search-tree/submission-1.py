# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root:
        #     return TreeNode(val)

        # if root.val> val:
        #     root.left = self.insertIntoBST(root.left, val)
        # else:
        #     root.right = self.insertIntoBST(root.right,val)
        # return root
        newn = TreeNode(val)
        current = root
        if not root:
            return newn

        while True:
            if val < current.val:
                if not current.left:
                    current.left = newn
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = newn
                    break
                current = current.right
        return root

