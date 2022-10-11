# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def foo(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1

            mn = float("inf")
            
            if root.left:
                mn = min(mn,foo(root.left))
            if root.right:
                mn = min(mn,foo(root.right))
            
            return mn + 1
        
        return foo(root)