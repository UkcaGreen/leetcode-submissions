# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def foo(root):
            if not root:
                return
            
            ans.append(root.val)
            
            foo(root.left)
            foo(root.right)
            
        foo(root)
        
        return ans