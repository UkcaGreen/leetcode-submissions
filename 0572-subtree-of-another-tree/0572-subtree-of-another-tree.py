# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.subRoot = subRoot

        def foo(p):
            
            if not p:
                return False
            
            ans = False
            
            if p.val == self.subRoot.val:
                ans = bar(p, self.subRoot)
            
            return ans or foo(p.left) or foo(p.right)
            
        def bar(p, q):
                
            if p is None and q is None:
                return True
            
            if p is not None and q is None:
                return False
            
            if p is None and q is not None:
                return False
                
            return p.val == q.val and bar(p.left, q.left) and bar(p.right, q.right)
            
        return foo(root)