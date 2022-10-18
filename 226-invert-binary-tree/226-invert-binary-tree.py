# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def foo(root):
            if root:
                root.left, root.right  = foo(root.right), foo(root.left)
            return root
        
        return foo(root)
        
        