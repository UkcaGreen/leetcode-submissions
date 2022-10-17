# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        def foo(root, depth):
            if not root:
                return
            
            if len(ans) <= depth:
                ans.append([])
                
            ans[depth].append(root.val)
            
            foo(root.left, depth + 1)
            foo(root.right, depth + 1)
        
        foo(root, 0)
        
        return ans