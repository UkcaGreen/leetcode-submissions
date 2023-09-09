# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.logest_path_len = 0
        
        def util(root):
            
            if not root:
                return 0, 0
            
            ll, lr = util(root.left)
            rl, rr = util(root.right)
            
            self.logest_path_len = max(max(ll, lr) + max(rl, rr), self.logest_path_len)
            
            return max(ll, lr) + 1, max(rl, rr) + 1
        
        util(root)
        
        return self.logest_path_len
        