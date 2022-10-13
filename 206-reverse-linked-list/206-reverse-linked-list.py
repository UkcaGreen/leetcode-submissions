# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def foo(prev, root):
            if not root:
                return prev
            
            ans = foo(root, root.next)
            
            root.next = prev
            
            return ans
        
        return foo(None, head)