# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def foo(root, result_list):
            if not root:
                return
            
            if root.left:
                foo(root.left, result_list)
            result_list.append(root.val)
            if root.right:
                foo(root.right, result_list)
                
        ans = []
        foo(root, ans)
        return ans