# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans, stack = [], []
        
        def foo(root):
            if not root:
                return
            
            stack.append(root.val)
            
            if root.left or root.right:               
                foo(root.left)
                foo(root.right)
            else:
                ans.append(stack.copy())

            stack.pop()
            
        foo(root)
        
        return ["->".join([str(n) for n in path]) for path in ans]
            