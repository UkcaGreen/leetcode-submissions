# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def foo(root):
            if not root:
                return 0
            
            total = foo(root.left) + foo(root.right)
            
            if root.left and not root.left.left and not root.left.right:
                total += root.left.val
            
            return total
        
        return foo(root)