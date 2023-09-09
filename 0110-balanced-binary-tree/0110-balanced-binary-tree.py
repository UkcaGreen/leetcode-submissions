# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def foo(root):
            if not root:
                return 0, True
            
            left_height, left_ans = foo(root.left)
            right_height, right_ans = foo(root.right)
            
            ans = left_ans and right_ans and abs(left_height - right_height) <= 1
            
            return 1 + max(left_height, right_height), ans
        
        _, ans = foo(root)
        
        return ans