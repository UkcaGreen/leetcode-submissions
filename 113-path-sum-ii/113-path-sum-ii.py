# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def foo(root, stack):
            if not root:
                return []
                
            if not root.left and not root.right:
                
                if sum(stack) + root.val == targetSum:
                    stack.append(root.val)
                    s = stack.copy()
                    stack.pop()
                    return [s]
                else:
                    return []
            
            stack.append(root.val)
            l = foo(root.left, stack)
            r =foo(root.right, stack)
            stack.pop()
            
            return l + r
        
        return foo(root, [])
            