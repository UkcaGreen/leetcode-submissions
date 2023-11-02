# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        c1, c2 = head, head.next
        
        while c1 and c2 and c2.next:
            
            n1, n2 = c1.next, c2.next.next
            
            if c1 == c2:
                return True
            
            c1, c2 = n1, n2
            
        return False