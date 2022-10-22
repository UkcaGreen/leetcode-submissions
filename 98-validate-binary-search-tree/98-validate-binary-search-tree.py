# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def foo(root, floor=float("-inf"), ceiling=float("inf")):
            if not root:
                return True
            
            return (
                ceiling > root.val > floor
                and foo(root.left, floor, root.val) 
                and foo(root.right, root.val, ceiling)
            )
            
            
                
        
        return foo(root)