# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def foo(_list):
            if not _list:
                return None
        
            value_idx = len(_list) // 2
            
            root = TreeNode(
                val=_list[value_idx],
                left=foo(_list[:value_idx]),
                right=foo(_list[value_idx+1:])
            )
            
            return root
        
        return foo(nums)