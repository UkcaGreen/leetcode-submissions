# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_path = []
        q_path = []
        
        def foo(root):
            
            if not root:
                return
            
            if not (p_path and p_path[-1].val == p.val):
                p_path.append(root)

            if not (q_path and q_path[-1].val == q.val):
                q_path.append(root)
                
            foo(root.left)
            foo(root.right)
            
            if not (p_path and p_path[-1].val == p.val):
                p_path.pop()
                
            if not (q_path and q_path[-1].val == q.val):
                q_path.pop()
        
        foo(root)
        
        LCA = None
        
        for i, n in enumerate(p_path):
            
            if i >= len(q_path):
                break
            
            if p_path[i].val == q_path[i].val:
                LCA = p_path[i]
        
        return LCA
                