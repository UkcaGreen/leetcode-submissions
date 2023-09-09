# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def foo(root1, root2):
            
            if root1 is None and root2 is None:
                return True  
            
            if root1 is None and root2 is not None:
                return False
            
            if root1 is not None and root2 is None:
                return False            

            if root1 is not None and root2 is not None:
                
                return (
                    root1.val == root2.val and 
                    foo(root1.left, root2.left) and 
                    foo(root1.right, root2.right)
                )
            
        return foo(p,q)
                
