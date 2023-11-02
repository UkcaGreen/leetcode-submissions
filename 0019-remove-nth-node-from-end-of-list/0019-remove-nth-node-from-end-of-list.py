# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    ans = None
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        self.ans = head
        
        def foo(root, prev):
            
            if not root:
                return 0
            
            idx = foo(root.next, root) + 1
            
            if idx != n:
                return idx
            
            if not prev:
                self.ans = root.next
            else:
                prev.next = root.next
            
            return idx + 1
        
        foo(head, None)
            
        return self.ans
            
            
            