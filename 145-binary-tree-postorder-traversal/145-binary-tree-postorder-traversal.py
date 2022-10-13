# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def foo(root):
            if not root:
                return
            
            foo(root.left)
            foo(root.right)
            
            ans.append(root.val)
            
        foo(root)
        
        return ans